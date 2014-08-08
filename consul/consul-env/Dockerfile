FROM xebia/consul
RUN wget --no-check-certificate https://github.com/hashicorp/envconsul/releases/download/v0.2.0/envconsul_linux_amd64
RUN chmod 755 ./envconsul_linux_amd64
CMD /opt/consul agent -data-dir /tmp/consul -config-dir /opt/config/ -dc xebia -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash