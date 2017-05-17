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


def kNNClassify(inputData, dataSet, labels, k):
    # the number of row
    dataSetSize = dataSet.shape[0]
    # 1 calculate Euclidean distance
    # tile(A,(x,y)) A沿各个维度复制x或y次,x为行，y为列
    # sum(axis=1) 行内求和，按照行的方向相加,sum(axis=0) 列内求和，按照列的方向相加，sum()全部相加  
    diffMat = tile(inputData, (dataSetSize, 1)) - dataSet  # subtract element-wise
    sqDiffMat = diffMat**2                      # squared for the subtract
    sqDistances = sqDiffMat.sum(axis=1)         # sum is performed by row 
    distances = sqDistances**0.5                # distances from inputData to each point in dataSet
    # 2 sort the distance  两行
    # argsort() returns the indices that would sort an array in a ascending order 
    sortedDistIndicies = distances.argsort() #返回矩阵升序排序的索引,如 array([5,2,4])返回 array([3,1,2])
    classCount = {}
    for i in range(k):
        # 3 choose the label of the min k distance
        voteIlabel = labels[sortedDistIndicies[i]]
        # 4 count the times labels occur
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # 5 the max voted class will return, use sorted()
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True) # sort
    return sortedClassCount[0][0]
