import adapters.adapters as adapters
import logic.product_list as productList

def retrieveProductListStream(request):
    """Calls the logic layer to get the product list.

    Args:
        arg (request): Data from the HTTP Get request which may come with userId.

    Returns:
        list: List with all the products from the database and the discounts applied by Service 1.

    """
    requestData = adapters.parseRequest(request)
    productListResponse = productList.getStream(requestData)
    return(productListResponse)