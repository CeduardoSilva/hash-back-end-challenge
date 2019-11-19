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