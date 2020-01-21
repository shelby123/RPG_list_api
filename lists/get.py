import json
import os
from pymongo import MongoClient

# TODO: refactor DB connection into separate file. 
def get(event, context):
    username = os.environ['DB_CREDENTIAL_USERNAME']
    password = os.environ['DB_CREDENTIAL_PASSWORD']
    url = "mongodb+srv://" + username + ":" + password + "@cluster0-gpeio.mongodb.net/test?retryWrites=true&w=majority";
    client = MongoClient(url);
    db = client.RPG;
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event, 
        "idRead": event['pathParameters']['id']
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