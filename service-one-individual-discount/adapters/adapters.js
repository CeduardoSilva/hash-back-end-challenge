function parseRequest(request) {

    return new Promise(async (resolve,reject) => {

        var productId = request.productId;
        var userId = request.userId;
        resolve({productId: productId, userId: userId});

    });
    
}

module.exports = {
    parseRequest: parseRequest
}