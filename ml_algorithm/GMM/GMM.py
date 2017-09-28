from numpy import *
import matplotlib.pyplot as plt
import random.math

def GMM(dataMat,k_or_centroids):
    '''
    ============================================================
    Expectation-Maximization iteration implementation of
    Gaussian Mixture Model.
    
    PX = GMM(dataMat, k_or_centroids)
    [PX MODEL] = GMM(dataMat, k_or_centroids)
    
     - dataMat: N-by-D data matrix.
     - k_or_centroids: either K indicating the number of
          components or a K-by-D matrix indicating the
          choosing of the initial K centroids.
          
     - PX: N-by-K matrix indicating the probability of each
          component generating each point.
     - MODEL: a structure containing the parameters for a GMM:
          MODEL.Miu: a K-by-D matrix.
          MODEL.Sigma: a D-by-D-by-K matrix.
          MODEL.Pi: a 1-by-K vector.
    ============================================================
    '''
    threshold   = 1e-15
    [N, D] = shape(dataMat) # get the row and col number of inX，return tuple tpye result
    # k_or_centroids 可以是质心数，也可以是k个D维质心的D维列向量。
    if shape(k_or_centroids)==():
        k = k_or_centroids
        rn_index = list(range(N))
        # randomly pick k centrids in [0, N]
        random.shuffle(list(rn_index) ) #random index N samples
        centroids = dataMat[rn_index[0:k],:]  # k random centroid
    else:
        k = len(k_or_centroids)
        centroids = k_or_centroids

    ## 初始化参数
    # pMiu:样本均值向量；pPi:模型概率向量；pSigma:协方差矩阵
    [pMiu, pPi, pSigma] = init_params(dataMat, centroids, k, N, D)
    preLoss = -inf #上一轮聚类的误差

    # EM Algorithm
    while True:
        ## Estimation Step
        Px = calc_prob(pMiu,pSigma,dataMat,k,N,D)
        # pGamma[i,k] : xi由第k个Gaussian生成的概率；xi中由第k个Gaussian生成的比例
        # 分子 = pi(k) * N(xi | pMiu(k), pSigma(k)) 
        # 分母 = Σ pi(j) * N(xi | pMiu(j), pSigma(j)),对所有Gaussian j∈[1,K] 得到的概率求和
        pGamma = mat(array(Px)*array(tile(pPi,(N,1)))) # tile() 把 pPi 复制成 N行1列 的 array 
        pGamma = pGamma / tile(sum(pGamma,axis=1),(1,k))
        ## Maximization Step - through Maximize likelihood Estimation
        # print 'dtpyedddddddd:',pGamma.dtype
        Nk = sum(pGamme, axis=0) #Nk(l*k) = 第k个高斯生成每个样本的概率和，所有Nk总和为N
        




def loadDataSet():
    '''
    返回一个 list，其中每一行为特征向量+标签
    '''
    dataMat = []
    fr=open('GMM//2D2CtestSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])]) # 1.0为bias项
        dataMat.append(int(lineArr[2]))
    return dataMat

def plotFit():
    dataMat,labelMat = loadDataSet()
    dataArr = array(dataMat)
    n=shape(dataMat)[0] # dataMat 行数, 即样本数
    xcord1 = []
    ycord1=[]
    xcord2 = []
    ycord2=[]
    for i in range(n):
        # 样本按标签分成两组
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1])
            ycord2.append(dataArr[i,2])
    fig = plt.figure() #创建新图
    ax = fig.add_subplot(111) # 子图划分成 1 行 1 列，绘制在第1块区域
    ax.scatter(xcord1, ycord1, s=30, c='red', marker = 's') # 标签为1的样本点样式
    ax.scatter(xcord2, ycord2, s=30, c='green') #标签为0的样本点样式
    # 坐标注释
    plt.xlabel('X1')
    plt.ylabel("X2")
    plt.show()






plotFit()