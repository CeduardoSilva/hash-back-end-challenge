var blackFridayDate = "11/12"; 

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

function discountBirthday(userData, productData) {
    if(userData.date_of_birth == getCurrDate()) {
        return 0.05;
    } else {
        return false;
    }
}

function discountBlackFriday(userData, productData) {
    if(blackFridayDate == getCurrDate()) {
        return 0.10;
    } else {
        return false;
    }
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
    rules: discountRules
}