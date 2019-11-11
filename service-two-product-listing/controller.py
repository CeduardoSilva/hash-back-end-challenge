import adapters.adapters as adapters
import logic.product_list as productList

def retrieveProductList(request):
    requestData = adapters.parseRequest(request)
    productListResponse = productList.get(requestData)
    response = []
    for product in productListResponse:
        product["discount"] = adapters.grpcToJSON(product["discount"])
        response.append(product)
    return(response)