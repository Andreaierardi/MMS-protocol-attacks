FROM ubuntu:18.10
RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils nano iptables python3 python3-pip tcpdump
RUN apt-get install -y --no-install-recommends net-tools python3-dev build-essential libnetfilter-queue-dev
RUN pip3 install --upgrade pip
RUN pip3 install setuptools
RUN pip3 install NetfilterQueue
RUN pip3 install scapy-python3
RUN pip install scapy


COPY attacks/ /home/
WORKDIR /home/
CMD ["sleep", "9999999"]
