import grpc_port as grpc
import mongodb_port as mongodb

def grpcToDict(data):
    print("Discount:")
    print(data.applicable_discounts)
    dataDict = { "pct": round(float(data.pct),2), "value_in_cents": int(data.value_in_cents), "applicable_discounts": data.applicable_discounts }
    return dataDict

def get(requestData):
    # Parametrizar
    productsCursor = mongodb.findAll("testProductsCollection", "TestDB")
    response = []
    if(requestData["userId"]):
        print("Received Id!")
        for product in productsCursor:
            ass = grpc.getDiscounts(requestData["userId"], product["id"])
            print(ass)
            product["discount"] = grpcToDict(ass)
            response.append(product)
    else:
        for product in productsCursor:
            product["discount"] = {}
            response.append(product)
    return(productsCursor)