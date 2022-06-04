# For original code:
#   Copyright 2019 The TensorFlow Hub Authors. All Rights Reserved.
# For modifications:
#   Copyright 2022 Bucket Interior Team. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import argparse

import torchvision.utils as tvu

from PIL import Image
import pandas as pd
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt


os.environ["TFHUB_DOWNLOAD_PROGRESS"] = "True"

SAVED_MODEL_PATH = "https://tfhub.dev/captain-pool/esrgan-tf2/1"


def preprocess_image(image_path):
    hr_image = tf.image.decode_image(tf.io.read_file(image_path))
    # If PNG, remove the alpha channel. The model only supports
    # images with 3 color channels.
    if hr_image.shape[-1] == 4:
        hr_image = hr_image[...,:-1]
    hr_image = tf.cast(hr_image, tf.float32)
    return hr_image


def plot_image(image, title=""):
    image = np.asarray(image)
    image = tf.clip_by_value(image, 0, 255)
    image = Image.fromarray(tf.cast(image, tf.uint8).numpy())
    plt.imshow(image)
    plt.axis("off")
    plt.title(title)


def resize_image(image, size: tuple):
    image = tf.cast(tf.clip_by_value(image, 0, 255), tf.uint8)
    image = np.asarray(Image.fromarray(image.numpy()).resize(size))
    image = tf.expand_dims(image, 0)
    image = tf.cast(image, tf.float32)
    return image


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--save4', type=str, help='Selected image path list')
    parser.add_argument('--width', type=int, help='Image target width')
    parser.add_argument('--height', type=int, help='Image target height')
    args = parser.parse_args()

    img_paths = os.listdir(args.save4)
    for cache in ['__pycache__', '.ipynb_checkpoints']:
        if cache in img_paths:
            img_paths.remove(cache)

    model = hub.load(SAVED_MODEL_PATH)
    plt.rcParams['figure.figsize'] = [25, 8 * len(img_paths)]
    fig, axes = plt.subplots(len(img_paths), 2)

    super_images = []
    for i in range(len(img_paths)):
        image = preprocess_image(os.path.join(args.save4, img_paths[i]))
        image = resize_image(image, (args.width // 4, args.height // 4))

        super_image = model(image)

        image = tf.squeeze(image)
        super_image = tf.squeeze(super_image)

        super_images.append(super_image)

        plt.subplot(len(img_paths), 2, 2 * i + 1)
        fig.tight_layout()
        plot_image(tf.squeeze(image), str(image.shape))

        plt.subplot(len(img_paths), 2, 2 * i + 2)
        fig.tight_layout()
        plot_image(tf.squeeze(super_image), str(super_image.shape))

    plt.savefig(os.path.join(args.save4, 'result.png'), dpi=150)

    super_images_paths = []
    for index, super_image in enumerate(super_images):
        tf.keras.preprocessing.image.save_img(os.path.join(args.save4, f"bedroom_upscaled_{index}.png"), super_image)

    for image_path in img_paths:
        os.remove(os.path.join(args.save4, image_path))
