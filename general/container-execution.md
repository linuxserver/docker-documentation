# Container Execution

You may find at some point you need to view the internal data of a container.

## Shell Access

Particularly useful when debugging the application - to shell in to one of our containers, run the following:

```shell
docker exec -it <container_name> /bin/bash
```

## Tailing the logs

The vast majority of our images are configured to output the application logs to the console, which in Docker's terms means you can access them using the `docker logs` command:

```shell
docker logs -f --tail=<number_of_lines_to_start_with> <container_name>
```

The `--tail` argument is optional, but useful if the application has been running for a long time - the `logs` command by default will output _all_ logs.

To make life simpler for yourself here's a handy bash alias to do some of the leg work for you:

```shell
# ~/.bash_aliases
alias dtail='docker logs -tf --tail="50" "$@"'
```

Execute it with `dtail <container_name>`.

## Checking the build version

If you are experiencing issues with one of our containers, it helps us to know which version of the image your container is running from. The primary reason we ask for this is because you may be reporting an issue we are aware of and have subsequently fixed. However, if you are running on the latest version of our image, it could indeed be a newly found bug, which we'd want to know more about.

To obtain the build version for the container:

```shell
docker inspect -f '{{ index .Config.Labels "build_version" }}' <container_name>
```

Or the image:

```shell
docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/<image_name>
```
