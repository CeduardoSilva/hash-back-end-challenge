const assert = require('chai').assert;
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
var mockedProductData = {
  'description': 'Description 1',
  'title': 'Product 1',
  'price_in_cents': 1000,
  'discount': {}, 
  'id': 'ID1'
};

var mockedDiscountData = { 
  'pct': 0.050000000000000044,
  'value_in_cents': 50,
  'applicable_discounts': 'Birthday Discount ' 
};

describe('Tests the function calculatesDiscount', () => {
  it('Test: Must return a discount object', () => {
    var testResult = JSON.stringify(discountCalculator.calculatesDiscount(mockedUserData, mockedProductData));
    assert.equal(testResult, JSON.stringify(mockedDiscountData));
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

//var result = discountPct(100, 50);
//console.log(result);