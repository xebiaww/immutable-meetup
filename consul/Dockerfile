FROM debian:wheezy
WORKDIR /opt
RUN apt-get update
RUN apt-get -y install unzip wget
RUN wget --no-check-certificate https://dl.bintray.com/mitchellh/consul/0.3.1_linux_amd64.zip
RUN unzip 0.3.1_linux_amd64.zip
RUN rm 0.3.1_linux_amd64.zip
CMD bash