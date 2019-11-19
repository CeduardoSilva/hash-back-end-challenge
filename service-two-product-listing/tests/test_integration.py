import pytest
import controller as controller

class request:
    def __init__(self, headers):
        self.headers = headers
    
    def get(header):
        return self.headers[header]

def test_integration():
    """
    Document
    """
    mocker.patch.object(logic, 'getStream') 
    logic.getStream.return_value = logicReturnValue
    mockedRequest = request({ "X-User-Id": "ID1" })
    assert controller.retrieveProductListStream(mockedRequest) == logicReturnValue
    
if __name__ == '__main__':
    unittest.main()