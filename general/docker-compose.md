# Docker Compose
## Intro
Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. You can follow these instructions to install docker-compose: https://docs.docker.com/compose/install/

## Single service
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
      - PUID: 1000
      - PGID: 1000
      - TZ=Europe/London
    ports:
      - 80:80
      - 443:443
    restart: unless-stopped
```

If you save the above snippet in a file named `docker-compose.yml`, you can simply run `docker-compose up -d` from within the same folder and the heimdall image will be automatically pulled, and a container will be created and started. `up` means bring the services up, and `-d` means do it in the background.

If you want to do it from a different folder or if you named the yaml file differently, ie. `heimdall.yml`, then you can define it in the command with `-f`: `docker-compose -f /path/to/heimdall.yml up -d`

To bring down the services, simply do `docker-compose down` or `docker-compose -f /path/to/heimdall.yml down` and all containers defined by the yml will be stopped and destroyed.

## Multiple Services
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
      - PUID: 1000
      - PGID: 1000
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
You now have 3 services defined in there: `heimdall`, `nginx` and `mariadb`. When you do a `docker-compose up -d`, it will first download the images for all three if they don't exist (if they exist, they are not updated) and it will create all three containers and start them. `docker-compose down` will bring all three services down and destroy the containers (persistent data will remain). 

## Updates
If you want to update the images and recreate the containers with the same vars, it's extremely easy with docker-compose. First we tell it to update all images via `docker-compose pull`. Then we issue `docker-compose up -d` and it will automatically recreate the containers (as necessary) based on the updated images. If a container's image is already the latest and there was no update, it remains untouched.

Similarly, if you edit the contents of the yaml file and re-issue `docker-compose up -d`, only the containers affected by the changes to the yaml file will be recreated, others will be untouched.

Defining the containers running on your server as code is a core tenet of a "Devops" approach to the world. Constructing elaborate `docker run` commands and then forgetting which variables you passed is a thing of the past when using `docker-compose`.

## Tips & Tricks

`docker-compose` expects a `docker-compose.yml` file in the current directory and if one isn't present it will complain. In order to improve your quality of life we suggest the use of bash aliases.

Create the file `~/.bash_aliases` and populate with the following content:

```bash
alias dcp='docker-compose -f /opt/docker-compose.yml '
alias dcpull='docker-compose -f /opt/docker-compose.yml pull'
alias dclogs='docker-compose -f /opt/docker-compose.yml logs -tf --tail="50" '
alias dtail='docker logs -tf --tail="50" "$@"'
```

You'll need to add the following to your `~/.bashrc` file in order for the aliases file to be picked up:

```bash
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

Once configured, log out and the log in again. Now you can type `dcpull` or `dcp up -d` to manage your entire fleet of containers at once. It's like magic.

