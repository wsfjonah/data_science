import os
import json
# import struct
import shutil
import time
# from _ctypes import pointer, POINTER
# from ctypes import c_int, cast, c_float
import traceback

import bson
import reporting.importer.high_time_series_data as hrtsda
import reporting.importer.time_series_data as tsda
from pymongo import MongoClient
import reporting.common.config4me as config
import reporting.common.log4me as log

client = MongoClient(config.get_config_default('Database', 'mongodb.client', 'mongodb://dws0:27017/'))
database = client[config.get_config_default('Database', 'mongodb.database', 'pooshlingang')]
collection = database["site"]

path = config.get_config_default('File_Storage', 'fs.import', '/var/data/rtu1.1/')
datafomat = "%Y%m%d%H%M%S"
converge_rate = bson.int64.Int64(1000000)


# bar=(Kx+B)*0.005-2.4
def data_calibrate(data, k, b):
    log.info("k and b velaue" + str(k) + ' ' + str(b))
    new_data = list()
    for i in data:
        if i == 0:
            new_data.append(0)
        else:
            # 电压值
            v = int(i) * k + b
            # 电压转水柱
            d = (v * 5 - 2.5) * 10.0025607225
            if 0 <= d <= 200:
                new_data.append(d)
    return new_data


def move_file(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        log.info("%s not exist!" % (srcfile))
    else:
        fpath = os.path.dirname(srcfile) + '/' + dstfile + ''
        filenewpath = fpath + '/' + os.path.basename(srcfile)
        if os.path.exists(filenewpath):
            os.remove(filenewpath)
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.move(srcfile, fpath)  # 移动文件
        log.info("move %s -> %s" % (srcfile, dstfile))


def importer():
    dirlist = os.listdir(path)
    time.sleep(1)
    log.info("importer start")
    for dir_entry in dirlist:
        dir_entry_path = os.path.join(path, dir_entry)
        print('import file', dir_entry_path)
        if os.path.isfile(dir_entry_path) and dir_entry_path.endswith('.json'):
            try:
                with open(dir_entry_path, 'r') as my_file:
                    mode = os.stat(dir_entry_path).st_mode;
                    print(mode)
                    if not os.access(dir_entry_path, os.F_OK) \
                            or not os.access(dir_entry_path, os.W_OK) \
                            or not os.access(dir_entry_path, os.R_OK):
                        continue
                    load_dict = json.load(my_file)
                    datatime = int(time.mktime(time.strptime(load_dict['read_time'], datafomat)) * 1000)
                    siteid = load_dict['site_id']
                    condition = {'device_ref': siteid[-8:]}
                    site = collection.find_one(condition)
                    if site:
                        site_id = site['_id']
                        log.info('site_id' + str(site_id))
                        hrinterval = 1000 / (int(load_dict['frequency'][-2:], 16))
                        log.info('hrinterval' + str(hrinterval))
                        data = data_calibrate(load_dict['data'], load_dict['k'], load_dict['b'])
                        hrtsda.update_hrtsdata(site_id, datatime, hrinterval, data)
                        tsda.update_tsdata(site_id, datatime, data)
                    else:
                        log.info(siteid + 'site can not be found')
                        raise Exception(siteid + 'site can not be found')
                move_file(dir_entry_path, 'archive')
            except Exception as e:
                move_file(dir_entry_path, 'error')
                log.info("importer error: " + str(e))
                traceback.print_exc()


if __name__ == '__main__':
    while True:
        try:
            importer()
            time.sleep(1)
        except Exception as e:
            log.info("importer main error: " + str(e))
            traceback.print_exc()
