import reporting.services.chart.tsda_chart as tsda_chart


class TransientChart(tsda_chart.TsdaChart):
    def __init__(self, title, xaxis_name, yaxis_name):
        tsda_chart.TsdaChart.__init__(self, title, xaxis_name, yaxis_name)

    def add_event_info(self, color='purple'):
        axes = self.fig.add_axes([0.3, 0.8, 0.001, 0.001])  # x, y, width, height
        axes.set_axis_off()
        axes.text(0.1, 0.8, 'Anomaly\n(78.4, 19.2m, 60s)', size=16,
                ha='left', va='center', alpha=0.6, color=color, transform=axes.transAxes)
        # axes.bar([1], [1], width=0.5, facecolor='blue', alpha=0.3)

    def plot(self):
        tsda_chart.TsdaChart.plot(self)
        self.add_event_info()
        length = int(len(self.data[0][0])/3)
        self.axes.axvspan(self.data[0][0][length], self.data[0][0][-length], facecolor='#2ca02c', alpha=0.2)
        return self
