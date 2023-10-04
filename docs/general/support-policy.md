# LinuxServer Support Policy

Any exceptions to this support policy will be clearly called out in the readme for the relevant image.

## Formally Supported Images

Any actively maintained image from the LinuxServer organisation, excluding base images, is in scope for support. Note that if you are running an old version of an image we will likely ask you to upgrade to the latest version before providing support, unless your issue is version-specific.

This means that images, tags, and architectures that have been deprecated or archived are not in scope.

## Formally Supported Environments

We build and test all of our images using the latest stable branch of Docker CE using containerd and runc, on Linux, building for x86_64 (amd64) and aarch64 (arm64) architectures. Any matching client environment is in scope for support. In addition, any currently supported version of Docker CE is in scope.

We support the use of both docker compose and the docker CLI to manage containers, though the former is preferred.

We support the running of our containers on Unraid, using our supplied templates. We will not provide support for Unraid itself.

## Docker Mods

Support for the underlying mod logic is within scope for support, however, support for the mods themselves is provided by the listed maintainer of that mod, whether it is published in our mods repo or elsewhere.

## Reasonable Endeavours Support

There are many alternative configurations that should broadly work for most of our images, but we make no guarantees to that effect, and expect that you have a solid understanding of the underlying technologies you're using. Although we do not formally support them, we will endeavour to provide help where we can with any of the following:

* Use of our base images for 3rd party projects
* Use of our images with alternative container runtimes
* Use of locally built versions of our images
* Docker Desktop on Windows, Mac, or Linux
* Rootless Docker
* Docker in Docker
* Docker Swarm
* EOL versions of Docker (where there is no option to upgrade)
* Podman (Rootless or Rootful)
* Routing container traffic through a VPN

## Unsupported

The following configurations are entirely unsupported and we will not provide help with them, even if you have been able to get them to work:

* Any of our images which have been deprecated or archived
* Any forks of our images maintained by 3rd parties
* Use of 3rd party guides or tutorials for configuring our images
* Use of 3rd party management tools, such as Portainer, to create or update containers
* Use of automated container update tools, such as Watchtower
* Use of remote file storage, such as SMB or NFS, for container `/config` mounts
* Use of LXC containers
* Use of k8s or k3s

## Unsupported and Known To Be Broken

The following configurations are entirely unsupported and you are unlikely to be able to get them to work at all, or experience serious issues if you do:

* Use of the `user` directive to run containers as a custom UID/GID
* Use of a custom `init` for Docker
* Overriding container entrypoints

## Change History

* 2023-10-03 - Initial release
