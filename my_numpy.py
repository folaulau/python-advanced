import numpy as np

print("numpy version={}".format(np.__version__))

class MyNumpy(object):
    def __init__(self):
        pass

    def run(self):
        arr = np.array([1, 2, 3, 4, 5])

        print(arr)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_numpy = MyNumpy()
    my_numpy.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
