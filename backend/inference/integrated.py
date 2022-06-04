import os
import subprocess

import hashlib

from PIL import Image

PATH = '/opt/ml/bucket-git/final-project-level3-cv-02/backend/app/inference/'


def combine_option(command: str, options: str) -> str:
    return command + " " + options


def integrated_pipeline(path_original: str, path_sketch: str, width: int, height: int) -> int:
    sha1 = hashlib.new('sha1')
    sha1.update(path_original.encode('utf-8'))
    random_id = sha1.hexdigest()[:8]

    path_options = f"--path1 {path_original} --path2 {path_sketch} --save3 /opt/ml/generated/{random_id}"
    result_options = f"--save4 /opt/ml/generated/{random_id}_super_resolution --width {width} --height {height}"

    subprocess.call(combine_option("python /opt/ml/bucket-git/final-project-level3-cv-02/backend/inference/SDEdit.py --sample_step 10 --t 500", path_options), shell=True)
    subprocess.call(combine_option("python /opt/ml/bucket-git/final-project-level3-cv-02/backend/inference/recommendation.py", path_options), shell=True)
    subprocess.call(combine_option("python /opt/ml/bucket-git/final-project-level3-cv-02/backend/inference/ESRGAN.py", result_options), shell=True)


    return f"/opt/ml/generated/{random_id}_super_resolution"
    


if __name__ == '__main__':
    path_original = None
    path_sketch = None

    size = Image.open(path_original).size
    assert size == Image.open(path_sketch).size, 'Size mismatch between two images'
    width, height = size

    paths = integrated_pipeline(path_original, path_sketch, width, height)
    print(type(paths))
    print(paths)
