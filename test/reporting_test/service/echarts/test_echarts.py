import numpy as np
import datetime

import reporting.services.echarts.bar_echarts as bar_echarts
import reporting.services.echarts.scatter_echarts as scatter_echarts
import reporting.services.echarts.base_axis as base_axis
import reporting.services.echarts.timeseries_axis as timeseries_axis
import reporting.services.simulator.transient_sim as transient_sim


def test_base_axis():
    chart = base_axis.BaseAxis('Data Chart', 'X', 'Y axis')
    n = 8
    x = (np.arange(n) + 1).tolist()
    y = np.random.randint(1, 10, n).tolist()
    chart.set_x_axis(x)
    chart.add_y_axis(y)
    print(x)
    print(y)
    chart.get_chart().render('base1.html')

    chart = base_axis.BaseAxis('Data Chart', 'X', 'Y axis', main_chart_type='bar')
    n = 8
    x = (np.arange(n) + 1).tolist()
    y = np.random.randint(1, 10, n).tolist()
    chart.set_x_axis(x)
    chart.add_y_axis(y)
    chart.get_chart().render('base2.html')


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


def test_timeseries_chart():
    chart = timeseries_axis.TimeSeriesAxis('Time Chart')
    x, y = transient_sim.TransientSimulator(datetime.datetime.now()).generate()
    chart.set_x_axis(x)
    chart.add_y_axis(y)
    chart.get_chart().render('timeseries.html')


if __name__ == "__main__":
    test_base_axis()
    # test_bar_echarts()
    # test_scatter_chart()

