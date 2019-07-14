import reporting.services.chart.base_chart as base_chart


class TsdaChart(base_chart.BaseChart):
    MAX_PLOT = 4
    facecolor = ['darkslateblue', 'lightskyblue', 'yellowgreen', 'lightblue', 'orange']

    def __init__(self, title, xaxis_name, yaxis_name):
        base_chart.BaseChart.__init__(self, title, xaxis_name, yaxis_name, win_x=12, win_y=4)

    def set_data(self, **data):
        if ('x' in data) & ('y' in data):
            self.data.append([data['x'], data['y']])
        return self

    def plot(self):
        if len(self.data) > self.MAX_PLOT:
            raise Exception("No. of data set " + str(len(self.data)) + " is more than max: " + str(self.MAX_PLOT))
        self.axes = self.get_axes()
        index = 0
        for data_set in self.data:
            self.axes.plot(data_set[0], data_set[1], color=self.facecolor[index], label=self.yaxis_name + " " + str(index))
            index += 1

        return self

