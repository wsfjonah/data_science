import reporting.bean.etl.wafer_test_etl as wafer_test_etl

etl = wafer_test_etl.WaferTestETL()

etl.extract('wafer_test_1.xlsx')
etl.draw()
