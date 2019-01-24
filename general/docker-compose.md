# Docker Compose

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

Here's a basic example for deploying a Linuxserver container with docker-compose:

```yaml
version: "2"
services:
  heimdall:
    image: linuxserver/heimdall
    container_name: heimdall
    mem_limit: 256m
    volumes:
      - /opt/appdata/heimdall:/config
    environment:
      - PUID: 1050
      - PGID: 1050
    restart: unless-stopped
```

Defining the containers running on your server as code is a core tenet of a "Devops" approach to the world. Constructing elaborate `docker run` commands and then forgetting which variables you passed is a thing of the past when using `docker-compose`.

## Tips & Tricks

`docker-compose` expects a `docker-compose.yml` file in the current directory and if one isn't present it will complain. In order to improve your quality of life we suggest the use of bash aliases.

Create the file `~/.bash_aliases` and populate with the following content:

```bash
alias dcp='docker-compose -f /opt/docker-compose.yml '
alias dcpull='docker-compose -f /opt/docker-compose.yml pull --parallel'
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
