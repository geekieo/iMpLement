from math import log
import copy

'''
计算给定数据集合的香浓熵
计算公式为：H = -∑ p(x)log p(x)
dataSet 中最后一列为 label，其余列为特征值
'''
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    # 为所有类别创建字典 label:统计计数(5行)
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel]+=1
    shannonEnt = 0.0
    for key in labelCounts:
        # p(x) 复用两次，首先计算p(x)
        prob = float(labelCounts[key])/numEntries # p(label_key)概率值
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
    样本处理
    设 dataSet 中的样本为 featVec，
    对给定的 axis 下标，遍历 featVec[axis]，
    跳过 featVec[axis]==value 的值，提取其他位置元素，组成新的 list
    '''     
    #1 创建用于存放剔除 featVec[axis] 后的样本列表
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis] == value:
            #2 遍历 axis 位置，跳过等于value的值，提取其他位置元素，组成新 list
            reducedFeatVec = featVec[:axis] # 不包括 axis
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    '''
    数据划分（核心步骤）
    遍历特征，根据信息增益，选择最佳决策划分方式
    '''
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bastInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        #1 创建唯一的分类标签列表
        feaList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        
        newEntropy = 0.0
        #2 计算每种划分结果的信息熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value):
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if(infoGain>bestInfoGain):
            #3 记录最好的信息增益
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature
