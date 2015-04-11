# Cheat Sheet Docker / Packer / Consul

## Docker

- boot2docker start
- export DOCKER_HOST=tcp://192.168.59.103:2375

Delete all containers:

- docker rm -f $(docker ps -a -q)

Delete all images (including running):

- docker rmi -f $(docker images -a -q)

Build and tag Docker image:

- docker build -t xebia/consul-base consul-base
- docker build -t xebia/consul-dns consul-dns
- docker build -t xebia/consul-service consul-service
- docker build -t xebia/consul-env consul-env
- docker build -t xebia/consul-ui consul-ui
- docker build -t xebia/consul-python consul-python


## Consul

Set DNS for Docker image and assign hostname:

- export RUN=run -ti --dns 127.0.0.1
- docker $RUN -h mybase xebia/consul-base
- docker $RUN -h mydns xebia/consul-dns
- docker $RUN -h mysvc xebia/consul-service
- docker $RUN -h myenv xebia/consul-env
- docker $RUN -h myui -p 8500:8500 xebia/consul-ui
- docker $RUN -h myapp xebia/consul-python



Set Hostname:

docker run -ti --dns 127.0.0.1:8600 -h bootstrap xebia/consul
docker run -ti --dns 127.0.0.1:8600 -h node2 xebia/consul
