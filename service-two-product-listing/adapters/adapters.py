# Adapters Layer

import json

def parseRequest(request):
    parsedRequest = {
        "userId": request.headers.get("X-User-Id")
    }
    return parsedRequest

def grpcToJSON(data):
    dataDict = { "pct": round(float(data.pct),2), "value_in_cents": int(data.value_in_cents), "applicable_discounts": data.applicable_discounts }
    return json.dumps(dataDict)

# Dict to JSON 
def dictToJson(dictData):
    return json.dumps(dictData)