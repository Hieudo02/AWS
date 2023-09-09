import json

print('Loading function')

def lambda_handler(event, context):
    #1 Parse out query string parameters
    transactionID = event['queryStringParameters']['transactionID']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']
## Note that all variables above are String type

    print('transactionID = ' + transactionID)
    print('transactionType = ' + transactionType)
    print('transactionAmount = ' + transactionAmount)

    #2 Construct the body of the response object
    transactionResponse = {} # dictionary
    transactionResponse['transactionID'] = transactionID
    transactionResponse['transactionType'] = transactionType
    transactionResponse['transactionAmount'] = transactionAmount

    #3 Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    #4 Return the response object
    return responseObject
--------------------------------------------------------------------------
def lambda_handler(event, context):
    #1 Get query string parameter input
    x = event['queryStringParameters']['x']
    y = event['queryStringParameters']['y']
    operator = event['queryStringParameters']['operator']

    #2 Log inputs (just checking option, not necessary)
    print(f"x:{x}, y:{y}, operator:{operator}")

    #3 Prepare the response_body
    res_body = {}
    res_body['x'] = x
    res_body['y'] = y
    res_body['operator'] = operator
    res_body['ans'] = int(x) + int(y)

    #4 Prepare http response                        
    http_res = {}
    http_res['statusCode'] = 200
    http_res['headers'] = {}
    http_res['headers']['Content-Type'] = 'application/json'
    http_res['body'] = json.dumps(res_body)

    return http_res