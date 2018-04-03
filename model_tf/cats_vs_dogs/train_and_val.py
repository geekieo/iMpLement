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

import os
import numpy as np
import tensorflow as tf
import input_train_val_split as input
import model

N_CLASSES = 2
IMG_W = 208 # resize the image
IMG_H = 208
RATIO = 0.2
BATCH_SIZE = 25
CAPACITY = 2000
MAX_STEP = 1000
LEARNING_RATE = 0.0001

def run_training():
    # you need to change this to your data directory
    train_dir = "D://Documents//PySpace//dataset//cats_vs_dogs//train//"

    logs_train_dir = ".//logs//train"
    logs_val_dir = ".//logs//val"

    tra_images, tra_labels, val_images, val_images = input.get_files(train_dir,RATIO)

