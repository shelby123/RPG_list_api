import json
import time
from lists.db import get_db_collection
from lists.db import update_list
from lists.db import query_list


def update(event, context):
    body = json.loads(event['body'])
    list_id = body['listId']
    elements = body['entries']
    if list_id is None:
        response = {
            "statusCode": 400,
            "body": json.dumps({'error': 'requires list_id', 'event': event})
        }
        return response

    collection = get_db_collection()
    existing_list = query_list(collection, list_id)

    if existing_list is None:
        response = {
            "statusCode": 400,
            "body": json.dumps({'error': 'list to update does not exist', 'event': event})
        }
        return response

    updated_list = format_update(existing_list, elements)
    result = update_list(collection, list_id, updated_list)

    body = {
        "successful": bool(result)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Access-Control-Allow-Origin" : "*" # Required for CORS support to work
        },
    }

    return response


def format_update(existing_list, elements):
    existing_list['lastModified'] = int(time.time())
    existing_list['entries'] = elements
    return existing_list
