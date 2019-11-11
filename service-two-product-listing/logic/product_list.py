import grpc_port as grpc
import mongodb_port as mongodb

def get(requestData):
    # Parametrizar
    productsCursor = mongodb.findAll("testProductsCollection", "TestDB")
    if(requestData["userId"]):
        print("Received Id!")
        for product in productsCursor:
            product["discount"] = grpc.getDiscounts(requestData["userId"], product["id"])
    else:
        print("Didn't receive Id!")
    return(productsCursor)