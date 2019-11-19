import pytest
import mock
import grpc_port as grpc
import mongodb_port as mongodb
import logic.product_list as logic
import mocks.grpc_response_mock as grpcReturnValue
import mocks.mongodb_response_mock as mongodbReturnValue
import mocks.test_logic_response as logicResponse

from pytest_mock import mocker 

def test_getStream(mocker):

    mocker.patch.object(grpc, 'getDiscountsStream')
    mocker.patch.object(mongodb, 'findAll')

    grpc.getDiscountsStream.return_value = grpcReturnValue.mock
    mongodb.findAll.return_value = mongodbReturnValue.mock

    mockedRequest = { "userId": "ID1" }

    result = logic.getStream(mockedRequest)
    assert result == logicResponse.response
    
if __name__ == '__main__':
    unittest.main()