# 내일의집

> [boostcamp AI Tech](https://boostcamp.connect.or.kr) - Level 3: CV_02 Bucket Interior


## Introduction  - 나중에 수아님
Samsung Bespoke, LG objet 등 고객들에게 맞춤형 가구 또는 인테리어를 제공해줄 수 있는 “퍼스널 인테리어” 서비스가 유행 중이기 때문에 최신 AI 기술을 도입하여 접근성이 높은 웹사이트로 제작해보고자 하였다.

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
1. 새로운 이미지를 생성하려면 Generative model 기술이 필요한데, 서비스 측면에서 최대한 완성도 높은 결과물을 제공하기 위해서 GAN의 성능을 크게 뛰어넘는 Diffusion Probabilistic model을 사용해보고자 결정했다.
2. GAN은 diffusion보다 속도가 빠르다는 장점이 있지만, 정성적인 평가에서 결과물의 성능이 현저히 떨어지고 우리 프로젝트는 실시간 서비스를 요구하지 않는다고 판단하여 diffusion으로 선정했다.
3. Diffusion model 중에서도 스케치한 영역에 새로 생성할 수 있는 DALLE-2, SDEdit 두 가지 모델을 고려했다
4. DALLE-2는 pretrained-weight도 존재하지 않아서 우리가 가진 V100 GPU로는 학습 시간&메모리 문제상으로 힘들것 같다고 판단하여 SDEdit 선정
5. Dalle-2는 API도 제공해주지 않아서 사용하기 어렵다.


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

## 프로젝트 장점 및 기대 효과
* 기존의 인테리어 컨설팅은 비용도 높고 전문 인력을 필요로하는데, 가구만 바꿔보는 작은 스케일의 인테리어 컨설팅을 위해서 전문업체에 의뢰하는 건 부담스러울 수 있다. 사용자들에게 접근성이 높은 웹과 전문 인력을 필요로 하지 않는 AI 기술을 사용하여 간단하게 배치를 해볼 수 있다는 장점이 있다.
* 현재 가상의 환경에서 가구를 배치하여 인테리어를 할 수 있는 프로그램이 존재한다. 하지만 어떤 가구를 놓아야 하는지 선택해야하는 것은 사용자의 몫이다. 내일의 집은 간단한 스케치만으로 내 방과 어울리는 가구의 배치를 볼 수 있으므로 사용자가 가구 선택을 위한 고민의 시간을 줄여줄 수 있는 장점이 있다.


## 아쉬운 점
* 시간이 더 있었다면 더 많은 실험을 통해 더 모델들을 개선할 수 있었을 것 같다.
* 시간적 여유가 더 있다면 추천하는 방식을 GAN의 discriminator로 도전했으면 좋겠다. (SOTA 중에서 인테리어 관련된 checkpoint를 제공해주는 것이 없어서 시간이 있었다면 직접 학습해서 discriminator를 구하고 싶다.)


## Author

|김예원|김주연|김주영|유환규|이수아|
|:-:|:-:|:-:|:-:|:-:|
|[Github](https://github.com/Yewon-dev)|[Github](https://github.com/zooyeonii)|[Github](https://github.com/nestiank)|[Github](https://github.com/hkyoo52)|[Github](https://github.com/heosuab)

## Reference


