On master branch


# Log commando's

## Consul

- boot2docker start
- export DOCKER_HOST=tcp://:2375

Delete all containers:

- docker rm -f $(docker ps -a -q)

Delete all images:

- docker rmi -f $(docker images -a -q)


Set DNS for Docker image:

- option: DNS: --dns 127.0.0.1:8600
- docker run -ti --dns 127.0.0.1:8600 xebia/consul bash
