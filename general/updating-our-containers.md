# Updating our containers

Our images are updated weekly, so make sure you're always running the latest version, as they contain important bug fixes and new features.

## Steps required to update

Docker containers are, for the most part, immutable. This means that important configuration such as volume and port mappings can't be easily changed once the container has been created. The containers created from our images run a very specific version of the application they wrap, so in order to update the application, you must recreate the container.

### Stop the container

Firstly, stop the container.

```bash
docker stop <container_name>
```

### Remove the container

Once the container has been stopped, remove it.

> **Important**: Did you remember to persist the `/config` volume when you originally created the container? Bear in mind, you'll lose any configuration inside the container if this volume was not persisted. [Read up on why this is important](https://github.com/linuxserver/docker-documentation/tree/2fbbd392c7399b6dc743a8c7ea97e2e124870cff/docs/running-our-containers/README.md#the-code-classlanguage-textconfigcode-volume).

```bash
docker rm <container_name>
```

### Pull the latest version

Now you can pull the latest version of the application image from Docker Hub.

```bash
docker pull linuxserver/<image_name>
```

### Recreate the container

Finally, you can recreate the container. This is often cited as the most arduous task as it requires you to remember all of the mappings you set beforehand. You can help mitigate this step by using Docker Compose instead - this topic has been [outlined in our documentation](https://github.com/linuxserver/docker-documentation/tree/2fbbd392c7399b6dc743a8c7ea97e2e124870cff/docs/started-with-compose/README.md).

```bash
docker create \
    --name=<container_name> \
    -v <path_to_data>:/config \
    -e PUID=<uid> \
    -e PGID=<gid> \
    -p <host_port>:<app_port> \
    linuxserver/<image_name>
```

