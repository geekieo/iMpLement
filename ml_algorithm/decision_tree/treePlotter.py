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


def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode(U'决策结点', (0.5, 0.1), (0.1, 0.5), decisionNode) #feature Name
    plotNode(U'决策类型结点', (0.8, 0.1), (0.3, 0.8), leafNode) #node belong to feature
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
    获取树的深度
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
    两组测试树
    '''
    listOfTrees=[{'no surfacing':{0:'no',1:{'flippers':{
        0:{'head':{0:'no',1:'yes'}},1:'no'}}}},
        {'no surfacing':{0:'no',1:{'flippers':{0:{'head':{
            0:'no',1:'yes'}},1:'no'}}}}]
    return listOfTrees[i]


def test():
    retrieveTree(1)
    myTree = retrieveTree(0)
    print(getNumLeafs(myTree))
    print(getTreeDepth(myTree))

test()