# Hash Back-end Challenge

Solution to Hash Back-end Challenge. It is comprised of two microservices written in Python and Node.JS to retrieve a list of products with their original prices and discount information following a set of discount rules. Each microservice and their shared database is to be run on Docker containers.

## Requirements

All dependencies are packed inside the service images after building them, but to build the images and run the containers Docker is needed:

* [Docker](https://docs.docker.com/install/)

## Main points about code design choices

* Focus on making the application easily changeable and extensible by encapsulation of business logic and use of "Ports and adapters" architeture.
* MongoDB was chosen as data base due to its single object structure which is very convienient to this application and the languages used reducing the need of complex data conversions/mapping.
* Bi-directional streaming was chosen as the communication method using gRPC between the two services in order to reduce latency.

## Architeture - Ports and Adapters

This application is organized using the "Ports and Adapters" architeture. This architecture allows code to be organized into multiple layers that makes greater application decoupling possible by making simple the replacement of external services, creating and running tests, and encapsulating business logic. The layers into which the application has been split are: `logic`, `adapters`, `ports` and `controller`. Following is a description of each of the layers.

### Logic

The business logic of the application. The functions in this layer are designed to be completely independent of any technology outside the application. In Service One the logic layer deals with the functions that implement the discount rules and how to apply them. In Service Two the logic layer deals with the retrieval of the products list.

### Adapters

This layer performs the conversion between external and internal representations of data. It makes it easier to handle any changes to external elements as it protects the business logic from those changes. In both microservices the adapters layer is used to parse the requests received in order to convert them in the default object format of the language.

### Ports

This layer has components responsible for communicating with external elements such as inputs, databases, external APIs, outputs, etc. Service One has ports for gRPC and the MongoDB database. Service Two has ports for gRPC, HTTP Requests and the MongoDB database.

### Controller

The controller acts as a connector between all the layers and orchestrates the flow between them.

## Instructions on running the services

To run the services you must first build the images for both services and start a Mongodb container. All three containers must be executed inside the same Docker Network.

### 1 - Building the images

Following are the instructions to build each image.

#### 1.1 Service One Image

From the `service-one-individual-discount` directory execute the following command to build the Service One Image.

```
docker build -t service-one-image:v1 .
```

Confirm that the image was correctly built by executing the following command. The service-one-image must be listed.

```
docker images
```

#### 1.2 Service Two Image

From the `service-two-product-listing` directory execute the following command to build the Service Two Image.

```
docker build -t service-two-image:v1 .
```

Confirm that the image was correctly built by executing the following command. The service-two-image must be listed.

```
docker images
```

### 2 - Creating the network

Run the following command to create the Docker Network which the services are going to use.

```
docker network create hash-challenge-net
```

Confirm the successfull creation of the network with the following command. The hash-challenge-net network must be listed.

```
docker network ls
```

### 3 - Starting all containers

Following are instructions to run all the containers and populate the tests databases. The services containers are going to execute tests and their deploy will fail in case any of the tests fail.

#### 3.1 MongoDB Container

To run the MongoDB Container execute the following command from any directory. After the deploy of the container the data base must be populated.

```
docker run -d -p 27017-27019:27017-27019 --net=hash-challenge-net --name mongodb mongo:4.0.4
```

#### 3.2 Populating database

To populate the database just run the following command from the `database` directory found at the root directory of the project, after successfully running the MongoDB Container.

```
python populate_database.py
```

#### 3.3 Service One Container
 
To run the Service One Container execute the following command from any directory.

```
docker run -d -p 50051:50051 --net=hash-challenge-net --name service-one service-one-image:v1
```

The command above will run the container on the background, if you want interactive mode execute the following command.

```
docker run -it -p 50051:50051 --net=hash-challenge-net --name service-one service-one-image:v1
```

You can verify if the container was correctly started by executing the following command and checking if the container is listed.

```
docker container ls
```

#### 3.4 Service Two Container

To run the Service Two Container execute the following commando from any directory.
 
 ```
 docker run -d -p 5000:5000 --net=hash-challenge-net --name service-two service-two-image:v1
 ```

 The command above will run the container on the background, if you want interactive mode execute the following command.

 ```
 docker run -it -p 5000:5000 --net=hash-challenge-net --name service-two service-two-image:v1
 ```

 You can verify if the container was correctly started by executing the following command and checking if the container is listed.

 ```
 docker container ls
 ```

### 4 - Using the services

After all the containers are running the `GET /product` route will be available at `localhost:5000`. A GET request to this route will return the list of all products contained at the data base and if the optional user id is sent in the request header `X-USER-ID` then the products will return with the applicable discounts regarding the user.

* Return Example
```javascript
{
    "products": [
        {
            "description": "Description 1", // Product's Description
            "discount": {
                "applicable_discounts": "Birthday Discount", // String with the names of all applicable discounts
                "pct": 0.05, // Discount Percentage
                "value_in_cents": 50 // Discount Value in cents
            },
            "id": "ID1",
            "price_in_cents": 1000, // Original Price
            "title": "Product 1" // Product's Title
        },
        {
            "description": "Description 2",
            "discount": {
                "applicable_discounts": "",
                "pct": 0.0,
                "value_in_cents": 0
            },
            "id": "ID2",
            "price_in_cents": 569,
            "title": "Product 2"
        },
        /* More products... */
    ]
}
```

In the case of Service One being offline or throwing an error the discount proprierty of the product will be a `{}`.
Configuration of ports used by both services and other parameters can be found on the config directory on both services root directory.

## Tests

The unit and integration tests are executed during the deployment of the containers, in case any test fail the container will not remain active.

## Extending the Application

### Adding new discount rules

To add new discount rules just add a function to implement this rule on the `service-one-individual-discount/logic/discount-rules.js` file.
All rule functions must follow the signature below.

```javascript
function ruleFunction(userData, productData) {
    if(/*Condition to discount is met*/) return /*discount percentage*/;
    /* else */return false;
}
```

Then you need to add the function to the discountRules array at the end of the file.

```javascript
var discountRules = [
    {
        ruleFunction: ruleFunction,
        ruleName: "Discount Rule Name" 
    }, 
    /*
    More rules...
    */
]
```