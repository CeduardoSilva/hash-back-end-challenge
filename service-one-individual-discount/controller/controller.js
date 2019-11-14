var adapters = require('../adapters/adapters');
var mongodbPort = require('../ports/mongodb_port');
var logic = require('../logic/discount-calculator');

/**
 * TESTED
 * @param {} request 
 */
async function individualDiscount(request) {
    return new Promise(async (resolve, reject) => {

        var params = await adapters.parseRequest(request);
        
        var user = await mongodbPort.findOne({id: params.userId}, "testUsersCollection", "TestDB");
        var product = await mongodbPort.findOne({id: params.productId}, "testProductsCollection", "TestDB");

        if(user == null) reject({});
        if(product == null) reject({});
        if(user && product) resolve(logic.calculatesDiscount(user, product));

    });
}

module.exports = {
    individualDiscount: individualDiscount
}