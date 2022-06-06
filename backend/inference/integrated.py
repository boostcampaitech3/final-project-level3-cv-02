import os
import subprocess

import hashlib

from PIL import Image

import torch
from torchvision import transforms
from torchvision import utils as tvu

from typing import List


PATH = '/opt/ml/bucket-git/final-project-level3-cv-02/backend/app/inference/'


def combine_option_call(command: str, options: str) -> None:
    subprocess.call(command + " " + options, shell=True)


def crop_sketch_image(path_original: str, path_sketch: str) -> None:
    img_original = Image.open(path_original).convert('RGB')
    img_sketch = Image.open(path_sketch).convert('RGB')

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

    os.remove(path_sketch)
    tvu.save_image(img_sketch, path_sketch)


def size_check(path_original: str, path_sketch: str, width: int, height: int) -> None:
    width_original, height_original = Image.open(path_original).size
    width_sketch, height_sketch = Image.open(path_sketch).size
    assert (width_original, height_original) == (width, height), 'Given size does not match with original image size'

    # Pass 1/9 case: original image size matches with sketch image size
    # Reject 5/9 cases: original image is broader or longer than sketch image
    if width_original > width_sketch or height_original > height_sketch:
        raise Exception('Original image is larger than sketch image')
    # Fix 3/9 cases: original image is narrower or shorter than sketch image
    if width_original < width_sketch or height_original < height_sketch:
        crop_sketch_image(path_original, path_sketch)


def integrated_pipeline(path_original: str, path_sketch: str, width: int, height: int) -> str:
    size_check(path_original, path_sketch, width, height)

    sha1 = hashlib.new('sha1')
    sha1.update(path_original.encode('utf-8'))
    random_id = sha1.hexdigest()[:8]

    path_options = f"--path1 {path_original} --path2 {path_sketch} --save3 /opt/ml/generated/{random_id}"
    result_options = f"--save4 /opt/ml/generated/{random_id}_super_resolution --width {width} --height {height}"

    combine_option_call("python SDEdit.py --sample_step 10 --t 500", path_options)
    combine_option_call("python recommendation.py", path_options)
    combine_option_call("python ESRGAN.py", result_options)

    return f"/opt/ml/generated/{random_id}_super_resolution"
    

if __name__ == '__main__':
    # Data those will be given from back-end
    path_original = None
    path_sketch = None
    width, height = (None, None)

    paths = integrated_pipeline(path_original, path_sketch, width, height)