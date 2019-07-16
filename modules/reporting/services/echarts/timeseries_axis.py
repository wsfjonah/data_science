import reporting.services.echarts.base_axis as base_axis
import pyecharts.options as opts
import pyecharts.charts


class TimeSeriesAxis(base_axis.BaseAxis):
    _main_chart_type = pyecharts.charts.Line
    _x_axis_type = 'time'

    def __init__(self, title, x_axis_name='Time', y_axis_name='Value', width=900, height=400):
        base_axis.BaseAxis.__init__(self, title, x_axis_name, y_axis_name, width, height)


