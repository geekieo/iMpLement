#!/usr/bin/python3
'''
kNN: k nearest neighbors (k 近邻)

Input:  inputData: vector to compare to existing dataset(1×N vector)
        dataSet： existing dataset. size: M, number: N (N×M)
        labels:   dataset labels (1XM vector)
        k:        number of neighbors to use for comparision

Output: the most popular(has more neighbors) class label
'''

from numpy import *
import operator
import os
# 绘图库
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# create a dataset which contains 4 samples with 2 classes
def createDataSet():
    # create a matrx: each row as a sample
    group = array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


# classify using kNN k近邻分类算法
def kNNClassify(inputData, dataSet, labels, k):
    # the number of row
    dataSetSize = dataSet.shape[0]
    # 1 calculate Euclidean distance
    # tile(A,(x,y)) A沿各个维度复制x或y次,x为行，y为列
    # sum(axis=0) 叠加到一行，列内求和; sum(axis=1) 叠加到一列，行内求和; sum()全部相加
    diffMat = tile(inputData,
                   (dataSetSize, 1)) - dataSet  # subtract element-wise
    sqDiffMat = diffMat**2  # squared for the subtract
    sqDistances = sqDiffMat.sum(axis=1)  # sum is performed by row
    distances = sqDistances**0.5  # distances from inputData to each point in dataSet
    # 2 sort the distance  两行
    # argsort() returns the indices that would sort an array in a ascending order
    #返回矩阵升序排序的索引,如 array([5,2,4])返回 array([3,1,2])
    sortedDistIndicies = distances.argsort() 
    classCount = {}
    for i in range(k):
        # 3 choose the label of the min k distance
        voteIlabel = labels[sortedDistIndicies[i]]
        # 4 count the times labels occur
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # 5 the max voted class will return, use sorted()
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True)  # sort
    return sortedClassCount[0][0]


# ========== hand writing digits classification - start ========== #
# convert image to vector
def img2vector(filename):
    rows = 32
    cols = 32
    imgVector = zeros((1, rows * cols))  # initialize vector
    fileIn = open(filename)
    for row in range(rows):
        lineStr = fileIn.readline()
        for col in range(cols):
            imgVector[0, row * 32 + col] = int(lineStr[col])
    return imgVector


# load dataSet
def loadDataSet():
    ## step 1: Getting training set
    print('- Getting training set...')
    dataSetDir = 'data/'
    trainingFileList = os.listdir(
        dataSetDir + 'training_digits')  # load training set
    numSamples = len(trainingFileList)

    train_x = zeros((numSamples, 1024))
    train_y = []
    for i in range(numSamples):
        filename = trainingFileList[i]
        # get train_x
        train_x[i, :] = img2vector(dataSetDir + 'training_digits/%s' % filename)
        # get label from file name such as '1_18.txt'
        label = int(filename.split('_')[0])  # return 1
        train_y.append(label)

    ## step 2: Getting testing set
    print('- Getting test set...')
    testingFileList = os.listdir(dataSetDir + 'test_Digits')  # load test set
    numSamples = len(testingFileList)
    test_x = zeros((numSamples, 1024))
    test_y = []
    for i in range(numSamples):
        filename = testingFileList[i]

        # get train_x
        test_x[i, :] = img2vector(dataSetDir + 'test_Digits/%s' % filename)

        # get label from file name such as '1_18.txt'
        label = int(filename.split('_')[0])  # return 1
        test_y.append(label)

    return train_x, train_y, test_x, test_y


# test hand writting class
def testHandWritingClass():
    ## step 1
    print('step 1: load data...')
    train_x, train_y, test_x, test_y = loadDataSet()

    ## step 2
    print('step 2: train...')
    pass

    ## step 3
    print('step 3: testing...')
    numTestSamples = test_x.shape[0]
    matchCount = 0
    for i in range(numTestSamples):
        predict = kNNClassify(test_x[i], train_x, train_y, 3)
        if predict == test_y[i]:
            matchCount += 1
    accuracy = float(matchCount) / numTestSamples

    ## step 4
    print('step 4: show the result...')
    print('The classify accuracy is: %.2f%%' % (accuracy * 100))


# ========== hand writing digits classification- end ========== #


# ========== dating classification - start ========== #
def file2matrix(filename):
    # transform datingTestSet.txy to matrix
    file = open(filename)
    arrayOfLines = file.readlines()
    numberOfLine = len(arrayOfLines)  #1 得到文件行数
    returnMat = zeros((numberOfLine, 3))  #2 创建返回的Numpy矩阵
    classLabelVector = []  # 标签存到一个向量中，初始化标签向量
    index = 0
    #3 解析文件数据到里列表
    for line in arrayOfLines:
        line = line.strip()  #去除行尾的回车
        listFromLine = line.split('\t')  #以\t为分隔符，将一行数据分割成一个元素列表
        returnMat[index, :] = listFromLine[0:3]  #将前三列存储到特征矩阵的第 index 行
        classLabelVector.append(listFromLine[-1])  #将最后一列存储到标签向量中
        index += 1
    return returnMat, classLabelVector


def drawPlot2D(array_x, array_y, labels):
    # 2D 作图
    # Make a scatter plot of array_x vs array_y
    # 条件：len(array_x) = len(array_y)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # Marker size is scaled by 15.0*array(labels), marker color is mapped to 15.0*array(labels)
    ax.scatter(array_x, array_y, 15.0 * array(labels),
               15.0 * array(labels))  # x轴，y轴，size， color
    plt.show()


def drawPlot3D(array_x, array_y, array_z, labels):
    # 3D 作图
    # 条件：len(array_x) = len(array_y) = len(array_z)
    # labels = {1，2，3}

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(array_x, array_y, array_z, c=255 * 10 * array(labels))
    ax.set_xlabel('Flight mileage')
    ax.set_ylabel('Game time')
    ax.set_zlabel('Icecream per week')
    plt.show()


def autoNorm(dataSet):
    # 特征数值归一化到[0,1]
    # 计算公式：newValue = (oldValue – min) / (max – min)
    # dataSet 中一行为一个样本特征组，每个样本特征组包含多列独立特征值
    # 1 向量部分
    minVals = dataSet.min(0)  # 取每列特征的最小值,得到一个每列为最小值的行向量
    maxVals = dataSet.max(0)  # 取每列特征的最大值,得到一个每列为最大值的行向量
    ranges = maxVals - minVals  # 计算特征组的数值范围向量

    # 2 矩阵部分
    normDataSet = zeros(shape(dataSet))  # 结果变量初始化
    m = dataSet.shape[0]  # 行数，样本特征组组数
    minValsMat = tile(minVals, (m, 1))
    normDataSet = (dataSet - minValsMat) / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def classifyPerson():
    # 对新人特征并做 knn 分类
    # input() 允许用户输入文本行命令并返回用户所输入的内容
    # raw_input() 将所有输入作为字符串看待，返回字符串类型
    labelList = ['不会喜欢', '有一点可能会喜欢', '有很大可能会喜欢']
    ffMiles = 8000
    percentTats = 10
    iceCream = 2
    # while(ffMiles is empty):
    #     ffMiles = float(input('每年攒下的飞机里程数(km)? 参考范围:0~10000: '))
    # while(percentTats is empty):
    #     percentTats = float(input('玩游戏的时间占比(%)? 参考范围:0~20: '))
    # while(iceCream is empty):
    #     iceCream = float(input('每年吃掉的冰淇淋(L)? 参考范围:0~2: '))
    datingMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = kNNClassify((inArr - minVals) / ranges, normMat,
                                   datingLabels, 3) # 结果在 {1,2,3} 之中
    print('你喜欢这个人的可能是：', labelList[classifierResult - 1])
