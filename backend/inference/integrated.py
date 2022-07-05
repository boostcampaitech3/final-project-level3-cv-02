import os
import hashlib

from PIL import Image

import torch
from torchvision import transforms
from torchvision import utils as tvu

from SDEdit import generator
from recommendation import recommender
from ESRGAN import upscaler


base_path = '/opt/ml/bucket-git'


def crop_sketch_image(original_path: str, sketch_path: str) -> None:
    img_original = Image.open(original_path).convert('RGB')
    img_sketch = Image.open(sketch_path).convert('RGB')

    width_original, height_original = img_original.size
    width_sketch, height_sketch = img_sketch.size

    to_tensor = transforms.ToTensor()
    img_original = to_tensor(img_original)
    img_sketch = to_tensor(img_sketch)

    min = 1e10
    for i in range(height_sketch - height_original + 1):
        for j in range(width_sketch - width_original + 1):
            candidate = img_sketch[:, i:i + height_original, j:j + width_original]
            pred = torch.sum(torch.abs(candidate - img_original))
            if pred < min:
                min = pred
                img_sketch = candidate

    os.remove(sketch_path)
    tvu.save_image(img_sketch, sketch_path)


def size_check(original_path: str, sketch_path: str, width: int, height: int) -> None:
    width_original, height_original = Image.open(original_path).size
    width_sketch, height_sketch = Image.open(sketch_path).size
    # assert (width_original, height_original) == (width, height), 'Given size does not match with original image size'

    # Pass 1/9 case: original image size matches with sketch image size
    # Reject 5/9 cases: original image is broader or longer than sketch image
    if width_original > width_sketch or height_original > height_sketch:
        raise Exception('Original image is larger than sketch image')
    # Fix 3/9 cases: original image is narrower or shorter than sketch image
    if width_original < width_sketch or height_original < height_sketch:
        crop_sketch_image(original_path, sketch_path)


def integrated_pipeline(original_path: str, sketch_path: str, width: int, height: int) -> str:
    size_check(original_path, sketch_path, width, height)

    sha1 = hashlib.new('sha1')
    sha1.update(original_path.encode('utf-8'))
    random_id = sha1.hexdigest()[:8]

    save_path = f"{base_path}/generated/{random_id}"
    generator(original_path, sketch_path, save_path)
    recommender(original_path, sketch_path, save_path)

    save_path += "_super_resolution"
    upscaler(save_path, width, height)

    return save_path


# Execution example code (not for service)
if __name__ == '__main__':
    # Data those will be given from back-end
    original_path = None
    sketch_path = None
    width, height = (None, None)

    path = integrated_pipeline(original_path, sketch_path, width, height)
