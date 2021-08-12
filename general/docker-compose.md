# Docker Compose

## Intro

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. 

## Installation

### Install Option 1 (recommended):
You can install docker-compose using our [docker-compose image](https://github.com/linuxserver/docker-docker-compose) via a run script. You can simply run the following commands on your system and you should have a functional install that you can call from anywhere as `docker-compose`:
```
sudo curl -L --fail https://raw.githubusercontent.com/linuxserver/docker-docker-compose/master/run.sh -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
In order to update the local image, you can run the following commands:
```
docker pull linuxserver/docker-compose:"${DOCKER_COMPOSE_IMAGE_TAG:-latest}"
docker image prune -f
```
To use the slimmer and more lightweight alpine based image, you can set an env var `DOCKER_COMPOSE_IMAGE_TAG=alpine` in your respective `.profile`. Alternatively you can set that var to a versioned image tag like `version-1.27.4` or `version-alpine-1.27.4` to pin it to a specific docker-compose version.

### Install Option 2:
We also publish binaries for docker-compose in [this repo](https://github.com/linuxserver/docker-docker-compose/releases). There are two versions, one for glibc based systems like Ubuntu and Debian, and one for musl based systems like Alpine. The latter are marked with the `alpine` tag. Each version contains binaries for `amd64`, `armhf` and `arm64`. You can pull these binaries into your system via the following commands to have a functional docker-compose install:
```
sudo curl -L --fail https://github.com/linuxserver/docker-docker-compose/releases/download/1.27.4-ls17/docker-compose-amd64 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## Single service Usage

Here's a basic example for deploying a Linuxserver container with docker-compose:

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

If you save the above snippet in a file named `docker-compose.yml`, you can simply run `docker-compose up -d` from within the same folder and the heimdall image will be automatically pulled, and a container will be created and started. `up` means bring the services up, and `-d` means do it in the background.

If you want to do it from a different folder or if you named the yaml file differently, ie. `heimdall.yml`, then you can define it in the command with `-f`: `docker-compose -f /path/to/heimdall.yml up -d`

To bring down the services, simply do `docker-compose down` or `docker-compose -f /path/to/heimdall.yml down` and all containers defined by the yml will be stopped and destroyed.

## Multiple Service Usage

You can have multiple services managed by a single compose yaml. Copy the contents below the `services:` line in any of our readme yaml samples into the same yaml file and the `docker-compose up/down` commands will apply to all services at once.

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

You now have 3 services defined in there: `heimdall`, `nginx` and `mariadb`. When you do a `docker-compose up -d`, it will first download the images for all three if they don't exist \(if they exist, they are not updated\) and it will create all three containers and start them. `docker-compose down` will bring all three services down and destroy the containers \(persistent data will remain\).

## Updates

If you want to update the images and recreate the containers with the same vars, it's extremely easy with docker-compose. First we tell it to update all images via `docker-compose pull`. Then we issue `docker-compose up -d` and it will automatically recreate the containers \(as necessary\) based on the updated images. If a container's image is already the latest and there was no update, it remains untouched.

Similarly, if you edit the contents of the yaml file and re-issue `docker-compose up -d`, only the containers affected by the changes to the yaml file will be recreated, others will be untouched.

Defining the containers running on your server as code is a core tenet of a "Devops" approach to the world. Constructing elaborate `docker run` commands and then forgetting which variables you passed is a thing of the past when using `docker-compose`.

## Tips & Tricks

`docker-compose` expects a `docker-compose.yml` file in the current directory and if one isn't present it will complain. In order to improve your quality of life we suggest the use of bash aliases. The file path for the aliases below assumes that the `docker-compose.yml` file is being kept in the folder `/opt`. If your compose file is kept somewhere else, like in a home directory, then the path will need to be changed.

Create or open the file `~/.bash_aliases` and populate with the following content:

```bash
alias dcup='docker-compose -f /opt/docker-compose.yml up -d' #brings up all containers if one is not defined after dcup
alias dcdown='docker-compose -f /opt/docker-compose.yml stop' #brings down all containers if one is not defined after dcdown
alias dcpull='docker-compose -f /opt/docker-compose.yml pull' #pulls all new images is specified after dcpull
alias dclogs='docker-compose -f /opt/docker-compose.yml logs -tf --tail="50" '  
alias dtail='docker logs -tf --tail="50" "$@"'
```
If the `docker-compose.yml` file is in a home directory, the following can be put in the `~/.bash_aliases` file.
```
alias dcup='docker-compose -f ~/docker-compose.yml up -d' #brings up all containers if one is not defined after dcup
alias dcdown='docker-compose -f ~/docker-compose.yml stop' #brings down all containers if one is not defined after dcdown
alias dcpull='docker-compose -f ~/docker-compose.yml pull' #pulls all new images unless one is specified
alias dclogs='docker-compose -f ~/docker-compose.yml logs -tf --tail="50" '
alias dtail='docker logs -tf --tail="50" "$@"'
```
There are multiple ways to see the logs of your containers. In some instances, using `docker logs` is preferable to `docker-compose logs`. By default `docker logs` will not run unless you define which service the logs are coming from. The `docker-compose logs` will pull all of the logs for the services defined in the `docker-compose.yml` file. 

When asking for help, you should post your logs or be ready to provide logs if someone requests it. If you are running multiple containers in your `docker-compose.yml` file, it is not helpful to submit **all** of the logs. If you are experiencing issues with a single service, say Heimdall, then you would want to get your logs using `docker logs heimdall` or `docker-compose logs heimdall`. The bash_alias for `dclogs` can be used if you define your service after you've typed the alias. Likewise, the bash_alias `detail` will not run without defining the service after it.


Some distributions, like Ubuntu, already have the code snippet below in the `~/.bashrc` file. If it is not included, you'll need to add the following to your `~/.bashrc` file in order for the aliases file to be picked up:

```bash
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

Once configured, you can run `source ~/.bashrc` or log out and the log in again. Now you can type `dcpull` or `dcup` to manage your entire fleet of containers at once. It's like magic.

