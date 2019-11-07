# In Memory Storage

import copy
import atomos.atom as atom

def setTransactionStorage(length):
    """
    Creates the list to store the authorized transactions
    """
    transactionStorage = []
    for i in range(0,length):
        transactionStorage.append({})
    return transactionStorage

def addTransaction(state, incomingTransaction):
    """
    Add a transaction to the application state
    """
    state = copy.deepcopy(state)
    incomingTransaction = copy.deepcopy(incomingTransaction)
    state["transactions"].pop()
    state["transactions"].insert(0, incomingTransaction)
    return state

def createAccount(state, data):
    """
    Tries to create an account in the application state returning a violation
    if the account already exists
    """
    state = copy.deepcopy(state)
    data = copy.deepcopy(data)
    if(state["accountData"]):
        if("account-already-initialized" not in state["accountData"]["account"]["violations"]):
            state["accountData"]["account"]["violations"].append("account-already-initialized")
    else:
        data["account"]["violations"] = []
        state["accountData"] = data
    return state

def resetState():
    """
    Resets the application to its initial state
    """
    stateAtom.reset({ "accountData": {}, "transactions": setTransactionStorage(transactionStorageLimit)})

def getStateAtom():
    """
    Returns the atom with the application state
    """
    return stateAtom

transactionStorageLimit = 3
stateAtom = atom.Atom({ "accountData": {}, "transactions": setTransactionStorage(transactionStorageLimit)})