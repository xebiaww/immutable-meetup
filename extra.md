# Extra exercises for fast students

!SLIDE
## Inject key-value pairs as Environment Variable

!SUB
Install essentials

```
{
  "builders": [
    {
      "type": "docker",
      "image": "consul:dns",
      "export_path": "consul-ui.tar",
      "pull": false
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "inline": [
        "wget --no-check-certificate https://dl.bintray.com/mitchellh/consul/0.3.1_web_ui.zip",
        "mkdir ui",
        "unzip 0.3.1_web_ui.zip -d /opt/ui",
        "rm 0.3.1_web_ui.zip"
      ]
    }
  ]
}
```

!SUB
Use GUI to set key-value pairs

```
{
  "builders": [
    {
      "type": "docker",
      "image": "consul:dns",
      "export_path": "consul-ui.tar",
      "pull": false
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "inline": [
        "wget --no-check-certificate https://dl.bintray.com/mitchellh/consul/0.3.1_web_ui.zip",
        "mkdir ui",
        "unzip 0.3.1_web_ui.zip -d /opt/ui",
        "rm 0.3.1_web_ui.zip"
      ]
    }
  ]
}
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
## Connect Python Hello World to MongoDB using Consul

!SUB
Install essentials:

- Dockerfile
```
{
  "builders": [
    {
      "type": "docker",
      "image": "consul:dns",
      "export_path": "consul-python.tar",
      "pull": false
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "inline": [
        "apt-get -y install python",
        "wget https://bootstrap.pypa.io/get-pip.py",
        "python get-pip.py",
        "pip install pymongo"
      ]
    },
    {
      "type": "file",
      "source": "config/",
      "destination": "/opt/config/"
    },
    {
      "type": "file",
      "source": "ws.py",
      "destination": "/opt/ws.py"
    }
  ]
}
```

!SLIDE
## DIY

Perform health checks on each service

!SLIDE
## DIY

Configure HAProxy as a load balancer using Consul

http://www.hashicorp.com/blog/haproxy-with-consul.html