import pyecharts.options as opts
import pyecharts.charts


class BaseAxis:
    _main_chart_type = pyecharts.charts.Line
    _x_axis_type = 'value'  # Line type is value, Bar type is category

    chart = None
    title = ''
    x_axis_name = ''
    y_axis_name = ''
    width = 0
    height = 0

    init_opt = {}
    global_opt = {}

    x_data = []

    def __init__(self, title, x_axis_name, y_axis_name, width=400, height=400, main_chart_type='line'):
        self.title = title
        self.x_axis_name = x_axis_name
        self.y_axis_name = y_axis_name
        self.width = width
        self.height = height
        if main_chart_type is 'bar':
            self._main_chart_type = pyecharts.charts.Bar
            self._x_axis_type = 'category'
        self._init_base_axis()

    def _init_base_axis(self):
        self.init_opt['page_title'] = self.title
        self.global_opt['title_opts'] = opts.TitleOpts(title=self.title)
        self.global_opt['toolbox_opts'] = opts.ToolboxOpts(is_show=True)
        self.global_opt['datazoom_opts'] = opts.DataZoomOpts(is_show=True, type_='slider', range_start=0, range_end=100)
        self.global_opt['xaxis_opts'] = opts.AxisOpts(name=self.x_axis_name, type_=self._x_axis_type, is_scale=True,
                                                      splitline_opts=opts.SplitLineOpts(is_show=True))
        self.global_opt['yaxis_opts'] = opts.AxisOpts(name=self.y_axis_name, is_scale=True,
                                                      splitline_opts=opts.SplitLineOpts(is_show=True))

        if self.width > 0:
            self.init_opt['width'] = str(self.width)+'px'
        if self.height > 0:
            self.init_opt['height'] = str(self.height)+'px'
        self.chart = self._main_chart_type(init_opts=opts.InitOpts(**self.init_opt))

    def set_x_axis(self, x):
        self.x_data = x
        self.chart.add_xaxis(x)

    def add_y_axis(self, y):
        self.chart.add_yaxis(self.y_axis_name, y)

    def get_chart(self):
        self.chart.set_global_opts(**self.global_opt)
        self.chart.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        return self.chart

