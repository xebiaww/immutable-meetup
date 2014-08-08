# Consul

!SUB
## Consul introduction


!SUB
## Start consul

- /opt/consul agent -server -bootstrap-expect 1 -data-dir /tmp/consul > /var/consul.log & bash


!SUB
## Join cluster

- /opt/consul join 172.17.0.25