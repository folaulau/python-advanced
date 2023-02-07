import matplotlib.pyplot as plt
import numpy as np

# print("matplotlib version={}".format(plt.__version__))

class MyMatPlot(object):
    def __init__(self):
        pass

    def run(self):
        # xpoints = np.array([0, 6])
        # ypoints = np.array([0, 250])
        #
        # plt.plot(xpoints, ypoints)
        # # plt.plot(xpoints, ypoints, 'x')
        # plt.show()

        plt.title("Sports Watch Data")
        plt.xlabel("Average Pulse")
        plt.ylabel("Calorie Burnage")

        xpoints = np.array([1, 2, 6, 8])
        ypoints = np.array([3, 8, 1, 10])

        # marker|linestyle|color
        plt.plot(xpoints, ypoints, marker= 'o', color='r', linestyle=':')
        plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_matplot = MyMatPlot()
    my_matplot.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
