from datetime import datetime
from datetime import timedelta
from functools import reduce
from operator import add

def timeIntervalBiggerThan(incomingTransaction, transaction, interval):
    """
    Receives two transactions and a integer representing minutes and checks 
    if the time interval between the transactions is bigger than the interval
    """
    return ((incomingTransaction["transaction"]["time"] - transaction["transaction"]["time"]) > timedelta(minutes=interval))

def isSimilar(incomingTransaction, transaction):
    """
    Checks if two transactions are similar following the definition
    given in the challenge
    """
    if(incomingTransaction != {}) and (transaction != {}):

        incomingTransactionMerchant = incomingTransaction["transaction"]["merchant"]
        incomingTransactionAmount = incomingTransaction["transaction"]["amount"]
        transactionMerchant = transaction["transaction"]["merchant"]
        transactionAmount = transaction["transaction"]["amount"]

        return ((incomingTransactionMerchant == transactionMerchant) \
            and (incomingTransactionAmount == transactionAmount))
            
    return False

def isSimilarAndSmallInterval(incomingTransaction, transaction, interval):
    """
    Checks if two transactions are similar following the definition
    given in the challenge and if the interval between them is 
    smaller than the integer representing minutes received
    """
    return (isSimilar(incomingTransaction, transaction) and not timeIntervalBiggerThan(incomingTransaction, transaction, interval))

def doubledTransaction(incomingTransaction, transactionData, accountData):
    """
    Receives a transaction and the state of the application to determine whether a doubled
    transaction violation ocurred
    """
    interval = 2
    transactionLimit = 2
    return True if reduce(add, [isSimilarAndSmallInterval(incomingTransaction, transaction, interval) \
        for transaction in transactionData]) >= transactionLimit else False

def highTransactionFrequency(incomingTransaction, transactionsData, accountData):
    """
    Receives a transaction and the state of the application to determine whether 
    a high-frequency-small-interval violation occurred
    """
    interval = 2
    thirdTransaction = transactionsData[2] 
    if(thirdTransaction != {}) and not (timeIntervalBiggerThan(incomingTransaction, thirdTransaction, interval)):
            return True
    return False

def cardNotActive(incomingTransaction, transactionData, accountData):
    """
    Receives a transaction and the state of the application to determine whether a 
    card-not-active violation ocurred
    """
    return (not accountData["account"]["activeCard"])

def insufficientLimit(incomingTransaction, transactionData, accountData):
    """
    Receives a transaction and the state of the application to determine whether a 
    insufficient-limit violation occurred
    """
    return incomingTransaction["transaction"]["amount"] > accountData["account"]["availableLimit"]

rules = [
    {"name": "card-not-active", "function": cardNotActive }, 
    {"name": "insufficient-limit", "function": insufficientLimit},
    {"name": "doubled-transaction", "function": doubledTransaction},
    {"name": "high-frequency-small-interval", "function": highTransactionFrequency}]