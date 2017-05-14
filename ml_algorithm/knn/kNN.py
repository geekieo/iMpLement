'''
kNN: k nearest neighbors (k 近邻)
     
Input:  newInput: vector to compare to existing dataset(1×N vector)
        dataSet： existing dataset. size: M, number: N (N×M)
        labels:   dataset labels (1XM vector)
        k:        number of neighbors to use for comparision

Output: the most popular(has more neighbors) class label
'''

from numpy import *
import operator

# create a dataset which contains 4 samples with 2 classes  
def createDataSet():
    # create a matrx: each row as a sample
    group = array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
    labels = ['A','A','B','B']
    return group, labels

# classify using kNN
def kNNClassify(newinput, dataSet, labels, k):