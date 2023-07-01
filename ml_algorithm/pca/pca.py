import numpy as np

def normalization(x:np.array) -> np.array:
    mean = np.mean(x)
    std = np.std(x)
    res =(x-mean)/std
    return res

