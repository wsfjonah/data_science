import reporting.bean.etl.excel_analyzer as excel_analyzer

analyzer = excel_analyzer.ExcelAnalyzer()

analyzer.extract('wafer_test_1.xlsx')
analyzer.draw()

analyzer.extract('wafer_test_2.xlsx')
analyzer.draw()
