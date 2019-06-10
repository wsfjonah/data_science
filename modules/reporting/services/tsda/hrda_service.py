import time
import reporting.common.mongodao as mongodao

HRDA_ENTITY_NAME = "hrda_pressure"


def read_last(datapoint_oid):
    coll = mongodao.get_proj_collection(HRDA_ENTITY_NAME)
    result = {}
    hrinterval = None
    cur = coll.find({"_id": {"$lte": datapoint_oid+str(int((time.time()+100)*1000))}}).sort("_id", -1).limit(1)
    for doc in cur:
        result = {**result, **doc['values']}
        hrinterval = doc['hrinterval']
    keys = sorted(result.keys(), reverse=True)
    # print(keys)
    return keys[0], result[keys[0]], hrinterval
