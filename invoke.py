import boto3
import json
import typing


def invoke_lambda_function():
    """
    invoke aws lamda function
    """

    payload = {
        'path': '/hello',
        'httpMethod': 'POST',
        'headers': {
            'content-type': 'application/json',
        },
        'requestContext': {
        },
        'body': json.dumps({'hello':"world"}),
        'isBase64Encoded': False
    }
    payload_str = json.dumps(payload)
    payload_bytes_arr = bytes(payload_str, encoding='utf8')
    client = boto3.client(
        'lambda'
    )
    response = client.invoke(
        FunctionName="zappa-dev",
        InvocationType="RequestResponse",
        Payload=payload_bytes_arr
    )
    data = json.loads(
        response['Payload'].read()
    )
    print(json.loads(data['body']))


if __name__ == "__main__":
    invoke_lambda_function()
