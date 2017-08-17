"""
逻辑回归梯度上升，求分类线
"""
from numpy import *
import matplotlib.pyplot as plt


def sigmoid(inX):
    '''
    函数: f(x) = 1 / (1 + exp(−x))
    导数: f(x)' = f(x)(1 − f(x))
    作用: 将(-∞，∞)映射到(0,1)，使输出结果和标签区间一致
    '''
    return 1.0 / (1 + exp(-inX))


def gradAscent(dataMatIn, labels, plotLive = False):
    '''
    dataMatIn 为二维的numpy矩阵
    '''
    # 转换为 NumPy 矩阵格式
    dataMatrix = mat(dataMatIn)
    labelMat = mat(labels).transpose()

    m, n = shape(dataMatrix)  #获取行列长度，m个样本，n个特征
    alpha = 0.001  #步长
    maxCycles = 5000  #最大迭代次数
    weights = ones((n, 1))  #初始化回归函数系数，n行1列，n为特征列数，列数包含bias常数项，array类型

    for k in range(maxCycles):
        # 矩阵相乘，对每个样本的特征项求加权和，结果再输入sigmoid
        h = sigmoid(dataMatrix * weights) # h为m行1列矩阵，没有sigmoid为线性回归
        error = (labelMat - h)
        # 该求导方法得益于 sigmoid 求导（待商榷）。weights 由 array 类型自动转换成 matrix 类型
        weights = weights + alpha * dataMatrix.transpose() * error 
        if plotLive == True:
            continue # TO DO
        if abs(sum(error)/len(error)) < 0.01: # 迭代结束条件2：误差均值小于1%
            break
    return weights


def loadDataSet():
    dataMat = []
    labelMat = []
    fr=open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])]) # 1.0为bias项
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def logRegTest():
    dataArr, labelMat = loadDataSet()
    weights = gradAscent(dataArr, labelMat)
    print(weights)
    # maxCycles=500， weights == [[ 4.12414349] /n[ 0.48007329] /n[-0.6168482 ]]

def plotFit(weights):
    if type(weights).__name__=="matrix":
        weights = array(weights)
    dataMat,labelMat = loadDataSet()
    dataArr = array(dataMat)
    n=shape(dataMat)[0] # dataMat 行数, 即样本数
    xcord1 = []
    ycord1=[]
    xcord2 = []
    ycord2=[]
    for i in range(n):
        # 样本按标签分成两组
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1])
            ycord2.append(dataArr[i,2])
    fig = plt.figure() #创建新图
    ax = fig.add_subplot(111) # 子图划分成 1 行 1 列，绘制在第1块区域
    ax.scatter(xcord1, ycord1, s=30, c='red', marker = 's') # 标签为1的样本点样式
    ax.scatter(xcord2, ycord2, s=30, c='green') #标签为0的样本点样式
    # 绘制直线
    x = arange(-3.0, 3.0, 0.1) #直线绘制区间
    y = (-weights[0]-weights[1]*x)/weights[2] # 拟合分类线
    ax.plot(x,y)
    # 坐标注释
    plt.xlabel('X1')
    plt.ylabel("X2")
    plt.show()
  

def plotFitTest():
    dataMat, labelMat = loadDataSet()
    weights = gradAscent(dataMat, labelMat)
    plotFit(weights)

plotFitTest()