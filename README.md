# 내일의집

> [boostcamp AI Tech](https://boostcamp.connect.or.kr) - Level 3: CV_02 Bucket Interior


## Introduction

## Data
LSUN bedrrom

ImageNet


## Model

![image](https://user-images.githubusercontent.com/63588046/169930202-56e1f0d1-d05b-40c9-82c8-5585fc239247.png)

원본 이미지와 스케치한 이미지를 넣으면 마스크를 뽑아냅니다. 마스크와 스케치한 이미지를 SDEdit에 넣어서 새로운 인테리어가 사진을 만듭니다.. 그러나 새로 나온 인테리어 사진은 해상도가 너무 낮습니다. 그래서 해상도를 높이기 위해 ESRGAN을 사용했습니다.

## Why SDEdit

https://paperswithcode.com/sota/image-super-resolution-on-urban100-4x

## Why ESRGAN

#### Origin
![image](https://user-images.githubusercontent.com/63588046/169933470-013b395b-e2d8-453c-9d65-b79b078a9baa.png)


#### ESRGAN
![image](https://user-images.githubusercontent.com/63588046/169933552-587bbd42-1230-4e0f-8f11-5af63590bdc6.png)


#### EDSR
![image](https://user-images.githubusercontent.com/63588046/169933922-12371538-5fb9-4e6f-84bc-9a08542559e9.png)

#### CAR
모델의 크기가 300MB
https://mega.nz/file/XzIm3YhT#jbIOOOGBOiKtv3VAOD782Mz7nK1L_kma-BzR-RhboW4 (pretrained)


## Author

|김예원|김주연|김주영|유환규|이수아|
|:-:|:-:|:-:|:-:|:-:|
|[Github](https://github.com/Yewon-dev)|[Github](https://github.com/zooyeonii)|[Github](https://github.com/nestiank)|[Github](https://github.com/hkyoo52)|[Github](https://github.com/heosuab)

## Reference


