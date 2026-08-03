from requests import Timeout

import boto3

lambda_client = boto3.client(
    "lambda",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1",
)

# response = lambda_client.list_functions()
# pprint(response)
response = lambda_client.create_function(
    FunctionName='churn-prediction-lambda',
    Role='arn:aws:iam::000000000000:role/lambda-role',
    Code={
        'ImageUri': 'quanvm4/churn-prediction-lambda:latest'
    },
    PackageType='Image',
    Timeout=30,
    MemorySize=128,
)

print(response)