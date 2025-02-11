# syntax=docker/dockerfile:1

FROM ghcr.io/linuxserver/d2-builder:latest AS d2

FROM ghcr.io/linuxserver/baseimage-alpine:edge

# set version label
ARG BUILD_DATE
ARG VERSION
ARG D2_VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="roxedus"

RUN \
  echo "**** install packages ****" && \
  apk add --no-cache \
    git \
    python3 && \
  mkdir -p /app/mkdocs/docs && \
  git config --global --add safe.directory /app/mkdocs && \
  python3 -m venv /lsiopy && \
  pip install -U --no-cache-dir \
    pip \
    wheel

COPY --from=d2 /usr/local/bin/d2 /usr/local/bin

COPY docs/requirements.txt /app/mkdocs/docs/requirements.txt

RUN \
  pip install -U --no-cache-dir \
    -r /app/mkdocs/docs/requirements.txt

COPY . /app/mkdocs/

WORKDIR /app/mkdocs

ENTRYPOINT ["catatonit", "--", "mkdocs", "serve"]

CMD [ "-a", "0.0.0.0:8000" ]
