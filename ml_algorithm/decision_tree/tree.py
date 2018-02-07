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
    numEntries = len(dataSet)  #样本数
    labelCounts = {}  #key:label，value：counts
    # 为所有类别 labels 创建字典，统计计数
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1

    shannonEnt = 0.0
    for key in labelCounts:
        # p(x) 复用两次，首先计算p(x)
        prob = float(labelCounts[key]) / numEntries  # p(label) label的统计概率
        # 每次循环计算一次独立的乘法，
        # 和上个循环结果相加，实现累加求和，得到期望
        shannonEnt -= prob * log(prob, 2)  # 以2为底数求对数
    return shannonEnt


def createDataSet():
    '''
    dataSet 格式说明：
        一行为一个样本 example
        最后一列为样本标签 label，其余列为特征分量 feature vector,包含一至多个feature
        不同取值为特征分量的不同结点，同一取值为同一结点，结点为特征类型 class（从属于一个feature）
    dataSet 数据格式：
        数据必须是一种由列表元素组成的列表，而且所有的列表元素都要具有相同的数据长度；
        每一行为一个样本，每个样本有1到多个特征分量，按列的形式顺序存储
        样本的最后一个元素(数据集的最后一个列)是当前实例的类别标签。
    '''
    dataSet = [[1, 1, 'yes'], 
               [1, 1, 'yes'], 
               [1, 0, 'no'], 
               [0, 1, 'no'],
               [0, 1, 'no']]
    featNames = ['no surfacing', 'flippers']  #列分量参数意义
    # dataSet2 = copy.deepcopy(dataSet) #内存拷贝，真拷贝
    # dataSet2[0][-1] = 'maybe'
    # print(dataSet,dataSet2)
    return dataSet, featNames


def splitDataSet(dataSet, axis, node):
    '''
    name：结点划分，chooseBestFeatureToSplit()调用
    parameter：
        dataSet: 二维特征集
        axis：列索引，即特征分量索引
        value：分量结点的值，划分依据，featVec[i][axis] 为同一个 value，则该特征样本为同一结点
    principle：
        设 dataSet 中的特征样本为 featVec[i]，
        对给定的 axis 下标，遍历 featVec[axis]，
        选择 featVec[axis]==node 的样本，组成新的 retDataSet ,同样是一个二维 list
    '''
    #1 创建用于存放剔除 featVec[axis] 后的样本列表
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == node:
            #2 遍历 axis 位置，抽取等于 node 的特征样本
            #  这里跳过 featVec[axis]  ，留下了其他分量，这一步保证了找到结点后迭代的收敛
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    '''
    description：以某个特征分量为根结点，标签为分支条件/最终结点。
                找出使分类结果熵减（增益）最大的特征分量。选择决策层的核心算法。
    parameter：[特征分量,label]；
    loop: 
        特征分量，对每个结点统计其特征样本集label的熵，对所有结点做加权和
        计算信息增益（熵差），baseEntropy - 特征分量结点加权Entropy，保留增益最大的特征分量的列索引
    return: 信息增益最大的特征分量索引
    '''
    numFeatures = len(dataSet[0]) - 1  #样本列数
    baseEntropy = calcShannonEnt(dataSet)  #计算原数据熵
    bestInfoGain = 0.0
    bestFeature = -1
    #按列遍历特征分量
    for i in range(numFeatures):
        #1 创建唯一的特征分量列表
        featList = [example[i] for example in dataSet]  #提取全部数据集的第i列元素
        uniqueNodes = set(featList)  # 分支结点，特征分量的结点类型
 
        newEntropy = 0.0
        #2 遍历结点类型，计算的加权信息熵
        for node in uniqueNodes:
            subDataSet = splitDataSet(dataSet, i, node)
            prob = len(subDataSet) / float(len(dataSet))  #结点权重
            # 熵 = 各子结点信息熵加权和。若分支类别比较纯，总熵低，熵减，（原始熵和它做差）增益大；若分支类别还是很多，总熵高，熵增，增益小，且可能为负。
            # 熵函数两端都属于低熵，类别纯；越到中间部分熵越高，类混杂；不同类的比例越均匀，信息熵越大。
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy  #信息增益
        if (infoGain > bestInfoGain):
            #3 记录最大的信息增益，及对应的特征分量索引
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def majorityCnt(labelList):
    '''
    labels数量统计并排序，返回数量最多的类型名
    '''
    # 统计类名频数
    labelCount = {}
    for vote in labelList:
        if vote not in labelCount.keys():
            labelCount[vote] = 0
        labelCount[vote] += 1
    # 对 labelCount 排序
    sortedLabelCount = sorted(
        labelCount.items(), key=lambda x: x[1], reverse=True)
    return sortedLabelCount[0][0]  #返回数量最多的label


# def chooseBestFeatureTest():
#     dataSet_1,labels = createDataSet()
#     chooseBestFeatureToSplit(dataSet_1)
# chooseBestFeatureTest()


def createTree(dataSet, featNames = None):
    '''
    name: 递归创建树，决策树主程序
    description:
        对每一组（子）数据集 ，查找最佳划分特征分量，构建一层树，
        对分量各结点 createTree()，输入样本集需删除该分量
        直到（子）数据集 label 一致，或特征分量删减结束为止
    param: 
        dataSet: 样本集，不变变量,每一行为一个样本
        featNames: 特征名称列表，可变变量，请使用 featNames.copy() 作为入参
    '''
    labelList = [example[-1] for example in dataSet]
    # 迭代结束条件1：label 完全相同，统计 labelList[0]，返回label
    if labelList.count(labelList[0]) == len(labelList):
        return labelList[0] #{结点: 标签}
    # 迭代结束条件2：遍历完所有特征分量，返回标签最多的 label
    if len(dataSet[0]) == 1:
        return majorityCnt(dataSet[0]) #{结点: 标签}
    bestFeatIndex = chooseBestFeatureToSplit(dataSet)
    bestFeatName = featNames[bestFeatIndex] # 特征分量名称
    myTree = {bestFeatName: {}}  # 创建一层树，{最佳特征：{结点：树}}
    # 得到列表包含的所有属性值
    del (featNames[bestFeatIndex])  # 从特征分量名称里删除这维特征分量，使 featNames 收敛
    featValues = [example[bestFeatIndex] for example in dataSet]
    uniqueNodes = set(featValues)  # 分支结点
    # 对各结点 createTree，进入 createTree() 递归迭代
    for node in uniqueNodes:
        subLabel = featNames[:]
        # 构建树，对每个结点子数据集 create tree
        # 使用二维字典{bestFeatName:{node:createTree(), node: label}}
        myTree[bestFeatName][node] = createTree(
            splitDataSet(dataSet, bestFeatIndex, node), subLabel)
    return myTree


def createTreeTest():
    dataSet_1, featNames = createDataSet()
    myTree = createTree(dataSet_1, featNames)
    print(myTree)
    #{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}


# createTreeTest()
