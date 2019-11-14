const assert = require('chai').assert;
const adapters = require('../adapters/adapters');

var mockedRequest = {
    'productId': 'ID1',
    'userId': 'ID1'
}

describe('Tests the function parseRequest', () => {
    it('Test: Must return a dict with the product and user id\'s', () => {
        adapters.parseRequest(mockedRequest).then(result => {
            assert.equal(JSON.stringify(result), JSON.stringify({productId: 'ID1', userId: 'ID1'}));
        });
    });
});