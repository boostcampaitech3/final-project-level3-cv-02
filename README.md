# 내일의집

> [boostcamp AI Tech](https://boostcamp.connect.or.kr) - Level 3: CV_02 Bucket Interior


## Introduction
(주)내일의집은 사용자의 ‘방 사진’에 자유롭게 인테리어를 수정 또는 추가(스케치를 통해)하면, 이를 실제 모습처럼 보여주는 역할을 한다. 

## 서비스 흐름도



## 서비스 시스템 구조

1. 사용자가 원본 이미지와 변형하고 싶어서 스케치한 이미지를 넣는다.
2. 스케치한 부분의 이미지 합성을 한다.
3. 2개의 이미지로 마스크를 생성한다.
4. 마스크된 부분 이미지 분류를 한다.
5. 분류된 이미지 바탕으로 생성된 이미지 중에서 사진을 추천한다.
6. 사진을 고해상도로 바꿔준다.
7. 고해상도 이미지를 이메일로 받는다.


## Data
#### LSUN bedrrom
* Lsun 데이터는 총 10개의 라벨로 구성되는데 그중 침실 데이터를 사용했다.
* train 데이터 : 3,033,042
* validation 데이터 : 300

#### ImageNet
* 총 1000개의 라벨로 구성되어 있음
* train 데이터 : 120만개
* validation 데이터 : 5만개


## Model
![image](https://user-images.githubusercontent.com/63588046/170953378-f07697bb-cd34-42ec-b8e9-b657c50a3e0c.png)

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


