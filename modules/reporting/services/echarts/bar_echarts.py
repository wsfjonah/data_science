import reporting.services.chart.base_chart as base_chart
import pyecharts.options as opts
from pyecharts.charts import Bar


class BarChart(base_chart.BaseChart):
    chart = None

    def __init__(self, title, label_x, label_y):
        base_chart.BaseChart.__init__(self, title, label_x, label_y)

    def set_data(self, **data):
        if ('x' in data) & ('y' in data):
            if 'label' in data:
                self.data.append([data['x'], data['y'], data['label']])
            else:
                self.data.append([data['x'], data['y']])
        return self

    def show(self):
        return self.chart

    def plot(self):
        self.chart = Bar(init_opts=opts.InitOpts(page_title=self.title))
        self.chart.add_xaxis(self.data[0][0])
        index = 0
        max_y = 0  # pyecharts bug to adjust yaxis when toolbox is shown in stack
        for data_set in self.data:
            if len(data_set) > 2:  # get label from data set
                label = data_set[2]
            else:
                label = self.label_y+str(index)
            # self.chart.add_yaxis(label, data_set[1], stack="stack"+str(index))
            self.chart.add_yaxis(label, data_set[1], stack="stack")
            max_y += max(data_set[1])
            index += 1

        self.chart.set_global_opts(
            title_opts=opts.TitleOpts(title=self.title),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=opts.DataZoomOpts(is_show=True, type_='slider', range_start=0, range_end=100),
            xaxis_opts=opts.AxisOpts(name=self.label_x, name_location='end', name_gap=15),
            yaxis_opts=opts.AxisOpts(name=self.label_y, name_location='center', name_gap=25, max_=int(max_y*1.1))
        )
        self.chart.set_series_opts(label_opts=opts.LabelOpts(is_show=False, position='inside'))

        return self

