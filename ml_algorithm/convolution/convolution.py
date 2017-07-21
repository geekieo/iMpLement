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
        kRRad = int(kRows / 2)  #半径
        kCols = len(kernal[0])
        kCRad = int(kCols / 2)  #半径
        sRows = len(src)
        sCols = len(src[0])

        #按 src 下标遍历
        for sRIndex, sRow in enumerate(src):
            #卷积时kernal边界不可超越src边界
            if ((sRIndex - kRRad) >= 0 and (sRIndex + kRRad) <= sRows - 1):
                for sCIndex, sPixel in enumerate(sRow):
                    #卷积时kernal边界不可超越src边界
                    if ((sCIndex - kCRad) >= 0 and
                        (sCIndex + kCRad) <= sCols - 1):
                        #按 kernal 下标遍历
                        for cRIndex, kRow in enumerate(kernal):
                            for cCIndex, kPixel in enumerate(kRow):
                                pass
                        print(sPixel)
                print("\n")
