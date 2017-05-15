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
    labels = ['A', 'A', 'B', 'B']
    return group, labels

# classify using kNN


def kNNClassify(inData, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # 1 距离计算 三行
    diffMat = tile(inData, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    # 2 选择距离最小的k个点 两行
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
                              # 3 排序
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
