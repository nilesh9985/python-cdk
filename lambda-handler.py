def main(event, context):
    mnumber=event['queryStringParameters']['mnumber']
    mydic={'98198': 'vodafone-mumbai', '98199': 'airtel-delhi'}
    code=str(mnumber)[-10:][:5]
    print(event)
    return {
        "statusCode": 200,
        "body": mydic[code]
    }
