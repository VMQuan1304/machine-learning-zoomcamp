# def handler(event, context):
#     name = event.get('url', 'World')

#     print(f'parameter: {event}')

#     return {
#         "statusCode": 200,
#         "body": f"Hello {name} this is the pa!"
#     }
import pickle

with open('model.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

def predict_single(customer):
    churn = pipeline.predict_proba(customer)[0, 1]
    return float(churn)
    # return 0.56


def lambda_handler(event, context):
    print(f'parameter: {event}')
    customer = event['customer']
    prob = predict_single(customer)
    # prob = predict_single(customer.dict())

    return {
        "churn_probability": prob,
        "churn": bool(prob >= 0.5)
    }