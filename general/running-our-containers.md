# Running LinuxServer Containers

## Image Structure

### Base Images

We have curated various base images which our main application images derive from. This is beneficial for two main reasons:

* A common dependency base between multiple images, reducing the likelihood of variation between two or more applications that share the same dependencies.
* Reduction in image footprint on your host machine by fully utilising Docker's image layering system. Multiple containers running locally that share the same base image will reuse that image and any of its ancestors.

### The `/config` volume

To help reduce variation between our images, we have adopted a common structure pattern for application config and dependent directories. This means that each image has its own internal `/config` directory which holds all application-specific configuration. With the exception of a small number of images, all of our images expose this volume.

We do this because we believe that it makes it easier to answer the common question of "where does the application data get persisted?" - the answer being "always in `/config`". If you don't map this directory when creating your containers, the config will only last as long as the lifespan of the container itself!

## Creating a Container

To create a container from one of our images, you must use either `docker create` or `docker run`. Each image follows the same pattern in the command when creating a container:

```shell
docker create \
    --name=<container_name> \
    -v <path_to_data>:/config \
    -e PUID=<uid> \
    -e PGID=<gid> \
    -p <host_port>:<app_port> \
    linuxserver/<image_name>
```
