"""
使用 Matplotlib 的注解功能绘制树形图
"""

import matplotlib.pyplot as plt
from tree import *

plt.rcParams['font.sans-serif']=['SimHei'] #设置字体编码为黑体
# 定义文本框和箭头格式
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

# 绘制带箭头的注解
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(
        nodeTxt,
        xy=parentPt,
        xycoords='axes fraction',
        xytext=centerPt,
        textcoords='axes fraction',
        va="center",
        ha="center",
        bbox=nodeType,
        arrowprops=arrow_args)

def plotMidText(cntrPt, parentPt, txtString):
    '''
    父子结点间添加的文本信息
    '''
    xMid = (parentPt[0]-cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1]-cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)

def plotTree(myTree, parentPt, nodeTxt):
    '''
    递归画树
    '''
    # 计算树的宽和高，使用这两个变量计算结点的摆放位置。
    # 全局变量 plotTree.totalW 存储树的宽度，plotTree.totalD 存储树的高度
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    cntrPt = (plotTree.xOff+(1.0+float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
    # 标记结点属性
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    #按比例减少全局变量 plotTree.yOff, 并标注此处绘制子结点
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            plotTree(secondDict[key], cntrPt, str(key)) #结点为字典，进入递归
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff),cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

def createPlot(inTree):
    '''
    主函数
    '''
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    # plotNode(U'决策结点', (0.5, 0.1), (0.1, 0.5), decisionNode) #feature Name
    # plotNode(U'决策类型结点', (0.8, 0.1), (0.3, 0.8), leafNode) #node belong to feature
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    # 作图范围: x，y 坐标在 [0,1] 之间
    plotTree.xOff = -0.5/plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree,(0.5,1.0), '')
    plt.show()

def getNumLeafs(myTree):
    '''
    将一层嵌套的字典分解出“根”和“叶子”,统计所有叶子数
    根为：特征名称，指代一组特征分量，作为每一组特征分量的根结点出现，不对训练产生影响
    叶子结点分为：label 和 字典 两种类型，字典代表此处为新的特征分量
    myTree 参考实例：{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
    '''
    numLeafs = 0
    firstStr = list(myTree.keys())[0] #根
    secondDict = myTree[firstStr] #叶子们
    for key in list(secondDict.keys()):
        # 判断结点数据类型是否为字典
        if type(secondDict[key]).__name__=='dict':
            numLeafs += getNumLeafs(secondDict[key]) #如果是字典，进入递归统计
        else:
            numLeafs +=1
    return numLeafs

def getTreeDepth(myTree):
    '''
    递归获取树的深度
    返回该树/子树最大深度
    '''
    maxDepth=0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in list(secondDict.keys()):
        if type(secondDict[key]).__name__=='dict':
            thisDepth = 1+getTreeDepth(secondDict[key]) # 如果是字典，进入递归统计
        else: thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth

def retrieveTree(i):
    '''
    测试树
    '''
    listOfTrees=[{'no surfacing':{0:'no',1:{'flippers':{
        0:{'head':{0:'no',1:'yes'}},1:'no'}}}},
        {'no surfacing':{0:'no',1:{'flippers':{0:{'head':{
        0:'no',1:'yes'}},1:'no'}}}},
        {'no surfacing ': {0: 'no', 1: {'flippers':{
        0: 'no', 1: 'yes'}}, 3: 'maybe'}}]
    return listOfTrees[i]


def test():
    myTree = retrieveTree(2)
    print(myTree)
    print(getNumLeafs(myTree))
    print(getTreeDepth(myTree))
    createPlot(myTree)


test()