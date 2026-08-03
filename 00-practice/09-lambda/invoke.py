import json, requests
import boto3

lambda_client = boto3.client(
    "lambda",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1",
)

customer = {
    "gender": "male",
    "seniorcitizen": 0,
    "partner": "no",
    "dependents": "yes",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 6,
    "monthlycharges": 29.85,
    "totalcharges": 129.85
}

# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
# event = {"customer": customer}
# result = requests.post(url, json=event).json()
# print(result)

# Invoke the function
response = lambda_client.invoke(
    FunctionName='churn-prediction-lambda',
    InvocationType='RequestResponse',
    Payload=json.dumps({"customer": customer}).encode(),
)

result = json.loads(response['Payload'].read())
print(result)

# response = lambda_client.invoke(
#     FunctionName="hello-lambda",
#     Payload=json.dumps({"customer": customer}).encode(),
# )

# result = json.loads(response["Payload"].read())
# print(result)