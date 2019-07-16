import datetime
import numpy as np

import reporting.services.echarts.tsda_echarts as tsda_echarts
import reporting.services.simulator.tsda_sim as tsda_sim

duration = 200  # hours
base = 0.87
leak = False
mnf_x = []
mnf_y = []


def base_value(length):
    return (np.random.standard_normal(length)+5)*0.2 + 5


def value_adjust(index, curr_x, curr_y):
    global base, duration, leak, mnf_x, mnf_y
    curr_time = curr_x
    value = curr_y

    mnf_x.append(curr_time)
    mnf_y.append(None)
    if 1 < curr_time.hour < 3:  # midnight
        if index > duration/2 and not leak:  # leak
            print('leak')
            base = base - 0.4
            leak = True
        value = 0.1*curr_y + 1.5 + base

        mnf_y[index] = value
    elif 0 <= curr_time.hour <= 1:
        value = 0.1*curr_y + 1.7 + base
    elif curr_time.hour < 5:
        value = 0.1*curr_y + 1.7 + base
    elif 20 < curr_time.hour:  # evening
        value = 0.1*curr_y + 1.9 + base
    elif 18 < curr_time.hour:  # evening
        value = curr_y - 3.3 + base
    elif curr_time.hour < 8:  # early morning
        value = curr_y - 3.2 + base
    else:
        value = curr_y - 2.7 + base

    return round(value, 2)


chart = tsda_echarts.TsdaChart('Min-Night Flow Analysis', 'Time', 'Flow(LT/Sec)')
sim = tsda_sim.TsdaSimulator(duration, 3600)
X, Y = sim.generate(base_value, value_adjust)

chart.set_data(x=X.tolist()[::-1], y=Y.tolist()[::-1])
chart.set_data(x=mnf_x[::-1], y=mnf_y[::-1], label='MNF')
chart.plot().show().render('tsda.html')


