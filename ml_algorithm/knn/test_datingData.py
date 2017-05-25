import kNN  

# 作图展示
datingMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
x=datingMat[:,0]
y=datingMat[:,1]
z=datingMat[:,2]
kNN.drawPlot3D(x,y,z,datingLabels)
# 归一化
normDatingMat,ranges,minVals = kNN.autoNorm(datingMat)
x=normDatingMat[:,0]
y=normDatingMat[:,1]
z=normDatingMat[:,2]
kNN.drawPlot2D(x,y,datingLabels)