from matplotlib.dates import DateFormatter
import os
import reporting.services.statistic.event_statistic as event_stat
import reporting.services.chart.scatter_chart as scatter_chart
import reporting.services.echarts.scatter_echarts as scatter_echarts
import reporting.bean.etl.base_etl as base_etl


class EventsETL(base_etl.BaseETL):
    key = ''

    def __init__(self, title, label_x, label_y):
        base_etl.BaseETL.__init__(self)
        self.title = title
        self.label_x = label_x
        self.label_y = label_y

    def extract(self, key):
        self.key = key
        pass

    def draw(self):
        statistic_key, x, y = event_stat.calculate_statistic('event_count', event_stat.EVENT_STATISTIC_TYPE_HOUR, self.key)
        if len(x):
            chart = scatter_chart.ScatterChart(self.title+" "+self.key, self.label_x, self.label_y, xaxis_formatter=DateFormatter('%H:%M'))
            chart.set_data(x=x, y=y)
            chart.plot().show()
        else:
            raise Exception('no event found for '+self.key+'.')

    def get_echarts(self):
        chart = scatter_echarts.ScatterChart(self.title, self.label_x, self.label_y, xaxis_formatter='time')
        statistic_key, x, y = event_stat.calculate_statistic('event_count', event_stat.EVENT_STATISTIC_TYPE_HOUR, self.key)
        chart.set_data(x=x, y=y, max_y=25, min_x=x[0].replace(hour=0, minute=0, second=0, microsecond=0),
                       max_x=x[0].replace(hour=23, minute=59, second=59, microsecond=999))
        return chart.plot().show()

    def save_echarts(self):
        file_path = os.path.join(self.key+'.html')
        self.get_echarts().render(file_path)


