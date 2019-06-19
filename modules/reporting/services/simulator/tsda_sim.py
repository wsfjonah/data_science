import reporting.services.simulator.base_sim as base_sim
import datetime
import numpy as np


class TsdaSimulator(base_sim.BaseSimulator):
    interval = None  # in seconds
    end_time = None

    def __init__(self, length, interval_sec=60, end_time=datetime.datetime.now()):  # default interval is 60s
        base_sim.BaseSimulator.__init__(self, length)
        self.interval = interval_sec
        self.end_time = end_time

    def value_uniform(self, length):
        return np.random.uniform(0.5, 1.0, length)

    def generate(self, value_func=value_uniform):
        x_list = np.array([])
        y_list = value_func(self, length=self.length)
        count = 0
        while count < self.length:
            curr_time = self.end_time-datetime.timedelta(seconds=self.interval*count)
            x_list = np.append(x_list, curr_time)
            # print(curr_time.hour)
            if curr_time.hour < 8:
                y_list[count] = y_list[count] + 20
            count = count + 1
        return x_list, y_list


if __name__ == "__main__":
    sim = TsdaSimulator(100, 3600)
    X, Y = sim.generate()
    print(X)
    print(Y)

