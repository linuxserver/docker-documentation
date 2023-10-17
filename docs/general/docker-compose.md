# Docker Compose

## Intro

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

Note that when inputting data for variables, you must follow standard YAML rules. In the case of passwords with special characters this can mean escaping them properly ($ is the escape character) or properly quoting the variable. The best course of action if you do not know how to do this or are unwilling to research, is to stick to alphanumeric characters only.

## Installation

### Option 1 (recommended)

Starting with version 2, Docker started publishing `docker compose` as a go based plugin for docker (rather than a python based standalone binary). And they also publish this plugin for various arches, including x86_64, armhf and aarch64 (as opposed to the x86_64 only binaries for v1.X). Therefore we updated our recommended install option to utilize the plugin.

Install docker from the official repos as described [here](https://docs.docker.com/engine/install/) or via the convenient [get-docker script](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script) as described below:

```shell
curl -fsSL https://get.docker.com -o get-docker.sh && \
sh get-docker.sh
```

### Option 2 (manual)

You can install `docker compose` manually via the following commands:

```shell
ARCH=$(uname -m) && [[ "${ARCH}" == "armv7l" ]] && ARCH="armv7" && \
sudo mkdir -p /usr/local/lib/docker/cli-plugins && \
sudo curl -SL "https://github.com/docker/compose/releases/latest/download/docker-compose-linux-${ARCH}" -o /usr/local/lib/docker/cli-plugins/docker-compose && \
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
```

Assuming you already have docker (or at the very least docker-cli) installed, preferably from the official docker repos, running `docker compose version` should display the compose version.

If you don't have docker installed yet, we recommend installing it via the following commands:

```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

#### v1.X compatibility

As v2 runs as a plugin instead of a standalone binary, it is invoked by `docker compose args` instead of `docker-compose args`. There are also some slight differences in how the yaml is operated as well. To make migration easier, Docker released a replacement binary for `docker-compose` on x86_64 and aarch64 platforms. More info on that can be found at the [upstream repo](https://github.com/docker/compose-switch).

### Option 3 (docker)

You can install docker-compose using our [docker-compose image](https://github.com/linuxserver/docker-docker-compose) via a run script. You can simply run the following commands on your system and you should have a functional install that you can call from anywhere as `docker-compose`:

```shell
sudo curl -L --fail https://raw.githubusercontent.com/linuxserver/docker-docker-compose/v2/run.sh -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

In order to update the local image, you can run the following commands:

```shell
docker pull linuxserver/docker-compose:"${DOCKER_COMPOSE_IMAGE_TAG:-v2}"
docker image prune -f
```

The above commands will use the v2 images (although invoked by`docker-compose` instead of `docker compose`). If you'd like to use v1 images, you can set an env var `DOCKER_COMPOSE_IMAGE_TAG=alpine`, `DOCKER_COMPOSE_IMAGE_TAG=ubuntu` in your respective `.profile`. Alternatively you can set that var to a versioned image tag like `v2-2.4.1-r1` or `version-alpine-1.27.4` to pin it to a specific docker-compose version.

## Single service Usage

Here's a basic example for deploying a Linuxserver container with docker compose:

```yaml
version: "2.1"
services:
  heimdall:
    image: linuxserver/heimdall
    container_name: heimdall
    volumes:
      - /home/user/appdata/heimdall:/config
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    ports:
      - 80:80
      - 443:443
    restart: unless-stopped
```

If you save the above snippet in a file named `docker-compose.yml`, you can simply run `docker compose up -d` from within the same folder and the heimdall image will be automatically pulled, and a container will be created and started. `up` means bring the services up, and `-d` means do it in the background.

If you want to do it from a different folder or if you named the yaml file differently, ie. `heimdall.yml`, then you can define it in the command with `-f`: `docker compose -f /path/to/heimdall.yml up -d`

To bring down the services, simply do `docker compose down` or `docker compose -f /path/to/heimdall.yml down` and all containers defined by the yml will be stopped and destroyed.

## Multiple Service Usage

You can have multiple services managed by a single compose yaml. Copy the contents below the `services:` line in any of our readme yaml samples into the same yaml file and the `docker compose up/down` commands will apply to all services at once.

Let's say you have the following in a yaml file named `docker-compose.yml`:

```yaml
version: "2.1"
services:
  heimdall:
    image: linuxserver/heimdall
    container_name: heimdall
    volumes:
      - /home/user/appdata/heimdall:/config
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    ports:
      - 80:80
      - 443:443
    restart: unless-stopped
  nginx:
    image: linuxserver/nginx
    container_name: nginx
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - /home/user/appdata/nginx:/config
    ports:
      - 81:80
      - 444:443
    restart: unless-stopped
  mariadb:
    image: linuxserver/mariadb
    container_name: mariadb
    environment:
      - PUID=1000
      - PGID=1000
      - MYSQL_ROOT_PASSWORD=ROOT_ACCESS_PASSWORD
      - TZ=Europe/London
    volumes:
      - /home/user/appdata/mariadb:/config
    ports:
      - 3306:3306
    restart: unless-stopped
```

You now have 3 services defined in there: `heimdall`, `nginx` and `mariadb`. When you do a `docker compose up -d`, it will first download the images for all three if they don't exist \(if they exist, they are not updated\) and it will create all three containers and start them. `docker compose down` will bring all three services down and destroy the containers \(persistent data will remain\).

## Updates

If you want to update the images and recreate the containers with the same vars, it's extremely easy with docker-compose. First we tell it to update all images via `docker compose pull`. Then we issue `docker compose up -d` and it will automatically recreate the containers \(as necessary\) based on the updated images. If a container's image is already the latest and there was no update, it remains untouched.

Similarly, if you edit the contents of the yaml file and re-issue `docker compose up -d`, only the containers affected by the changes to the yaml file will be recreated, others will be untouched.

Defining the containers running on your server as code is a core tenet of a "Devops" approach to the world. Constructing elaborate `docker run` commands and then forgetting which variables you passed is a thing of the past when using `docker compose`.

## Support Requests

If you would like to request support, you can do so on [our forum](https://discourse.linuxserver.io/) or on [our discord server](https://discord.gg/YWrKVTn?target=_blank). When you do so, please provide all the necessary information like the server and platform info, docker container log and the compose yaml.

If your compose yaml makes use of `.env`, please post an output of `docker compose convert` or `docker compose convert -f /path/to/compose.yml` for the entire yaml, or `docker compose convert <service name>` for a single service, as it will automatically replace the environment variables with their actual values.

## Common Gotchas

### Quoting variables

In compose yamls, the environment variables can be defined in a couple of different styles. For the style we use in our readme samples, wrapping the variables in quotes is not required unless the variables contain spaces. When it's necessary, you can wrap them in quotes as described below.

- Style 1 (our readme recommended style):
  ```yaml
  environment:
    - 'key=value'
  ```
  This method requires the entire line wrapped in quotes, including the key and the value.

- Style 2:
  ```yaml
  environment:
    key: 'value'
  ```
  With this method, you can wrap just the value in quotes.

### Escaping $ signs

Docker compose interprets values that follow a `$` as a variable and it will [interpolate at runtime](https://docs.docker.com/compose/compose-file/12-interpolation/). If your environment variables contain the `$` character as part of the value and it needs to be treated literally, you need to escape it with another `$` sign.

For example, if you want the variable `key` to have the value `real$value` exactly, you need to set `- 'key=real$$value'` in the compose yaml.

## Tips & Tricks

`docker compose` expects a `docker-compose.yml` file in the current directory and if one isn't present it will complain. In order to improve your quality of life we suggest the use of bash aliases. The file path for the aliases below assumes that the `docker-compose.yml` file is being kept in the folder `/opt`. If your compose file is kept somewhere else, like in a home directory, then the path will need to be changed.

Create or open the file `~/.bash_aliases` and populate with the following content:

```shell
alias dcup='docker compose -f /opt/docker-compose.yml up -d' #brings up all containers if one is not defined after dcup
alias dcdown='docker compose -f /opt/docker-compose.yml stop' #brings down all containers if one is not defined after dcdown
alias dcpull='docker compose -f /opt/docker-compose.yml pull' #pulls all new images is specified after dcpull
alias dclogs='docker compose -f /opt/docker-compose.yml logs -tf --tail="50" '
alias dtail='docker logs -tf --tail="50" "$@"'
```

If the `docker-compose.yml` file is in a home directory, the following can be put in the `~/.bash_aliases` file.

```shell
alias dcup='docker compose -f ~/docker-compose.yml up -d' #brings up all containers if one is not defined after dcup
alias dcdown='docker compose -f ~/docker-compose.yml stop' #brings down all containers if one is not defined after dcdown
alias dcpull='docker compose -f ~/docker-compose.yml pull' #pulls all new images unless one is specified
alias dclogs='docker compose -f ~/docker-compose.yml logs -tf --tail="50" '
alias dtail='docker logs -tf --tail="50" "$@"'
```

There are multiple ways to see the logs of your containers. In some instances, using `docker logs` is preferable to `docker compose logs`. By default `docker logs` will not run unless you define which service the logs are coming from. The `docker compose logs` will pull all of the logs for the services defined in the `docker-compose.yml` file.

When asking for help, you should post your logs or be ready to provide logs if someone requests it. If you are running multiple containers in your `docker-compose.yml` file, it is not helpful to submit **all** of the logs. If you are experiencing issues with a single service, say Heimdall, then you would want to get your logs using `docker logs heimdall` or `docker compose logs heimdall`. The bash_alias for `dclogs` can be used if you define your service after you've typed the alias. Likewise, the bash_alias `detail` will not run without defining the service after it.

Some distributions, like Ubuntu, already have the code snippet below in the `~/.bashrc` file. If it is not included, you'll need to add the following to your `~/.bashrc` file in order for the aliases file to be picked up:

```shell
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

Once configured, you can run `source ~/.bashrc` or log out and the log in again. Now you can type `dcpull` or `dcup` to manage your entire fleet of containers at once. It's like magic.
