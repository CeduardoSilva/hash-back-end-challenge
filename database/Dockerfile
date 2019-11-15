FROM mongo:4.0.4

RUN apt-get update -y
RUN apt-get install -y python-pip

WORKDIR /home

COPY ./helpers/products.json /home
COPY ./helpers/users.json /home
COPY ./helpers/populate_database.py /home
COPY ./helpers/visualizes_db.py /home
COPY ./helpers/run.sh /home

RUN pip install pymongo

ENTRYPOINT /bin/bash