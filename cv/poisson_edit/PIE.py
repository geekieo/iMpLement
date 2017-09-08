# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 15:29:01 2014
@author: Nannan Wu @躺在草原看夕阳
Notice: mask image and source image must be the same size,  destination image 
        must be of size larger than the Omega aera, that means destination image should be able
        to contain what you want to copy.
"""
from __future__ import division
from PIL import Image, ImageDraw
import numpy as np
from numpy import *
import copy
import datetime
import pickle
import os


def GaussSeidel(A,b,MaxIteration):
    '''
    Implement Gauss-Seidel iteration
    A is sparse matrix, that means A[i] is a dictionary, 'key' represents position
    and value means the value in row i and column 'key'.
    return x, the solution of linear problem Ax = b
    '''
    starttime = datetime.datetime.now()
    
#    A = np.array(A)
#    file_matrixA = open(A)
    
    b = np.array(b)
    
    #MAXITERATION = 500
    THRESHOLD = 1e-10
    x = np.zeros(len(b))
    for it in range(MaxIteration):
#        print 'iteration: ' , it
#        file_matrixA.seek(0,0)
        x_before = copy.copy(x)
        for i in range(len(x)):
#            Ai = pickle.load(file_matrixA)
            #s1: the sum of aij*xj(k) for j>i
            #s2: the sum of aij*xj(k+1) for j<i
#            sum = 0
#            for j in range(len(x)):#this kind of iteration is tooooo slow
#                if i != j:
#                    sum += A[i][j]*x[j]
            sum = 0
            for key in A[i].keys():
                if key != i:
                    sum += A[i][key]*x[key]
#            s1 = np.dot(Ai[ :i], x[:i])
#            s2 = np.dot(Ai[ i + 1:], x[i + 1:])
            x[i] = (b[i] - sum)/A[i][i]
            
#        error = x_before - x
#        error = np.dot(error,error)
#        error = np.sqrt(error)
#        if error < THRESHOLD :
#            break
        if np.allclose(x_before, x, rtol=1e-8):
            break
#        del x_before
        
    endtime = datetime.datetime.now()
    print('Gauss-Seidel Iteration consume time %d s' % (endtime - starttime).seconds)
    
#    file_matrixA.close()
    
    return x
    
    
def getOmegaAndBoundary(img_mask):
    '''
    According to the paper <Poisson image editing>, the boundary of Omega are
    those pixels  one of whoes four neighbours(left, right, up, down)is in Omega. 
    And Omega are thoes pixels whoes coresponding pixel in mask is 'white'
    input:input image is mask image, that means the 'white' aera is what we want.
    retur:1) indices(with respect to img_src) of pixels in Omega,
          2)Omega中像素在img_src中的序号，到在Omega中的序号的映射
          3) Omega's boundary(indices are in source image, and maybe out of range
             if Omega is mear to the boundary of source image).
    说明：我们用像素在源图像中的序号（源图像一行一行串在一起，从0开始）来表示Omega和边界，边界是Omega向外扩展一圈，因此当Omega靠近源图像边缘时，边界就超出了源图像范围，这时候，表示边界的像素序号可能为负，这没有关系，因为我们要用到的是边界在目标图像(S)中的值，而不是在Omega中的值。需要注意的一点是，程序中Omega区域及其边界，以及Omega中点p的4邻域用的都是像素在源图像的序号，之后再转换到目标图像。
    '''
    width, height = img_mask.size
    img_gray = img_mask.convert('L')
    data = img_gray.getdata()
#    boundary = [] # save the boundary pixels' indices(in source image).
    Omega = [] # save the Omega aera pixels' indices(in source image)
    #根据论文，我们需要将带求解的像素进行编号，带求解的像素即为Omega区域内的像素。
    #从左至右逐行扫描mask图像，碰到像素值非零，则index++
    pos2index = {} # pixel在源图像中的序号，到其在Omega区域的序号
    index2pos = {} #与pos2index对应
    index = 0
    THRESHOLD = 100 #to determine what kind of pixel is in Omega 
    for i in range(len(data)):
#        print 'the %d th pixel.' % i
        if data[i] >= THRESHOLD:
            #1. Omega区域
            Omega.append(i) # Omega area lies in where mask image pixel is white
            
            #2. Omega区域像素在源图像的序号到在Omega局部区域的序号的映射，方便构造方程组
            pos2index[i] = index
            index2pos[index] = i
            index += 1
            
            #3. 求解Omega的边界：
            #3.1 根据论文，Omega的边界由这些像素构成：其四邻域（上下左右）至少有一个像素在Omega中
            #且本身不在Omega中，由此可知，边界像素必然处在某个Omega像素的四邻域中
#            up = i - width #可能越界，当Omega区域位于源图像边缘时
#            down = i + width #可能越界，当Omega区域位于源图像边缘时
#            left = i - 1 #可能越界，当Omega区域位于源图像边缘时
#            right = i + 1 #可能越界，当Omega区域位于源图像边缘时
#            Np = [up, down, left, right]
            #3.2 这四个像素是边界像素只有两种可能：下标越界，或者本身不是Omega中的元素
#            for k in Np:
#                if( ( k not in range(0,len(data)) ) or (data[k] < THRESHOLD) ):
#                    if(k not in boundary): # 不要重复加入
#                        boundary.append(k)
            
            #print 'i:%d,value:%d' % (i, data[i])
            
    return Omega, pos2index, index2pos
    
    
def PoissonImageEditing(img_src, img_mask, img_dst, offset):
    '''
    input:
    img_src, img_dst-- we want to seamless clone something from img_src to img_dst
    img_mask--black white image. same size with img_src, and the white area define
                the aera want to clone.
    offset-- offset(x,y) the offset between img_src and img_dst, pixel(i,j) in 
                img_src corespond pixel( i + offset.x, j + offset.y ) in img_dst
    Notice: 
    1)img_src, img_mask, img_dst must be single channel image, so if you want to
      clone a color image, you should call this function thress times
    2)For more information please read the paper <Poisson image editing>
    
    '''
    #1. 求解源图像（拷贝来源）目标区域及其边界，获得的是像素序号
    starttime_total = datetime.datetime.now()
    print('Getting Omega aera...\n')
    # pos2index是一个字典，key是像素在img_src中的序号，value是该像素在Omega中的序号
    Omega, pos2index, index2pos = getOmegaAndBoundary(img_mask)
    
    #2. 构造线性方程组:逐行构造系数矩阵A和b,三个通道的A是一样的，b不相同
    print('Forming linear system...\n')
    starttime_ls = datetime.datetime.now()
    width_src, height_src = img_src.size
    width_dst, height_dst = img_dst.size
    OmegaSize = len(Omega)
    print('Size of Omega: ', OmegaSize)
    
    b_r = zeros(OmegaSize)
    b_g = zeros(OmegaSize)
    b_b = zeros(OmegaSize)
    A = []
#    A_t = zeros((OmegaSize,OmegaSize))
#    matrixA_fileName = 'Matrix_A'
#    file_matrixA = open(matrixA_fileName,'wb')
#    pickle.dump(OmegaSize,file_matrixA)
    #for all p belong Omega
    for i in range(OmegaSize):
#        print 'iteration %d times' % i
        #2.1 p值Omega中的像素，index_p是p点在Omega中的序号
        Ai = {}
        p = Omega[i]
        neighbourSize = 0 # 虽然只考虑4邻域，但当Omega位于S(img_dst)边界时，就没有4个相邻顶点S
        sumfstarq_r = 0 # 论文 equation (7)
        sumfstarq_g = 0
        sumfstarq_b = 0
        
        sumVpq_r = 0
        sumVpq_g = 0
        sumVpq_b = 0
        
        #2.2 p's four neighbour
        up = p - width_src #可能越界，当Omega区域位于源图像边缘时
        down = p + width_src #可能越界，当Omega区域位于源图像边缘时
        left = p - 1 #可能越界，当Omega区域位于源图像边缘时
        right = p + 1 #可能越界，当Omega区域位于源图像边缘时
        Np = [up, down, left, right]
        for q in Np:
            #2.3 when Omega contains pixels on the border of S(img_dst), some 
            #pixels has neighbours less than 4
            #将像素p转换成在S(img_dst)中的位置
            row_src = q//width_src
            col_src = q%width_src
            row_dst = row_src + offset[1]
            col_dst = col_src + offset[0]
            #我们假设Omega不许完全处于S中，则若q点不在S(img_dst)上，则2.4和2.5都不需要做了
            if (row_dst not in range(height_dst)) or (col_dst not in range(width_dst)):
                continue
            neighbourSize += 1
            #2.4 left side of equation (7) in paper <Poisson image editing>,
            # Modify the ith row of Matrix A 
            # I think equation (7) has some problem since q must belong to Omega
            # if you want to calculate Vpq, which eauqls gp - gq(g is img_src)
            # so I calculate the sum of Vpq here
            if q in Omega:
                index_q = pos2index[q]
#                A_t[i][index_q] = -1
                Ai[index_q] = -1
                sumVpq_r +=  img_src.getpixel((p%width_src, p//width_src))[0] -\
                            img_src.getpixel((q%width_src,q//width_src))[0]
                sumVpq_g +=  img_src.getpixel((p%width_src, p//width_src))[1] -\
                            img_src.getpixel((q%width_src,q//width_src))[1]
                sumVpq_b +=  img_src.getpixel((p%width_src, p//width_src))[2] -\
                            img_src.getpixel((q%width_src,q//width_src))[2]
            #2.5 right side of equation (7) in paper <Poisson image editing>
            # Modify the ith row of b
#            if q in boundary:
            # Since p is in Omega, and q is the neighbour of q, so if q is not 
            # in Omega , then q is the boudary of Omega
            if q not in Omega:
                sumfstarq_r += img_dst.getpixel((col_dst,row_dst))[0]
                sumfstarq_g += img_dst.getpixel((col_dst,row_dst))[1]
                sumfstarq_b += img_dst.getpixel((col_dst,row_dst))[2]

        #2.6填写当前行的系数矩阵        
        b_r[i] = sumfstarq_r +  sumVpq_r
        b_g[i] = sumfstarq_g +  sumVpq_g
        b_b[i] = sumfstarq_b +  sumVpq_b
        Ai[i] = neighbourSize
#        A_t[i][i] = neighbourSize
        A.append(Ai)
#        pickle.dump(Ai, file_matrixA, True)
#        print 'A[i]:',A[i]
#        print 'b_r[i]:',b_r[i]
#        print 'b_g[i]:',b_g[i]
#        print 'b_b[i]:',b_b[i]
#        if i==10:
#            break
#    file_matrixA.close()
    file_b = open('b_9k','wb')
    pickle.dump(b_r,file_b)
    file_b.close()

    file_A = open('A_9k','wb')
    pickle.dump(A,file_A)
    file_A.close()
    endtime_ls = datetime.datetime.now()
    print('Forming linear system consume time: %d s\n' % (endtime_ls - starttime_ls).seconds)
    
    #3. 为每一个通道(rgb)求解方程，Gauss-Seidel iteration
#    for i in range(len(Omega)):
#        if A[i][i] == 0:
#            print 'error: i', i 
    maxIteration = 5000
    print('Gauss-Seidel iterarion for "Red" channel...')
    x_r = GaussSeidel(A, b_r, maxIteration)
    print('\nGauss-Seidel iterarion for "Green" channel...')
    x_g = GaussSeidel(A, b_g, maxIteration)
    print('\nGauss-Seidel iterarion for "Blue" channel...')
    x_b = GaussSeidel(A, b_b, maxIteration)
    
    os.remove('b_9k');os.remove('A_9k')

    #4. 将计算出来的三个通道结果拷贝到目标图像对应区域
    print('\nForming result image...\n')
    img_dst_copy = img_dst.copy()#保存直接从源图像抠出目标区域拷贝到目标图像的结果
    for i in range(len(x_r)):
        #x[i]中存储的元素是Omega中的第i个像素，是源图像(img_src)中的第index2pos个像素
        pos_src = index2pos[i]
        row_src = pos_src//width_src
        col_src = pos_src%width_src
        #获得x[i]在目标图像S(img_dst)中的位置
        row_dst = row_src + offset[1]
        col_dst = col_src + offset[0]
        img_dst.putpixel( (col_dst,row_dst), (int(x_r[i]), int(x_g[i]), int(x_b[i])) )
        #上面语句是Poisson image editing 的结果，下面这条保存直接拷贝的结果
        img_dst_copy.putpixel( (col_dst,row_dst), img_src.getpixel((col_src, row_src)) )
    
    #5..保存并显示图像
    endtime_total = datetime.datetime.now()
    timeConsume_total = (endtime_total - starttime_total).seconds
    print('Poisson image editing consume time(totally): %d s' %  timeConsume_total)
    img_dst.save(img_src.filename.split('.')[0] + '_result_iteration'\
                + str(maxIteration)+ '_Consumetime'+ str(timeConsume_total) + 's.jpg')
    img_dst_copy.save(img_src.filename.split('.')[0] + '_result_directCopy.jpg')
    img_dst.show()
    img_dst_copy.show()


    
if __name__ == '__main__':
    print('-------Poisson Image Editing--------')
    print('Start reading images...\n')
    #bear
    img_src = Image.open('images/bear.jpg')
    img_mask = Image.open('images/bearmask_half.jpg')
    img_dst = Image.open('images/pooltarget.jpg')
    offset = [30,210]
    


#    #F16 warcraft clone
#    img_src = Image.open('images/F16Source.jpg')
#    img_mask = Image.open('images/F16Mask_half.jpg')
#    img_dst = Image.open('images/F16Target.jpg')
#    offset = [30,0]
    PoissonImageEditing(img_src, img_mask, img_dst, offset)