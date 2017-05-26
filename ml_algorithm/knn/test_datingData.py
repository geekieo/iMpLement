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
    hoRatio = 0.1
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = kNNClassify(normMat[i, :], normMat[numTestVecs:m, :],
                                     datingLabels[numTestVecs:m], 3)
        print('the classifier came back with: %d, the real answer is: %d' %
              (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print('the total error rate is %f' % (errorCount / float(numTestVecs)))

datingClassTest()