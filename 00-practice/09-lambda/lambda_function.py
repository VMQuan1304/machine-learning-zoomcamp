def handler(event, context):
    name = event.get('url', 'World')

    print(f'parameter: {event}')

    return {
        "statusCode": 200,
        "body": f"Hello {name} this is the pa!"
    }