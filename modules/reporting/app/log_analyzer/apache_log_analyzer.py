import os
import reporting.common.log4me as log
import reporting.common.config4me as config

root_dir = config.get_config_default('File_Storage', 'fs.dws', '/var/dws/')
sub_dir = 'apache'


def load_file(file):
    file_path = os.path.join(root_dir, sub_dir, file)
    try:
        fobj = open(file_path, 'r')
    except IOError as e:
        print('Fail to open file: '+file_path, e)
    else:
        for eachLine in fobj:
            print(eachLine)
        fobj.close()
