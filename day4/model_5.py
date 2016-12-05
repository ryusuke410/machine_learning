import tensorflow as tf
import numpy as np


def model(dataset):

    # The shape of pows should be nx2 to do with the meaning

    # Create the model
    pows = tf.placeholder(tf.float32, [None, 6])
    coeffs = tf.Variable(tf.zeros([6, 1]))
    y = tf.matmul(pows, coeffs)  # nx1

    # Define loss and optimizer
    y_ = tf.placeholder(tf.float32, [None, 1])
    error = tf.reduce_sum(tf.square(y_ - y))
    eps = 0.001
    train_step = tf.train.GradientDescentOptimizer(eps).minimize(error)

    # modify dataset
    mult = dataset.data.flatten().mean()
    dim0 = mult * np.ones(dataset.leng)
    dim1 = dataset.xs.reshape(dataset.leng)
    dim2 = dim1 * dim1
    dim3 = dim2 * dim1
    dim4 = dim3 * dim1
    dim5 = dim4 * dim1

    dataset.pows = np.c_[dim5, dim4, dim3, dim2, dim1, dim0]
    dataset.test_pows = dataset.pows[:dataset.test_leng]
    dataset.train_pows = dataset.pows[dataset.test_leng:]

    dataset.index = 0

    def next_batch(n):
        if dataset.index + n > dataset.train_leng:
            dataset.index = 0

        ind = dataset.index
        batch_pows = dataset.train_pows[ind: ind + n]
        batch_ys = dataset.train_ys[ind: ind + n]
        dataset.index += n
        return batch_pows, batch_ys

    # Train
    init_op = tf.initialize_all_variables()
    loop_times0 = 20
    loop_times = 1000

    # dataset.leng / 10 is not so important

    with tf.Session() as sess:
        sess.run(init_op)
        log_data = []           # type(log_data) != ndarray
        feed = {pows: dataset.test_pows, y_: dataset.test_ys}

        print("------------------------")

        for _ in range(loop_times0):
            batch_pows, batch_ys = next_batch(100)
            feed0 = {pows: batch_pows, y_: batch_ys}
            sess.run(train_step, feed_dict=feed0)
            log_data.append(sess.run(error, feed_dict=feed))
            print(sess.run(error, feed_dict=feed0))

        print("------------------------")

        for _ in range(loop_times):
            batch_pows, batch_ys = next_batch(100)
            feed0 = {pows: batch_pows, y_: batch_ys}
            sess.run(train_step, feed_dict=feed0)
            log_data.append(sess.run(error, feed_dict=feed))

        print("------------------------")

        for _ in range(loop_times0):
            batch_pows, batch_ys = next_batch(100)
            feed0 = {pows: batch_pows, y_: batch_ys}
            sess.run(train_step, feed_dict=feed0)
            log_data.append(sess.run(error, feed_dict=feed))
            print(sess.run(error, feed_dict=feed0))

        print("------------------------")

        coeffsfin = sess.run(coeffs).reshape(6)
        print(coeffsfin)

    np.save("./coeffs_1.npy", coeffsfin)
    np.save("./log_data.npy", log_data)

    def func(x):
        x2 = x * x
        x3 = x2 * x
        x4 = x3 * x
        x5 = x4 * x
        pows = np.array([x5, x4, x3, x2, x, mult])
        return np.sum(pows * coeffsfin)

    print(coeffsfin)

    # coeffs_modified = np.append(coeffsfin[:5], coeffsfin[5] * mult)

    return func
    # return (lambda x: np.polyval(coeffs_modified, x))
