# Docker Containers: 101

A container bundles all the libraries required by an application to run, you no longer need to know which version of Java, Apache or whatever – the person who built the container for you took care of that. Containers don’t usually ship with configuration files baked in though. This is because the contents of a container are ‘stateless’ or ‘immutable’. In English, this means the state or filesystem of the container itself cannot be modified after it is created.

## What do I need to know?

To get started, not much. You will need to know about some of the terminology or concepts when performing more advanced tasks or troubleshooting but getting started couldn't be much simpler.

```shell
docker run hello-world
```

That's it, your first docker container. It pre-supposes you have [docker installed](https://github.com/IronicBadger/til/blob/master/docker/yum-apt-repos-docker.md) but that's all it takes to run a container. You didn't need to know anything about installed what that app needed to run - this is the key benefit. `hello-world` is a simple example but imagine you have a complex application with a large number of dependencies and it is tied to a specific version of Python or Java. Then imagine you have a second app again tied to a specific, but different, version of Java or Python. Now you have to try and ensure these two \(often conflicting\) versions sit on the same host and play nice. In the world of containers these two versions can operate in complete isolation from one another. Bliss.

## Key Terminology

There are a few terms you might find useful to understand when working with containers:

* **docker** - the first, and most popular, container runtime - it sits as an abstraction layer between the kernels features such as cgroups or namespaces and running applications
* **container** - a sandboxed process isolated in memory and running instance of an image
* **image** - a pre-built filesystem in a format ready to be understood by a container runtime \(usually docker\)
* **volume** - use volumes to persist data outside of the containers sandboxed filesystem
* **environment** - a way of configuring the sandboxed environment your container runs in

## Key Concepts

Containers are completely sandboxed environments by the Linux kernel. It may help you to think of them _somewhat_ like a small VM however in practice this is largely false. The Linux kernel controls access to various system resources utilising control groups \(cgroups\). We rely on docker to translate these complex concepts into simple ones that users can understand and consume.

By default a running container has absolutely no context of the world around it. Out the box you cannot connect from the outside world to the running webservers on ports 80 and 443 below. To allow entry to the sandbox from the outside world we must explicitly allow entry using the `-p` flag.

```shell
docker run -d --name=letsencrypt -p 80:80 -p 443:443 linuxserver/letsencrypt
```

Take this concept and multiply it across all aspects of a running application. Ports, volumes \(i.e. the files you want to be available inside the container from outside the container\), environment variables and so on. For us as developers this allows us to isolate your system from troubleshooting as the box the container is running in \(the container\) is identical to the next.

Containers are an amazing way to run applications in a secure, sandboxed way.
