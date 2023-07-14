import numpy as np

def normalization(x:np.ndarray) -> np.ndarray:
    mean = np.mean(x)
    std = np.std(x)
    res =(x-mean)/std
    return res

def covarience(x:np.ndarray) -> np.ndarray:
    pass