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
consul agent -data-dir /tmp/consul > /var/consul.log & 
```


!SUB
Join cluster

```
consul join {IP OF FIRST IMAGE}
```

```
consul members
```

!SUB

*You have just created your first, small consul cluster*

 - Your cluster consists of one server and one client
 - In production, it is recommended to have 3 or 5 servers
 - In the next step, we are going to replace the server

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
*This server we will use as central point throughout the rest of the workshop so please save the IP address again*

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
## Note

In this workshop we are running Consul in each and every container. This will help us play around with Consul. However, you may prefer a setup with a single, central Consul container per Docker host once you start using this setup in larger environments.

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

```
docker run -ti --dns 127.0.0.1 xebia/consul-service
consul join {IP OF FIRST IMAGE}
dig fruit.service.consul
consul leave
```

!SLIDE

## Add an app that offers the service
Now set up the Python web app to run the service

```
#!/usr/bin/python
# From http://www.acmesystems.it/python_httpserver
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("Hello World from Docker image!")
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)

    #Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
```

!SUB
And check if it works
```
curl fruit.service.consul:8080
```

!SUB
Now perform a zero-downtime upgrade of your fruit service

!SLIDE
## Inject key-value pairs as Environment Variable

!SUB
Install essentials for environment variables

```
FROM xebia/consul-dns
RUN wget --no-check-certificate https://github.com/hashicorp/envconsul/releases/download/v0.5.0/envconsul_0.5.0_linux_amd64.tar.gz
RUN tar -zxvf envconsul_0.5.0_linux_amd64.tar.gz
RUN ls
RUN chmod 755 ./envconsul_0.5.0_linux_amd64
CMD /opt/consul agent -data-dir /tmp/consul -config-dir /opt/config/ -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash
```

!SUB
Run the container and join the cluster

!SUB
Set key-value pairs using the HTTP API
```
curl -X PUT -d 'myvalue' http://localhost:8500/v1/kv/web/mykey
```
*You should be able to guess how to read them. Recognize the [encoding](https://www.base64decode.org/) of the values?*

!SUB
Install web ui

```
FROM xebia/consul-dns
RUN wget --no-check-certificate https://dl.bintray.com/mitchellh/consul/0.5.0_web_ui.zip
RUN mkdir ui
RUN unzip 0.5.0_web_ui.zip -d /opt/ui
RUN rm 0.5.0_web_ui.zip
CMD /opt/consul agent -data-dir /tmp/consul -config-dir /opt/config/ -ui-dir /opt/ui/dist -client 0.0.0.0 -bind 0.0.0.0 > /var/consul.log & bash
```

!SUB
Run web ui and expose port and join the cluster

```
docker $RUN -p 8500:8500 xebia/consul-ui
consul join {IP of one of cluster members}
```

!SUB
Now you can also set key-value pairs using the Consul web ui at http://192.168.59.103:8500
![Consul web ui](img/consul-webui.png) <!-- .element: class="noborder" -->
[consul.io/intro/getting-started/ui](http://www.consul.io/intro/getting-started/ui.html)


!SUB
See the key/values in /web translated to environment variables
```
./envconsul web env
```

!SUB
See the restarting of your "application" in case of updates
```
envconsul web /bin/sh -c "env; echo "-----"; sleep 1000"
```
Go back to consul-env container and check the changes you make in the UI

!SLIDE

## Can execute one command on all the Consul nodes?
