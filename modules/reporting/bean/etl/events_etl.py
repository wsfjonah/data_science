from matplotlib.dates import DateFormatter

import reporting.services.statistic.event_statistic as event_stat
import reporting.services.chart.scatter_chart as scatter_chart
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



