import bson
import datetime
from pymongo import MongoClient
import reporting.util.statistic as statistic
import reporting.common.config4me as config
import reporting.common.log4me as log

client = MongoClient(config.get_config_default('Database', 'mongodb.client', 'mongodb://dws0:27017/'))
database = client[config.get_config_default('Database', 'mongodb.database', 'pooshlingang')]
collection = database["tsdata"]
converge_rate = bson.int64.Int64(10000000)


def update_tsdata(site_id, datatime, data):
    _id = site_id + '-pressure-' + str(str(datatime)[0:6] + '0000000')
    condition = {'_id': _id}
    tsda = collection.find_one(condition)
    if tsda:
        tsda['lastmod'] = datetime.datetime.now()
        tsda['values'][str(datatime)] = str(statistic.get_mean(data))
        collection.update(condition, tsda)
        log.info('tsdata_import ' + _id + ' ' + str(datatime) + 'success')
    else:
        tsda = dict()
        values = dict()
        tsda['_id'] = _id
        tsda['timestamp'] = datetime.datetime.fromtimestamp(int(str(datatime)[0:6] + '0000'))
        tsda['lastmod'] = datetime.datetime.now()
        tsda['created'] = datetime.datetime.now()
        tsda['converge_rate'] = converge_rate
        values[str(datatime)] = str(statistic.get_mean(data))
        tsda['values'] = values
        collection.insert(tsda)
        log.info('tsdata_import ' + _id + ' ' + str(datatime) + 'success')


client.close()
