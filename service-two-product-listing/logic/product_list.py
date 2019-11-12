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
            try:
                product["discount"] = grpcToDict(grpc.getDiscounts(requestData["userId"], product["id"]))
            except Exception as e: 
                print("Error connecting to Individual Discount Service")
                product["discount"] = {}
            response.append(product)
    else:
        for product in productsCursor:
            product["discount"] = {}
            response.append(product)
    return(productsCursor)