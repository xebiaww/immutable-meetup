FROM xebia/consul-dns
ADD config /opt/config/
CMD consul agent -server -bootstrap-expect 1 -config-dir /opt/config/ -data-dir /tmp/consul -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash
