# Back-end

### Poetry 가상환경 활성화

```shell
cd backend \
poetry install \    # 의존성 패키지 설치
poetry shell        # 가상환경 활성화
```

### Run

```shell
python3 -m app
```

### Google Cloud Storage 사용을 위한 환경 변수 설정 방법

1. key파일(json)을 구글드라이브에서 다운받고, local에 저장 (프로젝트 repo X)
2. '.env' 파일은 backend 폴더 하단에 생성 후 아래 코드 삽입
```shell 
# environment variables
GOOGLE_APPLICATION_CREDENTIALS = {json_location} ## ex) /opt/ml/~~.json
```
3. 저장 후 run
