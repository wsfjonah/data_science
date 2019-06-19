import numpy as np
import datetime

import reporting.services.chart.base_chart as base_chart
import reporting.services.chart.tsda_chart as tsda_chart
import reporting.services.chart.transient_chart as transient_chart
import reporting.services.chart.correlation_chart as correlation_chart
import reporting.services.simulator.transient_sim as transient_sim


def test_base_chart():
    chart = base_chart.BaseChart('Data Chart', 'X bar', 'Y bar')
    n = 8
    x = np.arange(n) + 1
    y = np.random.uniform(0.5, 1.0, n)
    chart.set_data(x=x, y=y).plot().show()


def test_tsda_chart():
    chart = tsda_chart.TsdaChart('Data Chart', 'X bar', 'Y bar')
    n = 8
    x = np.arange(n) + 1
    y = np.random.uniform(0.5, 1.0, n)
    chart.set_data(x=x, y=y).plot().show()


def test_transient_chart():
    time_list, value_list = transient_sim.TransientSimulator(datetime.datetime.now()).generate()
    chart = transient_chart.TransientChart("Transient", "Time", "Value")
    chart.set_data(x=time_list, y=value_list).plot().show()


def test_correlation_chart():
    chart = correlation_chart.CorrelationChart('Web Access Log', 'Hr', 'Count')
    n = 24
    chart.set_data(x=np.arange(n) + 1, y=np.random.uniform(50, 100, n))
    chart.set_data(x=np.arange(n) + 1, y=np.random.uniform(20, 50, n))
    chart.set_data(x=np.arange(n) + 1, y=np.random.uniform(10, 20, n))
    chart.plot().show()


if __name__ == "__main__":
    test_base_chart()
    test_tsda_chart()
    test_transient_chart()
    test_correlation_chart()
