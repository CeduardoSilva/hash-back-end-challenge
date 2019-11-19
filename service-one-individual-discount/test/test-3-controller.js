const assert = require('chai').assert;
const controller = require('../controller/controller');

var mockedRequest = {
    'productId': 'ID1',
    'userId': 'ID1'
}

/*describe('Tests the function individualDiscount', () => {
    it('Test: Must return a dict with the discount', () => {
        controller.individualDiscount(mockedRequest).then(result => {
            assert.equal(JSON.stringify(result), JSON.stringify({ 'pct': 0, 'value_in_cents': 0, 'applicable_discounts': '' }));
        });
    });
});*/
