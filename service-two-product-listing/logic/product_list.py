import grpc_port as grpc
import mongodb_port as mongodb

def grpcToDict(data):
    """Converts the discount information received via gRPC to a dict.

    Args:
        arg (gRPC Reply): Data received via gRPC

    Returns:
        dict: Dict containing the discount information

    """
    dataDict = { "pct": round(float(data.pct),2), "value_in_cents": int(data.value_in_cents), "applicable_discounts": data.applicable_discounts }
    return dataDict

# TODO - Remove this function and adjust
#def get(requestData):
    
#    productsCursor = mongodb.findAll("testProductsCollection", "TestDB")
#    response = []
#    if(requestData["userId"]):
#        print("Received Id!")
#        for product in productsCursor:
#            try:
#                product["discount"] = grpcToDict(grpc.getDiscounts(requestData["userId"], product["id"]))
#            except Exception as e: 
#                print("Error connecting to Individual Discount Service")
#                print(e)
#                product["discount"] = {}
#            response.append(product)
#    else:
#        for product in productsCursor:
#            product["discount"] = {}
#            response.append(product)
#    return(productsCursor)

# TODO - Parametrize this function
def getStream(requestData):
    """Gets the product list from the database and tries to apply discounts calling the Service 1.

    Args:
        arg (requestData): Data from the HTTP Get request which may come with userId.

    Returns:
        list: List with all the products from the database and the discounts applied by Service 1.

    """
    productsCursor = mongodb.findAll("testProductsCollection", "TestDB")
    response = []
    products = []

    for product in productsCursor:
        products.append(product)

    if(requestData["userId"]):
        requestList = []
        for product in products:
            requestList.append({"productId": product["id"], "userId": requestData["userId"]})
        
        try:
            discounts = grpc.getDiscountsStream(requestList)
            for i in range(0,len(discounts)):
                products[i]["discount"] = grpcToDict(discounts[i])
                response.append(products[i])
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