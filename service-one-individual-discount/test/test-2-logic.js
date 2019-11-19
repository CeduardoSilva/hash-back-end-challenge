const assert = require('chai').assert;
const expect = require('chai').expect;
const discountCalculator = require('../logic/discount-calculator');
const discountRules = require('../logic/discount-rules');

function getCurrDate() {
  var d = new Date(),
      month = '' + (d.getMonth() + 1),
      day = '' + d.getDate()

  if (month.length < 2) 
      month = '0' + month;
  if (day.length < 2) 
      day = '0' + day;

  return [month, day].join('/');
}

var mockedUserData = {
  'last_name': 'Last Name 1', 
  'date_of_birth': getCurrDate(),
  'first_name': 'First Name 1', 
  'id': 'ID1'
};
var mockedProductData = require('../test/mock/product_mock.json');

describe('Tests the function calculatesDiscount', () => {
  it('must return a discount object', () => {    
    var testResult = discountCalculator.calculatesDiscount(mockedUserData, mockedProductData);
    expect(testResult).to.have.property("pct");
    expect(testResult).to.have.property("value_in_cents");
    expect(testResult).to.have.property("applicable_discounts");
  });
});

describe('Tests the function discountPct', () => {
  it('Test: Must return the correct percentage value from the two arguments received', () => {
    assert.equal(discountCalculator.discountPct(100, 50), 0.5);
  });
});

describe('Tests the birthday discount rule', () => {
  it('Test: Must return the correct percentage value from the two arguments received', () => {
    assert.equal(discountRules.discountBirthday(mockedUserData, mockedProductData), 0.05);
  });
});