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

# classify using kNN 分类器实现


def kNNClassify(inData, dataSet, labels, k):
    # the number of row
    dataSetSize = dataSet.shape[0]
    # 1 calculate Euclidean distance
    # 通过重复迭代构造训练集矩阵
    diffMat = tile(inData, (dataSetSize, 1)) - dataSet  # subtract element-wise
    sqDiffMat = diffMat**2                              # squared for the subtract
    # sum is performed by row
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    # 2 sort the distance  两行
    # argsort() returns the indices that would sort an array in a ascending order
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        # 3 choose the min k distance
        voteIlabel = labels[sortedDistIndicies[i]]
        # 4 count the times labels occur
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # 5 the max voted class will return, use sorted()
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
