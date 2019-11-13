import grpc_port as grpc
import mongodb_port as mongodb

def grpcToDict(data):
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
                print(e)
                product["discount"] = {}
            response.append(product)
    else:
        for product in productsCursor:
            product["discount"] = {}
            response.append(product)
    return(productsCursor)


def getStream(requestData):
    # Parametrizar
    productsCursor = mongodb.findAll("testProductsCollection", "TestDB")
    response = []
    products = []

    for product in productsCursor:
        products.append(product)

    if(requestData["userId"]):
        print("Received Id!")
        requestList = []
        for product in products:
            requestList.append({"productId": product["id"], "userId": requestData["userId"]})
        
        try:
            discounts = grpc.getDiscountsStream(requestList)
            print("Discounts")
            print(len(discounts))
            for i in range(0,len(discounts)):
                print("Looping"+str(i))
                products[i]["discount"] = grpcToDict(discounts[i])
                print(products[i])
                response.append(products[i])
            print("ENDING LOOP")
        except Exception as e: 
            print("Error connecting to Individual Discount Service")
            print(e)
            for product in products:
                product["discount"] = {}
                response.append(product)
    else:
        for product in products:
            product["discount"] = {}
            response.append(product)
    return(response)