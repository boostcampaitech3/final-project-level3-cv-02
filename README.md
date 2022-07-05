# 내일의집

> [boostcamp AI Tech](https://boostcamp.connect.or.kr) - Level 3: CV_02 Bucket Interior <br>
> 간단한 스케치로, 당신의 가구를 현실로!

## Introduction

2020년부터 2022년까지의 트렌드를 살펴보면, 2030 세대의 인테리어 관심도가 증가함을 알 수 있습니다. 특히, 삼성 BESPOKE, LG objet 등 나만의 맞춤형 가구를 찾는 '퍼스널 인테리어'에 대한 관심이 증가하고 있고, 관련 기술의 수요가 늘어나고 있습니다.

'퍼스널 인테리어'의 핵심은 자신이 가장 원하는 가구를 직접 골라서, 직접 배치하는 것입니다. 하지만 원하는 가구의 모습에 꼭 맞는 상품을 찾는 것도, 내 방에 어울릴지 상상하는 것도 어려운 일입니다. 그렇다고 전문가와 직접 인테리어를 상의하는 것은 여전히 많은 비용이 듭니다. 이처럼 '퍼스널 인테리어'의 접근성은 오랫동안 개선되지 않고 있습니다.

저희는 최소한의 입력으로 '그 상품이 내 방에 있는 모습'을 보여주고자 했습니다. 이를 위해서 저희는 비슷한 서비스를 제공하는 '오늘의집' 서비스에 주목했습니다.

'오늘의집'은 인테리어 및 소품을 판매하는 서비스로, 다른 사용자들의 방에 배치된 모습을 보며 상품을 고를 수 있습니다. 하지만 직접 내 방에 적용된 모습을 상상하는 데에는 한계가 있습니다. 내가 원하는 상품이 배치된 모습을 확인할 수 있다면 상품 선택이 더 효율적일 것입니다.

그래서 저희는 AI 기술을 도입하여 간단한 스케치만으로 방의 인테리어를 꾸며 보고, 상품 구매 전 미리 체험해볼 수 있는 웹사이트를 제작했습니다.

내일의집은 사용자가 자신의 '방 사진'에 스케치를 통해 자유롭게 인테리어를 수정 또는 추가하면, 이를 실제로 적용한 것 같은 사진을 보여주는 서비스입니다.

## 시연 영상

[![내일의집 시연 영상](https://res.cloudinary.com/marcomontalbano/image/upload/v1655805746/video_to_markdown/images/youtube--M57tLcO3A3c-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/M57tLcO3A3c "내일의집 시연 영상")

<!-- Thanks to https://github.com/marcomontalbano/video-to-markdown -->

## 프로젝트 결과

![image](/static/results.png)

## 서비스 아키텍쳐

### 서비스 측면

![image](/static/service_architecture_user.png)

### 기술 측면

![image](/static/service_architecture_tech.png)

### 배포 환경

  * GPU 서버: Tesla V100(32GB memory)
  * 이미지 서버: Google Cloud Storage

## Data

저희는 모든 고화질 가구 데이터셋의 크기가 GPU 서버의 디스크 용량(100GB)을 넉넉히 초과하고, 일반적으로 diffusion model은 학습이 매우 오래 걸린다는 점을 고려하여, 모든 모델을 학습 과정 없이 공개된 checkpoint 사용을 통해 도입하기로 결정했습니다.

아래의 목록은 해당 checkpoint들이 학습에 사용한 데이터셋들입니다.

### LSUN Bedroom

  * LSUN 데이터셋은 10개의 class로 구성되는데, 그 중 침실 데이터를 사용했습니다.
  * Train 데이터: 3,033,042
  * Validation 데이터: 300

### ImageNet

  * ImageNet 데이터셋은 1000개의 class로 구성되어 있습니다.
  * Train 데이터: 1,200,000
  * Validation 데이터: 50,000

### DIV2K

  * 1단계부터 4단계까지 순서대로 해상도에 따라 저장되어 있습니다.
  * Train 데이터: 각 단계당 800
  * Validation 데이터: 각 단계당 100

## Model Pipeline

1. 사용자가 원본 방 사진과 스케치를 추가한 방 사진을 업로드합니다.
2. 사용자가 스케치한 영역을 찾아서 이미지 마스크를 생성합니다.
3. SDEdit: 원본 방 이미지에 스케치의 내용을 추가한 이미지를 80장 합성합니다.
4. CNN: 이미지 마스크 영역에 대한 물체 종류 분류를 진행합니다.
5. 합성된 이미지와 스케치 이미지의 마스크 영역 분류 결과가 비슷한 순으로 합성된 이미지 80장을 정렬합니다.
6. 스케치와 비슷한 색으로 합성된 이미지인지 코사인 유사도로 확인하며 순서대로 4장을 선택합니다.
7. ESRGAN: 선택된 이미지 4장의 해상도를 높입니다.
8. 사용자에게 최종 이미지 4장을 이메일로 보내 줍니다.

### Why SDEdit?

  * Why diffusion model?
    * 새로운 이미지를 생성하려면 generative model이 필요한데, 완성도 높은 결과물을 제공하기 위해서 GAN의 성능을 크게 뛰어넘는 diffusion probabilistic model을 사용해 보고자 결정했습니다.
    * GAN은 diffusion model보다 속도가 빠르다는 장점이 있지만, 정성적인 평가를 해 보면 결과물의 성능이 현저히 떨어지고, 이번 프로젝트에서는 실시간 서비스가 요구되지 않는다고 판단하여, 속도의 이점을 포기하고 diffusion model을 선정했습니다.
  * Why SDEdit?
    * Diffusion model 중에서도, 스케치한 영역에 새로운 물체를 생성할 수 있는 DALLE-2, SDEdit의 두 가지 모델을 고려했습니다.
    * DALLE-2는 pretrained weight이 존재하지 않아서 처음부터 학습시켜야 했는데, 저희가 사용할 V100 GPU 서버로는 학습 시간 및 메모리 관점에서 몹시 힘들 것 같다고 판단하여 모델을 SDEdit으로 선정했습니다.

### Why CNN?

  * Why CNN logit?
    * 합성된 영역이 스케치를 충실히 따랐는지 확인하고자 했습니다.
    * 스케치한 영역과 합성된 영역에 분류 모델을 사용했을 때 같은 물체로 분류되는 경우, 형태가 잘 갖춰진 것으로 판단하기로 결정했습니다.
  * Why cosine similarity?
    * 녹색 의자를 스케치했지만 보라색 의자가 합성된 경우, 합성이 잘못된 것으로 판단하고자 했습니다.
    * RGB 값에 직접 cosine similarity를 적용한다면 비슷한 색상으로 합성되었을 때 점수가 높을 것이라고 생각했습니다.

### Why ESRGAN?

  * 저희는 가장 흔한 super resolution 모델인 EDSR과, 현재 모델 중 가장 성능이 좋은 CAR을 사용하지 않고 ESRGAN을 사용했습니다.
  * EDSR은 일반적으로 성능이 좋았지만, 인접한 픽셀들의 색상이 유사한 경우 경계선을 더욱 뚜렷하게 해 주지는 못하는 경향이 나타났습니다.
  * CAR과 ESRGAN은 육안으로 보았을 때 성능에서 큰 차이가 없었습니다. 그러나 CAR 모델은 메모리 크기가 360MB가 넘는 반면 ESRGAN은 16MB 정도로 20배가 넘는 차이가 났습니다. 따라서 ESRGAN으로 선정했습니다.

#### Original Image

![super-resolution-demo-original](/static/original.png)

#### ESRGAN

![super-resolution-demo-esrgan](/static/esrgan.png)

#### EDSR

![super-resolution-demo-edsr](/static/edsr.png)

#### CAR

![super-resolution-demo-car](/static/car.png)

## Product Serving

### Front-end

React.js를 사용하였습니다.

### Back-end

FastAPI를 사용하였고, 이미지는 Google Cloud Storage에 저장하면서 SQLite를 도입하였습니다. 모델은 백엔드에서 실행되며, 사진 합성이 완료된 경우 사용자에게 이메일을 발송합니다.

## 프로젝트의 장점 및 기대 효과

  * 기존의 인테리어 컨설팅은 비용도 크고 전문 인력을 필요로 하기에, 가구를 바꿔 보는 정도의 간단한 인테리어 컨설팅을 위해서 전문 업체를 찾는 것은 부담스러울 수 있습니다. 사용자들에게 접근성이 높은 웹과, 전문 인력을 필요로 하지 않는 AI 기술을 사용하여 간단하게 배치를 해볼 수 있다는 장점이 있습니다.
  * 현재 가상의 환경에서 가구를 배치하여 인테리어를 할 수 있는 프로그램이 존재합니다. 하지만 어떤 가구를 놓아야 하는지 선택해야 하는 것은 여전히 사용자의 몫입니다. 내일의집은 간단한 스케치만으로 내 방과 어울리는 가구의 배치를 볼 수 있으므로, 가구 선택을 위한 사용자의 고민 시간을 줄여 줄 수 있다는 장점이 있습니다.

## 개선할 점

### 모델 성능 관점

  * 시간이 더 있었다면, 더 많은 실험을 통해 성능을 개선할 수 있을 것입니다.
    * 모델을 직접 학습시킬 수 있을 것입니다.
    * 높은 해상도의 실내 이미지 데이터셋을 확보할 수 있을 것입니다.
    * 현재 CNN으로 처리하고 있는 이미지 선정 과정을 GAN의 discriminator로 처리해 볼 수 있을 것입니다. 인테리어 관련 데이터셋으로 학습시킨 checkpoint가 공개된 GAN 모델이 없어서 시도해 보지 못했는데, 학습시킬 수 있을 것입니다.
  * SDEdit의 결과물 이미지 해상도가 256 * 256이므로, 정사각형 이미지라고 해도 해상력 관점에서 ESRGAN의 최대 이미지 해상도가 1024 * 1024라서, 최고 해상도의 이미지를 생성하지 못합니다. Super-resolution 작업을 4x보다 더 강력하게 수행할 수 있는 모델을 찾을 수 있을 것입니다.
  * 스케치를 특정 프로그램(Procreate 등)으로 할 경우, 원본 이미지에 노이즈가 많이 생기는데, 이 문제가 성능에 미치는 영향을 분석할 수 있을 것입니다.

### 모델 서빙 관점

  * GPU의 한계로 인해 V100 기준으로 10명 이상의 사람이 동시에 사용하기 어려운데, 비용 문제만 해결된다면 auto-scaling GPU 서버를 이용해서 더 많은 사용자에게 동시에 서비스를 제공할 수 있을 것입니다.

### 사용자 경험 관점

  * 웹페이지에서 이미지에 바로 스케치할 수 있도록 웹페이지를 개선할 수 있을 것입니다.
  * 연관 상품을 찾아서 구매 링크를 추천해 줄 수 있을 것입니다.

## Contributors

| 이름 | 캠퍼 ID | GitHub | 역할 |
| ---- | ------ | ------ | ---- |
| 김예원 | T3041 | [*Link*][yewon] | **Back-end(FastAPI, GCS, SQLite), DB 설계**<br>Front-end 코드 리뷰, 모델링 작업 검토 |
| 김주연<br>(Special Thanks) | T3052 | [*Link*][juyeon] | **프로젝트 아이디어 제안 및 고도화**<br>프로젝트 아이디어를 통해 팀원 모집 및 팀 구성 주도 |
| 김주영 | T3053 | [*Link*][juyoung] | **모델링(SDEdit)**, 모델링 코드 리뷰<br>Front-end, Back-end 작업 검토<br>GitHub 관리 |
| 유환규 | T3134 | [*Link*][hwankyu] | **모델링(CNN, ESRGAN)**, 모델링 코드 리뷰<br>Front-end, Back-end 작업 검토 |
| 이수아 | T3153 | [*Link*][sua] | **프론트엔드(React.js)**<br>Back-end 코드 리뷰, 모델링 작업 검토<br>초기 SDEdit 코드 작성 |

## References

  * SDEdit
    * [Paper](https://arxiv.org/abs/2108.01073)
    * [GitHub](https://github.com/ermongroup/SDEdit)
  * [Score Modeling](https://arxiv.org/abs/1907.05600)
  * [Score-Based SDE](https://arxiv.org/abs/2011.13456)

<!-- Links: GitHub Profiles -->
[yewon]: https://github.com/Yewon-dev
[juyeon]: https://github.com/zooyeonii
[juyoung]: https://github.com/nestiank
[hwankyu]: https://github.com/hkyoo52
[sua]: https://github.com/heosuab
