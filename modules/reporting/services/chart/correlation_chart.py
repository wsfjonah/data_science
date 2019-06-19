import reporting.services.chart.base_chart as base_chart


class CorrelationChart(base_chart.BaseChart):
    MAX_PLOT = 4
    width = 0.35
    facecolor = ['lightskyblue', 'yellowgreen', 'lightblue', 'orange']
    edgecolor = 'white'

    data = []

    def __init__(self, title, label_x, label_y):
        base_chart.BaseChart.__init__(self, title, label_x, label_y, win_x=12, win_y=6)

    def set_data(self, **data):
        if ('x' in data) & ('y' in data):
            self.data.append([data['x'], data['y']])
        return self

    def plot(self):
        if len(self.data) > self.MAX_PLOT:
            raise Exception("No. of data set " + str(len(self.data)) + " is more than max: " + str(self.MAX_PLOT))
        self.sub_plt = self.get_plotter()
        index = 0
        for data_set in self.data:
            self.sub_plt.bar(data_set[0], data_set[1], width=self.width, facecolor=self.facecolor[index],
                             edgecolor=self.edgecolor)
            index += 1
        return self
