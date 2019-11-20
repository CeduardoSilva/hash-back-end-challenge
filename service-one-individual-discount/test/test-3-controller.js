const sinon = require('sinon');
const assert = require('chai').assert;
const controller = require('../controller/controller');
const logic = require('../logic/discount-calculator');
const mongodbPort = require('../ports/mongodb_port');

var mockedRequest = {
    'productId': 'ID1',
    'userId': 'ID1'
}

describe('Tests the function individualDiscount', () => {
    it('Test: Must return a dict with the discount', () => {
        
        var userMock = require('../test/mock/user_mock.json');
        var productMock = require('../test/mock/product_mock.json');
        var logicMock = require('../test/mock/calculates_discount_mock.json');

        var stubMongo = sinon.stub(mongodbPort, "findOne").onFirstCall().returns(userMock).onSecondCall().returns(productMock);
        var stubLogic = sinon.stub(logic, "calculatesDiscount").returns(logicMock);

        controller.individualDiscount(mockedRequest).then(result => {
            assert.equal(JSON.stringify(result), JSON.stringify({ 'pct': 0, 'value_in_cents': 0, 'applicable_discounts': '' }));
            stubMongo.restore();
            stubLogic.restore();
        });
    });
});
