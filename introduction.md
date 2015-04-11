# Immutable Servers
with

![Docker logo](img/docker-logo-no-text.png) <!-- .element: class="noborder" -->
![plus](img/plus.png) <!-- .element: class="noborder" -->
![Consul logo](img/consul-logo.png) <!-- .element: class="noborder" -->

Slides: [blog.xebia.in/immutable-meetup](http://blog.xebia.in/immutable-meetup)

Adriaan de Jonge - [adejonge@xebia.com](mailto:adejonge@xebia.com)

<sup style="font-size: 16px;">*Initial version created together with [Simon van der Veldt](mailto:svanderveldt@xebia.com)*</sup>

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

*Question answered in this meetup: *

 - How do you configure an image without modifying it?


!SLIDE
# Setup


!SUB
Install boot2docker

[docs.docker.com/installation](http://docs.docker.com/installation)

!SUB
Start boot2docker
```
boot2docker start
```

!SUB
Get the files

[github.com/xebiaww/immutable-meetup](https://github.com/xebiaww/immutable-meetup)
```
git clone https://github.com/xebiaww/immutable-meetup.git
```



