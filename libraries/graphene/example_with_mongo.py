from graphene import ObjectType, String, Schema

from pymongo import MongoClient

import json

mongo_client = MongoClient(host='localhost')


class Query(ObjectType):
    fullname = String(username=String(default_value="John"))

    def resolve_fullname(root, info, username):
        # NOTE: you should have data in the
        # db & collection below
        res = mongo_client.testdb.testcollection.find_one(
            {'username': username})
        return res


schema = Schema(query=Query)

if __name__ == "__main__":
    username = "mr123"
    _query_string = '{ fullname(username: "{username}") }'.format({
        'username': username})
    print(_query_string)
    res = schema.execute(_query_string)
    print(res.data['fullname'])
