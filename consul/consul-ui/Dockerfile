FROM xebia/consul
RUN wget --no-check-certificate https://dl.bintray.com/mitchellh/consul/0.3.1_web_ui.zip
RUN mkdir ui
RUN unzip 0.3.1_web_ui.zip -d /opt/ui
RUN rm 0.3.1_web_ui.zip
CMD /opt/consul agent -data-dir /tmp/consul -config-dir /opt/config/ -ui-dir /opt/ui/dist -dc xebia -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash