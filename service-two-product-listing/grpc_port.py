# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""
# python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/individualdiscount.proto

from __future__ import print_function
import logging

import grpc

import protobuffers.individualdiscount_pb2 as indDisc
import protobuffers.individualdiscount_pb2_grpc as indDisc_grpc

def makeRequest(productId, userId):
    return indDisc.IndividualDiscountRequest(
        productId=productId,
        userId=userId
    )

def generateMessages(dataList):
    for pair in dataList:
        yield makeRequest(pair["productId"], pair["userId"])

# TRY CATCH HERE
def getDiscounts(userId, productId):
    with grpc.insecure_channel('localhost:50051') as channel:    
        print("Creating stub...")
        stub = indDisc_grpc.DiscountStub(channel)
        print("Connecting to stub...")
        response = stub.IndividualDiscount(indDisc.IndividualDiscountRequest(productId=productId, userId=userId))
        return(response)

def getDiscountsStream(dataList):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = indDisc_grpc.DiscountStub(channel)
        discounts = stub.IndividualDiscountStream(generateMessages(dataList))
        response = []
        for discount in discounts:
            response.append(discount)
        return(response)

#if __name__ == '__main__':
#    logging.basicConfig()
#    run()
