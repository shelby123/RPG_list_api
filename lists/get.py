import json
from bson import json_util
from lists.db import get_db_collection
from lists.db import query_list


def get(event, context):
    collection = get_db_collection()
    doc = query_list(collection, event.pathParameters['id'])

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


