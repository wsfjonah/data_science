from matplotlib import pyplot as plt
import numpy as np


class BaseChart:
    fig = ''
    title = ''
    label_x = ''
    label_y = ''
    data_x = ''
    data_y = ''

    def __init__(self, title, label_x, label_y, style='bmh', win_x=9, win_y=6):
        plt.style.use(style)
        self.fig = plt.figure(figsize=(win_x, win_y))
        self.title = title
        self.label_x = label_x
        self.label_y = label_y

    def show(self):
        plt.show()

    def set_data(self, **data):
        if 'x' in data:
            self.data_x = data['x']
        if 'y' in data:
            self.data_y = data['y']
        return self

    def plot(self):
        sub_plt = self.fig.add_subplot(1, 1, 1)
        sub_plt.set_title(self.title, fontsize=20)
        sub_plt.set_xlabel(self.label_x)
        sub_plt.set_ylabel(self.label_y)
        sub_plt.bar(self.data_x, self.data_y, width=0.35, facecolor='lightskyblue', edgecolor='white')
        # sub_plt.axvspan(1, 2, alpha=0.2)
        return self


if __name__ == "__main__":
    chart = BaseChart('Data Chart', 'X bar', 'Y bar')
    n = 8
    X = np.arange(n) + 1
    Y1 = np.random.uniform(0.5, 1.0, n)

    chart.set_data(x=X, y=Y1).plot().show()

