from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MINIST_data', one_hot=True)

import tensorflow as tf

def logisticRegression():
    # 交互式会话，可以在运行图的时候插入一些计算图
    sess = tf.InteractiveSession()
    # 定义结点
    x = tf.placeholder("float", shape=[None, 784])
    y_ = tf.placeholder("float", shape=[None, 10])
    # 定义参数
    W = tf.Variable(tf.zeros([784,10]))
    b = tf.Variable(tf.zeros([10]))
    # 定义在会话中，初始化全局变量的操作
    sess.run(tf.global_variables_initializer())
    # 定义输出层和损失函数(交叉熵)
    y = tf.nn.softmax(tf.matmul(x,W) + b)
    cross_entropy = -tf.reduce_sum(y_*tf.log(y))
    # 定义优化函数，最小化损失函数（交叉熵），这是一步训练操作
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
    # 迭代调用优化函数，训练W和b
    # feed_dict() 向占位符填充数值，至此图运算的所有元素准备完成，由run运行计算图
    for i in range(1000):
        batch = mnist.train.next_batch(50)
        train_step.run(feed_dict={x: batch[0], y_: batch[1]})
    
    # 评估模型，使用均方差损失函数，仅一步操作
    # argmax(y,1)返回y中元素是1的索引，equal()返回匹配值，一个布尔数组
    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    # 统计匹配概率，cast()类型转换，将布尔型变为浮点数值型
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    # Tensor.eval()是 Session.run() 的速用方式,区别是调用方不同
    print(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

def 