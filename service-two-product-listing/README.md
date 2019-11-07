# Code Challenge - Authorizer

Solution to Nubank's Authorizer Code Challenge. It is a simple application written in Python to authorize a transaction for a specific account following a set of predefined rules. It can be run normally on the machine's terminal or on a Docker container.

## Requirements

All dependencies are packed inside the application image after building it, but to run the application **outside** of its Docker container the following requirements are needed

* [Python 2](https://www.python.org/downloads/) 
* [Atomos](https://pypi.org/project/atomos/)

To build the Docker image and run the Docker container you will need

* [Docker](https://docs.docker.com/install/)

## Main points about code design choices 

* Focus on avoiding side effects in business logic functions and in the application in general.
* Focus on making the application easily changeable and extensible by encapsulation of business logic and use of "Ports and adapters" architeture.
* Prevention of concurrency issues using atomic operations on state changes.

## Architeture - Ports and Adapters

This application is organized using the "Ports and Adapters" architeture. This architecture allows code to be organized into multiple layers that makes greater application decoupling possible by making simple the replacement of external services, creating and running tests, and encapsulating business logic. The layers into which the application has been split are: `logic`, `adapters`, `ports` and `controller`. A `memory` directory was also created to house a memory structure for the state of the application following the guidance given by the challenge of not using any external database. Following is a description of each of the layers.

### Logic

The business logic of the application. The functions in this layer are designed to have no side effects and to be completely independent of any technology outside the application. This layer is divided into two files: `authorizer.py` and `business_logic_violations.py`.
Functions that implements the violations of business logic have been isolated in the `business_logic_violations.py` in order to make code maintenance simpler in case a new rule appear or a old one is removed or altered. In the `authorizer.py` file is the logic of the transition authorization that uses the functions of `business_logic_violations.py`.

### Adapters

This layer performs the conversion between external and internal representations of data and is located in the `adapters.py `file. It makes it easier to handle any changes to external elements as it protects the business logic from those changes. In the use case described in the challenge, the external representation of the data is a json string, since the Python language works with dictionaries the functions in the `adapter.py` file convert json to dictionary and vice versa.

### Ports

This layer has components responsible for communicating with external elements such as inputs, databases, external APIs, outputs, etc. This application has a single port implemented in the file `std_input_port.py` that receives data through stdin and outputs data through the stdout.

### Controller

The controller acts as a connector between all the layers and orchestrates the flow between them. The controller uses atomic operations provided by the atomos library to ensure data integrity in case of concurrency.

### In-Memory Storage

The `in_memory_storage.py` is designed to manage the memory structure that represents the state of the application and the functions for changing this state.
The structure is a dictionary with two fields, one for keeping account data and one for keeping the most recent authorized transactions. The transaction storage limit was set to 3 transactions as it is the minimum required to run the business rules described in the challenge but this limit can be easily extended by changing the data structure in the state.

## Instrucions to execute the application directly

### 1. Just run the application from the project root directory

```
python std_input_port.py < path/to/operations/file
```

`std_input_port.py` is the port that connects to stdin and is therefore used as the starting point to send a stream of operations to the application. The operations file is the text file containing the jsons of the operations to be executed.
The application displays the results through stdout.

## Instrucions to execute the dockerized version

### 1. Placing you files on the input-files directory

If you want to run the application with your own operations files you can place them in the `input-files` directory and they will be copied to the same directory inside the container.

### 2. Building the Docker image

Just enter the following command in the project root directory to build the image

```
docker build -t code-challenge:v1 .
```

### 3. Running the Docker container

To run a container with the application simply enter the following command at the terminal

```
docker run -it --name code-challenge-container code-challenge:v1
```

This will open a terminal in the container from which the application can be run. 

### 4. Running the application

To run the application just enter the following command in the project root directory at the container terminal

```
python std_input_port.py < path/to/operations/file
```

## Tests

In this application the test runner Pytest was used. Both unit and integration tests were created, located in the `tests` directory. All tests assume that only valid input will be evaluated as stated in the challenge and therefore only cover scenarios with valid data. In the `resources` directory there are files with valid operations and expected outputs which are used by the integration tests.

### Unit Tests

The unit tests were divided into 3 files: `test_unit_adapters.py`, `test_unit_logic.py`, `test_unit_memory.py`.

### Integration Tests

The integration tests are in the `test_integration.py file`. Scenarios have been included for each of the business logic violations as well as a sequence that runs without any violations.

## Running Tests

To run the tests just enter the following command in the project root directory

```
pytest -v
```

To run only a specific test file you can enter the command with the file path, for example

```
pytest tests/test_unit_logic.py 
```

## Extending the Application

Following the principles of "Ports and Adapters" architecture the application is easy to extend by simply adding new elements like ports to receive data in other ways, adapters to handle other data representations and altering files in the `logic` directory to modify business logic.

### Adding new business logic violations rules

To add a new business logic violations rule you must add a new function with the following signature to the `business_logic_violations.py` file

```python
def newRule(incomingTransaction, transactionsData, accountData)
    # Code to evaluate if a violation ocurred
```

Where `incomingTransaction` is the dictionary representing the transaction to be evaluated, `transactionsData` is the list holding all previous authorized transactions and `accountData` is the current state of the account. 
This function must return True if the violations ocurred and False if it didn't.
Then you must add the name of violation and the function to the `rules` list at the end of the `business_logic_violations.py` file

```python
rules = [
    {"name": "new-rule", "function": newRule}
    {"name": "card-not-active", "function": cardNotActive }, 
    {"name": "insufficient-limit", "function": insufficientLimit},
    {"name": "doubled-transaction", "function": doubledTransaction},
    {"name": "high-frequency-small-interval", "function": highTransactionFrequency}]
```

