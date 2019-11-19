import pytest
import mock
import controller as controller
import mongodb_port as mongodb
import grpc_port as grpc
import mocks.mongodb_response_mock as mongoResponse
import mocks.grpc_response_mock as grpcResponse

from pytest_mock import mocker 

class request:
    def __init__(self, headers):
        self.headers = headers
    
    def get(header):
        return self.headers[header]
    
def test_integration(mocker):
    mockedRequest = request({ "X-User-Id": "ID1" })
    
    mocker.patch.object(mongodb, 'findAll') 
    mocker.patch.object(grpc, 'getDiscountsStream')

    mongodb.findAll.return_value = mongoResponse.mock
    grpc.getDiscountsStream.return_value = grpcResponse.mock

    result = controller.retrieveProductListStream(mockedRequest)
    print(result)
    assert result[0]["discount"] 
    
if __name__ == '__main__':
    unittest.main()