import pyecharts.options as opts
from pyecharts.charts import Bar
import numpy as np

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]

Bar().add_xaxis(attr).add_yaxis("商家A", v1, stack="stack1").add_yaxis("商家B", v2, stack="stack1").\
    set_series_opts(label_opts=opts.LabelOpts(is_show=False)).\
    set_global_opts(title_opts=opts.TitleOpts(title="柱状图数据堆叠示例")).render("bar1.html")

x = np.arange(6) + 1
v = np.random.uniform(1, 10, 6).tolist()

print(x)
chart = Bar(init_opts=opts.InitOpts(page_title='Bar Echart2'))
chart.add_xaxis(x.tolist())
chart.add_yaxis("Y bar", v, stack="stack1")
chart.set_series_opts(label_opts=opts.LabelOpts(is_show=True))
chart.set_global_opts(
    title_opts=opts.TitleOpts(title="Bar Echart 2", pos_top='top', pos_left='left'),
    toolbox_opts=opts.ToolboxOpts(is_show=True),
    xaxis_opts=opts.AxisOpts(name='X Axis', name_location='center'),
    yaxis_opts=opts.AxisOpts(name='Y Axis'),
)
# chart.set_global_opts(datazoom_opts=opts.DataZoomOpts(is_show=True, type_='slider', range_start=0, range_end=100))
# chart.set_global_opts(xaxis_opts=opts.AxisOpts(name='X Axis', name_location='center'))
# chart.set_global_opts(yaxis_opts=opts.AxisOpts(name='Y Axis'))
# chart.set_global_opts(title_opts=opts.TitleOpts(title="Bar Echart 2", pos_top='top', pos_left='left'))
chart.render("bar2.html")
