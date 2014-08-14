# Consul

!SUB
## Consul introduction


!SLIDE
## Create an image with consul installed

- Create base image with Packer file consul-base.json

```
{
  "builders": [
    {
      "type": "docker",
      "image": "debian:wheezy",
      "export_path": "consul.tar"
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "inline": [
        "cd /opt",
        "apt-get update",
        "apt-get -y install unzip wget curl dnsutils procps",
        "wget --no-check-certificate https://dl.bintray.com/mitchellh/consul/0.3.1_linux_amd64.zip",
        "unzip 0.3.1_linux_amd64.zip",
        "rm 0.3.1_linux_amd64.zip"
      ]
    }
  ]
}
```

!SUB
## Start image

```
packer build consul-base.json
cat consul-base.tar | docker import - repo:consul
docker run -ti repo:consul bash
```

- You can run the last command directly from your host OS (Mac OS)

!SUB
## Start consul

```
/opt/consul agent -server -bootstrap-expect 1 -data-dir /tmp/consul > /var/consul.log & bash
```

!SUB
## Check that Consul is running

```
ps
cd opt
./consul members
ip addr

```

- Save the IP address for a later step

!SUB
## Start a second consul

```
docker run -ti repo:consul sh
/opt/consul agent -server -bootstrap-expect 1 -data-dir /tmp/consul > /var/consul.log & bash
```


!SUB
## Join cluster

- ```/opt/consul join {IP OF FIRST IMAGE}```

- ```/opt/consul members```

!SLIDE
# Configure DNS with Consul

- Clean up previous images

## Configure DNS for Consul

- dns.json:
```
{
	"recursor": "8.8.8.8",
	"ports": {
		"dns": 53
	}
}
```
- Add `-config-file /opt/dns.json` to the consul command
- Add `-config-dir /opt/config/` to the consul command and move the dns.json file


Add
```
,
    {
      "type": "file",
      "source": "config",
      "destination": "/opt/config/"
    }
```

!SLIDE
# Inject key-value pairs as Environment Variable

!SUB
## Install essentials

```
FROM xebia/consul
RUN wget --no-check-certificate https://github.com/hashicorp/envconsul/releases/download/v0.2.0/envconsul_linux_amd64
RUN chmod 755 ./envconsul_linux_amd64
CMD /opt/consul agent -data-dir /tmp/consul -config-dir /opt/config/ -dc xebia -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash
```

!SUB
## Use GUI to set key-value pairs

```
FROM xebia/consul
RUN wget --no-check-certificate https://dl.bintray.com/mitchellh/consul/0.3.1_web_ui.zip
RUN mkdir ui
RUN unzip 0.3.1_web_ui.zip -d /opt/ui
RUN rm 0.3.1_web_ui.zip
CMD /opt/consul agent -data-dir /tmp/consul -config-dir /opt/config/ -ui-dir /opt/ui/dist -dc xebia -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash
```

!SUB
## Configure environment variables

```
./envconsul_linux_amd64 -addr="localhost:8500" prefix env
```

!SUB
## Configure Service Definition

- Add service.json to /config directory:
```
{
    "service": {
        "name": "python",
        "tags": ["master"],
        "port": 3000
    }
}
```
- Use service `dig python.service.consul`
- Use tag: `dig master.python.service.consul`
- Try adding one more to the cluster

!SLIDE
# Create Hello World in Python

!SUB
## Install essentials:

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