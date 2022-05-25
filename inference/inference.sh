#!/bin/sh

nohup python main.py --sample_step 10 --t 500 --path1 ./custom_images/bedroom00_original.PNG --path2 ./custom_images/bedroom00_sketch.PNG --save3 ./bedroom00_result --num 0 &
# 약 4분*10iter=40m, 동시에 실행되지 않도록 40분간 sleep
sleep 40m
nohup python main.py --sample_step 10 --t 500 --path1 ./custom_images/bedroom01_original.PNG --path2 ./custom_images/bedroom01_sketch.PNG --save3 ./bedroom01_result --num 1 &
sleep 40m
nohup python main.py --sample_step 10 --t 500 --path1 ./custom_images/bedroom02_original.PNG --path2 ./custom_images/bedroom02_sketch.PNG --save3 ./bedroom02_result --num 2 &
sleep 40m
nohup python main.py --sample_step 10 --t 500 --path1 ./custom_images/bedroom03_original.PNG --path2 ./custom_images/bedroom03_sketch.PNG --save3 ./bedroom03_result --num 3 &
sleep 40m
nohup python main.py --sample_step 10 --t 500 --path1 ./custom_images/bedroom04_original.PNG --path2 ./custom_images/bedroom04_sketch.PNG --save3 ./bedroom04_result --num 4 &
sleep 40m
nohup python main.py --sample_step 10 --t 500 --path1 ./custom_images/bedroom05_original.PNG --path2 ./custom_images/bedroom05_sketch.PNG --save3 ./bedroom05_result --num 5 &
sleep 40m
nohup python main.py --sample_step 10 --t 500 --path1 ./custom_images/bedroom06_original.PNG --path2 ./custom_images/bedroom06_sketch.PNG --save3 ./bedroom06_result --num 6 &
sleep 40m
nohup python main.py --sample_step 10 --t 500 --path1 ./custom_images/bedroom07_original.PNG --path2 ./custom_images/bedroom07_sketch.PNG --save3 ./bedroom07_result --num 7 &
sleep 40m
nohup python main.py --sample_step 10 --t 500 --path1 ./custom_images/bedroom08_original.PNG --path2 ./custom_images/bedroom08_sketch.PNG --save3 ./bedroom08_result --num 8 &
sleep 40m
nohup python main.py --sample_step 10 --t 500 --path1 ./custom_images/bedroom09_original.PNG --path2 ./custom_images/bedroom09_sketch.PNG --save3 ./bedroom09_result --num 9 &