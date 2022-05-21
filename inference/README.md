# Inference code for SDEdit

> https://github.com/ermongroup/SDEdit

### How to use

이 코드는 #23 을 해결하기 위해 작성되었습니다.

1. Execute `git clone https://github.com/ermongroup/SDEdit.git`
2. Replace main.py
3. Replace runners/image_editing.py
4. Execute below for inference

```shell
python main.py --exp ./runs/ --config bedroom.yml --sample -i images --npy_name lsun_edit --sample_step 10 --t 500 --ni --path1 {ORIGINAL_IMAGE_PATH} --path2 {SKETCH_IMAGE_PATH}
```
