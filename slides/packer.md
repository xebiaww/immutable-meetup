# Packer


!SLIDE
## Packer introduction


!SLIDE
## Your first packer image
2 simple steps:

- Create Packer template
- Build image


!SUB
### Step 1 - Create Packer template
exampletemplate.json
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

