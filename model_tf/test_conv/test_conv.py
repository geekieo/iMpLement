# -*- encode:utf-8 -*-
"""校验 tensorflow 卷积运算的微观操作

通过实验可确定, 输入 channel c1, 输出 channel c2 的卷积运算, 卷积核尺寸 (s1,s2), 
总共需要 c1*c2 个卷积, （卷积）参数量为 c1*c2*s1*s2.

实验探索 tensorflow 卷积的微观操作, 以输入矩阵 c1=2, h=3, w=3, 
输出矩阵 c2=5, h=2, w= 2, 卷积核尺寸 (2,2) 为例, 
输入矩阵为: [[[[3,1,1], 
              [1,1,1],
              [1,1,1]],
             [[2,2,2],
              [2,2,2],
              [2,2,2]]]]  shape=(1,2,3,3)   #BCHW
  运算转置: [[[[3., 2.],
              [1., 2.],
              [1., 2.]],
             [[1., 2.],
              [1., 2.],
              [1., 2.]],
             [[1., 2.],
              [1., 2.],
              [1., 2.]]]]  shape=(1,3,3,2)  #BHWC
10个卷积分别为: [[[[0, 0],
                  [0, 0]],
                  ...
                 [[4, 4],
                  [4, 4]]],
                [[[5, 5],
                  [5, 5]],
                  ...
                 [[9, 9],
                  [9, 9]]]]  shape=(2,5,2,2)    #CiCoHW
    运算转置: [[[[0, 1, 2, 3, 4],
                 [5, 6, 7, 8, 9]],
                [[0, 1, 2, 3, 4],
                 [5, 6, 7, 8, 9]]],
               [[[0, 1, 2, 3, 4],
                 [5, 6, 7, 8, 9]],
                [[0, 1, 2, 3, 4],
                 [5, 6, 7, 8, 9]]]]  shape=(2,2,2,5)    #HWCiCo
输出矩阵为: [[[[40, 54, 68, 82, 96],
              [40, 52, 64, 76, 88]],
             [[40, 52, 64, 76, 88],
              [40, 52, 64, 76, 88]]]]  shape=(1,2,2,5)  #BHWC
  易读转置: [[[[40, 40],
              [40, 40]],
             [[54, 52],
              [52, 52]],
             [[68, 64],
              [64, 64]],
             [[82, 76],
              [76, 76]],
             [[96, 88],
              [88, 88]]]]  shape=(1,5,2,2)  #BCHW
结果分析:
  conv 运算图解为:
      x1┐      ┌f0 ┌f1 ┌f2 ┌f3 ┌f4
        ├ conv ┤   ┤   ┤   ┤   ┤   → x1©f0+x2©f5 x1©f1+x2©f6 ... = y1 y2 y3 y4 y5
      x2┘      └f5 └f6 └f7 └f8 └f9  
  其中, © 表示二维卷积操作
"""
import tensorflow as tf


print(tf.__version__)

# input_x = tf.ones([1,4,4,2],dtype=tf.float16)  # NHWC
input_x1 = tf.constant(
    [[[[4., 2.],
       [1., 2.],
       [1., 2.]],
      [[1., 2.],
       [1., 2.],
       [1., 2.]],
      [[1., 2.],
       [1., 2.],
       [1., 2.]]]], dtype=tf.float16)           # (1,3,3,2)
input_x2 = tf.constant(
    [[[[3., 2.],
       [1., 2.],
       [1., 2.]],
      [[1., 2.],
       [1., 2.],
       [1., 2.]],
      [[1., 2.],
       [1., 2.],
       [1., 2.]]]], dtype=tf.float16)           # (1,3,3,2)

# initializer=tf.constant_initializer(0.1)
# initializer=tf.truncated_normal_initializer(stddev=0.1, dtype=tf.float32)
filter_f1 = tf.get_variable('filters',
                          shape=[2, 2, 2, 5],   # HWIO
                          dtype=tf.float16,
                          initializer=tf.constant_initializer(1))

filter_f2 = tf.constant(
    [[[[0,1,2,3,4],
       [5,6,7,8,9]],
      [[0,1,2,3,4],
       [5,6,7,8,9]]],
     [[[0,1,2,3,4],
       [5,6,7,8,9]],
      [[0,1,2,3,4],
       [5,6,7,8,9]]]], dtype=tf.float16
)

init_op = tf.initialize_all_variables()


if __name__ == "__main__":
    with tf.Session() as sess:
        inputs = sess.run([input_x1, input_x2])
        sess.run(init_op)
        filters = sess.run([filter_f1, filter_f2])
        for item in zip(inputs, filters):
            input_x = item[0]
            filter_f = item[1]
            print("input shape:{}, filter shape:{}".format(input_x.shape, filter_f.shape))
            x = tf.nn.conv2d(input_x, filter_f, strides=[1, 1, 1, 1], padding='VALID')
            print(sess.run(x))

