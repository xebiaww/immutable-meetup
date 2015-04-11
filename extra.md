# Extra exercises


!SLIDE
## DIY
Build & run a mongodb image

!SLIDE
## DIY
Connect `hellowebworld` to MongoDB using Consul

!SUB
Install essentials:

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

[hashicorp.com/blog/haproxy-with-consul](http://hashicorp.com/blog/haproxy-with-consul.html)
