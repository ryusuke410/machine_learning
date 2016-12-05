import numpy as np
import matplotlib.pyplot as plt


# mk_plot_result returns a shower(printer)
# showers take a function and do show the result


def g_mk_plot_result(dom, dataset, save_cond=[False, ""]):

    # dom is the domain of function the shower will take.

    def shower(func):
        fig = plt.figure()
        subplot = fig.add_subplot(1, 1, 1)

        # plot func
        cod = func(dom)
        subplot.plot(dom, cod, color='red')

        # plot dataset
        xs = dataset.data[:, 0]
        y_s = dataset.data[:, 1]
        subplot.scatter(xs, y_s, color='blue')

        plt.show()

        [do_save, name] = save_cond
        if do_save:
            fig.savefig(name)
        fig.clf()

    return shower


def mk_plot_result(dataset, save_cond=[False, ""]):

    # set dom

    x_min = np.min(dataset.xs)
    x_max = np.max(dataset.xs)
    margin = (x_max - x_min) / 100
    left = x_min - margin
    right = x_max + margin
    dom = np.arange(left, right, margin)

    return g_mk_plot_result(dom, dataset, save_cond=[False, ""])
