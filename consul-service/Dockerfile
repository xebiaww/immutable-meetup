FROM xebia/consul-dns
ADD config /opt/config/
CMD /opt/consul agent -data-dir /tmp/consul -config-dir /opt/config/ -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash
