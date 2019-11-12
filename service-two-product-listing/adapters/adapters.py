# Adapters Layer

import json

def parseRequest(request):
    parsedRequest = {
        "userId": request.headers.get("X-User-Id")
    }
    return parsedRequest

# Dict to JSON 
def dictToJson(dictData):
    return json.dumps(dictData)