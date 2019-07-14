import reporting.services.chart.base_chart as base_chart
import pyecharts.options as opts
from pyecharts.charts import Scatter


class ScatterChart(base_chart.BaseChart):
    chart = None
    max_y = None
    max_x = None
    min_x = None

    def __init__(self, title, xaxis_name, yaxis_name, xaxis_formatter):
        base_chart.BaseChart.__init__(self, title, xaxis_name, yaxis_name, xaxis_formatter=xaxis_formatter)

    def clear(self):
        self.data.clear()

    def set_data(self, **data):
        self.clear()
        if ('x' in data) & ('y' in data):
            self.data.append([data['x'], data['y']])
            self.max_x = max(data['x'])
            self.max_y = max(data['y'])
            self.min_x = min(data['x'])
            if 'max_x' in data:
                self.max_x = data['max_x']
            if 'min_x' in data:
                self.min_x = data['min_x']
            if 'max_y' in data:
                self.max_y = data['max_y']
        return self

    def show(self):
        return self.chart

    def plot(self):
        self.chart = Scatter(init_opts=opts.InitOpts(page_title=self.title, width='600px', height='500px'))

        # load data
        self.chart.add_xaxis(self.data[0][0])
        self.chart.add_yaxis(self.yaxis_name, self.data[0][1])

        # set options
        self.chart.set_global_opts(
            title_opts=opts.TitleOpts(title=self.title),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=opts.DataZoomOpts(is_show=True, type_='slider', range_start=0, range_end=100),
            xaxis_opts=opts.AxisOpts(name=self.xaxis_name, type_='time',
                                     name_location='end', name_gap=15, splitline_opts=opts.SplitLineOpts(is_show=True),
                                     min_=self.min_x, max_=self.max_x),
            yaxis_opts=opts.AxisOpts(name=self.yaxis_name, name_location='center',
                                     name_gap=15, splitline_opts=opts.SplitLineOpts(is_show=True),
                                     max_=self.max_y),
            visualmap_opts=opts.VisualMapOpts(max_=self.max_y)
        )
        self.chart.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

        return self
