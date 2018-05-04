import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import os
import random

BATCH_SIZE = 3

img_dir_path = "D:\\Program\\PythonWorkspace\\ocr_tensorflow_cnn\\srcImage\\trainning-data\\"

for parent, dirnames, filenames in os.walk(img_dir_path):
    x = random.randint(0, len(filenames) - 1)
    print(filenames[x])
