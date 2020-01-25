import json
import time
from lists.db import get_db_collection
from lists.db import insert_list


def create(event, context):
    body = json.loads(event['body'])
    if 'name' not in body or 'user' not in body: 
        response = {
            "statusCode": 400,
            "body": json.dumps({'error': 'requires name and user', 'event': event})
        }
        return response

    listObject = {
        "createdAt": int(time.time()),
        "lastModified": int(time.time()),
        "name": body['name'],
        "user": body['user'],
        "entries": []
    }
    print("Object to add to the DB is " + str(listObject))
    collection = get_db_collection()
    result = insert_list(collection, listObject)
    resultId = result.inserted_id
    print("result id is " + str(resultId))
    body = {
        "id": str(resultId)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Access-Control-Allow-Origin" : "*" # Required for CORS support to work
        },
    }

    return response

