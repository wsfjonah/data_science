import reporting.services.chart.base_chart as base_chart
import pyecharts.options as opts
from pyecharts.charts import Bar


class BarChart(base_chart.BaseChart):
    chart = None

    def __init__(self, title, label_x, label_y):
        base_chart.BaseChart.__init__(self, title, label_x, label_y)

    def set_data(self, **data):
        if ('x' in data) & ('y' in data):
            self.data.append([data['x'], data['y']])
        return self

    def show(self):
        return self.chart

    def plot(self):
        self.chart = Bar()
        self.chart.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        self.chart.set_global_opts(title_opts=opts.TitleOpts(title=self.title))
        self.chart.add_xaxis(self.data[0][0])
        index = 0
        for data_set in self.data:
            self.chart.add_yaxis(self.label_y+str(index), data_set[1], stack="stack")
            index += 1
        return self

