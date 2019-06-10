import reporting.app.log_analyzer.apache_log_analyzer as apache_log_analyzer
import reporting.app.log_analyzer.log_analyzer as log_analyzer


analyzer = apache_log_analyzer.APILogAnalyzer()
apache_log_analyzer.load_file("access_20190610.log", analyzer)

print(analyzer.output)
