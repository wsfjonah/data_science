import reporting.services.chart.base_chart as base_chart


class TsdaChart(base_chart.BaseChart):
    def __init__(self, title, label_x, label_y):
        base_chart.BaseChart.__init__(self, title, label_x, label_y, win_x=12, win_y=4)

    def plot(self):
        self.sub_plt = self.get_plotter()
        self.sub_plt.plot(self.data_x, self.data_y, color='lightskyblue')
        return self
