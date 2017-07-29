from math import log
import copy


def calcShannonEnt(dataSet):
    '''
    description：计算给定数据集的 label 香浓熵
    formula：H = -∑ p(x)log p(x)
    note：
        dataSet 中最后一列为 label，为主要统计对象。
        其余列为特征，此处无用。
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
    '''
    格式说明：
        按行看，最后一列为样本标签，其余列为特征分量
        按列看，不同取值为特征分量的不同结点，同一取值为同一结点
    dataSet数据格式：
        数据必须是一种由列表元素组成的列表，而且所有的列表元素都要具有相同的数据长度；
        每一行为一个样本，每个样本有1到多个特征分量，按列的形式顺序存储
        样本的最后一个元素(数据集的最后一个列)是当前实例的类别标签。
    '''
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
    loop: 
        特征分量，对每个结点统计其特征样本集label的熵，对所有结点做加权和
        计算信息增益（熵差），baseEntropy - 特征分量结点加权Entropy，保留增益最大的特征分量的列索引
    return: 信息增益最大的特征分量索引
    '''
    numFeatures = len(dataSet[0]) - 1 #样本列数
    baseEntropy = calcShannonEnt(dataSet) #计算原数据熵
    bestInfoGain = 0.0
    bestFeature = -1
    #按列遍历特征分量
    for i in range(numFeatures):
        #1 创建唯一的分类标签列表
        #  提取数据集的列元素
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList) #归纳结点类型
        
        newEntropy = 0.0
        #2 遍历结点类型，计算的加权信息熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value) 
            prob = len(subDataSet)/float(len(dataSet)) #结点权重
            newEntropy += prob * calcShannonEnt(subDataSet) #结点信息熵加权和，同类有序，分类减熵，加权和不会大过比原始信息熵
        infoGain = baseEntropy - newEntropy #信息增益
        if(infoGain>bestInfoGain):
            #3 记录最大的信息增益，及对应的特征分量索引
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def test():
    dataSet_1,labels,ddataSet_2 = createDataSet()
    chooseBestFeatureToSplit(dataSet_1)

test()