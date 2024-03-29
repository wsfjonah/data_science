import pandas as pd
import os

import reporting.services.chart.bar3d_chart as bar3d_chart
import reporting.bean.etl.base_etl as base_etl
import reporting.util.tool as tool


class ExcelETL(base_etl.BaseETL):
    report_dir = '/var/dws/wafer/'
    curr_key = None

    title = 'Wafer Testing Report'
    label_x = 'Tester (6 as STDX06A, 50 as STDX50A)'
    label_y = 'P/C (1 as SB776-1-01, 11 as SB776-1-11)'
    label_z = 'Fail%'

    field_x = 'Tester'
    field_y = 'P/C'
    field_z = 'Bin26'

    def __init__(self):
        base_etl.BaseETL.__init__(self)

    def extract(self, key):
        self.data.clear()
        self.curr_key = key
        file = os.path.join(self.report_dir, key)
        sheet = pd.read_excel(io=file, header=8)
        for i in sheet.index.values:
            row_data = sheet.loc[i]
            self._parse_row(row_data)

    def _parse_row(self, row):
        x = tool.extract_num_from_str(row[self.field_x])
        y = int(row[self.field_y].split('-')[2])
        z = int(row[self.field_z])
        self.store_value((x, y), z)

    def to_chart_data(self):
        x = []
        y = []
        z = []
        for k in self.data.keys():
            x.append(k[0])
            y.append(k[1])
            z.append(self.data[k])
        return x, y, z

    def draw(self):
        chart = bar3d_chart.Bar3DChart(self.title, self.label_x, self.label_y, self.label_z)
        x, y, z = self.to_chart_data()
        chart.set_data(x=x, y=y, z=z)
        chart.plot().show()
