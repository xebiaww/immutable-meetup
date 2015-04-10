# Immutable Servers
with

![Docker logo](img/docker-logo-no-text.png) <!-- .element: class="noborder" -->
![plus](img/plus.png) <!-- .element: class="noborder" -->
![Consul logo](img/consul-logo.png) <!-- .element: class="noborder" -->

Slides: [xebia.github.io/immutable-meetup](http://xebia.github.io/immutable-meetup)

Adriaan de Jonge - [adejonge@xebia.com](mailto:adejonge@xebia.com)

<sup style="font-size: 10px;">*Initial version created together with [Simon van der Veldt](mailto:svanderveldt@xebia.com)*</sup>

!SLIDE
# Introduction

!SUB
"An Immutable Server is [...] a server that once deployed, is never modified, merely replaced with a new updated instance"

[_Kief Morris @ martinfowler.com_](http://martinfowler.com/bliki/ImmutableServer.html)

!SUB
## Antonyms

 - Snowflake Server
 - Phoenix Server

!SUB

The deliverable of the DevOps/NoOps team is a fully installed and configured server image.


!SUB

*Questions answered in this meetup: *

 - How do you easily deliver fully configured server images?
 - How do you configure an image without modifying it?


!SLIDE
# Setup


!SUB
Install boot2docker

[docs.docker.com/installation](http://docs.docker.com/installation)

!SUB
Start boot2docker and ssh into it
```
boot2docker start
boot2docker ssh
```

!SUB
Install Packer (inside boot2docker)
```
wget http://dl.bintray.com/mitchellh/packer/0.6.1_linux_amd64.zip
unzip 0.6.1_linux_amd64.zip -d /usr/local/bin/
```

!SUB
Check if it works
```
packer --version
> Packer v0.6.1
```

!SUB
Get the files

[github.com/xebia/immutable-meetup](https://github.com/xebia/immutable-meetup)
```
git clone https://github.com/xebia/immutable-meetup.git
```



