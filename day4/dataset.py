import numpy as np


class Dataset:

    def __init__(self, xys):    # xys: (L, 1)

        # type(dom)=numpy.array

        np.random.shuffle(xys)  # shuffle xys
        self.leng = len(xys)
        self.test_leng = int(min(100, self.leng / 100))
        self.train_leng = self.leng - self.test_leng

        self.data = xys
        self.test_data = xys[:self.test_leng]
        self.train_data = xys[self.test_leng:]

        self.xs, self.ys = np.hsplit(self.data, [1])  # shape = (L, 1)
        self.test_xs, self.test_ys = np.hsplit(self.test_data, [1])
        self.train_xs, self.train_ys = np.hsplit(self.train_data, [1])


def create_graph(func_, dom, noise=False):
    xs = dom
    ys_ = func_(dom)              # map dom with func
    if noise:
        l = xs.size             # length
        noise_arr = np.random.randn(l)
        ys = ys_ + noise_arr
    else:
        ys = ys_

    return np.c_[xs, ys]         # (L, 2)
