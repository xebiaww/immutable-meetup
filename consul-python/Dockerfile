FROM xebia/consul-service
RUN apt-get -y install python
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
ADD ws.py /opt/ws.py
CMD /opt/consul agent -data-dir /tmp/consul -config-dir /opt/config/ -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & python ws.py & bash
