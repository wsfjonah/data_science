import reporting.services.chart.tsda_chart as tsda_chart
import reporting.services.simulator.transient_sim as transient_sim
import datetime


class TransientChart(tsda_chart.TsdaChart):
    def __init__(self, title, label_x, label_y):
        tsda_chart.TsdaChart.__init__(self, title, label_x, label_y)

    def add_event_area(self, color='purple'):
        ax = self.fig.add_axes([0.36, 0.11, 0.3, 0.81])  # x, y, width, height
        ax.set_axis_off()
        ax.text(0.1, 0.8, 'Anomaly\n(78.4, 19.2m, 60s)', size=16,
                ha='left', va='center', alpha=0.6, color=color, transform=ax.transAxes)
        ax.bar([1], [1], width=0.5, facecolor='blue', alpha=0.3)

    def plot(self):
        tsda_chart.TsdaChart.plot(self)
        self.add_event_area()
        return self


if __name__ == "__main__":
    time_list, value_list = transient_sim.TransientSimulator(datetime.datetime.now()).generate()
    chart = TransientChart("Transient", "Time", "Value")
    chart.set_data(x=time_list, y=value_list).plot().show()

