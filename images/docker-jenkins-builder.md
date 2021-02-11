---
title: jenkins-builder
---
# linuxserver/jenkins-builder

Expects to run as part of the LSIO CI process. Not for public consumption.

**Running against remote: **
```
docker run --rm \
  -e CONTAINER_NAME=${CONTAINER_NAME} \
  -v ${TEMPDIR}:/ansible/jenkins \
  linuxserver/jenkins-builder:latest
```
**Running locally: **

If you need to test functionality just navigate to the folder with the jenkins-vars.yml and run:
```
docker run --rm \
  -v $(pwd):/tmp \
  -e LOCAL=true \
  -e PUID=$(id -u) -e PGID=$(id -g) \
  linuxserver/jenkins-builder:latest && \
rm -rf .jenkins-external
```
Newly generated files (including `README.md`, `Jenkinsfile`, issue templates, etc.) will overwrite the existing files in your current working directory.

The following line is only in this repo for loop testing:

- { date: "01.01.50:", desc: "I am the release message for this internal repo." }
