const sinon = require('sinon');
const expect = require('chai').expect;
const controller = require('../controller/controller');
const mongodbPort = require('../ports/mongodb_port');

var mockedRequest = {
    'productId': 'ID1',
    'userId': 'ID1'
}

describe('Integration Test', () => {
    it('must return a dict with the discount', async () => {

        var userMock = require('../test/mock/user_mock.json');
        var productMock = require('../test/mock/product_mock.json');

        var stub = sinon.stub(mongodbPort, "findOne").onFirstCall().returns(userMock).onSecondCall().returns(productMock);

        var testResult = await controller.individualDiscount(mockedRequest);
        stub.restore();
        expect(testResult).to.have.property("pct");
        expect(testResult).to.have.property("value_in_cents");
        expect(testResult).to.have.property("applicable_discounts");
    });
});


