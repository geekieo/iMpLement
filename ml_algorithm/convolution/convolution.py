class Convolution(object):
    '''
    二维数组卷积运算
    '''

    def convolution(self, kernal, src):
        '''
        kernal 为卷积算子矩阵,\n
        src 为被卷积矩阵
        '''
        #获取 kernal, src 长宽
        kRows = len(kernal)
        kRRad = int(kRows/2) #半径
        kCols = len(kernal[0])
        kCRad = int(kCols/2) #半径
        sRows = len(src)
        sCols = len(src[0])

        #按 src 下标遍历
        for sRIndex,sRow in enumerate(src):           
            for sCIndex,sPixel in enumerate(sRow):
                #卷积时kernal边界不可超越src边界
                if((sRIndex+kRRad)>sRows or (sRIndex-kRRad)<0 or (sCIndex+kCRad)>sCols or (sCIndex - kCRad)<0):
                    break
                #按 kernal 下标遍历
                for cRIndex,kRow in enumerate(kernal):
                    for cCIndex,kPixel in enumerate(kRow):
                        pass
                print(sPiexl)
            print("\n")        


