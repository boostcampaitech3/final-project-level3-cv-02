import os
import argparse
import shutil

from PIL import Image
from torchvision import transforms

import matplotlib.pyplot as plt
import torch
import torchvision
import numpy as np
import math
import copy

# from imagenet_labels import image_label


# 이미지 로드
def load_img(img_path):
    img = Image.open(img_path).resize((256, 256)).convert('RGB')
    return transforms.ToTensor()(img)


# 코사인 유사도 구하기
def cos_sim(mask_sketch, mask_generated):
    mask_sketch, mask_generated = np.array(mask_sketch), np.array(mask_generated)
    sum = np.sum(mask_sketch * mask_generated)
    divider = math.sqrt(np.sum(mask_sketch * mask_sketch)) * math.sqrt(np.sum(mask_generated * mask_generated))
    return sum / divider


# 이미지 마스크 부분만 자르기
def make_mask(img, np_min, np_max):
    mask = np.array([
        [
            [
                float(j) for j in i[np_min[1] : np_max[1] + 1]
            ] for i in img[channel][np_min[0] : np_max[0] + 1]
        ] for channel in range(3)])
    return transforms.ToTensor()(mask)


# 마스크 뽑기
def extract_mask(input_original, input_sketch):
    # 원본 이미지, sketch 추가된 이미지 불러오기
    img_original_tensor = load_img(input_original)
    img_sketch_tensor = load_img(input_sketch)

    # 두 이미지 차이 계산 후 0, 1 binary mask 생성
    mask_tensor = img_original_tensor - img_sketch_tensor
    mask_tensor = torch.clamp(torch.abs(mask_tensor), min=0, max=1)
    threshold = 3 / 255
    for i in range(len(mask_tensor[0])):
        for j in range(len(mask_tensor[0][0])):
            for rgb in range(3):
                if mask_tensor[rgb][i][j] < threshold:
                    mask_tensor[rgb][i][j] = 0

    # Different(mask): 0, Same: 1
    mask_tensor = torch.ones(mask_tensor.size()) - torch.ceil(mask_tensor)

    return mask_tensor[0] * mask_tensor[1] * mask_tensor[2]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path1', type=str, help='Original image path')
    parser.add_argument('--path2', type=str, help='Sketch image path')
    parser.add_argument('--save_path', type=str, help='Saving 256*256 generated image path')
    args = parser.parse_args()

    image_num = 0

    origin_path = args.path1
    sketch_path = args.path2

    # 이미지 불러오기
    # img_original = load_img(origin_path)
    img_sketch = load_img(sketch_path)

    mask = extract_mask(origin_path, sketch_path)

    # 마스크 부분 직사각형 구하기
    # 0: Not visited mask
    # 1: Visited mask or not mask
    visited = copy.deepcopy(mask)
    mask_pixel_list = []

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    # 마스크 부분 전처리(노이즈 제거, 마스크 데이터만 따로 보아서 저장)
    def bfs(i, j):
        count = 1
        change_list = []
        visited[i][j] = 1
        queue = [[i, j]]
        while queue:
            a, b = queue[0][0], queue[0][1]
            del queue[0]
            for k in range(8):
                x = a + dx[k]
                y = b + dy[k]
                if 0 <= x < visited.shape[0] and 0 <= y < visited.shape[1] and visited[x][y] == 0:
                    visited[x][y] = 1
                    queue.append([x, y])
                    change_list.append([x, y])
                    count += 1
        # Ignore mask smaller than 328 pixels
        # 328 pixels = 0.5% area when image is resized to (256, 256)
        if count < 328:
            for pixel in change_list:
                mask[pixel[0]][pixel[1]] = 1
        else:
            mask_pixel_list.append(change_list)

    # 전처리 실행
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if visited[i][j] == 0:
                bfs(i, j)

    x_y_min, x_y_max, to_mask_x_y_list = [], [], []
    for i in range(len(mask_pixel_list)):
        x_y_min.append(np.min(np.array(mask_pixel_list[i]), axis=0))
        x_y_max.append(np.max(np.array(mask_pixel_list[i]), axis=0))
        to_mask_x_y_list.append(mask_pixel_list[i] - x_y_min[i])

    # 모델 불러오기
    model = torchvision.models.resnet18(pretrained=True)

    # 마스크 부분을 모델에 넣기 -> category 찾기
    preds = []
    for object_idx in range(len(mask_pixel_list)):
        img = make_mask(img_sketch, x_y_min[object_idx], x_y_max[object_idx])
        img = img.permute(1, 2, 0)

        mask = torch.zeros((img.size()[1], img.size()[2]))
        for [i, j] in to_mask_x_y_list[object_idx]:
            mask[i][j] = 1

        masked_img = torch.unsqueeze(mask * img, 0)
        if torch.cuda.is_available():
            masked_img = masked_img.to('cuda', dtype=torch.float)
            model.to('cuda')

        model.eval()
        out = model(masked_img)
        pred = torch.argmax(out, dim=-1)
        preds.append(pred)

        # print(f"Class {pred[0]}: {image_label[pred[0]]}")

    result = [i for i in range(48 * int(image_num), 48 * int(image_num) + 80)]
    path = args.save_path + "/bedroom_generated_"

    # 생성된 모든 그림에 대해서 원하는 category에 대한 logit 찾기
    logits = np.ones(len(result))
    cosine_similarities = np.ones(len(result))
    for file_idx, file_number in enumerate(result):
        img_path = path + f"{file_number:04d}.png"
        img_generated = load_img(img_path)
        for mask_idx in range(len(mask_pixel_list)):
            mask_generated = make_mask(img_generated, x_y_min[mask_idx], x_y_max[mask_idx])
            mask_generated = mask_generated.permute(1, 2, 0)
            mask_generated = torch.unsqueeze(mask_generated, 0)

            mask_sketch = make_mask(img_sketch, x_y_min[mask_idx], x_y_max[mask_idx])
            mask_sketch = mask_sketch.permute(1, 2, 0)
            mask_sketch = torch.unsqueeze(mask_sketch, 0)

            '''
            Logit & Cosine Similarity
            덧셈을 통해 여러 objects에 대한 값을 병합합니다.

            1. 사용 목적
            - Logit: 해당 object가 동일한 class로 그려진 정도를 확인(의미 측면의 유사도)
            - Cosine Similarity: 해당 object가 비슷한 색상으로 그려진 정도를 확인(색상 측면의 유사도)

            2. 곱셈을 사용하는 이유
            - 내림차순 정렬했을 때 덧셈에 비해서 모든 object에 대해 고르게 좋은 결과를 낸 사진을 추천함

            3. 미리 상수를 더하는 이유
            - 0 <= x < 1인 경우 x를 곱하는 것은 penalty가 될 수 있음
            - Logit
                - 모델의 마지막 layer가 ReLU임을 가정함
                - 0 <= logit
                - 0 <= logit < 1인 값에 대해 penalty를 주지 않기 위해 1을 더함
                - 1 <= logit + 1
            - Cosine Similarity
                - RGB 값이므로 음수가 없음
                - 0 <= cos_sim <= 1
                - 0 <= cos_sim < 0.5인 값에 대해 penalty를 주기 위해 0.5를 더함
                - 0.5 <= cos_sim < 1인 값에 대해 penalty를 주지 않기 위해 0.5를 더함
                - 0.5 <= cos_sim + 0.5 <= 1.5
            '''

            cosine_similarities[file_idx] *= (cos_sim(mask_sketch, mask_generated) + 0.5)

            if torch.cuda.is_available():
                mask_generated = mask_generated.to('cuda', dtype=torch.float)

            # 물체를 새로 그린 경우: 물체에 맞는 ImageNet label 넣기
            # 의자: 559, 시계: 892, 커튼: 854, 창문: 904
            # logits[i] += model(mask_generated)[0][559]

            # 이미지 위에 색칠한 경우
            logits[file_idx] *= (model(mask_generated)[0][preds[mask_idx]] + 1)

    # 이미지 선택 및 시각화
    # fig = plt.figure(figsize=(20, 15))
    # ax = fig.add_subplot(3, 2, 1)
    # ax.imshow(img_original.permute(1, 2, 0))
    # ax = fig.add_subplot(3, 2, 2)
    # ax.imshow(img_sketch.permute(1, 2, 0))

    index_and_logits = [[result[i], logits[i]] for i in range(len(result))]
    selected_image_paths = []

    displayed_images = 0
    for index, logit in sorted(index_and_logits, key=lambda x: x[1], reverse=True):
        if displayed_images >= 4:
            break

        # print(f"Image bedroom_generated_{result[index]:04d}.png")
        # print(f"Multiplied Logit: {logit:.4f}")
        # print(f"Multiplied Cosine Similarity: {cosine_similarities[index]:.4f}")

        # 코사인 유사도가 0.95 이상인 이미지만 선택
        if cosine_similarities[index] > 1.45 ** len(mask_pixel_list):
            # print("OK!\n")
            change_path = path + f"{result[index]:04d}.png"
            selected_image_paths.append(change_path)

            # img_generated = load_img(change_path)
            # ax = fig.add_subplot(3, 2, displayed_images + 3)
            # ax.imshow(img_generated.permute(1, 2, 0))
            displayed_images += 1
        # else:
        #     print("Checking other images...\n")

    # print(selected_image_paths)

    os.mkdir(args.save_path + "_super_resolution")
    for selected_image_path in selected_image_paths:
        shutil.copy(selected_image_path, args.save_path + "_super_resolution")

    shutil.rmtree(args.save_path)
