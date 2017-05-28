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

classifyPerson()