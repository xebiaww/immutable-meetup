# Immutable Servers
with

![Docker logo](img/docker-logo-no-text.png) <!-- .element: class="noborder" -->
![plus](img/plus.png) <!-- .element: class="noborder" -->
![Packer logo](img/packer.png) <!-- .element: class="noborder" -->
![plus](img/plus.png) <!-- .element: class="noborder" -->
![Consul logo](img/consul-logo.png) <!-- .element: class="noborder" -->

Slides: [xebia.github.io/immutable-meetup](http://xebia.github.io/immutable-meetup)

Simon van der Veldt - [svanderveldt@xebia.com](mailto:svanderveldt@xebia.com)

Adriaan de Jonge - [adejonge@xebia.com](mailto:adejonge@xebia.com)


!SLIDE
# Introduction


!SLIDE
# Setup


!SUB
## Toolchain

boot2docker (version 1.1.2+)

[docs.docker.com/installation](http://docs.docker.com/installation)

Packer (version 0.6.0+)

[packer.io/downloads](http://packer.io/downloads)


!SUB
## Configure local machine
```
boot2docker start
export DOCKER_HOST=tcp://:2375
```


!SUB
### Files
[github.com/xebia/immutable-meetup](https://github.com/xebia/immutable-meetup)


