# Extra exercises for fast students

!SLIDE
## Inject key-value pairs as Environment Variable

!SUB
Install essentials

```
FROM repo:consul
RUN wget --no-check-certificate https://github.com/hashicorp/envconsul/releases/download/v0.2.0/envconsul_linux_amd64
RUN chmod 755 ./envconsul_linux_amd64
CMD /opt/consul agent -data-dir /tmp/consul -config-dir /opt/config/ -dc xebia -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash
```

!SUB
Use GUI to set key-value pairs

```
FROM repo:consul
RUN wget --no-check-certificate https://dl.bintray.com/mitchellh/consul/0.3.1_web_ui.zip
RUN mkdir ui
RUN unzip 0.3.1_web_ui.zip -d /opt/ui
RUN rm 0.3.1_web_ui.zip
CMD /opt/consul agent -data-dir /tmp/consul -config-dir /opt/config/ -ui-dir /opt/ui/dist -dc xebia -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash
```

!SUB
Configure environment variables

```
./envconsul_linux_amd64 -addr="localhost:8500" prefix env
```

!SLIDE
## DIY
Build & run a mongodb image

!SLIDE
## Connect Python Hello World to MongoDB

!SUB
Install essentials:

- Dockerfile
```
FROM xebia/consul
ADD config /opt/config/
RUN apt-get -y install python
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install pymongo
CMD /opt/consul agent -data-dir /tmp/consul -config-dir /opt/config/ -dc xebia -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash
```