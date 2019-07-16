import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Line
from example.commons import Faker


def overlap_line_scatter() -> Bar:
    x = Faker.choose()
    y = Faker.values()
    x2 = [x[0], x[2], x[3]]
    y2 = [y[0], y[2], y[3]]
    print('x', x)
    print('x2', x2)
    bar = (
        Bar()
        .add_xaxis(x2)
        .add_yaxis("商家A", y2)
    )
    line = (
        Line()
        .add_xaxis(x)
        .add_yaxis("商家B", y)
        .set_global_opts(title_opts=opts.TitleOpts(title="Overlap-line+scatter"), toolbox_opts=opts.ToolboxOpts(is_show=True),)
    )
    line.overlap(bar)
    # bar.overlap(line)
    return line


overlap_line_scatter().render()

