import os
import re
import time
import numpy as np

import reporting.common.config4me as config
import reporting.common.log4me as log
import reporting.services.chart.correlation_chart as correlation_chart
import reporting.services.echarts.bar_echarts as bar_echarts
import reporting.bean.etl.base_etl as base_etl

root_dir = config.get_config_default('File_Storage', 'fs.dws', '/var/dws/')
sub_dir = 'apache'
LOG_TIME_PATTERN = '(?<=\[)[^\]]*(?=\])'
XAXIS_NUM = 24


def extract_hr(text):
    global LOG_TIME_PATTERN
    time_zone_str = re.search(re.compile(LOG_TIME_PATTERN), text).group(0)
    time_str = time_zone_str.split(" ")[0]
    return time.strptime(time_str, '%d/%b/%Y:%H:%M:%S').tm_hour


class AccessLogETL(base_etl.BaseETL):
    url_patterns = ('/api/', '/api/tsevent/', '/api/site/')

    title = 'Access Log Report'
    label_x = 'Date Time'
    label_y = 'Count'

    def __init__(self, title, label_x, label_y, url_patterns='api'):
        base_etl.BaseETL.__init__(self)
        self.title = title
        self.label_x = label_x
        self.label_y = label_y
        self.url_patterns = url_patterns

    def extract(self, key):
        self.data.clear()
        file_path = os.path.join(root_dir, sub_dir, key)
        try:
            fobj = open(file_path, 'r')
        except IOError as e:
            log.info('Fail to open file: ' + file_path+str(e))
        else:
            for line in fobj:
                self._parse_row(line)
            fobj.close()

    def _parse_row(self, row):
        for url in self.url_patterns:
            try:
                if url in row:
                    key = extract_hr(row)
                    self.store_value((url, key), 1)
            except Exception:
                pass

    def get_xaxis(self):
        global XAXIS_NUM
        return np.arange(XAXIS_NUM).tolist()

    def init_yaxis(self):
        global XAXIS_NUM
        return np.zeros(XAXIS_NUM).tolist()

    def to_chart_data(self):
        result = {}
        for url in self.url_patterns:
            x = self.get_xaxis()
            y = self.init_yaxis()
            for k in self.data.keys():
                if url in k:
                    # x.append(k[1])
                    # y.append(self.data[k])
                    y[k[1]] = self.data[k]
            result[url] = (x, y)
        return result

    def draw(self):
        chart = correlation_chart.CorrelationChart(self.title, self.label_x, self.label_y)
        result = self.to_chart_data()

        for k in result.keys():
            v = result[k]
            chart.set_data(x=v[0], y=v[1], label=k)
        chart.plot().show()

    def get_echarts(self):
        chart = bar_echarts.BarChart(self.title, self.label_x, self.label_y)
        result = self.to_chart_data()
        for k in result.keys():
            v = result[k]
            chart.set_data(x=v[0], y=v[1], label=k)
        return chart.plot().show()




