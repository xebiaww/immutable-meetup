# Consul
![Consul logo](img/consul-logo.png) <!-- .element: class="noborder" -->

!SUB
## Consul introduction

Consul "is a tool for discovering and configuring services in your infrastructure"


[_consul.io_](http://www.consul.io)


!SUB

### Consul Features:

 - Service discovery
 - Health checking
 - Key value store
 - Multi-datacenter


[_consul.io_](http://www.consul.io)

!SUB

### Consul works with:

 - Peer to peer networking
 - Gossip protocol (Serf)
 - An agent per node
 - A DNS interface (compatibility)
 - A REST interface (rich API)

!SLIDE
## Create an image with consul installed

!SUB
`consul-base/Dockerfile`
```
FROM debian:wheezy
WORKDIR /opt
ENV PATH /opt:$PATH
RUN apt-get update
RUN apt-get -y install unzip wget curl dnsutils procps
RUN wget --no-check-certificate https://dl.bintray.com/mitchellh/consul/0.5.0_linux_amd64.zip
RUN unzip 0.5.0_linux_amd64.zip
RUN rm 0.5.0_linux_amd64.zip

```

!SUB
Build, import & run the image

```
docker build -t xebia/consul-base consul-base
docker run -ti xebia/consul-base bash
```

!SUB
Start consul

```
consul agent -server -bootstrap-expect 1 -data-dir /tmp/consul > /var/consul.log &
```

!SUB
Check that Consul is running

```
ps
consul members
ip addr

```

_Save the IP address for a later step_

!SUB
Create a 2nd consul container

```
docker run -ti xebia/consul-base bash
consul agent -server -bootstrap-expect 1 -data-dir /tmp/consul > /var/consul.log & 
```


!SUB
Join cluster

```
consul join {IP OF FIRST IMAGE}
```

```
consul members
```

!SLIDE
## Configure DNS with Consul

!SUB
Clean up previous containers
```
docker rm -f {container-id or name}
```

!SUB
Configure DNS for Consul

Add config/dns.json:
```
{
	"recursor": "8.8.8.8",
	"ports": {
		"dns": 53
	}
}
```

!SUB
Create a new Dockerfile
```
FROM xebia/consul-base
ADD config /opt/config/
```

!SUB
Build your image and tag it as `xebia/consul-dns`

!SUB
Start the docker image and check that the DNS does not work yet

```
docker run -ti  --dns 127.0.0.1 -h myhost xebia/consul-dns bash
ping google.com
cat /etc/resolv.conf
```

!SUB
Start consul with the new configuration: `-config-dir /opt/config/` and check again:

```
consul agent -server -bootstrap-expect 1 -config-dir /opt/config/ -data-dir /tmp/consul > /var/consul.log & 
ping google.com
```

!SUB

Now try internal nodes

```
dig myhost.node.consul
ping myhost.node.consul
```


!SLIDE
## Configure Service Definition

Create a new image that adds service.json to /config directory:

```
{
    "service": {
        "name": "fruit",
        "tags": ["master"],
        "port": 8080
    }
}
```



!SUB
## Configure Service Definition

This time we add the command to startup Consul to avoid typing the same thing over and over

```
FROM xebia/consul-dns
ADD config /opt/config/
CMD /opt/consul agent -data-dir /tmp/consul -config-dir /opt/config/ -dc xebia -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash
```

!SUB

Use service:

```
dig fruit.service.consul
```

!SUB
Use tag:

```
dig master.fruit.service.consul
```

!SUB
Try adding one more container to the cluster and `dig` again

!SUB
Make this work with the web server image you made in the Packer section:

```
curl fruit.service.consul:8080
```

!SUB
Now perform a zero-downtime upgrade of your fruit service

