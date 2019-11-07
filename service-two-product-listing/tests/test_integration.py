import pytest
import controller as controller
import memory.in_memory_storage as memory
import adapters.adapters as adapters

def getFileContents(filePath):
    """
    Receives a file path and return a list containing the files lines
    """
    with open(filePath) as fileData:
        return(fileData.read().splitlines())

def test_accountAlreadyInitializedOperations():
    """
    Tests the ocurrence of account-already-initialized violation
    """
    memory.resetState()
    operations = getFileContents("./resources/operations/operations-account-already-initialized")
    expectedOutputs = getFileContents("./resources/outputs/outputs-account-already-initialized")
    actualOutputs = []

    for i in range(0,len(operations)):
        assert controller.receive(operations[i]) == expectedOutputs[i]

def test_cardNotActiveOperations():
    """
    Tests the ocurrence of card-not-active violation
    """
    memory.resetState()
    operations = getFileContents("./resources/operations/operations-card-not-active")
    expectedOutputs = getFileContents("./resources/outputs/outputs-card-not-active")
    actualOutputs = []

    for i in range(0,len(operations)):
        assert controller.receive(operations[i]) == expectedOutputs[i]

def test_doubledTransactionOperations():
    """
    Tests the ocurrence of double-transaction violation
    """
    memory.resetState()
    operations = getFileContents("./resources/operations/operations-doubled-transaction")
    expectedOutputs = getFileContents("./resources/outputs/outputs-doubled-transaction")
    actualOutputs = []

    for i in range(0,len(operations)):
        assert controller.receive(operations[i]) == expectedOutputs[i]

def test_highFrequencySmallIntervalOperations():
    """
    Tests the ocurrence of high-frequency-small-interval violation
    """
    memory.resetState()
    operations = getFileContents("./resources/operations/operations-high-frequency-small-interval")
    expectedOutputs = getFileContents("./resources/outputs/outputs-high-frequency-small-interval")
    actualOutputs = []

    for i in range(0,len(operations)):
        assert controller.receive(operations[i]) == expectedOutputs[i]

def test_insufficientLimitOperations():
    """
    Tests the ocurrence of insufficient-limit violation
    """
    memory.resetState()
    operations = getFileContents("./resources/operations/operations-insufficient-limit")
    expectedOutputs = getFileContents("./resources/outputs/outputs-insufficient-limit")
    actualOutputs = []

    for i in range(0,len(operations)):
        assert controller.receive(operations[i]) == expectedOutputs[i]

def test_normalOperations():
    """
    Tests a normal flow of transactions without violations
    """
    memory.resetState()
    operations = getFileContents("./resources/operations/operations-normal")
    expectedOutputs = getFileContents("./resources/outputs/outputs-normal")
    actualOutputs = []

    for i in range(0,len(operations)):
        assert controller.receive(operations[i]) == expectedOutputs[i]






if __name__ == '__main__':
    unittest.main()