import pytest
import mock
import controller as controller
import logic.product_list as logic
import mocks.logic_response_mock as logicReturnValue

from pytest_mock import mocker 

class request:
    def __init__(self, headers):
        self.headers = headers
    
    def get(header):
        return self.headers[header]

def test_retrieveProductListStream(mocker):

    mocker.patch.object(logic, 'getStream') 
    logic.getStream.return_value = logicReturnValue

    mockedRequest = request({ "X-User-Id": "ID1" })
    
    assert controller.retrieveProductListStream(mockedRequest) == logicReturnValue
    
if __name__ == '__main__':
    unittest.main()