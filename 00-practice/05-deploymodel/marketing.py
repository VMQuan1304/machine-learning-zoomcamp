import requests
import google.auth.transport.requests
import google.oauth2.id_token
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"D:/github/machine-learning-zoomcamp/00-practice/05-deploymodel/data-470504-f8d51730d6df.json"
# url = 'http://localhost:9696/predict'
# url = 'https://holy-mountain-8999.fly.dev/predict'
url = 'https://churn-prediction-62791570809.asia-southeast3.run.app'

auth_req = google.auth.transport.requests.Request()
token = google.oauth2.id_token.fetch_id_token(auth_req, url)

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

response = requests.post(
    f'{url}/predict',
    json=customer,
    headers={"Authorization": f"Bearer {token}"}
)
print('response', response.json())
churn = response.json()['churn']

if churn >= 0.5:
    print('let send promotion email')
else:
    print("don't do anything")