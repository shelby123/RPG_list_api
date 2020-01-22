import json
import os
from pymongo import MongoClient
import time

# TODO: refactor DB connection into separate file. 
def create(event, context):
    if 'name' not in event or 'user' not in event: 
        response = {
            "statusCode": 400,
            "body": json.dumps({'error': 'requires name and user'})
        }
        return response

    username = os.environ['DB_CREDENTIAL_USERNAME']
    password = os.environ['DB_CREDENTIAL_PASSWORD']
    url = "mongodb+srv://" + username + ":" + password + "@cluster0-gpeio.mongodb.net/test?retryWrites=true&w=majority";
    client = MongoClient(url);
    db = client.RPG;

    listObject = {
        "createdAt": time.time,
        "lastModified": time.time,
        "name": event['name'],
        "user": event['user'],
        "entries": []
    }
    print("Object to add to the DB is " + listObject);
    collection = client.list_entries
    result = collection.insert_one(listObject)
    resultId = result.inserted_id
    print("result id is " + resultId.str);
    body = {
        "id": resultId
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
