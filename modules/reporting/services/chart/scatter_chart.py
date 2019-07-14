from matplotlib import cm
import reporting.services.chart.base_chart as base_chart


class ScatterChart(base_chart.BaseChart):
    def __init__(self, title, xaxis_name, yaxis_name, xaxis_formatter=None):
        base_chart.BaseChart.__init__(self, title, xaxis_name, yaxis_name, xaxis_formatter=xaxis_formatter, win_x=12, win_y=4)

    def plot(self):
        self.axes = self.get_axes()
        # self.axes.xaxis.set_major_formatter(DateFormatter('%H:%M'))
        self.axes.scatter(self.data[0][0], self.data[0][1], s=60, c='r', cmap=cm.Reds, alpha=0.5)
        self.axes.set_xlim(min(self.data[0][0]), max(self.data[0][0]))
        return self
