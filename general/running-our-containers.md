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

## Running Rootless Containers

In order to increase the security of your containers, you can run them in a rootless state using podman. Podman aims to be a direct drop-in for Docker, supporting most of Docker's features — while bringing a few of its own, namely rootless containers.

Do keep in mind, however, that `docker-compose` is not fully compatible with podman. There is a `podman-compose` in the works but it is not yet up to par with `docker-compose`.

Using rootless containers is pretty straight forward once set up properly. The main things we will need are:
* a modern 64-bit linux distribution
* root access to host (for configuration only)
* `podman`
* `slirp4netns`
* `fuse-overlayfs`

### Setup

First, we need to configure `/etc/subuid` and `/etc/subgid`.

We can configure both files using `usermod`, however, for educational purposes we will do it manually (it's really not that hard ;)).

Logged in as root and using your favorite text editor, create and open `/etc/subuid` and enter the following:

```text
user:100000:65536
```
Then repeat the same for `/etc/subgid`.

Note: Be sure to stick to this format: `USERNAME:UID:RANGE`.

If that process is too much for you, here is a single command that can accomplish the same task:

```shell
usermod --add-subuids 100000-165535 --add-subgids 100000-165535 user
```

With that finished, we are ready to start using rootless containers.

### Usage

Using rootless containers is the easiest part of the migration. Simply use `podman` in scripts where `docker` is used, or create an alias as the podman devs recommend. For example: `podman run hello-world` instead of `docker run hello-world`.

Since `docker-compose` is not fully compatible with podman, you may need to translate any `docker-compose.yml` files to shell scripts. The difficulty of doing this depends on your shell scripting skills and knowledge of the Docker CLI commands.

For more information about a rootless podman setup, be sure to visit the [official podman rootless tutorial](https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md).
