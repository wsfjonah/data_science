import reporting.services.chart.base_chart as base_chart


class CorrelationChart(base_chart.BaseChart):
    MAX_PLOT = 4
    width = 0.35
    facecolor = ['lightskyblue', 'yellowgreen', 'lightblue', 'orange']
    edgecolor = 'white'

    data = []

    def __init__(self, title, xaxis_name, yaxis_name):
        base_chart.BaseChart.__init__(self, title, xaxis_name, yaxis_name, win_x=12, win_y=6)

    def set_data(self, **data):
        if ('x' in data) & ('y' in data):
            if 'label' in data:
                self.data.append([data['x'], data['y'], data['label']])
            else:
                self.data.append([data['x'], data['y']])
        return self

    def plot(self):
        if len(self.data) > self.MAX_PLOT:
            raise Exception("No. of data set " + str(len(self.data)) + " is more than max: " + str(self.MAX_PLOT))
        self.axes = self.get_axes()
        index = 0
        for data_set in self.data:
            label = str(index)
            if len(data_set) > 2:  # get label from data set
                label = data_set[2]

            self.axes.bar(data_set[0], data_set[1], width=self.width, facecolor=self.facecolor[index],
                             edgecolor=self.edgecolor, label=label)
            index += 1
        return self
