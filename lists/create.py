import json
import os
from pymongo import MongoClient
import time

# TODO: refactor DB connection into separate file. 
def create(event, context):
    let body = JSON.parse(event.body)
    if 'name' not in body or 'user' not in body: 
        response = {
            "statusCode": 400,
            "body": json.dumps({'error': 'requires name and user', 'event': event})
        }
        return response

    username = os.environ['DB_CREDENTIAL_USERNAME']
    password = os.environ['DB_CREDENTIAL_PASSWORD']
    url = "mongodb+srv://" + username + ":" + password + "@cluster0-gpeio.mongodb.net/test?retryWrites=true&w=majority";
    client = MongoClient(url);
    db = client.RPG;

    listObject = {
        "createdAt": int(time.time()),
        "lastModified": int(time.time()),
        "name": body['name'],
        "user": body['user'],
        "entries": []
    }
    print("Object to add to the DB is " + str(listObject))
    collection = db.list_entries
    result = collection.insert_one(listObject)
    resultId = result.inserted_id
    print("result id is " + str(resultId))
    body = {
        "id": str(resultId)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
