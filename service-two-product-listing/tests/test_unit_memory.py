import pytest
import memory.in_memory_storage as memory

def test_setTransactionStorage():
    """
    Tests setting the transaction storage to a initial state
    """
    expectedResult = [{}, {}, {}]
    assert memory.setTransactionStorage(3) == expectedResult
    
def test_addTransaction():
    """
    Tests adding transactions to the transaction storage
    """
    memory.resetState()
    state = memory.getStateAtom().deref()

    transactions = [
        { "transaction": { "merchant": "Merchant A", "amount": 50, "time": "2019-02-13T10:00:00.000Z" } }, \
        { "transaction": { "merchant": "Merchant B", "amount": 100, "time": "2019-02-13T10:30:00.000Z" } }, \
        { "transaction": { "merchant": "Merchant C", "amount": 150, "time": "2019-02-13T11:00:00.000Z" } }, \
        { "transaction": { "merchant": "Merchant D", "amount": 200, "time": "2019-02-13T11:30:00.000Z" } }]
    
    expectedStateTransactions = [
        { "transaction": { "merchant": "Merchant D", "amount": 200, "time": "2019-02-13T11:30:00.000Z" } }, \
        { "transaction": { "merchant": "Merchant C", "amount": 150, "time": "2019-02-13T11:00:00.000Z" } }, \
        { "transaction": { "merchant": "Merchant B", "amount": 100, "time": "2019-02-13T10:30:00.000Z" } }, \
    ]

    for transaction in transactions:
        state = memory.addTransaction(state, transaction)

    assert state["transactions"] == expectedStateTransactions

def test_createAccount():
    """
    Tests creating an account on the application state
    """
    memory.resetState()
    state = memory.getStateAtom().deref()

    operations = [
        { "account": { "activeCard": True, "availableLimit": 100 } }, \
        { "account": { "activeCard": True, "availableLimit": 200 } }]
    
    expectedStateAccount = [
        {"account": {"activeCard": True, "availableLimit": 100, "violations": []}}, \
        {"account": {"activeCard": True, "availableLimit": 100, "violations": ["account-already-initialized"]}}]

    for i in range(0,len(operations)):
        state = memory.createAccount(state, operations[i])
        assert state["accountData"] == expectedStateAccount[i]

def test_resetState():
    """
    Tests resetting the application to its original state
    """
    operation = { "account": { "activeCard": True, "availableLimit": 100 } }
    initialState = { "accountData": {}, "transactions": [{}, {}, {}]}

    memory.resetState()
    state = memory.getStateAtom().deref()
    assert state == initialState

    state = memory.createAccount(state, operation)
    assert state != initialState

    memory.resetState()
    state = memory.getStateAtom().deref()
    assert state == initialState

def test_getStateAtom():
    """
    Tests getting the atom with the application current state
    """
    memory.resetState()
    assert memory.getStateAtom().deref() == { "accountData": {}, "transactions": [{}, {}, {}]}

if __name__ == '__main__':
    unittest.main()