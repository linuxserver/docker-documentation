# Updating our containers

Our images are updated whenever the upstream application or dependencies get changed, so make sure you're always running the latest version, as they may contain important bug fixes and new features.

## Steps required to update

Docker containers are, for the most part, immutable. This means that important configuration such as volume and port mappings can't be easily changed once the container has been created. The containers created from our images run a very specific version of the application they wrap, so in order to update the application, you must recreate the container.

### Stop the container

Firstly, stop the container.

```shell
docker stop <container_name>
```

### Remove the container

Once the container has been stopped, remove it.

!!! warning
    Did you remember to persist the `/config` volume when you originally created the container? Bear in mind, you'll lose any configuration inside the container if this volume was not persisted. [Read up on why this is important](volumes.md).

```shell
docker rm <container_name>
```

### Pull the latest version

Now you can pull the latest version of the application image from Docker Hub.

```shell
docker pull linuxserver/<image_name>
```

### Recreate the container

Finally, you can recreate the container. This is often cited as the most arduous task as it requires you to remember all of the mappings you set beforehand. You can help mitigate this step by using Docker Compose instead - this topic has been [outlined in our documentation](docker-compose.md).

```shell
docker create \
    --name=<container_name> \
    -v <path_to_data>:/config \
    -e PUID=<uid> \
    -e PGID=<gid> \
    -p <host_port>:<app_port> \
    linuxserver/<image_name>
```

## Docker Compose

It is also possible to update a single container using Docker Compose:

```shell
docker-compose pull linuxserver/<image_name>
docker-compose up -d <container_name>
```

Or, to update all containers at once:

```shell
docker-compose pull
docker-compose up -d
```

## Removing old images

Whenever a Docker image is updated, a fresh version of that image gets downloaded and stored on your host machine. Doing this, however, does not remove the _old_ version of the image. Eventually you will end up with a lot of disk space used up by stale images. You can `prune` old images from your system, which will free up space:

```shell
docker image prune
```
