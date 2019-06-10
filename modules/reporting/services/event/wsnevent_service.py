import reporting.common.mongodao as mongodao
import reporting.services.statistic.event_statistic as event_stat

WSNEVENT_ENTITY_NAME = "wsnevent"
WSNEVENT_CONVERGE = 10000000


def get_event(event_id):
    # TODO(): fetch the event from database
    coll = mongodao.get_proj_collection(WSNEVENT_ENTITY_NAME)
    event = None
    return event


def search_cache_event(from_time, to_time, **search_filter):
    # TODO(): search the events from database and write to disk one by one
    count = 0
    # if (to_time-from_time) > WSNEVENT_CONVERGE*2:
    #     raise Exception("event search time range (%.2fhr) is too big" % ((to_time-from_time)/3600000))

    coll = mongodao.get_proj_collection(WSNEVENT_ENTITY_NAME)
    from_time = from_time//WSNEVENT_CONVERGE*WSNEVENT_CONVERGE
    to_time = to_time//WSNEVENT_CONVERGE*WSNEVENT_CONVERGE

    cur = coll.find({"_id": {"$lte": str(to_time), "$gte": str(from_time)}})
    for doc in cur:
        try:
            event_list = doc["events"]
            for event_id in event_list:
                try:
                    validate_event(event_list[event_id], **search_filter)
                    count = count+1
                    event_stat.cache_event_statistic(event_list[event_id], "event_count",
                                                     event_stat.EVENT_STATISTIC_TYPE_HOUR)
                except Exception as e:
                    # print(e)
                    pass
        except Exception:
            pass

    return count


def validate_event(event, **search_filter):
    if search_filter['confidence'] is not None:
        if event["confidence"] < search_filter['confidence']:
            raise Exception("confidence too small")
    return event


def cache_event(event_id):
    # TODO(): get the event from database, and cache all relevant data from db to local
    event = get_event(event_id)

    return


def analyze_event(event_id):
    # TODO():
    return


def extract_event(event_list):
    # TODO(): from a list of events, extract the real events

    return


if __name__ == '__main__':
    count = search_cache_event(1556255039000-WSNEVENT_CONVERGE*2000, 1556255039000, confidence=20)

    print(count)
