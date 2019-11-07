import pytest
import adapters.adapters as adapters

def test_jsonToDict():
    """
    Tests whether the json_to_dict function correctly converts a json string to a valid dict
    """
    jsonData = '{ "account": { "activeCard": true, "availableLimit": 1000 } }'

    assert adapters.jsonToDict(jsonData) == { 'account': {'activeCard': True, 'availableLimit': 1000 }}

def test_dictToJson():
    """
    Tests wheter the dict_to_json function correctly converts a dict into a valid json string
    """
    dictData = { 'account': { 'activeCard': True, 'availableLimit': 1000 } }

    assert adapters.dictToJson(dictData) == "{\"account\": {\"activeCard\": true, \"availableLimit\": 1000}}"

if __name__ == '__main__':
    unittest.main()