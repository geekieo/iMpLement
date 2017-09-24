from numpy import *
import matplotlib.pyplot as plt

def loadDataSet():
    dataMat = []
    labelMat = []
    fr=open('GMM//2D2CtestSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])]) # 1.0为bias项
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

def plotFit():
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
    # 坐标注释
    plt.xlabel('X1')
    plt.ylabel("X2")
    plt.show()

plotFit()