import reporting.services.chart.base_chart as base_chart
import numpy as np


class TsdaChart(base_chart.BaseChart):
    sub_plt = None

    def __init__(self, title, label_x, label_y):
        base_chart.BaseChart.__init__(self, title, label_x, label_y, win_x=12, win_y=4)

    def plot(self):
        self.sub_plt = self.fig.add_subplot(1, 1, 1)
        self.sub_plt.set_title(self.title, fontsize=20)
        self.sub_plt.set_xlabel(self.label_x)
        self.sub_plt.set_ylabel(self.label_y)

        self.sub_plt.plot(self.data_x, self.data_y, color='lightskyblue')
        return self


if __name__ == "__main__":
    chart = TsdaChart('Data Chart', 'X bar', 'Y bar')
    n = 8
    X = np.arange(n) + 1
    Y1 = np.random.uniform(0.5, 1.0, n)

    chart.set_data(x=X, y=Y1).plot().show()

