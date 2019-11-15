import grpc_port as grpc
import mongodb_port as mongodb
import config.dbconfig as config

def grpcToDict(data):
    """Converts the discount information received via gRPC to a dict.

    Args:
        arg (gRPC Reply): Data received via gRPC

    Returns:
        dict: Dict containing the discount information

    """
    dataDict = { "pct": round(float(data.pct),2), "value_in_cents": int(data.value_in_cents), "applicable_discounts": data.applicable_discounts }
    return dataDict

def getStream(requestData):
    """Gets the product list from the database and tries to apply discounts calling the Service 1.

    Args:
        arg (requestData): Data from the HTTP Get request which may come with userId.

    Returns:
        list: List with all the products from the database and the discounts applied by Service 1.

    """
    productsCursor = mongodb.findAll(config.productsCollectionName, config.databaseName)
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