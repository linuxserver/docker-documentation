# [linuxserver/diskover](https://github.com/linuxserver/docker-diskover)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/diskover.svg)](https://microbadger.com/images/linuxserver/diskover "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/diskover.svg)](https://microbadger.com/images/linuxserver/diskover "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/diskover.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/diskover.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-diskover/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-diskover/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/diskover/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/diskover/latest/index.html)

[diskover](https://github.com/shirosaidev/diskover) is a file system crawler and disk space usage software that uses Elasticsearch to index and manage data across heterogeneous storage systems.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/diskover` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=diskover \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e REDIS_HOST=redis \
  -e REDIS_PORT=6379 \
  -e ES_HOST=elasticsearch \
  -e ES_PORT=9200 \
  -e ES_USER=elastic \
  -e ES_PASS=changeme \
  -e INDEX_NAME=diskover- \
  -e DISKOVER_OPTS= \
  -e WORKER_OPTS= \
  -e RUN_ON_START=true \
  -e USE_CRON=true \
  -p 80:80 \
  -p 9181:9181 \
  -p 9999:9999 \
  -v </path/to/diskover/config>:/config \
  -v </path/to/diskover/data>:/data \
  --restart unless-stopped \
  linuxserver/diskover
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
version: '2'
services:
  diskover:
    image: linuxserver/diskover
    container_name: diskover
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - REDIS_HOST=redis
      - REDIS_PORT=6379
      - ES_HOST=elasticsearch
      - ES_PORT=9200
      - ES_USER=elastic
      - ES_PASS=changeme
      - RUN_ON_START=true
      - USE_CRON=true
    volumes:
      - </path/to/diskover/config>:/config
      - </path/to/diskover/data>:/data
    ports:
      - 80:80
      - 9181:9181
      - 9999:9999
    mem_limit: 4096m
    restart: unless-stopped
    depends_on:
      - elasticsearch
      - redis
  elasticsearch:
    container_name: elasticsearch
    image: docker.elastic.co/elasticsearch/elasticsearch:5.6.9
    volumes:
      - ${DOCKER_HOME}/elasticsearch/data:/usr/share/elasticsearch/data
    environment:
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms2048m -Xmx2048m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
  redis:
    container_name: redis
    image: redis:alpine
    volumes:
      - ${HOME}/docker/redis:/data

```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80` | diskover Web UI |
| `9181` | rq-dashboard web UI |
| `9999` | diskover socket server |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `REDIS_HOST=redis` | Redis host (optional) |
| `REDIS_PORT=6379` | Redis port (optional) |
| `ES_HOST=elasticsearch` | ElasticSearch host (optional) |
| `ES_PORT=9200` | ElasticSearch port (optional) |
| `ES_USER=elastic` | ElasticSearch username (optional) |
| `ES_PASS=changeme` | ElasticSearch password (optional) |
| `INDEX_NAME=diskover-` | Index name prefix (optional) |
| `DISKOVER_OPTS=` | Optional arguments to pass to the diskover crawler (optional) |
| `WORKER_OPTS=` | Optional argumens to pass to the diskover bots launcher (optional) |
| `RUN_ON_START=true` | Initiate a crawl every time the container is started (optional) |
| `USE_CRON=true` | Run a crawl on as a cron job (optional) |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Persistent config files |
| `/data` | Default mount point to crawl |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Once running the URL will be `http://<host-ip>/` initial application spinup will take some time so please reload if you get an empty response. We highly reccomend using Docker compose for this image as it includes multiple database backends to link into.
If you are looking to mount the elasticsearch and redis data to your host machine for access neither of them currently support setting a custom UID or GID they will run by default as:

- Redis - UID=999 GID=999
- Elasticsearch - UID=1000 GID=1000

ElasticSearch also requires a sysctl setting on the host machine to run properly. Running `sysctl -w vm.max_map_count=262144` will solve this issue. To make this setting persistent through reboots, set this value in `/etc/sysctl.conf`.

If you simply want the application to work you can mount these to folders with 0777 permissions, otherwise you will need to create these users host level and set the folder ownership properly.

By default this compose example is pointed to a single directory and the UID and GID you pass to the diskover container needs to match that folders ownership. If these are shared folders with many owners the indexing will likely fail.

For specific questions or help setting up diskover in your environment please refer to the project's Github page [Diskover](https://github.com/shirosaidev/diskover).



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it diskover /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f diskover`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' diskover`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/diskover`

## Versions

* **12.04.19:** - Rebase to Alpine 3.9.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **01.11.18:** - Initial Release.
