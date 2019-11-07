# Controller

import copy
import memory.in_memory_storage as memory
import logic.authorizer as authorizer
import adapters.adapters as adapters

def processTransaction(currState, incomingTransaction):
    """
    Sends a transaction to the authorizer and updates the application 
    state based on its output
    """
    currState = copy.deepcopy(currState)
    incomingTransaction = copy.deepcopy(incomingTransaction)
    transactions = currState["transactions"]
    account = currState["accountData"]
    newState = currState

    newState["accountData"]["account"]["violations"] = []

    output = authorizer.authorizeTransaction(incomingTransaction, transactions, account)
    if not output["account"]["violations"]:
        newState = memory.addTransaction(newState, incomingTransaction)
    newState["accountData"] = output
    return newState

def receive(event):
    """
    Calls the create account operation or the authorized transaction
    operation depending on the event received
    """
    eventDict = adapters.jsonToDict(event)
    if("account" in eventDict):
        state = memory.getStateAtom()
        state.swap(memory.createAccount, eventDict)
        output = adapters.dictToJson(state.deref()["accountData"])
        return(output)
    elif("transaction" in eventDict):
        state = memory.getStateAtom()
        state.swap(processTransaction, eventDict)
        output = adapters.dictToJson(state.deref()["accountData"])
        return(output)
