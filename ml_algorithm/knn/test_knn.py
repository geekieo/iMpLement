import kNN
from numpy import *


def __test__():
    dataSet, labels = kNN.createDataSet()
    
    
    inX = array([1.2, 1.1])
    k = 3
    outputLabel = kNN.kNNClassify(inX, dataSet, labels, 3)
    print("Your input is:", inX, "and classified to class: ", outputLabel)

    inX = array([0.1, 0.3])
    outputLabel = kNN.kNNClassify(inX, dataSet, labels, 3)
    print("Your input is:", inX, "and classified to class: ", outputLabel)

__test__()