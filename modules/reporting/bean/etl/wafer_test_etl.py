import numpy as np
import pandas as pd
import os

import reporting.bean.etl.excel_etl as excel_etl
import reporting.services.chart.heatmap_chart as heatmap_chart
import reporting.services.echarts.heatmap_echarts as heatmap_echarts
import reporting.services.echarts.bar3d_echarts as bar3d_echarts


class WaferTestETL(excel_etl.ExcelETL):
    label_x = 'Tester (e.g. STDX06A)'
    label_y = 'P/C (e.g. SB776-1-11)'
    label_z = 'Fail'

    def _parse_row(self, row):
        x = row[self.field_x]
        y = row[self.field_y]
        z = int(row[self.field_z])
        self.store_value((x, y), z)

    def to_chart_data(self):
        x = []
        y = []
        for k in self.data.keys():
            if k[0] not in x:
                x.append(k[0])
            if k[1] not in y:
                y.append(k[1])

        xy_map = np.zeros((len(y), len(x))).tolist()
        for x0 in x:
            for y0 in y:
                if (x0, y0) in self.data:
                    xy_map[y.index(y0)][x.index(x0)] = self.data[(x0, y0)]
        return x, y, xy_map

    def draw(self):
        chart = heatmap_chart.HeatMapChart(self.title, self.label_x, self.label_y, self.label_z)
        x, y, xy_map = self.to_chart_data()
        chart.set_data(x=x, y=y, map=xy_map)
        chart.plot().show()

    def get_echarts(self):
        chart = heatmap_echarts.HeatMapChart(self.title, self.label_x, self.label_y, self.label_z)
        x, y, xy_map = self.to_chart_data()
        chart.set_data(x=x, y=y, map=xy_map)
        return chart.plot().show()

    def save_echarts(self):
        file_path = os.path.join(self.report_dir, self.curr_key+'.html')
        self.get_echarts().render(file_path)

    def save_3decharts(self):
        chart = bar3d_echarts.Bar3DChart(self.title, self.label_x, self.label_y, self.label_z)
        x, y, xy_map = self.to_chart_data()
        chart.set_data(x=x, y=y, map=xy_map)

        file_path = os.path.join(self.report_dir, self.curr_key+'3d.html')
        chart.plot().show().render(file_path)
