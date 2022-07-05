# Back-end

### Poetry 가상 환경 활성화

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

1. Key 파일(json)을 구글드라이브에서 다운 받고, local에 저장 (프로젝트 repo X)
2. Backend 폴더 내에 '.env' 파일 생성 후 아래 코드 삽입

```shell
# Environment variables
GOOGLE_APPLICATION_CREDENTIALS = {json_location}
```

3. 저장 후 run
