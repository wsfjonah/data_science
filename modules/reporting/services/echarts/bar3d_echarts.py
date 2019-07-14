import reporting.services.chart.base_chart as base_chart
import pyecharts.options as opts
from pyecharts.charts import Bar3D


class Bar3DChart(base_chart.BaseChart):
    chart = None

    zaxis_name = None

    data_x = []
    data_y = []
    heat_map = []
    max_value = 0
    min_value = 0

    def __init__(self, title, xaxis_name, yaxis_name, zaxis_name):
        base_chart.BaseChart.__init__(self, title, xaxis_name, yaxis_name)
        self.zaxis_name = zaxis_name

    def clear(self):
        self.data_x.clear()
        self.data_y.clear()
        self.heat_map.clear()

    def set_data(self, **data):
        if ('x' in data) & ('y' in data) & ('map' in data):
            self.data_x = data['x']
            self.data_y = data['y']
            self.to_echarts_map(data['map'])
        return self

    def show(self):
        return self.chart

    def to_echarts_map(self, map) -> []:
        self.max_value = map[0][0]
        self.min_value = map[0][0]
        for i in range(len(map)):
            for j in range(len(map[i])):
                if self.max_value < map[i][j]:
                    self.max_value = map[i][j]
                if self.min_value > map[i][j]:
                    self.min_value = map[i][j]
                self.heat_map.append([j, i, map[i][j]])
        return self.heat_map

    def plot(self):
        self.chart = Bar3D(init_opts=opts.InitOpts(page_title=self.title))
        self.chart.add(
            self.zaxis_name,
            [[d[1], d[0], d[2]] for d in self.heat_map],
            xaxis3d_opts=opts.Axis3DOpts(self.data_y, type_="category", name=self.yaxis_name, name_gap=25),
            yaxis3d_opts=opts.Axis3DOpts(self.data_x, type_="category", name=self.xaxis_name, name_gap=25),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        self.chart.set_global_opts(
            title_opts=opts.TitleOpts(title=self.title),
            visualmap_opts=opts.VisualMapOpts(max_=self.max_value, min_=self.min_value)
        )
        return self

