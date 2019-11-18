FROM centos:7

RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y python-pip

WORKDIR /home

RUN mkdir service-two-product-listing

COPY ./adapters /home/service-two-product-listing/adapters
COPY ./config /home/service-two-product-listing/config
COPY ./logic /home/service-two-product-listing/logic
COPY ./protobuffers /home/service-two-product-listing/protobuffers
COPY ./tests /home/service-two-product-listing/tests
COPY ./controller.py /home/service-two-product-listing
COPY ./grpc_port.py /home/service-two-product-listing
COPY ./http_port.py /home/service-two-product-listing
COPY ./mongodb_port.py /home/service-two-product-listing

RUN pip install pymongo flask waitress grpcio grpcio-tools mock pytest pytest_mock

ENTRYPOINT python service-two-product-listing/http_port.py