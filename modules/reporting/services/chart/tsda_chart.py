import reporting.services.chart.base_chart as base_chart
from matplotlib import pyplot as plt
import numpy as np


class TsdaChart(base_chart.BaseChart):
    def __init__(self, title, label_x, label_y):
        base_chart.BaseChart.__init__(self, title, label_x, label_y)

    def plot(self):
        sub_plt = self.fig.add_subplot(1, 1, 1)
        sub_plt.set_title(self.title, fontsize=20)
        sub_plt.set_xlabel(self.label_x)
        sub_plt.set_ylabel(self.label_y)

        plt.plot(self.data_x, self.data_y, color='lightskyblue')
        plt.show()


if __name__ == "__main__":
    chart = TsdaChart('Data Chart', 'X bar', 'Y bar')
    n = 8
    X = np.arange(n) + 1
    Y1 = np.random.uniform(0.5, 1.0, n)

    chart.set_data(x=X, y=Y1)

    chart.plot()
