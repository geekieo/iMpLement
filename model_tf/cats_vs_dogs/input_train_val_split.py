# By @geekieo
# geekieo@hotmail.compile
# reference: https://www.youtube.com/channel/UCVCSn4qQXTDAtGWpWAe4Plw

# The aim of this project is to use Tensorflow to process our data.
#   - input_train_val_split: read in data; split data into training sets and validation sets; generate batches
#   - model: build the model architecture
#   - train_and_val: train and validate
# use Python 3.5, Tensorflow 1.3, cuda 8.0
# gpu gt750m

# data: cats vs. dogs from Kaggle
# Download link: https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data
# data size: {train set: 544MB, 25000 images; test set: 271MB,12500 images}

# How to run?
# 1. run the train_and_val.py once
# 2. call the run_training() in the console to train the model

# Note:
# restart your kenel to train the model multiple times
# in order to clear all the variables in memory
# otherwise errors may occur, e.g.:conv1/weights/bias already exist

import tensorflow as tf 
import numpy as np 
import os
import math

# you need to change this to your data directory
train_dir = "D:\\Documents\\PySpace\\dataset\\cats_vs_dogs\\train\\"

def get_files(file_dir, ratio):
    """
    Args:
        file_dir: file directory
        ratio: ratio of validation set in train set
    Return:
        list of images directory and labels
    """
    cats = []
    label_cats = []
    dogs = []
    label_dogs = []
    # 解析文件名，划分正负样本
    with open(file_dir) as file:
        name = file.split(sep='.')
        if name[0] == 'cat':
            cats.append(file_dir+file)
        else:
            dogs.append(file_dir+file)
    label_cats = [0]*len(cats) #label_cats=[0 for _ in range(len(cats))]
    label_dogs = [1]*len(dogs)
    print('There are %d cats\nThere are %d dogs'%len(cats),len(dogs))

    # 用numpy实现样本随机划分
    image_list = np.hstack((cats,dogs))
    label_list = np.hstack((label_cats,label_dogs))

    image_label_pair = np.array([image_list,label_list])
    image_label_pair = image_label_pair.transpose()
    np.random.shuffle(image_label_pair)

    ran_image_list = image_label_pair[:,0]
    ran_label_list = image_label_pair[:,1]
