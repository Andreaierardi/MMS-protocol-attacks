FROM ubuntu:18.10

RUN apt-get install bash
RUN apt-get update
RUN apt-get install -y net-tools
RUN apt-get install -y build-essential
RUN apt-get install -y iputils-ping
RUN rm -rf /var/cache/apk/*
RUN mkdir libreriaMMS
COPY /client /libreriaMMS/examples/tls_client_example
COPY /server /libreriaMMS/examples/tls_server_example
COPY /libiec61850-1.3.2 /libreriaMMS

