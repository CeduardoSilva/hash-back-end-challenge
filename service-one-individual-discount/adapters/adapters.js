function parseRequest(request) {

    return new Promise(async (resolve,reject) => {

        var productId = request.productId;
        var userId = request.userId;

        console.log(`Product Id: ${productId}`);
        console.log(`User Id: ${userId}`);

        resolve({productId: productId, userId: userId});

    });
    
}

module.exports = {
    parseRequest: parseRequest
}