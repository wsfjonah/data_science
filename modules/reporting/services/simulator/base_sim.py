import numpy as np


class BaseSimulator:
    length = 10

    def __init__(self, length):
        self.length = length

    def generate(self):
        x_list = np.arange(self.length) + 1
        y_list = np.random.uniform(0.5, 1.0, self.length)
        return x_list, y_list
