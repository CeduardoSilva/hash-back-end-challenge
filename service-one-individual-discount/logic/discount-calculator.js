var discountRules = require('./discount-rules').rules;
var discountLimit = 0.30;

function discountPct(normalPrice, discountedPrice) {
    return (1-(discountedPrice/normalPrice));
}

function calculatesDiscount(userData, productData) {

    var discount = {
        pct: 0,
        value_in_cents: 0,
        applicable_discounts: ""
    };

    var currPrice = productData.price_in_cents;
    var limitPrice = currPrice - (currPrice * discountLimit);

    for(let i = 0; i < discountRules.length; i++) {
        let discountPct = discountRules[i].ruleFunction(userData, productData);
        if(discountPct) {
            currPrice -= (currPrice * discountPct);
            discount.applicable_discounts += (discountRules[i].ruleName + " ");
        }
        if(currPrice < limitPrice) {
            currPrice = limitPrice;
            break;
        }
    }

    discount.pct = discountPct(productData.price_in_cents, currPrice);
    discount.value_in_cents = Math.ceil(productData.price_in_cents - currPrice);
    return discount;
    
}

module.exports = {
    calculatesDiscount: calculatesDiscount
}