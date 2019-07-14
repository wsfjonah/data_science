import numpy as np

import reporting.services.echarts.bar_echarts as bar_echarts
import reporting.services.echarts.scatter_echarts as scatter_echarts


def test_bar_echarts():
    chart = bar_echarts.BarChart('Data Chart', 'X bar', 'Y bar')
    n = 8
    chart.set_data(x=(np.arange(n) + 1).tolist(), y=np.random.randint(1, 10, n).tolist())
    # chart.set_data(x=(np.arange(n) + 1).tolist(), y=np.random.randint(1, 10, n).tolist())
    chart.plot().show().render('bar.html')


def test_scatter_chart():
    chart = scatter_echarts.ScatterChart('Data Chart', 'X bar', 'Y bar')
    chart.set_data(x=np.arange(30).tolist(), y=(np.arange(30) + 3 * np.random.randn(30)).tolist())
    chart.plot().show().render('scatter.html')


if __name__ == "__main__":
    test_bar_echarts()
    test_scatter_chart()

