# Packer
![Packer logo](img/packer.png) <!-- .element: class="noborder" -->


!SUB
## Packer introduction


!SLIDE
## Your first packer image
#### 2 simple steps

- Create Packer template
- Build image


!SUB
### Step 1 - Create Packer template
`example.json`
```
{
  "builders": [{
    "type": "docker",
    "image": "debian:wheezy",
    "export_path": "example.tar"
  }]
}
```

!SUB
### Step 2 - Build image
```
packer build exampletemplate.json
```

!NOTE
Note that it's a good idea to validate the Packer template first.
You can do so with `packer validate exampletemplate.json`


!SUB
### Result! 
```
==> docker: Creating a temporary directory for sharing data...
==> docker: Pulling Docker image: debian:wheezy
    docker: Pulling repository debian
==> docker: Starting docker container...
    docker: Run command: docker run -d -i -t -v /var/folders/yb/tbryjz896sgc6wl82k2m5y6r0000gn/T/packer-docker059094652:/packer-files debian:wheezy /bin/bash
    docker: Container ID: 2d087f4e41fd9282fda315e5be0505ea139faea8ed03ff784323ea6124da704a
==> docker: Exporting the container
==> docker: Killing the container: 2d087f4e41fd9282fda315e5be0505ea139faea8ed03ff784323ea6124da704a
Build 'docker' finished.

==> Builds finished. The artifacts of successful builds are:
--> docker: Exported Docker file: exampleimage.tar
```


!SUB
### Using your image
Import the image into Docker to use it

```
cat exampleimage.tar | docker import - simonvanderveldt:exampleimage
#or
docker import - simonvanderveldt:exampleimage < exampleimage.tar
```

Create a new container from your image
```
docker run -ti simonvanderveldt:exampleimage /bin/bash
```

!NOTE
Note that it's possible to have Packer automatically import the generated image into Docker by using the [docker-import](http://www.packer.io/docs/post-processors/docker-import.html) post-processor.


!SLIDE
## Make your image do something
`fruit.json`
```
{
  "builders": [
  {
    "type": "docker",
    "image": "debian:wheezy",
    "export_path": "fruit.tar"
  }],
  "provisioners": [
  {
    "type": "shell",
    "inline": [
    "echo orange > /opt/fruit.txt"
    ]
  }]
}
```


!SUB
Import the image & run it
```
packer build fruit.json
cat fruit.tar | docker import - simonvanderveldt:fruit
docker run -ti simonvanderveldt:fruit /bin/bash
```


!SUB
See the fruit of your labour
```
root@18220a274fbb:/# cat /opt/fruit.txt
orange
```

!SLIDE
## Your first application image
`hellowebworld.json`
```
{
  "builders": [
    {
      "type": "docker",
      "image": "debian:wheezy",
      "export_path": "python.tar"
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "inline": [
        "apt-get update",
        "apt-get -y install python"
      ]
    },
    {
      "type": "file",
      "source": "hellowebworld.py",
      "destination": "/srv/hellowebworld.py"
    }
  ]
}
```

!SUB
Import the image & run it
```
packer build hewllowebworld.json
cat hellowebworld.tar | docker import - simonvanderveldt:hellowebworld
docker run -ti -p 8080:8080 simonvanderveldt:hellowebworld python /srv/hellowebworld.py
```

!SUB
Check the result
```
curl {CONTAINERIP}:8080
> Hello World!
```


!SLIDE
## DIY
Build & run a mongodb image
