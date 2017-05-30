from math import log

'''
计算给定数据集合的香浓熵
计算公式为：H = -∑ p(x)log p(x)
dataSet 中最后一列为 label，其余列为特征值
'''
@staticmethod
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    # 为所有类别创建字典 label:统计计数(5行)
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.key():
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
