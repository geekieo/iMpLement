import tensorflow as tf
hello = tf.constant('Hello, Tensorflow!')
sess = tf.Session()
x1 = tf.constant(10)
x2 = tf.constant(32)
print(sess.run(x1 + x2))

# creates a graph
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
# creates a session with log_device_placement set to True
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# runs the op
print("a=",a,"\n")
print(sess.run(c))