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

## Using Rootless Podman (Optional)

**NOTE:** Using a rootless configuration is not officially supported. Our containers are designed to run in an unmodified Docker environment and may need manual troubleshooting to run properly in a rootless environment. Use at your own risk!

Podman aims to be a drop-in replacement for Docker, supporting most of it's features — while bringing a few of it's own. One such feature being rootless containers, which increases the security of your container environment by running the main Podman process as an unprivileged user. 

Do note that Podman is not fully compatible with `docker-compose`. You will need to translate your `docker-compose.yml` files to shell scripts. There is a `podman-compose` in the works but it is not yet up to par with `docker-compose`.

Using rootless containers is pretty straight forward once set up properly. The main things you will need are:
* a modern 64-bit Linux system
* root access to host (for setup only)
* cgroup V2 (found in most distributions)
* `podman`
* `slirp4netns`
* `fuse-overlayfs`

### Setup
All commands below must be run as root.

First, install required packages.

Next, create an unprivileged user to run Podman:
```shell
useradd -m -s /bin/bash podman && passwd podman
```

Finally, configure `/etc/subuid` and `/etc/subgid`:
```shell
usermod --add-subuids 100000-165535 --add-subgids 100000-165535 podman
```

### Usage

Simply use `podman` in commands where `docker` is used, or create an alias.

For more information about a rootless podman setup, be sure to visit the [official podman rootless tutorial](https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md).
