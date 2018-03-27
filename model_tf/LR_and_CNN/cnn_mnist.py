import tensorflow as tf

CKPT_DIR="Model/model.ckpt"

# 按标准差0.1随机初始化权重，新建模型调用
# shape 参数例子：[3,3,1,32] 意义:[高，宽，通道数，卷积核数]
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


# 初始化bias项权重
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


# x:[图片数，图高，图宽，图通道数]
# W:[核高，核宽，核通道数=图通道数，输出通道数(卷积核数)]
#   strides：滑动步长，参数意义：[图片数，高，宽，通道数]
# return:[图片数，高，宽，通道数*卷积核数]
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


# ksize：下采样卷积窗大小，格式和stride一样,
def max_pool_2x2(x):
    return tf.nn.max_pool(
        x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


class CNN():
    def __init__(self):
        self.sess = tf.InteractiveSession()
        
    def restore(self,CKPT_DIR):
        '''加载模型'''
        saver = tf.train.Saver()
        ckpt = tf.train.get_checkpoint_state(CKPT_DIR)


    def train(self):
        '''Convolutional Layer #1: Applies 32 5x5 filters (extracting 5x5-pixel subregions), with ReLU activation function
        Pooling Layer #1: Performs max pooling with a 2x2 filter and stride of 2 (which specifies that pooled regions do not overlap)
        Convolutional Layer #2: Applies 64 5x5 filters, with ReLU activation function
        Pooling Layer #2: Again, performs max pooling with a 2x2 filter and stride of 2
        Dense Layer #1: 1,024 neurons, with dropout regularization rate of 0.4 (probability of 0.4 that any given element will be dropped during training)
        Dense Layer #2 (Logits Layer): 10 neurons, one for each digit target class (0–9).'''
        mnist = tf.contrib.learn.datasets.mnist.read_data_sets(
            "MNIST_data", one_hot=True)
        x = tf.placeholder("float", shape=[None, 784])
        y_ = tf.placeholder("float", shape=[None, 10])

        # Input Layer
        # [图片数，高，宽，通道数]
        x_image = tf.reshape(x, [-1, 28, 28, 1])
        # Conv Layer #1
        # W_conv1:[高，宽，通道数，输出通道数], 第三维数值即 x_image 第四维
        W_conv1 = weight_variable([5, 5, 1, 32])
        b_conv1 = bias_variable([32])  # 每个卷积核1个bias
        a_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)  #[-1,28,28,32]
        # Pooling Layer #1
        a_pool1 = max_pool_2x2(a_conv1)  #[-1,14,14,32]
        # Conv Layer #2
        W_conv2 = weight_variable([5, 5, 32, 64])
        b_conv2 = bias_variable([64])
        a_conv2 = tf.nn.relu(conv2d(a_pool1, W_conv2) + b_conv2)  #[-1,14,14,64]
        # Pooling Layer #2
        a_pool2 = max_pool_2x2(a_conv2)  #[-1,7,7,64]
        # Dense Layer #1
        W_fc1 = weight_variable([7 * 7 * 64, 1024])
        b_fc1 = bias_variable([1024])
        a_pool2_flat = tf.reshape(a_pool2, [-1, 7 * 7 * 64])
        a_fc1 = tf.nn.relu(tf.matmul(a_pool2_flat, W_fc1) + b_fc1)
        # Dropout
        keep_prob = tf.placeholder("float")
        a_fc1_drop = tf.nn.dropout(a_fc1, keep_prob)
        # Dense Layer #2
        W_fc2 = weight_variable([1024, 10])
        b_fc2 = bias_variable([10])
        y_predict = tf.nn.softmax(tf.matmul(a_fc1_drop, W_fc2) + b_fc2)

        # 损失函数
        cross_entropy = -tf.reduce_sum(y_ * tf.log(y_predict))
        # 优化方法
        train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
        # 误差统计真值表，argmax()中 axis=1，即每一行中，列与列比，返回最大值下标
        correct_prediction = tf.equal(
            tf.argmax(y_predict, axis=1), tf.argmax(y_, 1))
        # 误差概率
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        # 实例化保存模型对象
        saver = tf.train.Saver()
        self.sess.run(tf.global_variables_initializer())   
        # 训练
        for i in range(200): # 迭代次数过多，显存也会不够
            batch = mnist.train.next_batch(20) # batch(35)显存不够,调小batch_size
            if i % 100 == 0:
                train_accuracy = accuracy.eval(
                    feed_dict={x: batch[0],
                            y_: batch[1],
                            keep_prob: 1.0})
                print("step %d, train accuracy %g" % (i, train_accuracy))
            train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.4})
        # 保存模型
        print("model saved in \"%s\"" %saver.save(self.sess,CKPT_DIR))
        # 验证
        batch_test = mnist.train.next_batch(1000) #全部10000张运算内存不够
        print("test accuracy %g" % accuracy.eval(feed_dict={
            x: batch_test[0],
            y_: batch_test[1],
            keep_prob: 1.0
        }))

    def predict(self):
        pass


if __name__ == "__main__":
    cnn = CNN()
    cnn.train()