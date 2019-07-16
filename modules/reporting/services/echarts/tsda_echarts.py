import reporting.services.chart.base_chart as base_chart
import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Line


class TsdaChart(base_chart.BaseChart):
    chart = None
    max_x = None
    min_x = None

    def __init__(self, title, xaxis_name, yaxis_name):
        base_chart.BaseChart.__init__(self, title, xaxis_name, yaxis_name)

    def clear(self):
        self.data.clear()

    def set_data(self, **data):
        if ('x' in data) & ('y' in data):
            self.max_x = max(data['x'])
            self.min_x = min(data['x'])
            if 'label' in data:
                self.data.append([data['x'], data['y'], data['label']])
            else:
                self.data.append([data['x'], data['y']])
        return self

    def show(self):
        return self.chart

    def plot(self):
        self.chart = Line(init_opts=opts.InitOpts(page_title=self.title))

        # load data
        self.chart.add_xaxis(self.data[0][0])
        index = 0
        for data_set in self.data:
            if len(data_set) > 2:  # get label from data set
                label = data_set[2]
            else:
                label = self.yaxis_name + str(index)

            if index == 0:
                print('append line:', data_set[0])
                print(data_set[1])
                self.chart.add_yaxis(label, data_set[1])
            else:
                print('append bar:', data_set[0])
                print(data_set[1])
                bar = Bar()
                bar.add_xaxis(data_set[0])
                bar.add_yaxis(label, data_set[1])

                self.chart.overlap(bar)
            index += 1

        # set options

        self.chart.set_global_opts(
            title_opts=opts.TitleOpts(title=self.title),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=opts.DataZoomOpts(is_show=True, type_='slider', range_start=0, range_end=100),
            # xaxis_opts=opts.AxisOpts(name=self.xaxis_name, type_='time', name_location='end', name_gap=15,
            #                          splitline_opts=opts.SplitLineOpts(is_show=True),
            #                          min_=self.min_x, max_=self.max_x),
            yaxis_opts=opts.AxisOpts(name=self.yaxis_name, name_location='center', name_gap=25,
                                     splitline_opts=opts.SplitLineOpts(is_show=True))
        )

        self.chart.set_series_opts(label_opts=opts.LabelOpts(is_show=False, position='inside'))

        return self

