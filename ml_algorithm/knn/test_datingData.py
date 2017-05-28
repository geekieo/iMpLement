from kNN import *


def drawPlot():
    # 作图展示
    datingMat, datingLabels = file2matrix('datingTestSet2.txt')
    x = datingMat[:, 0]
    y = datingMat[:, 1]
    z = datingMat[:, 2]
    drawPlot3D(x, y, z, datingLabels)
    # 归一化
    normMat, ranges, minVals = autoNorm(datingMat)
    x = normMat[:, 0]
    y = normMat[:, 1]
    z = normMat[:, 2]
    drawPlot2D(x, y, datingLabels)


def datingClassTest():
    # 数据集自测
    hoRatio = 0.1 # 测试集的分割比例
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0] # 数据集总数
    numTestVecs = int(m * hoRatio) #测试集数量
    errorCount = 0.0
    for i in range(numTestVecs):
        # [0, numTestVecs) 为测试集，[numTestVecs, m) 为训练集
        classifierResult = kNNClassify(normMat[i, :], normMat[numTestVecs:m, :],
                                     datingLabels[numTestVecs:m], 3)
        print('the classifier came back with: %s, the real answer is: %s' %
              (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print('the total error rate is %f' % (errorCount / float(numTestVecs)))

def classifyPerson():
    # 对新人特征并做 knn 分类
    # input() 允许用户输入文本行命令并返回用户所输入的内容
    # raw_input() 将所有输入作为字符串看待，返回字符串类型
    labelList = ['不会喜欢', '有一点可能会喜欢', '有很大可能会喜欢']
    ffMiles = 10
    percentTats = 20
    iceCream = 10
    # while(ffMiles is empty):
    #     ffMiles = float(input('每年攒下的飞机里程数(km)? 参考范围:0~10000: '))
    # while(percentTats is empty):
    #     percentTats = float(input('玩游戏的时间占比(%)? 参考范围:0~20: '))
    # while(iceCream is empty):
    #     iceCream = float(input('每年吃掉的冰淇淋(L)? 参考范围:0~2: '))
    datingMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = kNNClassify((inArr - minVals) / ranges, normMat,
                                   datingLabels, 3)
    print('你喜欢这个人的可能是：', labelList[int(classifierResult) - 1])

datingClassTest()