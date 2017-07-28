"""
dataSet数据格式：
1. 数据必须是一种由列表元素组成的列表，而且所有的列表元素都要具有相同的数据长度；
2. 数据的最后一列(每个实例的最后一个元素)是当前实例的类别标签。
"""


from math import log
import copy


def calcShannonEnt(dataSet):
    '''
    计算给定数据集合的香浓熵
    类别标签为 dataSet 的最后一列
    计算公式为：H = -∑ p(x)log p(x)
    dataSet 中最后一列为 label，其余列为特征值
    '''
    numEntries = len(dataSet)   #样本数
    labelCounts = {}    #key:label，value：counts
    # 为所有类别创建字典 label:统计计数(5行)
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel]+=1

    shannonEnt = 0.0
    for key in labelCounts:
        # p(x) 复用两次，首先计算p(x)
        prob = float(labelCounts[key])/numEntries # p(label) label的统计概率
        # 每次循环计算一次独立的乘法，
        # 和上个循环结果相加，实现累加求和，得到期望
        shannonEnt -= prob*log(prob,2) # 以2为底数求对数
    return shannonEnt


def createDataSet():
    dataSet = [ [1, 1, 'yes'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    dataSet2 = copy.deepcopy(dataSet) #内存拷贝，真拷贝
    dataSet2[0][-1] = 'maybe'
    return dataSet, labels, dataSet2


def splitDataSet(dataSet, axis, value):
    '''
    name：结点划分，子核心步骤
    parameter：
        dataSet: 二维特征集
        axis：列索引，即特征分量索引
        value：分量结点的值，划分依据，featVec[i][axis] 为同一个 value，则该特征样本为同一结点
    principle：设 dataSet 中的特征样本为 featVec[i]，
    对给定的 axis 下标，遍历 featVec[axis]，
    选择 featVec[axis]==value 的样本，组成新的 retDataSet ,同样是一个二维 list
    '''     
    #1 创建用于存放剔除 featVec[axis] 后的样本列表
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis] == value:
            #2 遍历 axis 位置，抽取等于 value 的特征样本
            #  这里跳过 featVec[axis]  ，留下了其他分量，这一步保证了找到结点后迭代的收敛
            reducedFeatVec = featVec[:axis] 
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    '''
    description：找出使分类结果熵最大的特征分量，这是决策树的核心步骤
    parameter：[特征分量,label]
    step: 计算信息增益（熵差），baseEntropy - 特征分量Entropy，选择增益最大的为最佳决策划分方式
    '''
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet) #计算原数据熵
    bestInfoGain = 0.0
    bestFeature = -1
    #遍历所有特征
    for i in range(numFeatures):
        #1 创建唯一的分类标签列表
        feaList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        
        newEntropy = 0.0
        #2 计算每种划分结果的信息熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value): 
            prob = len(subDataSet)/float(len(dataSet)) #结点权重
            newEntropy += prob * calcShannonEnt(subDataSet) #结点信息熵加权和，同类有序，分类减熵，加权和不会大过比原始信息熵
        infoGain = baseEntropy - newEntropy #信息增益
        if(infoGain>bestInfoGain):
            #3 记录最好的信息增益
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature
