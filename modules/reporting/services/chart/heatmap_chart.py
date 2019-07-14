from matplotlib import cm
from matplotlib import pyplot as plt

import reporting.services.chart.base_chart as base_chart


class HeatMapChart(base_chart.BaseChart):
    color_map = cm.Reds
    label_z = ''

    data_x = []
    data_y = []
    heat_map = []

    def __init__(self, title, xaxis_name, yaxis_name, zaxis_name):
        base_chart.BaseChart.__init__(self, title, xaxis_name, yaxis_name, win_x=20, win_y=5)
        self.zaxis_name = zaxis_name

    def set_data(self, **data):
        if ('x' in data) & ('y' in data) & ('map' in data):
            self.data_x = data['x']
            self.data_y = data['y']
            self.heat_map = data['map']

    def plot(self):
        self.axes = self.get_axes()
        self.axes.set_yticks(range(len(self.data_y)))
        self.axes.set_yticklabels(self.data_y)
        self.axes.set_xticks(range(len(self.data_x)))
        self.axes.set_xticklabels(self.data_x)
        vmax = self.heat_map[0][0]
        vmin = self.heat_map[0][0]
        for i in self.heat_map:
            for j in i:
                if j > vmax:
                    vmax = j
                if j < vmin:
                    vmin = j

        im_map = self.axes.imshow(self.heat_map, interpolation='nearest', cmap=self.color_map, aspect='auto', vmin=vmin, vmax=vmax)
        plt.colorbar(mappable=im_map, cax=None, ax=None, shrink=0.5)
        plt.xticks(rotation=0)  # 90 to rotate the text in x bar
        plt.yticks(rotation=360)
        return self

