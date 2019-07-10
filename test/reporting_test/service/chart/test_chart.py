import numpy as np
import datetime

import reporting.services.chart.base_chart as base_chart
import reporting.services.chart.tsda_chart as tsda_chart
import reporting.services.chart.transient_chart as transient_chart
import reporting.services.chart.correlation_chart as correlation_chart
import reporting.services.chart.scatter_chart as scatter_chart
import reporting.services.simulator.transient_sim as transient_sim
import reporting.services.chart.bar3d_chart as bar3d_chart


def test_base_chart():
    chart = base_chart.BaseChart('Data Chart', 'X bar', 'Y bar')
    n = 8
    x = np.arange(n) + 1
    y = np.random.uniform(0.5, 1.0, n)
    chart.set_data(x=x, y=y).plot().show()


def test_tsda_chart():
    chart = tsda_chart.TsdaChart('Data Chart', 'X bar', 'Y bar')
    n = 8
    chart.set_data(x=np.arange(n) + 1, y=np.random.uniform(0.5, 1.0, n))
    chart.set_data(x=np.arange(n) + 1, y=np.random.uniform(0.5, 1.0, n))
    chart.set_data(x=np.arange(n) + 1, y=np.random.uniform(0.5, 1.0, n))
    chart.set_data(x=np.arange(n) + 1, y=np.random.uniform(0.5, 1.0, n))
    chart.plot().show()


def test_transient_chart():
    time_list, value_list = transient_sim.TransientSimulator(datetime.datetime.now()).generate()
    chart = transient_chart.TransientChart("Transient", "Time", "Value")
    chart.set_data(x=time_list, y=value_list).plot().show()


def test_correlation_chart():
    chart = correlation_chart.CorrelationChart('Web Access Log', 'Hr', 'Count')
    n = 24
    chart.set_data(x=np.arange(n) + 1, y=np.random.uniform(50, 100, n))
    chart.set_data(x=np.arange(n) + 1, y=np.random.uniform(30, 60, n))
    chart.set_data(x=np.arange(n) + 1, y=np.random.uniform(20, 35, n))
    chart.set_data(x=np.arange(n) + 1, y=np.random.uniform(10, 20, n))
    chart.plot().show()


def test_bar3d_chart():
    chart = bar3d_chart.Bar3DChart('Data Chart', 'X bar', 'Y bar', 'Z')
    n = 8
    chart.set_data(x=np.arange(n) + 1, y=np.random.uniform(0.5, 1.0, n), z=np.random.uniform(20, 30, n))
    chart.plot().show()


def test_scatter_chart():
    chart = scatter_chart.ScatterChart('Data Chart', 'X bar', 'Y bar')
    n = 60
    chart.set_data(x=np.arange(30), y=np.arange(30) + 3 * np.random.randn(30))
    chart.plot().show()


if __name__ == "__main__":
    test_base_chart()
    '''
    test_tsda_chart()
    test_transient_chart()
    test_correlation_chart()
    test_bar3d_chart()
    
    test_scatter_chart()
    '''
