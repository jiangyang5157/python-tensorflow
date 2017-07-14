import tensorflow as tf

a = tf.placeholder(tf.int32, shape=())
b = tf.placeholder(tf.int32, shape=())
add = tf.add(a, b)
sess = tf.InteractiveSession()
print(sess.run(add, feed_dict={a: 1, b: 2}))
