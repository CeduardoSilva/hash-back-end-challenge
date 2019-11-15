// TODO - Parametrize this
var blackFridayDate = "11/15"; 

/**
 * Returns current day and month in the format MM/DD
 * @returns {String} MM/DD
 */
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

/**
 * Returns a percentage if the birthday discount is applicable to the received user and product, otherwise returns false
 * @param {Object} userData 
 * @param {Object} productData 
 * @returns {Number} percentage
 * @returns {Boolean} false
 */
function discountBirthday(userData, productData) {
    if(userData.date_of_birth == getCurrDate()) return 0.05;
    return false;
}

//TODO - Test
/**
 * Returns a percentage if the black friday discount is applicable to the received user and product, otherwise returns false
 * @param {Object} userData 
 * @param {Object} productData 
 * @returns {Number} percentage
 * @returns {Boolean} false
 */
function discountBlackFriday(userData, productData) {
    if(blackFridayDate == getCurrDate()) return 0.10;
    return false;
}


var discountRules = [
    {
        ruleFunction: discountBirthday,
        ruleName: "Birthday Discount" 
    }, 
    {
        ruleFunction: discountBlackFriday,
        ruleName: "Black Friday Discount"
    }
]

module.exports = {
    rules: discountRules,
    discountBirthday: discountBirthday,
    discountBlackFriday: discountBlackFriday
}