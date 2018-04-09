from __future__ import print_function

import tensorflow as tf


# Importing the MNIST dataset from tensorflow
from tensorflow.examples.tutorials.mnist import input_data
Dataset_mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
print(Dataset_mnist)

# HyperParameters for the MNIST Dataset
lrn_rt = 0.1
trin_ep = 40
batch_siz = 100
disp_step = 1

# tf Graph Input
x_label = tf.placeholder(tf.float32, [None, 784],name="img") # mnist data image of shape 28*28=784
y_label= tf.placeholder(tf.float32, [None, 10],name="lbl") # 0-9 digits recognition => 10 classes

# Set model weights
Wt = tf.Variable(tf.zeros([784, 10]),name="Weigh")
bs = tf.Variable(tf.zeros([10]),name="bias")

# Construct model
predict_val = tf.nn.softmax(tf.matmul(x_label, Wt) + bs,name="Softmax") # Softmax

# Minimize error using cross entropy
cst_val = tf.reduce_mean(-tf.reduce_sum(y_label*tf.log(predict_val), reduction_indices=1))
# Gradient Descent
optim_zer = tf.train.GradientDescentOptimizer(lrn_rt).minimize(cst_val)

# Initialize the variables (i.e. assign their default value)
initial = tf.global_variables_initializer()

# Start training
with tf.Session() as sess:

    # Run the initializer
    sess.run(initial)
    writer = tf.summary.FileWriter('./graphs/logistic_reg1', sess.graph)

    # Training cycle
    for epch in range(trin_ep):
        average_cst = 0.
        total_batch = int(Dataset_mnist.train.num_examples/batch_siz)
        # Loop over all batches
        for i in range(total_batch):
            batch_xs, batch_ys = Dataset_mnist.train.next_batch(batch_siz)
            # Run optimization op (backprop) and cost op (to get loss value)
            _, c = sess.run([optim_zer, cst_val], feed_dict={x_label: batch_xs,
                                                          y_label: batch_ys})
            # Compute average loss
            average_cst += c / total_batch
        # Display logs per epoch step
        if (epch+1) % disp_step == 0:
            print("Epochs:", '%04d' % (epch+1), "cost=", "{:.9f}".format(average_cst))
    writer.close()
    print("Optimizing Finished Here!")

    # Test model
    crrect_prediction = tf.equal(tf.argmax(predict_val, 1), tf.argmax(y_label, 1))
    # Calculate accuracy
    acuracy = tf.reduce_mean(tf.cast(crrect_prediction, tf.float32))
    print("Accuracy_of_the_model:", acuracy.eval({x_label: Dataset_mnist.test.images, y_label: Dataset_mnist.test.labels}))

