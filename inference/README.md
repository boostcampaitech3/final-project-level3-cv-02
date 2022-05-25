# Inference code for SDEdit

> https://github.com/ermongroup/SDEdit



### #35 (Training data 제작)을 위해 이미지를 따로 저장하는 baseline

* --save1 : 256*256으로 resize된 original image를 저장하는 폴더
* --save2 : 256*256으로 resize된 sketch image를 저장하는 폴더
* --save3 : 256*256의 generated image를 저장하는 폴더
* --num : image filename에 사용되는 변수
  * {args.save1}/bedroom_original_{num}.png
  * {args.save2}/bedroom_sketch_{num}.png
  * {args.save3}/bedroom_generated\_{num*48}.png 부터 {args.save3}/bedroom_generated\_{num\*80-1}까지 생성

**※ num이 0일 경우 generated_image를 0000\~0079까지 생성하고, num이 1일 경우 0048\~0096까지 생성하는 등등 index가 겹쳐서 동일한 폴더에 저장할경우 겹치는 index는 파일을 덮어쓰게 됨. save3를 각각 다르게 설정하여 다른 폴더에 저장하고, 선정한 48장의 이미지만 generated_image 폴더로 옮기는 걸 추천!** 



### How to use main.py

```shell
python main.py --sample_step 10 --t 500 --path1 {ORIGINAL_IMAGE_PATH} --path2 {SKETCH_IMAGE_PATH} --save3 {OUTPUT_FOLDER_NAME} --num {FILE_INDEX_NUM}
```



### How to use inference.sh

~~~shell
# 실행
nohup sh inference.sh > train_log.txt &

# 현재 돌아가고 있는지 확인
ps -ef

# 실행 종료하고 싶을 때 ps -ef에서 PID 확인 후 kill (inference.sh, main.py, sleep 3가지 모두 kill)
kill {PID}
~~~



Resolves #35
