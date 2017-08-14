"""
决策树分类器
"""

def classify(inTree, featNames, testVec):
    '''
    递归分类(决策树/子树，特征名列表，待分类样本)
    返回类别标签
    '''
    firstStr = list(inTree.keys())[0]
    secondDict = inTree[firstStr]
    # 找到特征名在特征列表的索引
    featIndex = featNames.index(firstStr)
    # 遍历结点
    for key in list(secondDict.keys()):
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__=='dict':
                #子树结点，进入递归
                label = classify(secondDict[key], featNames, testVec) 
            else: #叶子结点，返回标签
                label = secondDict[key] 
    return label

def classifyTest():
    import tree as t
    import treePlotter as tp
    
    dataSet, labels = t.createDataSet()
    myTree = t.createTree(dataSet,labels.copy())
    print(myTree)
    print(labels)

    print(classify(myTree, labels, [1,0]))
    print(classify(myTree, labels, [1,1]))
    
    tp.createPlot(myTree)

classifyTest()
    