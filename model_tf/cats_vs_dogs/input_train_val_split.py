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
    split_samples(train_dir, cats, dogs)

    label_cats = [0] * len(cats)  # label_cats=[0 for _ in range(len(cats))]
    label_dogs = [1] * len(dogs)
    print('There are %d cats\nThere are %d dogs' % (len(cats), len(dogs)))

    # use numpy to split samples at random
    image_list = np.hstack((cats, dogs))
    label_list = np.hstack((label_cats, label_dogs))

    image_label_pair = np.array([image_list, label_list])
    image_label_pair = image_label_pair.transpose()
    np.random.shuffle(image_label_pair)

    ran_image_list = image_label_pair[:, 0]
    ran_label_list = image_label_pair[:, 1]

    n_sample = len(ran_image_list)  # 25000
    n_val = math.ceil(n_sample * ratio)  # number of validation set, round up to a integer
    n_tra = n_sample - n_val  # number of train set

    tra_images = ran_image_list[0:n_tra]
    tra_labels = ran_label_list[0:n_tra]
    val_images = ran_image_list[n_tra:]
    val_images = ran_label_list[n_tra:]

    return tra_images, tra_labels, val_images, val_images


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
        file_path = os.path.join(path, file)  # maybe a file, maybe a folder
        if os.path.isdir(file_path):
            split_samples(file_path, cats, dogs)  # if file_path is a path of folder
        else:
            name = file.split(sep='.')  # anlysis filename
            if name[0] == 'cat':
                # cats.append(path+file)
                cats.append(os.path.join(path, file))
            elif name[0] == 'dog':
                # dogs.append(path+file)
                dogs.append(os.path.join(path, file))


def get_batch(image, label, image_W, image_H, batch_size, capacity):
    """
    Description:
        get image data by image dir
    Args:
        image: image dir, list type
        label: image label, list type
        image_W: image width
        image_H: image height
        batch_size: batch size
        capacity: the maximum elements in queue
    Return:
        image_batch: 4D tensor [batch_size, width, height, 3], dtype=tf.float32
        label_batch: 1D tensor [batch_size], dtype=tf.int32
    """
    # convert numpy type to tensorflow type
    image = tf.cast(image, tf.string)
    label = tf.cast(label, tf.int32)

    # make an input queue
    input_queue = tf.train.slice_input_producer([image, label])

    label = input_queue[1]
    image_contents = tf.read_file(input_queue[0])
    image = tf.image.decode_jpeg(image_contents, channels=3)
    ####################################
    # data argumentation should code here
    ####################################
    image = tf.image.resize_image_with_crop_or_pad(image, image_H, image_W)
    image = tf.image.per_image_standardization(image)
    # if image dir is not randomized use tf.train.shuffle_batch()
    image_batch, label_batch = tf.train.batch([image, label],
                                              batch_size=batch_size,
                                              num_threads=64,
                                              capacity=capacity)
    label_batch = tf.reshape(label_batch,[batch_size])
    return image_batch, label_batch


#%% TEST

import matplotlib.pyplot as plt

BATCH_SIZE = 2
CAPACITY = 256
IMG_H = 208
IMG_W = 208
train_dir = "D://Documents//PySpace//dataset//cats_vs_dogs//train//"
tra_images, tra_labels, val_images, val_images = input.get_files(train_dir,RATIO=0.2)
image_batch, label_batch = get_batch(tra_images,tra_labels,IMG_W,IMG_H,BATCH_SIZE,CAPACITY)

with tf.Session() as sess:
    i = 0
    coord = tf.train.Coordinator()  # in queue
    threads = tf.train.start_queue_runners(coord=coord) # out queue
    try:
        while not coord.should_stop() and i<1




if __name__ == "__main__":
    tra_images, tra_labels, val_images, val_image = get_files(train_dir, 0.2)
