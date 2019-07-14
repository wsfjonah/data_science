import reporting.services.chart.base_chart as base_chart
import pyecharts.options as opts
from pyecharts.charts import Bar


class BarChart(base_chart.BaseChart):
    chart = None
    max_sum_y = 0  # pyecharts bug to adjust yaxis when toolbox is shown in stack
    count_y = 0

    def __init__(self, title, xaxis_name, yaxis_name):
        base_chart.BaseChart.__init__(self, title, xaxis_name, yaxis_name)

    def clear(self):
        self.data.clear()
        self.max_sum_y = 0
        self.count_y = 0

    def set_data(self, **data):
        if ('x' in data) & ('y' in data):
            self.count_y += 1
            self.max_sum_y += max(data['y'])
            if 'label' in data:
                self.data.append([data['x'], data['y'], data['label']])
            else:
                self.data.append([data['x'], data['y']])
        return self

    def show(self):
        return self.chart

    def plot(self):
        self.chart = Bar(init_opts=opts.InitOpts(page_title=self.title))

        # load data
        self.chart.add_xaxis(self.data[0][0])
        index = 0
        for data_set in self.data:
            if len(data_set) > 2:  # get label from data set
                label = data_set[2]
            else:
                label = self.yaxis_name + str(index)
            # self.chart.add_yaxis(label, data_set[1], stack="stack"+str(index))
            self.chart.add_yaxis(label, data_set[1], stack="stack")
            index += 1

        # set options
        self.chart.set_global_opts(
            title_opts=opts.TitleOpts(title=self.title),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=opts.DataZoomOpts(is_show=True, type_='slider', range_start=0, range_end=100),
            xaxis_opts=opts.AxisOpts(name=self.xaxis_name, name_location='end', name_gap=15),
            yaxis_opts=opts.AxisOpts(name=self.yaxis_name, name_location='center', name_gap=25,
                                     max_=None if self.count_y <= 1 else int(self.max_sum_y*1.1))
        )
        self.chart.set_series_opts(label_opts=opts.LabelOpts(is_show=False, position='inside'))

        return self

