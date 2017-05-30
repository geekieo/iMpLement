from math import log

'''
计算给定数据集合的香浓熵
'''
@staticmethod
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts{}
    # 为所有可能分类创建字典(5行)
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.key():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel]+=1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob*log(prob,2) # 以2为底数求对数
    return shannonEnt
