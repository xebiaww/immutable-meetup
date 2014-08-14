# Consul

!SUB
## Consul introduction


!SLIDE
## Create an image with consul installed

!SUB
Create base image with Packer file consul-base.json

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
Start image

```
packer build consul-base.json
cat consul-base.tar | docker import - repo:consul
docker run -ti repo:consul bash
```

_You can run the last command directly from your host OS (Mac OS)_

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
Start a second consul

```
docker run -ti repo:consul sh
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
      "source": "config",
      "destination": "/opt/config/"
    }
```

!SUB
Provision your image again

!SUB
Add `-config-dir /opt/config/` to the consul command and move the dns.json file

```
docker run -ti repo:consul sh
/opt/consul agent -server -bootstrap-expect 1 -config-dir /opt/config/ -data-dir /tmp/consul > /var/consul.log & bash
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
Try adding one more to the cluster

!SUB
Make this work with the image made in the Packer section:

```
curl fruit.service.consul:8080
```

!SUB
Now perform a zero-downtime upgrade of your fruit service

