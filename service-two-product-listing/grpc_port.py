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
        print("Sending data...")
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
        for data in discounts:
            response.append({ "pct": round(float(data.pct),2), "value_in_cents": int(data.value_in_cents), "applicable_discounts": data.applicable_discounts })
        print("Response")
        print(response)
        return(response)