import numpy as np

import reporting.services.echarts.bar_echarts as bar_echarts


def test_bar_echarts():
    chart = bar_echarts.BarChart('Data Chart', 'X bar', 'Y bar')
    n = 8
    chart.set_data(x=np.arange(n) + 1, y=np.random.randint(1, 10, n).tolist())
    chart.set_data(x=np.arange(n) + 1, y=np.random.randint(1, 10, n).tolist())
    chart.plot().show().render()


if __name__ == "__main__":
    test_bar_echarts()

