import json


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def helloWorld(event, context):
    body = {
        "message": "Hello World!",
        
    }

    response = {"statusCode": 200, "body": json.dumps(body)}
    return response
