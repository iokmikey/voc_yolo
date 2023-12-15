"""Configurations
File paths to labels and image/xml files
"""
LABEL_DIR = "../labels"      #需要yolo2voc 时候  则yolo的labels，放这   反之 voc2yolo  则是转化后保存位置    
IMAGE_DIR = "../images"    #图片地址
XML_DIR = "../res"     #需要yolo2voc 时候 则是转化后保存位置 放这   反之 voc2yolo 则voc的xml，

names = [    #数据集类别
    "face"
 
]
