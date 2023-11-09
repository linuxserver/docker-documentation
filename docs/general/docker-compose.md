# Docker Compose

## Intro

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

Note that when inputting data for variables, you must follow standard YAML rules. In the case of passwords with special characters this can mean escaping them properly ($ is the escape character) or properly quoting the variable. The best course of action if you do not know how to do this or are unwilling to research, is to stick to alphanumeric characters only.

## Installation

### Official Repos

Starting with version 2, Docker started publishing `docker compose` as a go based plugin for docker (rather than a python based standalone binary). They publish this plugin for multiple arches as opposed to the x86_64 only binaries for v1.x.

Install docker from the official repos as described [here](https://docs.docker.com/engine/install/), making sure that you install the `docker-compose-plugin` package as part of the process.

### Manual Package

You can install `docker compose` manually via the following commands:

```shell
mkdir -p "$HOME/.docker/cli-plugins" && \
curl -sL "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o "$HOME/.docker/cli-plugins/docker-compose" && \
chmod +x $HOME/.docker/cli-plugins/docker-compose
```

If you prefer to install it system-wide you can use `/usr/local/lib/docker/cli-plugins` instead of `$HOME/.docker/cli-plugins`

Assuming you already have docker (or at the very least docker-cli) installed, preferably from the official docker repos, running `docker compose version` should display the compose version.

#### v1.x compatibility

As v2 runs as a plugin instead of a standalone binary, it is invoked by `docker compose args` instead of `docker-compose args`. To make migration easier, Docker released a replacement binary for `docker-compose` on x86_64 and aarch64 platforms. More info on that can be found at the [upstream repo](https://github.com/docker/compose-switch).

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

If you save the above snippet in a file named `compose.yml`, you can simply run `docker compose up -d` from within the same folder and the heimdall image will be automatically pulled, and a container will be created and started. `up` means bring the services up, and `-d` means do it in the background.

If you want to do it from a different folder or if you named the yaml file differently, ie. `heimdall.yml`, then you can define it in the command with `-f`: `docker compose -f /path/to/heimdall.yml up -d`

To bring down the services, simply do `docker compose down` or `docker compose -f /path/to/heimdall.yml down` and all containers defined by the yml will be stopped and destroyed.

## Multiple Service Usage

You can have multiple services managed by a single compose yaml. Copy the contents below the `services:` line in any of our readme yaml samples into the same yaml file and the `docker compose up/down` commands will apply to all services at once.

Let's say you have the following in a yaml file named `compose.yml`:

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

You now have 3 services defined in there: `heimdall`, `nginx` and `mariadb`. When you do a `docker compose up -d`, it will first download the images for all three if they don't exist (if they exist, they are not updated) and it will create all three containers and start them. `docker compose down` will bring all three services down and destroy the containers (persistent data will remain).

## Updates

If you want to update the images and recreate the containers with the same vars, it's extremely easy with docker compose. First we tell it to update all images via `docker compose pull`. Then we issue `docker compose up -d` and it will automatically recreate the containers (as necessary) based on the updated images. If a container's image is already the latest and there was no update, it remains untouched.

Similarly, if you edit the contents of the yaml file and re-issue `docker compose up -d`, only the containers affected by the changes to the yaml file will be recreated, others will be untouched.

Defining the containers running on your server as code is a core tenet of a "Devops" approach to the world. Constructing elaborate `docker run` commands and then forgetting which variables you passed is a thing of the past when using `docker compose`.

## Support Requests

If you would like to request support, you can do so on [our discord server](https://discord.gg/linuxserver) or [our forum](https://discourse.linuxserver.io/). When you do so, please provide all the necessary information like the server and platform info, docker container log and the compose yaml.

If your compose yaml makes use of .env files, please post an output of `docker compose config` or `docker compose config -f /path/to/compose.yml` for the entire yaml, or `docker compose config <service name>` for a single service, as it will automatically replace the environment variables with their actual values.

There are multiple ways to see the logs of your containers. In some instances, using `docker logs` is preferable to `docker compose logs`. By default `docker logs` will not run unless you define which service the logs are coming from. The `docker compose logs` will pull all of the logs for the services defined in the `compose.yml` file.

When asking for help, you should post your logs or be ready to provide logs if someone requests it. If you are running multiple containers in your `compose.yml` file, it is not helpful to submit **all** of the logs. If you are experiencing issues with a single service, say Heimdall, then you would want to get your logs using `docker logs heimdall` or `docker compose logs heimdall`. The bash_alias for `dclogs` can be used if you define your service after you've typed the alias. Likewise, the bash_alias `detail` will not run without defining the service after it.

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

`docker compose` expects a `compose.yml` file in the current directory and if one isn't present it will complain. In order to improve your quality of life we suggest the use of bash aliases. The file path for the aliases below assumes that the `compose.yml` file is being kept in the folder `/opt`. If your compose file is kept somewhere else, like in a home directory, then the path will need to be changed.

Create or open the file `~/.bash_aliases` and populate with the following content:

```shell
alias dcup='docker compose -f /opt/compose.yml up -d' #brings up all containers if one is not defined after dcup
alias dcdown='docker compose -f /opt/compose.yml stop' #brings down all containers if one is not defined after dcdown
alias dcpull='docker compose -f /opt/compose.yml pull' #pulls all new images is specified after dcpull
alias dclogs='docker compose -f /opt/compose.yml logs -tf --tail="50" '
alias dtail='docker logs -tf --tail="50" "$@"'
```

If the `compose.yml` file is in a home directory, the following can be put in the `~/.bash_aliases` file.

```shell
alias dcup='docker compose -f ~/compose.yml up -d' #brings up all containers if one is not defined after dcup
alias dcdown='docker compose -f ~/compose.yml stop' #brings down all containers if one is not defined after dcdown
alias dcpull='docker compose -f ~/compose.yml pull' #pulls all new images unless one is specified
alias dclogs='docker compose -f ~/compose.yml logs -tf --tail="50" '
alias dtail='docker logs -tf --tail="50" "$@"'
```

Some distributions, like Ubuntu, already have the code snippet below in the `~/.bashrc` file. If it is not included, you'll need to add the following to your `~/.bashrc` file in order for the aliases file to be picked up:

```shell
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

Once configured, you can run `source ~/.bashrc` or log out and the log in again. Now you can type `dcpull` or `dcup` to manage your entire fleet of containers at once. It's like magic.
