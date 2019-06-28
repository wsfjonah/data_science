from matplotlib import pyplot as plt


class BaseChart:
    fig = None
    axes = None

    title = None
    label_x = None
    label_y = None

    xaxis_formatter = None

    data = []

    def __init__(self, title, label_x, label_y, style='bmh', win_x=9, win_y=6, xaxis_formatter=None):
        plt.style.use(style)
        self.fig = plt.figure(figsize=(win_x, win_y))
        self.title = title
        self.label_x = label_x
        self.label_y = label_y
        self.xaxis_formatter = xaxis_formatter
        self.data.clear()

    def clear(self):
        self.data.clear()

    def show(self):
        if self.axes is not None:
            self.axes.legend()
        plt.show()

    def print_meta(self):
        print(self.title, self.label_x, self.label_y)

    def set_data(self, **data):
        if ('x' in data) & ('y' in data):
            self.clear()
            self.data.append([data['x'], data['y']])
        return self

    def get_axes(self):
        axes0 = self.fig.add_subplot(1, 1, 1)
        axes0.set_title(self.title, fontsize=20)
        axes0.set_xlabel(self.label_x)
        axes0.set_ylabel(self.label_y)
        if self.xaxis_formatter is not None:
            axes0.xaxis.set_major_formatter(self.xaxis_formatter)
        return axes0

    def plot(self):
        self.axes = self.get_axes()
        self.axes.bar(self.data[0][0], self.data[0][1], width=0.35, facecolor='lightskyblue', edgecolor='white',
                      label=self.label_y)
        # self.axes.axvspan(1, 2, alpha=0.2)
        return self
