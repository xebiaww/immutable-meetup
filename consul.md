# Consul

!SUB
## Consul introduction


!SUB
## Start consul

- /opt/consul agent -server -bootstrap-expect 1 -data-dir /tmp/consul > /var/consul.log & bash


!SUB
## Join cluster

- /opt/consul join 172.17.0.25

!SUB
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