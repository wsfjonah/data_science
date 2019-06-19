import numpy as np


class BaseSimulator:
    length = 10

    def __init__(self, length):
        self.length = length

    def generate(self, value_func):
        x_list = np.arange(self.length) + 1
        y_list = value_func(self.length)
        return x_list, y_list
