import os
import json
import datetime

import reporting.common.config4me as config
import reporting.bean.etl.base_etl as base_etl
import reporting.services.chart.transient_chart as transient_chart


root_dir = config.get_config_default('File_Storage', 'fs.dws', '/var/dws/')
sub_dir = 'smartwater/transient/'


class JsonETL(base_etl.BaseETL):
    title = 'Data Report'
    label_x = 'Date Time'
    label_y = 'Value'

    def __init__(self, title, label_x, label_y):
        base_etl.BaseETL.__init__(self)
        self.title = title
        self.label_x = label_x
        self.label_y = label_y

    def extract(self, key):
        self.data.clear()
        file_path = os.path.join(root_dir, sub_dir, key)
        try:
            with open(file_path, 'r') as load_f:
                json_obj = json.load(load_f)
                for k, v in json_obj['tsda']['data'].items():
                    self._parse_row((k, v))
        except Exception as e:
            print(e)
            pass

    def _parse_row(self, row):
        key = datetime.datetime.fromtimestamp(int(row[0])/1000)
        value = row[1]
        self.store_value(key, value)

    def store_value(self, key, value):
        self.data[key] = value

    def to_chart_data(self):
        x = []
        y = []
        for k in self.data.keys():
            x.append(k)
            y.append(self.data[k])
        return x, y,

    def draw(self):
        chart = transient_chart.TransientChart(self.title, self.label_x, self.label_y)
        x, y = self.to_chart_data()
        chart.set_data(x=x, y=y)
        chart.plot().show()
