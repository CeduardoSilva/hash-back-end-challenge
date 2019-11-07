FROM centos:7

RUN yum update -y

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum install -y python-pip
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install atomos pytest

WORKDIR /home

RUN mkdir code-challenge-authorizer

WORKDIR /home/code-challenge-authorizer

COPY ./adapters /home/code-challenge-authorizer/adapters
COPY ./logic /home/code-challenge-authorizer/logic
COPY ./memory /home/code-challenge-authorizer/memory
COPY ./resources /home/code-challenge-authorizer/resources
COPY ./input-files /home/code-challenge-authorizer/input-files
COPY ./tests /home/code-challenge-authorizer/tests
COPY ./__init__.py /home/code-challenge-authorizer
COPY ./controller.py /home/code-challenge-authorizer
COPY ./std_input_port.py /home/code-challenge-authorizer
COPY ./README.md /home/code-challenge-authorizer

ENTRYPOINT /bin/bash
