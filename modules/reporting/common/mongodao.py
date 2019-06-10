import pymongo
import reporting.common.config4me as config
import reporting.common.log4me as log

MONGO_CLIENT = None
DB_PROJECT_PREFIX = "poo"


def get_mongo_client():
    global MONGO_CLIENT
    if MONGO_CLIENT is None:
        log.info("MONGO_CLIENT not defined, initialized MongoDB Client.")
        mongo_server = config.get_config('Database', 'mongodb.client')
        MONGO_CLIENT = pymongo.MongoClient(mongo_server)
    return MONGO_CLIENT


def get_mongo_db(dbname):
    # log.info("initialized Mongo DB for ("+dbname+").")
    dblist = get_mongo_client().list_database_names()
    if dbname in dblist:
        return get_mongo_client()[dbname]
    else:
        raise Exception("Invalid dbname: "+dbname)


def get_mongo_basedb():
    return get_mongo_db("base")


def get_mongo_projdb():
    curr_proj = config.get_config('System', 'system.project.current')
    return get_mongo_db(DB_PROJECT_PREFIX+curr_proj)


def get_proj_collection(collection):
    return get_mongo_projdb()[collection]


def get_base_collection(collection):
    return get_mongo_basedb()[collection]


if __name__ == '__main__':
    get_mongo_db("test")
    get_mongo_basedb()
    get_mongo_projdb()
    get_proj_collection("tsda")
    get_base_collection("user")
