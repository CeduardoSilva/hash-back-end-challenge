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
import config.grpcconfig as grpcconfig

def makeRequest(productId, userId):
    """Generates a gRPC request with the data received.

    Args:
        arg1 (string): Product Id
        arg2 (string): User Id

    Returns:
        IndividualDiscountRequest: IndividualDiscountRequest to be sent to the gRPC server
    """
    return indDisc.IndividualDiscountRequest(
        productId=productId,
        userId=userId
    )

def generateMessages(dataList):
    """Yields messages to be streamed to the gRPC server

    Args:
        arg (list): List of products to be streamed to the gRPC server.

    Yields:
        IndividualDiscountRequest: IndividualDiscountRequest to be streamed to the gRPC server

    """
    for pair in dataList:
        yield makeRequest(pair["productId"], pair["userId"])

def getDiscountsStream(dataList):
    """Streams a list of products to the gRPC server and receives a list of products with discounts.

    Args:
        arg1 (list): Products List

    Returns:
        list: Discounted Products List
    """
    with grpc.insecure_channel(grpcconfig.url) as channel:
        stub = indDisc_grpc.DiscountStub(channel)
        discounts = stub.IndividualDiscountStream(generateMessages(dataList))
        response = []
        for discount in discounts:
            response.append(discount)
        return(response)