from matplotlib import pyplot as plt
import numpy as np


class BaseChart:
    fig = ''
    title = ''
    label_x = ''
    label_y = ''
    data_x = ''
    data_y = ''

    def __init__(self, title, label_x, label_y):
        self.fig = plt.figure(figsize=(9, 6))
        self.title = title
        self.label_x = label_x
        self.label_y = label_y

    def set_data(self, **data):
        if 'x' in data:
            self.data_x = data['x']
        if 'y' in data:
            self.data_y = data['y']

    def plot(self):
        sub_plt = self.fig.add_subplot(1, 1, 1)
        sub_plt.set_title(self.title, fontsize=20)
        sub_plt.set_xlabel(self.label_x)
        sub_plt.set_ylabel(self.label_y)

        plt.bar(self.data_x, self.data_y, width=0.35, facecolor='lightskyblue', edgecolor='white')
        plt.show()


if __name__ == "__main__":
    chart = BaseChart('Data Chart', 'X bar', 'Y bar')
    n = 8
    X = np.arange(n) + 1
    Y1 = np.random.uniform(0.5, 1.0, n)

    chart.set_data(x=X, y=Y1)

    chart.plot()

