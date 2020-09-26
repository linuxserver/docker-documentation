# Building our images locally

On occasion you might wish to build our images locally. This might be for development purposes or to test out some customized logic of some sort.

## Standard x86 builds

If you want to make local modifications to these images for development purposes or just to customize the logic.

    git clone https://github.com/linuxserver/docker-heimdall.git
    cd docker-heimdall
    docker build \
    --no-cache \
    --pull \
    -t linuxserver/heimdall:latest .

## Building ARM variants on x86

The ARM variants can be built on x86_64 hardware using [multiarch/qemu-user-static](https://github.com/multiarch/qemu-user-static). `multiarch/qemu-user-static` enables the execution of different multi-architecture containers by QEMU.

    docker run --rm --privileged multiarch/qemu-user-static:register --reset

Once registered you can define the dockerfile to build thus:

    git clone https://github.com/linuxserver/docker-heimdall.git
    cd docker-heimdall
    docker build \
    --no-cache \
    --pull \
    -f Dockerfile.aarch64
    -t linuxserver/heimdall:latest .

Note that in the root of every LinuxServer containers repo are multiple Dockerfiles pertaining to the different architectures available.