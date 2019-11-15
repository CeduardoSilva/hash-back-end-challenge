# Adapters Layer

import json

def parseRequest(request):
    """Returns a dict with the X-User-Id header value.

    Args:
        arg (request): HTTP Get Request

    Returns:
        dict: Dict containing the userId

    """
    parsedRequest = {
        "userId": request.headers.get("X-User-Id")
    }
    return parsedRequest

# TODO - Check if I even use this function and remove or document it
def dictToJson(dictData):
    return json.dumps(dictData)