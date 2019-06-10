import time
import reporting.common.mongodao as mongodao

TSDA_ENTITY_NAME = "tsdata"


def read_any(datapoint_oid):
    coll = mongodao.get_proj_collection(TSDA_ENTITY_NAME)
    result = {}
    cur = coll.find({"_id": {"$lte": datapoint_oid+str(int((time.time()+100)*1000))}}).sort("_id", -1).limit(3)
    for doc in cur:
        result = {**result, **doc['values']}
    return result


def read_last(datapoint_oid):
    coll = mongodao.get_proj_collection(TSDA_ENTITY_NAME)
    result = {}
    cur = coll.find({"_id": {"$lte": datapoint_oid+str(int((time.time()+100)*1000))}}).sort("_id", -1).limit(1)
    for doc in cur:
        result = {**result, **doc['values']}
    keys = sorted(result.keys(), reverse=True)
    # print(keys)
    return keys[0], result[keys[0]]


if __name__ == '__main__':
    print(str(int((time.time()+100)*1000)))
    # res = read_any('5a6eb4e70b272a1f64fa26b6-pressure')
    # print(res)

    t, value = read_last('5a6eb4e70b272a1f64fa26b7-pressure')
    print(int(t))
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(t)/1000)), "%.2f" % float(value))
