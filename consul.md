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
- Add -config-file /opt/dns.json to the consul command

!SUB
## Configure environment variables

```
./envconsul_linux_amd64 -addr="localhost:8500" prefix env
```
