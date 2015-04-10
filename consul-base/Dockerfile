FROM debian:wheezy
WORKDIR /opt
RUN apt-get update
RUN apt-get -y install unzip wget curl dnsutils procps
RUN wget --no-check-certificate https://dl.bintray.com/mitchellh/consul/0.5.0_linux_amd64.zip
RUN unzip 0.5.0_linux_amd64.zip
RUN rm 0.5.0_linux_amd64.zip
CMD /opt/consul agent -server -bootstrap-expect 1 -data-dir /tmp/consul -dc xebia -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash
