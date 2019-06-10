import reporting.common.mongodao as mongodao

SITE_ENTITY_NAME = "site"


def get_all_sites():
    coll = mongodao.get_proj_collection(SITE_ENTITY_NAME)
    res = []
    for doc in coll.find():
        res.append(doc)
    return res


def get(oid):
    coll = mongodao.get_proj_collection(SITE_ENTITY_NAME)
    res = coll.find_one({"_id": oid})
    return res


if __name__ == '__main__':
    res = get_all_sites()
    print(res)

    res = get('5a6eb4e70b272a1f64fa26b3')
    print(res)
