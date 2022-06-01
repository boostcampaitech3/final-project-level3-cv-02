# 내일의집

> [boostcamp AI Tech](https://boostcamp.connect.or.kr) - Level 3: CV_02 Bucket Interior


## Introduction
(주)내일의집은 사용자의 ‘방 사진’에 자유롭게 인테리어를 수정 또는 추가(스케치를 통해)하면, 이를 실제 모습처럼 보여주는 역할을 한다. 

## 서비스 흐름도



## 서비스 시스템 구조




## Data
#### LSUN bedrrom
* Lsun 데이터는 총 10개의 라벨로 구성되는데 그중 침실 데이터를 사용했다.
* train 데이터 : 3,033,042
* validation 데이터 : 300

#### ImageNet
* 총 1000개의 라벨로 구성되어 있음
* train 데이터 : 120만개
* validation 데이터 : 5만개


## 모델
![image](https://user-images.githubusercontent.com/63588046/170953378-f07697bb-cd34-42ec-b8e9-b657c50a3e0c.png)

## 모델 구조 설명

1. 사용자가 원본 이미지와 변형하고 싶어서 스케치한 이미지를 넣는다.
3. 스케치한 부분의 이미지 합성을 한다.
4. 2개의 이미지로 마스크를 생성한다.
5. 마스크된 부분 이미지 분류를 한다.
6. 분류된 이미지 바탕으로 생성된 이미지 중에서 사진을 추천한다.
7. 사진을 고해상도로 바꿔준다.
8. 고해상도 이미지를 이메일로 받는다.

## Why SDEdit
1. Diffusion 모델의 성능이 GAN 보다 좋다
2. Diffusion 모델은 오래 걸린다는 단점이 있는데 우리는 실시간으로 서비스를 제공해줄 필요가 없다.
3. Diffusion 모델중에 Dalle2와 고민했는데 Dalle2는 코드 공개를 해주지 않았다.
4. 또한 Dalle2는 API를 통해 사용할 수도 없었다.
5. 생성 모델을 학습하기에는 시간이 부족했다.


## Why ESRGAN

#### Origin
![image](https://user-images.githubusercontent.com/63588046/169933470-013b395b-e2d8-453c-9d65-b79b078a9baa.png)


#### ESRGAN
![image](https://user-images.githubusercontent.com/63588046/171135605-00a9eea0-c611-4eb0-96cc-3799f1834e4a.png)

#### EDSR
![image](https://user-images.githubusercontent.com/63588046/169933922-12371538-5fb9-4e6f-84bc-9a08542559e9.png)

#### CAR
![image](https://user-images.githubusercontent.com/63588046/171135260-90233af8-3186-4b27-94f1-24ee90202810.png)


* 가장 흔한 super resolution 모델인 EDSR과 현재 모델중 가장 성능이 좋은 CAR을 사용하지 않고 우리는 ESRGAN을 사용했다.
* EDSR은 일반적으로 성능이 좋았다. 그러나 동일한 색으로 겹쳐있을 경우 깨지는 경향이 나타났다.. 
* CAR과 ESRGAN은 육안으로 보았을 때 크게 차이가 없었다. 그러나 CAR모델은 메모리 크기가 360MB가 넘는 방면에 ESRGAN은 16MB 정도로 20배 넘게 차이가 났다.
* 그래서 ESRGAN을 사용했다.


## 아쉬운 점
* SDEdit을 통해 나온 이미지 대부분이 사용하기 안좋은 이미지였다. 좀 더 성능이 높은 생성모델이 있으면 더 좋았을 것 같다.
* 시간적 여유가 더 있다면 추천하는 방식을 GAN의 discriminator로 도전했으면 좋겠다. (SOTA 중에서 인테리어 관련된 checkpoint를 제공해주는 것이 없어서 시간이 있었다면 직접 학습해서 discriminator를 구하고 싶다.)


## Author

|김예원|김주연|김주영|유환규|이수아|
|:-:|:-:|:-:|:-:|:-:|
|[Github](https://github.com/Yewon-dev)|[Github](https://github.com/zooyeonii)|[Github](https://github.com/nestiank)|[Github](https://github.com/hkyoo52)|[Github](https://github.com/heosuab)

## Reference


