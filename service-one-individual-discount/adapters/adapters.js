/**
 * Parse a IndividualDiscount Request.
 * @param {IndividualDiscountRequest} request 
 * @returns {Object} With productId and userId from the request.
 */
function parseRequest(request) {

    var productId = request.productId;
    var userId = request.userId;
    return({productId: productId, userId: userId});
    
}

module.exports = {
    parseRequest: parseRequest
}