import json
import os
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId


# TODO: refactor DB connection into separate file. 
def get(event, context):
    collection = get_db_collection()
    doc = query_list(collection, event['list_id'])

    body = {
        "message": "get list lambda invoked",
        "input": event, 
        "list": json.dumps(doc, sort_keys=True, indent=4, default=json_util.default)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response


def get_db_collection():
    username = os.environ['DB_CREDENTIAL_USERNAME']
    password = os.environ['DB_CREDENTIAL_PASSWORD']
    url = "mongodb+srv://" + username + ":" + password + "@cluster0-gpeio.mongodb.net/test?retryWrites=true&w=majority"
    client = MongoClient(url)
    db = client.RPG
    return db.list_entries


def query_list(collection, list_id):
    return collection.find_one({'_id': ObjectId(list_id)})

