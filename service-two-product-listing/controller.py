import adapters.adapters as adapters
import logic.product_list as productList

def retrieveProductList(request):
    requestData = adapters.parseRequest(request)
    productListResponse = productList.get(requestData)
    print(productListResponse)
    #response = adapters.grpcToJSON(productListResponse)
    print(productListResponse)
    return(productListResponse)