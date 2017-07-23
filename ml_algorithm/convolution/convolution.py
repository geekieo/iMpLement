class Convolution(object):
    '''
    二维数组卷积运算
    '''
    def convolution(self, src, kernal):
        '''
        src 为被卷积矩阵,\n
        kernal 为卷积算子矩阵,
        '''
        #获取 kernal, src 长宽
        kRowLen = len(kernal)
        kRRad = int(kRowLen / 2)  #半径
        kColLen = len(kernal[0])
        kCRad = int(kColLen / 2)  #半径
        kSize = kRowLen * kColLen
        sRowLen = len(src)
        sColLen = len(src[0])
        #初始化结果矩阵
        dstRows = sRowLen-2*kRRad
        dstCols = sColLen-2*kCRad
        dst = [[0 for col in range(dstCols)]for row in range(dstRows)]
        #按 src 下标遍历
        for sRIndex, sRow in enumerate(src):
            #在src上遍历，行的范围
            minPixY = sRIndex - kRRad
            maxPixY = sRIndex + kRRad
            #卷积时kernal边界不可超越src边界
            if (minPixY >= 0 and maxPixY <= sRowLen - 1):
                for sCIndex, sPixel in enumerate(sRow):
                    #在 src 上遍历，列的范围
                    minPixX = sCIndex - kCRad
                    maxPixX = sCIndex + kCRad
                    #卷积时kernal边界不可超越src边界
                    if (minPixX >= 0 and maxPixX <= sColLen - 1):
                        dstPixel = 0
                        # 按 kernal 卷积
                        for kRIndex, kRow in enumerate(kernal):
                            for kCIndex, kPixel in enumerate(kRow):
                                dstPixel += kPixel * src[minPixY + kRIndex][minPixX + kCIndex]
                        dst[sRIndex - kRRad][sCIndex - kCRad] = dstPixel
        return dst

    def transpose(self, src):
        '''矩阵转置'''
        sRowLen= len(src)
        sColLen= len(src[0])
        #初始化转置矩阵数组结构
        dst = [[0 for dCol in range(sRowLen)] for dRow in range(sColLen)]
        for sRIndex, sRow in enumerate(src):
            for sCIndex, sPixel in enumerate(sRow):
                dst[sCIndex][sRIndex]=sPixel
        return dst

    # def deConvolution(self, src, kernal):

