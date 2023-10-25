# Understanding PUID and PGID

!!! info
    We are aware that recent versions of the Docker engine have introduced the `--user` flag. Our images are not yet compatible with this, so we recommend continuing usage of PUID and PGID.

## Why use these?

Docker runs all of its containers under the `root` user domain because it requires access to things like network configuration, process management, and your filesystem. This means that the processes running inside your containers also run as `root`. This kind of elevated access is not ideal for day-to-day use, and potentially gives applications the access to things they shouldn't \(although, a strong understanding of volume and port mapping will help with this\).

Another issue is file management within the container's mapped volumes. If the process is running under `root`, all files and directories created during the container's lifespan will be owned by `root`, thus becoming inaccessible by you.

Using the `PUID` and `PGID` allows our containers to map the container's internal user to a user on the host machine. All of our containers use this method of user mapping and should be applied accordingly.

## Using the variables

When creating a container from one of our images, ensure you use the `-e PUID` and `-e PGID` options in your docker command:

```shell
docker create --name=beets -e PUID=1000 -e PGID=1000 linuxserver/beets
```

Or, if you use `docker-compose`, add them to the `environment:` section:

```yaml
environment:
  - PUID=1000
  - PGID=1000
```

It is most likely that you will use the `id` of yourself, which can be obtained by running the command below. The two values you will be interested in are the `uid` and `gid`.

```shell
id $user
```
