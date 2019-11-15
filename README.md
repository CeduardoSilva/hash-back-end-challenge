# Hash Back End Challenge

## Service One - Individual Discount 

### Features checklist
- Receive a UserId using gRPC
- Receive a ProductId using gRPC
- Return a discount using gRPC (?)

RUnning Docker:

docker build -t mongodb-image:v1 .
docker run -it -p 27017:27017 --rm --name mongodb mongodb-image:v1
docker run -it -p 27017:27017 --name mongodb mongodb-image:v1

mongod --fork --logpath /var/log/mongod.log
python populate_database.py

docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:4.0.4