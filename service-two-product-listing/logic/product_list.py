import grpc_port as grpc
import mongodb_port as mongodb
import config.dbconfig as config

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

            with open('ass', 'w') as file:
                file.write(str(discounts))
                file.close()

            for i in range(0,len(discounts)):
                products[i]["discount"] = discounts[i]
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