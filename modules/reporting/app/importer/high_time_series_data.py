import bson
import datetime
from pymongo import MongoClient
import reporting.util.tool as tool
import reporting.common.config4me as config
import reporting.common.log4me as log

client = MongoClient(config.get_config_default('Database', 'mongodb.client', 'mongodb://dws0:27017/'))
database = client[config.get_config_default('Database', 'mongodb.database', 'pooshlingang')]
collection = database["hrda_pressure"]
converge_rate = bson.int64.Int64(1000000)


def update_hrtsdata(site_id, datatime, hrinterval, data):
    _id = site_id + '-pressure-' + str(str(datatime)[0:7] + '000000')
    str_data = ''
    for i in data:
        str_data = str_data + tool.base62_encode(i)

    condition = {'_id': _id}
    hrtsda = collection.find_one(condition)
    if hrtsda:
        hrtsda['lastmod'] = datetime.datetime.now()
        hrtsda['values'][str(datatime)] = str_data
        collection.update(condition, hrtsda)
        log.info('hrtsdata_import ' + _id + ' ' + str(datatime) + 'success')
    else:
        hrtsda = dict()
        values = dict()
        hrtsda['_id'] = _id
        hrtsda['timestamp'] = datetime.datetime.fromtimestamp(int(str(datatime)[0:7] + '000'))
        hrtsda['lastmod'] = datetime.datetime.now()
        hrtsda['created'] = datetime.datetime.now()
        hrtsda['converge_rate'] = converge_rate
        hrtsda['hrinterval'] = hrinterval
        values[str(datatime)] = str_data
        hrtsda['values'] = values
        collection.insert(hrtsda)
        log.info('hrtsdata_import ' + _id + ' ' + str(datatime) + 'success')


client.close()
