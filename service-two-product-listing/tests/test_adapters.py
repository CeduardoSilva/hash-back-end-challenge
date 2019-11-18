import pytest
import adapters.adapters as adapters

class request:
    def __init__(self, headers):
        self.headers = headers
    
    def get(header):
        return self.headers[header]

def test_parseRequest():
    """
    Document
    """
    mockedRequest = request({ "X-User-Id": "ID1" })
    assert adapters.parseRequest(mockedRequest) == { "userId": "ID1" }
    
if __name__ == '__main__':
    unittest.main()