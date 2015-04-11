FROM xebia/consul-dns
RUN wget --no-check-certificate https://dl.bintray.com/mitchellh/consul/0.5.0_web_ui.zip
RUN mkdir ui
RUN unzip 0.5.0_web_ui.zip -d /opt/ui
RUN rm 0.5.0_web_ui.zip
EXPOSE 8500
CMD /opt/consul agent -data-dir /tmp/consul -config-dir /opt/config/ -ui-dir /opt/ui/dist -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash
