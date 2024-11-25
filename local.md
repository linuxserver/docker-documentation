# Local development

To speed up the build, you should consider commenting out the `git-revision-date-localized` and `minify` plugin in mkdocs.yml

## Build image

```shell
docker build -t lsio/documentation -f Dockerfile .
```

## Run image

With docs from buildtime

```shell
docker run --rm --name=docs -p 8000:8000 lsio/documentation
```

With docs from runtime

```shell
docker run --rm --name=docs -p 8000:8000 -v $PWD:/app/mkdocs lsio/documentation
```

With watching at runtime

```shell
docker run --rm --name=docs -p 8000:8000 -v $PWD:/app/mkdocs lsio/documentation -a 0.0.0.0:8000 --dirty
```

With custom port

```shell
docker run --rm --name=docs -p 9999:9999 lsio/documentation -a 0.0.0.0:9999
```
