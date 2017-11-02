from numpy import *
import matplotlib.pyplot as plt
import random
import math


def gmm(dataMat, K_or_centroids):
    '''
    ============================================================
    Expectation-Maximization iteration implementation of
    Gaussian Mixture Model.
    
    PX = GMM(dataMat, K_or_centroids)
    [PX MODEL] = GMM(dataMat, K_or_centroids)
    
     - dataMat: N-by-D data matrix.
     - K_or_centroids: either K indicating the number of
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
    # 初始化质心
    threshold = 1e-15
    [N, D] = shape(
        dataMat)  # get the row and col number of inX，return tuple tpye result
    # K_or_centroids 可以是单高斯模型数（质心数），也可以是K个 D 维的列向量（质心）。
    if shape(K_or_centroids) == ():
        K = K_or_centroids
        rn_index = list(range(N))
        # randomly pick K centrids in [0, N]
        random.shuffle(rn_index)  # 将数组 rn_index 随机化
        centroids = [dataMat[i] for i in rn_index[0:K]]  # 取 rn_index 前K个数作为索引，根据这K个索引从 dataMat 中获得样本，作为随机质心
    else:
        K = len(K_or_centroids)
        [cN,cD]=shape(K_or_centroids)
        if(cD == D):
            centroids = K_or_centroids
        else:
            print("提供的初始质心维数错误！")
            return

    ## 初始化参数
    # pMiu:样本均值向量；pPi:模型概率向量；pSigma:协方差矩阵
    [pMiu, pPi, pSigma] = init_params(dataMat, centroids, k, N, D)
    prevLoss = -inf  #上一轮聚类的误差

    # EM Algorithm 迭代
    while True:
        ## Estimation Step
        PX = calc_prob(pMiu, pSigma, dataMat, K, N, D)
        # pGamma[i,k] : xi由第 k 个Gaussian生成的概率；xi中由第 k 个Gaussian生成的比例
        # 分子 = pi(k) * N(xi | pMiu(k), pSigma(k))
        # 分母 = Σ pi(j) * N(xi | pMiu(j), pSigma(j)),对所有Gaussian j∈[1,K] 得到的概率求和
        pGamma = mat(array(PX) *
                     array(tile(pPi, (N, 1))))  # tile() 把 pPi 复制成 N行1列 的 array
        pGamma = pGamma / tile(sum(pGamma, axis=1), (1, K))
        ## Maximization Step - through Maximize likelihood Estimation
        # print('dtpye:',pGamma.dtype)
        Nk = sum(pGamma, axis=0)  #Nk(l*K) = 第k个高斯生成每个样本的概率和，所有Nk总和为N

        # 通过极大似然估计（MLE） 更新 pMiu (令似然函数偏导 = 0得到)
        # diag(1D-array): 将 1D-array 转换为2D对角矩阵
        pMiu = mat(diag((1 / Nk).tolist()[0])) * (pGamma.T) * dataMat
        pPi = Nk / N

        # 更新 K 个 pSigma
        print('kk=', K)
        for kk in range(K):
            Xshift = dataMat - tile(pMiu[kk], (N, 1))
            Xshift.T * mat(diag(pGamma[:, kk].Ttolist()[0])) * Xshift / 2
            pSigma[:, :, kk] = (Xshift.T * mat(diag(pGamma[:, kk].T.tolist()[0]))*Xshift)\
                /Nk[kk]

        # check for convergence
        L = sum(log(Px*(pPi.T)))
        if L-Lprev < threshold:
            break
        Lprev = L

    return Px

def init_params(X,centroids,K,N,D):
    pMiu = centroids # K*D, 即k类的中心点
    pPi = zeros([1, K]) # k类GMM所占权重（influence factor）
    pSigma = zeros([D, D, K]) # k类GMM的协方差矩阵，每个是D*D的

    # 距离矩阵，计算 N*K 的矩阵（x-pMiu）^2 = x^2+pMiu^2-2*x*Miu
    # x^2, N*1 的矩阵 replicate K列\#pMiu^2，1*K 的矩阵replicateN行
    distmat = tile(sum(power(X,2), 1),(1, K)) + \
        tile(transpose(sum(power(pMiu,2), 1)),(N, 1)) - \
        2*X*transpose(pMiu)
    labels = distmat.argmin(1) #Return the minimum from each row

    # 获取 K 类的pPi和协方差矩阵
    for k in range(K):
        boolList = (labels==k).tolist()
        indexList = [boolList.index(i) for i in boolList if i==[True]]
        Xk = X[indexList, :]
        #print(cov(Xk))
        # 也可以用shape(XK)[0]
        pPi[0][k] = float(size(Xk, 0))/N
        pSigma[:, :, k] = cov(transpose(Xk))

    return pMiu,pPi,pSigma

# 计算每个数据由第k类生成的概率矩阵Px
def calc_prob(pMiu,pSigma,X,K,N,D):
    # Gaussian posterior probability
    # N(x|pMiu,pSigma) = 1/((2pi)^(D/2))*(1/(abs(sigma))^0.5)*exp(-1/2*(x-pMiu)'pSigma^(-1)*(x-pMiu))
    Px = mat(zeros([N, K]))
    for k in range(K):
        Xshift = X-tile(pMiu[k, :],(N, 1)) #X-pMiu
        #inv_pSigma = mat(pSigma[:, :, k]).I
        inv_pSigma = linalg.pinv(mat(pSigma[:, :, k]))

        tmp = sum(array((Xshift*inv_pSigma)) * array(Xshift), 1) # 这里应变为一列数
        tmp = mat(tmp).T
        #print(linalg.det(inv_pSigma),'54545')

        Sigema = linalg.det(mat(inv_pSigma))

        if Sigema < 0:
            Sigema=0

        coef = power((2*(math.pi)),(-D/2)) * sqrt(Sigema)
        Px[:, k] = coef * exp(-0.5*tmp)
    return Px

        
#========================= ↓ DateSet code ↓ ============================#

def loadDataSet():
    '''
    特征向量+标签
    '''
    dataMat = []
    labelMat = []
    fr = open('GMM//2D2CtestSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]),
                        float(lineArr[1])])  # 1.0为bias项
        labelMat.append(int(lineArr[2])) #第 3 列为标签
    return dataMat,labelMat


def plotFit():
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataMat)[0]  # dataMat 行数, 即样本数
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        # 样本按标签分成两组
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()  #创建新图
    ax = fig.add_subplot(111)  # 子图划分成 1 行 1 列，绘制在第1块区域
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')  # 标签为1的样本点样式
    ax.scatter(xcord2, ycord2, s=30, c='green')  #标签为0的样本点样式
    # 坐标注释
    plt.xlabel('X1')
    plt.ylabel("X2")
    plt.show()


#plotFit()

#=========================
if __name__ =='__main__':
    dataMat,labelMat = loadDataSet()
    gmm(dataMat,2)