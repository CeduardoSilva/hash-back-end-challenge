# Adapters Layer

import json
from datetime import datetime
from datetime import timedelta

# JSON to Dict and a small problem converting stuff
def jsonToDict(jsonString):
    
    dateFormat = '%Y-%m-%dT%H:%M:%S.%fZ' 
    dictResult = json.loads(jsonString)

    if("transaction" in dictResult):
        dictResult["transaction"]["time"] = datetime.strptime(dictResult["transaction"]["time"], dateFormat)
    return dictResult

# Dict to JSON 
def dictToJson(dictData):
    return json.dumps(dictData)
    