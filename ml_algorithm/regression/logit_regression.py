"""
逻辑回归梯度上升，求分类线
"""
from numpy import *

def sigmoid(inX):
    '''
    函数：f(z) = 1 / (1 + exp( − z))
    导数：f(z)' = f(z)(1 − f(z))
    '''
    return 1.0 / (1 + exp(-inX))


def gradAscent(dataMatIn, labels):
    '''
    dataMatIn 为二维的numpy矩阵
    '''
    # 转换为 NumPy 矩阵格式
    dataMatrix = mat(dataMatIn)
    labelMat = mat(labels).transpose()

    m, n = shape(dataMatrix)  #获取行列长度，m个样本，n个特征
    alpha = 0.001  #步长
    maxCycles = 5000  #最大迭代次数
    weights = ones((n, 1))  #初始化回归函数系数，n行1列，n为特征列数，列数包含bias常数项

    for k in range(maxCycles):
        # 矩阵相乘，对每个样本的特征项求加权和，结果再输入sigmoid
        h = sigmoid(dataMatrix * weights) # h为m行1列矩阵，没有sigmoid为线性回归
        error = (labelMat - h)
        weights = weights + alpha * dataMatrix.transpose() * error # 得益于 sigmoid 求导
        if abs(sum(error)/len(error)) < 0.01: # 迭代结束条件2：误差小于1%
            break
    return weights


def loadDataSet():
    dataMat = []
    labelMat = []
    fr=open('regression/testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])]) # 1.0为bias项
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def test():
    dataArr, labelMat = loadDataSet()
    weights = gradAscent(dataArr, labelMat)
    print(weights)
    # maxCycles=500， weights == [[ 4.12414349] /n[ 0.48007329] /n[-0.6168482 ]]
test()