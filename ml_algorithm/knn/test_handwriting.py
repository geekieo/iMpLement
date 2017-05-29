from kNN import *  

# test hand writting class
def handwritingClassTest():
    ## step 1
    print('step 1: load data...')
    train_x, train_y, test_x, test_y = loadDataSet()

    ## step 2
    print('step 2: train...')
    pass

    ## step 3
    print('step 3: testing...')
    numTestSamples = test_x.shape[0]
    matchCount = 0
    for i in range(numTestSamples):
        predict = kNNClassify(test_x[i], train_x, train_y, 3)
        if predict == test_y[i]:
            matchCount += 1
    accuracy = float(matchCount) / numTestSamples

    ## step 4
    print('step 4: show the result...')
    print('The classify accuracy is: %.2f%%' % (accuracy * 100))


