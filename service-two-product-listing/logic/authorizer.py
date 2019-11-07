# Business Logic

import copy
from logic.business_logic_violations import rules

# Authorizes an transaction
def authorizeTransaction(incomingTransaction, transactionsData, accountData):
    """
    Receives a incoming transaction and the states of the account and authorized
    transactions and then loops through all rules set in bussines_logic_violations.py.
    Return a new account state based on whether or not violations occurred.
    """
    incomingTransaction = copy.deepcopy(incomingTransaction)    
    accountData = copy.deepcopy(accountData)
    transactionsData = copy.deepcopy(transactionsData)

    for rule in rules:
        if(rule["function"](incomingTransaction, transactionsData, accountData)):
            accountData["account"]["violations"].append(rule["name"])

    if not accountData["account"]["violations"]:
        accountData["account"]["availableLimit"] = accountData["account"]["availableLimit"] - incomingTransaction["transaction"]["amount"]

    return accountData