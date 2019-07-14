import random
from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import HeatMap


def heatmap_base() -> HeatMap:
    value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    print(Faker.clock)
    print(Faker.week)
    print(value)
    c = (
        HeatMap()
            .add_xaxis(Faker.clock)
            .add_yaxis("series", Faker.week, value)
            .set_global_opts(title_opts=opts.TitleOpts(title="HeatMap-基本示例"), visualmap_opts=opts.VisualMapOpts(), )
    )
    return c


if __name__ == "__main__":
    heatmap_base().render("heatMap.html")