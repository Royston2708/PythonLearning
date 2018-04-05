import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("tmp/data/", one_hot=True)

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10
batch_size = 100

# The picture taken in is 28x28 pixels. Matrix dimensions are height x width
x = tf.placeholder("float", [None, 784])
y = tf.placeholder("float")

def neural_network_model(data):
    hidden_1_layer  = {"weights": tf.Variable(tf.random_normal([784,n_nodes_hl1])),
                       "biases": tf.Variable(tf.random_normal(n_nodes_hl1))}

    hidden_2_layer = {"weights": tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      "biases": tf.Variable(tf.random_normal(n_nodes_hl2))}

    hidden_3_layer = {"weights": tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      "biases": tf.Variable(tf.random_normal(n_nodes_hl3))}

    output_layer = {"weights": tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                      "biases": tf.Variable(tf.random_normal(n_classes))}

# The network format is ((input* weights) + biases)

    l1 = tf.add(tf.matmul(data,hidden_1_layer["weights"]),hidden_1_layer["biases"])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(data,hidden_2_layer["weights"]),hidden_2_layer["biases"])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(data, hidden_3_layer["weights"]),hidden_3_layer["biases"])
    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3,output_layer["weights"]) + output_layer["biases"]

    return output

def train_neural_net(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(prediction,y))
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    hm_epochs = 10

    with tf.Session as sess:
        sess.run(tf.initialize_all_variables())

        for epoch in hm_epochs:
            epoch_cost = 0
            for _ in range(int(mnist.train.num_examples/batch_size)):

                x,y = mnist.train.next_batch(batch_size)
                _,c = sess.run([optimizer,cost], feed_dict= {x:x, y:y})
                epoch_cost += c

            print("Epoch", epoch , "completed out of:", hm_epochs , "Cost:", epoch_cost)
