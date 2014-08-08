FROM debian:wheezy
WORKDIR /opt
ADD dns.json /opt/
RUN apt-get update
RUN apt-get -y install unzip wget dnsutils procps
RUN wget --no-check-certificate https://dl.bintray.com/mitchellh/consul/0.3.1_linux_amd64.zip
RUN unzip 0.3.1_linux_amd64.zip
RUN rm 0.3.1_linux_amd64.zip
CMD /opt/consul agent -server -bootstrap-expect 1 -data-dir /tmp/consul -config-file /opt/dns.json > /var/consul.log & bash