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
train_dir = "D://Documents//PySpace//dataset//cats_vs_dogs//train//"

def get_files(path, ratio):
    """
    Args:
        path: file directory
        ratio: ratio of validation set in train set
    Return:
        list of images directory and labels
    """
    cats = []
    label_cats = []
    dogs = []
    label_dogs = []
    # analysis filename, split positive and negative samples 
    # for file in os.listdir(path):
    #     name = file.split(sep='.')
    #     if name[0] == 'cat':
    #         #cats.append(path+file)
    #         cats.append(os.path.join(path, file))
    #     elif name[0] == 'dog':
    #         #dogs.append(path+file)
    #         dogs.append(os.path.join(path, file))
    split_samples(train_dir, cats, dogs)

    label_cats = [0]*len(cats) #label_cats=[0 for _ in range(len(cats))]
    label_dogs = [1]*len(dogs)
    print('There are %d cats\nThere are %d dogs'%(len(cats),len(dogs)))

    # use numpy to split samples at random
    image_list = np.hstack((cats,dogs))
    label_list = np.hstack((label_cats,label_dogs))

    image_label_pair = np.array([image_list,label_list])
    image_label_pair = image_label_pair.transpose()
    np.random.shuffle(image_label_pair)

    ran_image_list = image_label_pair[:,0]
    ran_label_list = image_label_pair[:,1]

    n_sample = len(ran_image_list)  #25000
    n_val = math.ceil(n_sample*ratio)   # number of validation set, round up to a integer
    n_tra = n_sample - n_val #number of train set

    tra_images = ran_image_list[0:n_tra]
    tra_labels = ran_label_list[0:n_tra]
    val_images = ran_image_list[n_tra:]
    val_images = ran_label_list[n_tra:]

    return tra_images,tra_labels,val_images,val_images


def split_samples(path, cats, dogs):
    """
    Args:
        path: path of folders
        cats: path of cat files
        dogs: path of dog files
    Return:
        list of cat or dog files in folder and subfolder
    """
    for file in os.listdir(path):
        file_path = os.path.join(path,file) # maybe a file, maybe a folder
        if os.path.isdir(file_path):
            split_samples(file_path, cats, dogs) # if file_path is a path of folder
        else:
            name = file.split(sep='.') # anlysis filename
            if name[0] == 'cat':
                #cats.append(path+file)
                cats.append(os.path.join(path, file))
            elif name[0] == 'dog':
                #dogs.append(path+file)
                dogs.append(os.path.join(path, file))


if __name__ == "__main__":
    tra_images,tra_labels,val_images,val_image=get_files(train_dir,0.2)
