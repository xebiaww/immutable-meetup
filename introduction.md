# Immutable Servers
## with Docker, Packer and Consul

![Docker logo](img/docker-logo-no-text.png)

Slides: [xebia.github.io/immutable-meetup/slides](http://xebia.github.io/immutable-meetup/slides/)

Simon van der Veldt - [svanderveldt@xebia.com](mailto:svanderveldt@xebia.com)

Adriaan de Jonge - [adejonge@xebia.com](mailto:adejonge@xebia.com)


!SLIDE
## Introduction


!NOTE
Eventuele presenter notes


!SUB
### Eerste pagina


!SUB
### Tweede pagina


!SLIDE
## Toolchain

boot2docker (version 1.1.2+)

[docs.docker.com/installation](http://docs.docker.com/installation/)

Packer (version 0.6.0+)

[www.packer.io/downloads.html](http://www.packer.io/downloads.html)

!SLIDE
## Configure local machine
```
boot2docker start
export DOCKER_HOST=tcp://:2375
```
