import os
from pymongo import MongoClient
from bson.objectid import ObjectId


def get_db_collection():
    username = os.environ['DB_CREDENTIAL_USERNAME']
    password = os.environ['DB_CREDENTIAL_PASSWORD']
    url = "mongodb+srv://" + username + ":" + password + "@cluster0-gpeio.mongodb.net/test?retryWrites=true&w=majority"
    client = MongoClient(url)
    db = client.RPG
    return db.list_entries


def query_list(collection, list_id):
    return collection.find_one({'_id': ObjectId(list_id)})


def insert_list(collection, list_object):
    return collection.insert_one(list_object)
