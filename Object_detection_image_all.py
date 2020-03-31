######## Image Object Detection Using Tensorflow-trained Classifier #########
#
# Author: Joy Lin
# Date: 2/21/20
# Description: 
# 將原本的 Object_detection_image.py 包成 function，利用本程式跑迴圈一次處理

import glob, os
import Object_detection_image as odi
import xml_to_txt as xtt


# List possible extensions
ext = [".jpg", ".jpeg", ".png"]
        
# Loop the images
for f in os.listdir("images/test"):
    # Generate .txt files of groundtruth images - 2020.3.12 Joy
    if f.endswith(".xml"):
        xtt.xml_to_txt(f)
    if f.endswith(tuple(ext)):  #tuple(ext)
        odi.object_detection_image(f)

print('Finished.')