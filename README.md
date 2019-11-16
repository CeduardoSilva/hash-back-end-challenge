# Hash Back-end Challenge

Solution to Hash Back-end Challenge. It is comprised of two microservices written in Python and Node.JS to retrieve a list of products and discounts following a set of discount rules. Each microservice and their shared database is to be run on Docker containers.

## Requirements

All dependencies are packed inside the application images after building them, but to build the images and run the containers Docker is needed:

* [Docker](https://docs.docker.com/install/)

## Main points about code design choices

* Focus on making the application easily changeable and extensible by encapsulation of business logic and use of "Ports and adapters" architeture.
* MongoDB chosen as data base due to its ...
* Streaming

## Architeture - Ports and Adapters

This application is organized using the "Ports and Adapters" architeture. This architecture allows code to be organized into multiple layers that makes greater application decoupling possible by making simple the replacement of external services, creating and running tests, and encapsulating business logic. The layers into which the application has been split are: `logic`, `adapters`, `ports` and `controller`. Following is a description of each of the layers.

### Logic

The business logic of the application. The functions in this layer are designed to be completely independent of any technology outside the application. In Service 1 the logic layer deals with the functions that implement the discount rules and how to apply them. In Service 2 the logic layer deals with the retrieval of the products list.

### Adapters

This layer performs the conversion between external and internal representations of data. It makes it easier to handle any changes to external elements as it protects the business logic from those changes. In both microservices the adapters layer is used to parse the requests received in order to convert them in the default object format of the language.

### Ports

This layer has components responsible for communicating with external elements such as inputs, databases, external APIs, outputs, etc. Service One has ports for gRPC and the MongoDB database. Service Two has ports for gRPC, HTTP Requests and the MongoDB database.

### Controller

The controller acts as a connector between all the layers and orchestrates the flow between them.

## Instructions on running the services

### Building the images

#### Service One Image

```
docker build -t service-one-image:v1 .
```

#### Service Two Image

```
docker build -t service-two-image:v1 .
```

### Creating the network

```
docker network create hash-challenge-net
```

### Starting all containers

#### MongoDB Container

```
docker run -d -p 27017-27019:27017-27019 --net=hash-challenge-net --name mongodb mongo:4.0.4
```

#### Populating database

```
python populate_database.py
```

#### Service One Container
 
 ```
 docker run -it -p 50051:50051 --net=hash-challenge-net --name service-one service-one-image:v1
 ```

#### Service Two Container
 
 ```
 docker run -it -p 5000:5000 --net=hash-challenge-net --name service-two service-two-image:v1
 ```

 ## Tests

 ### Unit Tests

 ### Integration Tests

 ## Running Tests

 ## Extending the Application

 ### Adding new discount rules