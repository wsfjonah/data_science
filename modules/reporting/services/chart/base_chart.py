from matplotlib import pyplot as plt


class BaseChart:
    fig = None
    sub_plt = None

    title = None
    label_x = None
    label_y = None

    data = []

    def __init__(self, title, label_x, label_y, style='bmh', win_x=9, win_y=6):
        plt.style.use(style)
        self.fig = plt.figure(figsize=(win_x, win_y))
        self.title = title
        self.label_x = label_x
        self.label_y = label_y
        self.data.clear()

    def clear(self):
        self.data.clear()

    def show(self):
        plt.show()

    def print_meta(self):
        print(self.title, self.label_x, self.label_y)

    def set_data(self, **data):
        if ('x' in data) & ('y' in data):
            self.clear()
            self.data.append([data['x'], data['y']])
        return self

    def get_plotter(self):
        sub_plt = self.fig.add_subplot(1, 1, 1)
        sub_plt.set_title(self.title, fontsize=20)
        sub_plt.set_xlabel(self.label_x)
        sub_plt.set_ylabel(self.label_y)
        return sub_plt

    def plot(self):
        self.sub_plt = self.get_plotter()
        self.sub_plt.bar(self.data[0][0], self.data[0][1], width=0.35, facecolor='lightskyblue', edgecolor='white')
        # self.sub_plt.axvspan(1, 2, alpha=0.2)
        return self
