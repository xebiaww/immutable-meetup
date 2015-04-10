FROM xebia/consul-dns
RUN wget --no-check-certificate https://github.com/hashicorp/envconsul/releases/download/v0.5.0/envconsul_0.5.0_linux_amd64.tar.gz
RUN tar -zxvf envconsul_0.5.0_linux_amd64.tar.gz -C .
RUN mv envconsul_0.5.0_linux_amd64/envconsul .
RUN rmdir envconsul_0.5.0_linux_amd64
RUN chmod 755 ./envconsul
CMD /opt/consul agent -data-dir /tmp/consul -config-dir /opt/config/ -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash
