const assert = require('chai').assert;
const discountCalculator = require('../logic/discount-calculator');

var mockedUserData = {};
var mockedProductData = {};
var mockedDiscountData = {};

describe('Tests the function calculatesDiscount', () => {
  it('Test: Must return a discount object for', () => {
    assert.equal(discountCalculator.calculatesDiscount(mockedUserData, mockedProductData), mockedDiscountData);
  });
});