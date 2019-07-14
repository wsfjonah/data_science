import reporting.bean.etl.access_log_etl as access_log_etl

etl = access_log_etl.AccessLogETL('Access Log Report', 'Date Time', 'Count', ('/api/', '/api/tsevent/', '/api/tsda/'))
etl.extract('access_20190610.log')
# etl.draw()

etl.save_echarts()
