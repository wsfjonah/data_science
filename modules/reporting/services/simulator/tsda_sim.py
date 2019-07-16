import reporting.services.simulator.base_sim as base_sim
import datetime
import numpy as np


class TsdaSimulator(base_sim.BaseSimulator):
    interval = None  # in seconds
    end_time = None
    x_list = np.array([])
    y_list = np.array([])

    def __init__(self, length, interval_sec=60, end_time=datetime.datetime.now()):  # default interval is 60s
        base_sim.BaseSimulator.__init__(self, length)
        self.interval = interval_sec
        self.end_time = end_time

    def value_uniform(length):
        return np.random.uniform(0.5, 2.0, length)+5

    def value_adjust(index, curr_x, curr_y):
        curr_time = curr_x
        if 0 < curr_time.hour < 4:
            return curr_y - 5
        return curr_y

    def generate(self, base_value_func=value_uniform, value_adjust_func=value_adjust):
        self.y_list = base_value_func(self, length=self.length)
        count = 0
        while count < self.length:
            curr_time = self.end_time-datetime.timedelta(seconds=self.interval*count)
            self.x_list = np.append(self.x_list, curr_time)
            self.y_list[count] = round(self.y_list[count], 2)
            if value_adjust_func is not None:
                self.y_list[count] = value_adjust_func(count, curr_time, self.y_list[count])
            count = count + 1

        return self.x_list, self.y_list


if __name__ == "__main__":
    sim = TsdaSimulator(100, 3600)
    X, Y = sim.generate()
    print(X)
    print(Y)

