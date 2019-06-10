import os
import re
import reporting.common.log4me as log
import reporting.common.config4me as config
import reporting.app.log_analyzer.log_analyzer as log_analyzer

root_dir = config.get_config_default('File_Storage', 'fs.dws', '/var/dws/')
sub_dir = 'apache'


def load_file(file, analyzer):
    file_path = os.path.join(root_dir, sub_dir, file)
    try:
        fobj = open(file_path, 'r')
    except IOError as e:
        log.info('Fail to open file: '+file_path, e)
    else:
        for eachLine in fobj:
            analyzer.process_line(eachLine)
        fobj.close()


class APILogAnalyzer(log_analyzer.LogAnalyzer):
    def process_line(self, line):
        try:
            key = re.search(re.compile("(?<=\")[^\"]*(?=\")"), line).group(0)
            key = key.split(" ")[1]
        except Exception:
            pass
        else:
            log_analyzer.LogAnalyzer.__record__(self, key)
