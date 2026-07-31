import requests

url = 'http://localhost:9696/predict'
url = 'https://holy-mountain-8999.fly.dev/predict'

customer = {
    "gender": "male",
    "seniorcitizen": 1,
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
    "totalcharges": 129.85,
    # "whatever": 22
}

response = requests.post(url, json=customer)
print('response', response.json())
churn = response.json()['churn']

if churn >= 0.5:
    print('let send promotion email')
else:
    print("don't do anything")