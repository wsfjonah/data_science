import reporting.bean.etl.json_etl as json_etl

etl = json_etl.JsonETL("Transient Analysis", "Time", "Pressure (meter)")

etl.extract('1527034420000-wsntransient-5a6eb4e70b272a1f64fa26b2-pressure.json')
etl.draw()

etl.extract('1523146390000-wsntransient-5a6eb4e70b272a1f64fa26b2-pressure.json')
etl.draw()
