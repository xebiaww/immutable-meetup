# Packer


!SLIDE
## Packer introduction


!SLIDE
## Your first packer image
#### 2 simple steps

- Create Packer template
- Build image


!SUB
### Step 1 - Create Packer template
`exampletemplate.json`
```
{
  "builders": [{
    "type": "docker",
    "image": "debian:wheezy",
    "export_path": "exampleimage.tar"
  }]
}
```

!SUB
### Step 2 - Build image
```
packer build exampletemplate.json
```


!SUB
### Result! 
`exampleimage.tar`


!SUB
### Using your image
Import the image into Docker to use it

```
cat exampleimage.tar | docker import - simonvanderveldt:exampleimage
```

Create a new container from your image
```
docker run -ti simonvanderveldt:exampleimage /bin/bash
```

!NOTE
Note that it's possible to have Packer automatically import the generated image into Docker by using the [docker-import](http://www.packer.io/docs/post-processors/docker-import.html) post-processor.
