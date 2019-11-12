var adapters = require('../adapters/adapters');
var mongodbPort = require('../ports/mongodb_port');
var logic = require('../logic/discount-calculator');

async function individualDiscount(request) {
    return new Promise(async (resolve, reject) => {

        var params = await adapters.parseRequest(request);
        
        var user = await mongodbPort.findOne({id: params.userId}, "testUsersCollection", "TestDB");
        var product = await mongodbPort.findOne({id: params.productId}, "testProductsCollection", "TestDB");

        console.log(`Product: ${JSON.stringify(product)}`);
        console.log(`User: ${JSON.stringify(user)}`);

        if(user == null) {
            console.log(`User came null`);
            reject({});
        }
        if(product == null) {
            console.log(`Product came null`);
            reject({});
        }

        if(user && product) {
            console.log("CALLING SHIT ANYWAY");
            var discount = logic.calculatesDiscount(user, product);
            resolve(discount);
        }

    });
}

module.exports = {
    individualDiscount: individualDiscount
}