import pytest
import logic.business_logic_violations as bl
import logic.authorizer as authorizer

from datetime import datetime
from datetime import timedelta

def test_timeIntervalBiggerThan():
    """
    Test that the timeInterval function is returning the correct interval between two transactions
    """
    interval = 30
    incomingTransaction = { "transaction": { "merchant": "Merchant A", "amount": 5, "time": datetime(2019, 2, 13, 11, 0) } }
    olderTransaction = { "transaction": { "merchant": "Merchant B", "amount": 10, "time": datetime(2019, 2, 13, 10, 0) } }
    
    assert bl.timeIntervalBiggerThan(incomingTransaction, olderTransaction, interval) == True

def test_isSimilarAndSmallInterval():
    """
    Test that the isSimilarAndSmallInterval function correctly identifies two similar transactions with small intervals
    """
    interval = 2
    incomingTransaction = { "transaction": { "merchant": "Merchant A", "amount": 5, "time": datetime(2019, 2, 13, 10, 0, 1) }} 
    olderTransaction = { "transaction": { "merchant": "Merchant A", "amount": 5, "time": datetime(2019, 2, 13, 10, 0, 0) }}

    assert bl.isSimilarAndSmallInterval(incomingTransaction, olderTransaction, interval) == True

def test_doubledTransaction():
    """
    Test that the doubledTransaction function correctly identifies a case of doubled transaction
    """
    incomingTransaction = { "transaction": { "merchant": "Merchant A", "amount": 10, "time": datetime(2019, 2, 13, 12, 0, 3) }} 
    transactions = [{'transaction': {'merchant': "Merchant A", 'amount': 10, 'time': datetime(2019, 2, 13, 12, 0, 2)}}, {'transaction': {'merchant': "Merchant A", 'amount': 10, 'time': datetime(2019, 2, 13, 12, 0, 1)}}, {'transaction': {'merchant': 'Merchant B', 'amount': 10, 'time': datetime(2019, 2, 13, 11, 0, 0)}}]
    accountData = {'account': {'activeCard': True, 'availableLimit': 1000, 'violations': []}}

    assert bl.doubledTransaction(incomingTransaction, transactions, accountData) == True

def test_highTransactionFrequency():
    """
    Test that the highTransactionFrequency function correctly identifies a case of high frequency within small intervals
    """
    incomingTransaction = { "transaction": { "merchant": "Merchant A", "amount": 10, "time": datetime(2019, 2, 13, 12, 0, 4) }} 
    transactions = [{'transaction': {'merchant': "Merchant B", 'amount': 20, 'time': datetime(2019, 2, 13, 12, 0, 3)}}, {'transaction': {'merchant': "Merchant C", 'amount': 30, 'time': datetime(2019, 2, 13, 12, 0, 2)}}, {'transaction': {'merchant': 'Merchant D', 'amount': 40, 'time': datetime(2019, 2, 13, 12, 0, 1)}}]
    accountData = {'account': {'activeCard': True, 'availableLimit': 1000, 'violations': []}}

    assert bl.highTransactionFrequency(incomingTransaction, transactions, accountData) == True
    
def test_cardNotActive():
    """
    Test that the cardNotActive function correctly identifies whether the card is active or not
    """
    incomingTransaction = {}
    transactions = []
    accountData = {'account': {'activeCard': False, 'availableLimit': 1000, 'violations': []}}

    assert bl.cardNotActive(incomingTransaction, transactions, accountData) == True

def test_insufficientLimit():
    """
    Test that the insufficientLimit function correctly identifies whether a transaction amount is above the available limit
    """
    incomingTransaction = { "transaction": { "merchant": "Merchant A", "amount": 2000, "time": datetime(2019, 2, 13, 12, 0, 4) }} 
    transactions = []
    accountData = {'account': {'activeCard': True, 'availableLimit': 1000, 'violations': []}}

    assert bl.insufficientLimit(incomingTransaction, transactions, accountData) == True

def test_authorizeTransaction():
    """
    Test that the authorize_transaction function correctly authorizes a valid transaction
    """
    incomingTransaction = { "transaction": { "merchant": "Merchant A", "amount": 10, "time": datetime(2019, 2, 13, 13, 0, 0) }} 
    transactions = [{},{},{}]
    accountData = {'account': {'activeCard': True, 'availableLimit': 1000, 'violations': []}}

    assert authorizer.authorizeTransaction(incomingTransaction, transactions, accountData) == {'account': {'activeCard': True, 'availableLimit': 990, 'violations': []}}

if __name__ == '__main__':
    unittest.main()