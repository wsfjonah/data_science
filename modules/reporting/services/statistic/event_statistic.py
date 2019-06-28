import os
import time
import datetime
import json
import traceback
import reporting.common.config4me as config
import reporting.util.tool as tool

EVENT_STATISTIC_TYPE_WEEK = 'w'
EVENT_STATISTIC_TYPE_HOUR = 'h'
EVENT_STATISTIC_TYPE_MNTH = 'm'

CACHE_ROOT = config.get_config('File_Storage', 'fs.cache')


def cache_event_statistic(event, statistic_name, statistic_type):
    # TODO: based on the event data, update the event statistics and store in local
    try:
        file_path = get_cache_file(event['timestamp'], statistic_name, statistic_type)
        file = open(file_path, 'a')
        file.write(str(event)+"\n")
        file.close()
    except Exception as e:
        exstr = traceback.format_exc()
        print(exstr)
        pass
    return


def get_cache_properties(statistic_name, statistic_type, **details):
    global CACHE_ROOT
    statistic_type_name = ''
    statistic_index = ''
    statistic_keys = []
    if statistic_type == EVENT_STATISTIC_TYPE_WEEK:
        statistic_type_name = 'week'
        statistic_keys = [0, 1, 2, 3, 4, 5, 6]
        try:
            timestamp = details['timestamp']
            statistic_index = time.strftime("%w", time.localtime(timestamp.timestamp()))
        except Exception:
            pass
    elif statistic_type == EVENT_STATISTIC_TYPE_HOUR:
        statistic_type_name = 'hour'
        statistic_keys = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14',
                          '15', '16', '17', '18', '19', '20', '21', '22', '23']
        try:
            timestamp = details['timestamp']
            statistic_index = time.strftime("%H", time.localtime(timestamp.timestamp()))
        except Exception:
            pass
    elif statistic_type == EVENT_STATISTIC_TYPE_MNTH:
        statistic_type_name = 'month'
        statistic_keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        try:
            timestamp = details['timestamp']
            statistic_index = time.strftime("%m", time.localtime(timestamp.timestamp()))
        except Exception:
            pass
    else:
        raise Exception("Invalid statistic_type " + statistic_type)

    cache_dir = os.path.join(CACHE_ROOT, statistic_name, statistic_type_name)
    os.makedirs(cache_dir, 0o775, True)

    return cache_dir, statistic_index, statistic_keys


def get_cache_file(timestamp, statistic_name, statistic_type):
    cache_dir, statistic_index, statistic_keys = get_cache_properties(statistic_name, statistic_type, **{'timestamp': timestamp})
    file_path = os.path.join(cache_dir, statistic_index+".dat")
    return file_path


def load_statistic(statistic_name, statistic_type):
    cache_dir, statistic_index, statistic_keys = get_cache_properties(statistic_name, statistic_type)
    statistics = []
    statistics2 = []
    for key in statistic_keys:
        file_path = os.path.join(cache_dir, str(key)+".dat")
        size = os.path.getsize(file_path)
        statistics.append(size)
        f = open(file_path, 'r')
        try:
            statistics2.append(len(f.readlines()))
        except Exception:
            pass
        finally:
            f.close()
    return statistic_keys, statistics, statistics2


def calculate_statistic(statistic_name, statistic_type, keyword=''):
    cache_dir, statistic_index, statistic_keys = get_cache_properties(statistic_name, statistic_type)
    x = []
    y = []
    for key in statistic_keys:
        file_path = os.path.join(cache_dir, str(key)+".dat")
        f = open(file_path, 'r')
        try:
            while True:
                text_line = f.readline()
                if text_line:
                    if keyword not in text_line:
                        continue
                    try:
                        json_obj = json.loads(tool.json_prop(text_line))
                        # value = json_obj['confidence']
                        value = round(json_obj['max']-json_obj['min'], 2)
                        if 4 < value < 30:
                            timestamp = datetime.datetime.fromtimestamp(json_obj['ts']/1000).replace(year=2017, month=1, day=1)
                            x.append(timestamp)
                            y.append(value)
                    except Exception:
                        pass
                else:
                    break
        finally:
            f.close()
    return statistic_keys, x, y


if __name__ == '__main__':
    print(load_statistic("event_count", EVENT_STATISTIC_TYPE_WEEK))
