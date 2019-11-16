FROM centos:7

RUN yum update -y
RUN yum install -y gcc-c++ make curl
RUN curl -sL https://rpm.nodesource.com/setup_12.x | bash -
RUN yum install -y nodejs

WORKDIR /home

RUN mkdir service-one-individual-discount

COPY ./adapters /home/service-one-individual-discount/adapters
COPY ./config /home/service-one-individual-discount/config
COPY ./controller /home/service-one-individual-discount/controller
COPY ./logic /home/service-one-individual-discount/logic
COPY ./ports /home/service-one-individual-discount/ports
COPY ./test /home/service-one-individual-discount/test
COPY ./package.json /home/service-one-individual-discount
COPY ./package-lock.json /home/service-one-individual-discount
COPY ./protos /home/service-one-individual-discount/protos

WORKDIR /home/service-one-individual-discount

RUN npm install

ENTRYPOINT node ports/grpc_port.js