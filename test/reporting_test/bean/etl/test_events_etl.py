import reporting.bean.etl.events_etl as events_etl

events_etl = events_etl.EventsETL('WSN Events', 'Hour', 'Magnitude')
try:
    events_etl.extract('5a6eb4e70b272a1f64fa26bb')
    # events_etl.draw()
    events_etl.save_echarts()
except Exception as e:
    print(e)

try:
    events_etl.extract('5a6eb4e70b272a1f64fa26b3')
    # events_etl.draw()
    events_etl.save_echarts()
except Exception as e:
    print(e)

try:
    events_etl.extract('5a6eb4e70b272a1f64fa26ba')
    # events_etl.draw()
    events_etl.save_echarts()
except Exception as e:
    print(e)

try:
    events_etl.extract('5a6eb4e70b272a1f64fa26b2')
    # events_etl.draw()
    events_etl.save_echarts()
except Exception as e:
    print(e)

try:
    events_etl.extract('')
    # events_etl.draw()
    events_etl.save_echarts()
except Exception as e:
    print(e)

