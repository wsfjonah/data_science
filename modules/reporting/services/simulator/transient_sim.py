import reporting.services.simulator.tsda_sim as tsda_sim
import datetime
import numpy as np


class TransientSimulator(tsda_sim.TsdaSimulator):
    data_list = [16.8, 16.7, 16.8, 16.7, 16.5, 16.7, 17.0, 16.7, 16.6, 17.0, 16.7, 16.8, 13.0, 15.8, 14.3, 17.2, 15.9,
                 15.9, 16.7, 16.4, 21.8, 17.5, 15.9, 17.5, 17.0, 16.8, 17.2, 16.6, 16.6, 17.0, 16.6, 16.9, 16.9, 17.0,
                 17.0, 17.0]

    def __init__(self, end_time):
        tsda_sim.TsdaSimulator.__init__(self, len(self.data_list), interval_sec=5, end_time=end_time)
        # transient interval is 5s

    def get_data(self, length):
        if len(self.data_list) != length:
            raise Exception("Different data length ", len(self.data_list), "and key length", length)
        return self.data_list[::-1]  # reverse the list

    def generate(self, value_func=get_data):
        return tsda_sim.TsdaSimulator.generate(self, value_func)
