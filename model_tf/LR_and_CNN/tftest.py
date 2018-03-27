import tensorflow as tf

mnist = tf.contrib.learn.datasets.mnist.read_data_sets("MNIST_data",one_hot=True)
x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", shape=[None, 10])

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

batch_test = mnist.test.labels
print(y_.eval(feed_dict={y_: batch_test}))

batch_train = mnist.train.next_batch(20)
print(y_.eval(feed_dict={y_: batch_train[1]}))