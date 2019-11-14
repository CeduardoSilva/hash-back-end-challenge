import pytest
import requests
import adapters.adapters as adapters

def test_parseRequest():
    """
    Document
    """
    mockedRequest = {}
    local = Local()
    assert adapters.parseRequest(mockedRequest) == { "userId": "ID1" }
    
if __name__ == '__main__':
    unittest.main()