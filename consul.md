# Consul
![Consul logo](img/consul-logo.png) <!-- .element: class="noborder" -->

!SUB
## Consul introduction

Consul "is a tool for discovering and configuring services in your infrastructure"


_source: consul.io_

!SUB

### Consul Features:

 - Service discovery
 - Health checking
 - Key value store
 - Multi-datacenter


_source: consul.io_

!SUB

### Consul works with:

 - Peer to peer networking
 - Gossip protocol (Serf)
 - An agent per node
 - A DNS interace (compatibility)
 - A REST interface (rich API)

!SLIDE
## Create an image with consul installed

!SUB
`consul-base.json`
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
Build, import & run the image

```
packer build consul-base.json
cat consul-base.tar | docker import - consul:base
docker run -ti consul:base bash
```

!SUB
Start consul

```
/opt/consul agent -server -bootstrap-expect 1 -data-dir /tmp/consul > /var/consul.log & bash
```

!SUB
Check that Consul is running

```
ps
cd opt
./consul members
ip addr

```

_Save the IP address for a later step_

!SUB
Create a 2nd consul container

```
docker run -ti consul:base bash
/opt/consul agent -server -bootstrap-expect 1 -data-dir /tmp/consul > /var/consul.log & bash
```


!SUB
Join cluster

```
/opt/consul join {IP OF FIRST IMAGE}
```

```
/opt/consul members
```

!SLIDE
## Configure DNS with Consul

!SUB
Clean up previous images
```
docker rm -f {container-id or name}
docker rmi -f {image-id or tag}
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
Add to your provisioner
```
    {
      "type": "file",
      "source": "config/",
      "destination": "/opt/config/"
    }
```

!SUB
Provision your image again, tag it as `consul:dns`

!SUB
Add `-config-dir /opt/config/` to the consul command and move the dns.json file

```
docker run -ti  --dns 127.0.0.1 -h myhost consul:dns sh
/opt/consul agent -server -bootstrap-expect 1 -config-dir /opt/config/ -data-dir /tmp/consul > /var/consul.log & bash
```

!SUB

Try the DNS:

```
dig myhost.node.consul
ping myhost.node.consul
```


!SLIDE
## Configure Service Definition

Add service.json to /config directory:

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
Try adding one more container to the cluster and `dig` agains

!SUB
Make this work with the web server image you made in the Packer section:

```
curl fruit.service.consul:8080
```

!SUB
Now perform a zero-downtime upgrade of your fruit service

