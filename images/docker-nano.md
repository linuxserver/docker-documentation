# [linuxserver/nano](https://github.com/linuxserver/docker-nano)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-nano.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-nano)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-nano.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-nano/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-nano/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-nano/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/nano)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/nano.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/nano "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/nano.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/nano)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/nano.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/nano)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-nano/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-nano/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/nano/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/nano/latest/index.html)

[Nano](https://nano.org/) is a digital payment protocol designed to be accessible and lightweight, with a focus on removing inefficiencies present in other cryptocurrencies. With ultrafast transactions and zero fees on a secure, green and decentralized network, this makes Nano ideal for everyday transactions.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/nano` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=nano \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e PEER_HOST=localhost `#optional` \
  -e LIVE_GENESIS_PUB=GENESIS_PUBLIC `#optional` \
  -e LIVE_GENESIS_ACCOUNT=nano_xxxxxx `#optional` \
  -e LIVE_GENESIS_WORK=WORK_FOR_BLOCK `#optional` \
  -e LIVE_GENESIS_SIG=BLOCK_SIGNATURE `#optional` \
  -e CLI_OPTIONS='--config node.receive_minimum = "1000000000000000000000000"' `#optional` \
  -e LMDB_BOOTSTRAP_URL=http://example.com/Nano_64_version_20.7z `#optional` \
  -p 7075:7075/udp \
  -p 7075:7075/tcp \
  -p 7076:3000 \
  -p 7077:3001 \
  -v /path/to/data:/config \
  --restart unless-stopped \
  linuxserver/nano
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  nano:
    image: linuxserver/nano
    container_name: nano
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - PEER_HOST=localhost #optional
      - LIVE_GENESIS_PUB=GENESIS_PUBLIC #optional
      - LIVE_GENESIS_ACCOUNT=nano_xxxxxx #optional
      - LIVE_GENESIS_WORK=WORK_FOR_BLOCK #optional
      - LIVE_GENESIS_SIG=BLOCK_SIGNATURE #optional
      - CLI_OPTIONS='--config node.receive_minimum = "1000000000000000000000000"' #optional
      - LMDB_BOOTSTRAP_URL=http://example.com/Nano_64_version_20.7z #optional
    volumes:
      - /path/to/data:/config
    ports:
      - 7075:7075/udp
      - 7075:7075/tcp
      - 7076:3000
      - 7077:3001
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `7075/udp` | Nano communication port UDP |
| `7075/tcp` | Nano communication port TCP |
| `3000` | RPC interface filtered through a proxy |
| `3001` | Https RPC interface filtered through a proxy |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `PEER_HOST=localhost` | Default peer host (can be overidden with an array by command line options) |
| `LIVE_GENESIS_PUB=GENESIS_PUBLIC` | Genesis block public key |
| `LIVE_GENESIS_ACCOUNT=nano_xxxxxx` | Genesis block account |
| `LIVE_GENESIS_WORK=WORK_FOR_BLOCK` | Genesis block proof of work |
| `LIVE_GENESIS_SIG=BLOCK_SIGNATURE` | Genesis block signature |
| `CLI_OPTIONS='--config node.receive_minimum = "1000000000000000000000000"'` | Node run command cli args |
| `LMDB_BOOTSTRAP_URL=http://example.com/Nano_64_version_20.7z` | HTTP/HTTPS endpoint to download a 7z file with the data.ldb to bootstrap to this node |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Database and Radarr configs |




## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

### Your Genesis account
By default this container will launch with a genesis block based on the private key `0000000000000000000000000000000000000000000000000000000000000000`, this should obviously only ever be used for testing purposes. Before you run your node you should use a script baked into this image to determine your private key and required environment variables: 

```
docker run --rm --entrypoint /genesis.sh linuxserver/nano
Generating Genesis block
!!!!!!! ACCOUNT INFO SAVE THIS INFORMATION IT WILL NOT BE SHOWN AGAIN !!!!!!!!
Private Key: CD4CD6B1E5523D4B5AEDD2B1E5A447C6C6797E729A531A95F9AD7937FC7CD9EA
Public Key:  2D057DF2EB09E918D3F95B5FCA69A5FD3EA406EF7D1810106324CD7A99FAA32D
Account:     nano_1da7hqsgp4hb55bzkptzsbntdzbyni5gyzar41a88b8fhcezoasfjkgmyk5y
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Container Environment Values:
 -e LIVE_GENESIS_PUB=2D057DF2EB09E918D3F95B5FCA69A5FD3EA406EF7D1810106324CD7A99FAA32D \
 -e LIVE_GENESIS_ACCOUNT=nano_1da7hqsgp4hb55bzkptzsbntdzbyni5gyzar41a88b8fhcezoasfjkgmyk5y \
 -e LIVE_GENESIS_WORK=7fd88e48684600b7 \
 -e LIVE_GENESIS_SIG=D1DF3A64BB43C131944401632215569A40AAE858ACF6CB59D5C77070E69DBF6435D93807877628A8B142DBF1AC4C562CD2F4CEBEB7D15486BDB7494A6146E007 \
```

These environment variables will be used for all of the peers in your payment network, but if you are running what you would consider a public or live network never share your private key even if you have drained the funds from that account it can be potentionally used to create valid forks.
**Even Better**, you should never even trust our Docker image for generating a private key and open block. Do it on an airgapped machine and keep it on a paper wallet.

### RPC Proxy settings
By default this container will enable RPC control and publish a custom service that acts as an RPC firewall giving you the ability to whitelist specific RPC calls and overide/add default values.

The default proxy config is stored in `/config/rpc-proxy.json`: 

```
{
  "port":3000,
  "httpsport":3001,
  "rpchost":"127.0.0.1",
  "rpcport":7076,
  "certfile":"/config/ssl/cert.crt",
  "keyfile":"/config/ssl/cert.key",
  "whitelist":[
    "account_info",
    "account_history",
    "block_info",
    "pending",
    "process"
  ],
  "overrides":{
    "account-history":{
      "count":"64"
    },
    "pending":{
      "count":"64"
    }
  }
}
```

This should be a minimal amount of RPC access needed to run a local light wallet against this endpoint. If you plan on having your network users only run clientside light wallets (local blake2b block generation and block `process` call publishing) you should publically publish this port for access for both port 7076 and 7077. For functional light wallets on Https endpoints we will generate a self signed cert/key combo but you should add the ones associated with your domain. This will allow yours and other https hosted light wallets to hit your RPC endpoint clientside from the users web browser.

Outside of potential https tunneling and actual object parsing (will remove duplicate keys) this is not a conventional API, it simply acts as a firewall and will send and return data just like a local RPC server would. The goal is to be compatible with any existing Nano software if the developers decide to add the ability to connect to alternative network endpoints. 

**Our Proxy has not been audited by any security team and is provided as is, though we make the best effort to keep it simple and secure**

### Node configuration via environment
Before you get started please review the configuration docs [here](https://docs.nano.org/running-a-node/configuration/)

We will pass the `CLI_OPTIONS` to the node, here is a run command example:

```
-e CLI_OPTIONS='--config node.preconfigured_peers=["peering.yourhost.com","peering.yourhost2.com"] \
                --config node.receive_minimum = "1000000000000000000000000"\
                --config node.enable_voting=true'
```

There are many options to know here to run an actual live node especially peering and voting, again please review the docs if you plan to run something outside of a local setup.

### Quickstart Guide
If you just want to see some numbers on a screen you can run a couple local nodes capable of having our light wallet pointed to. In this example we will be running the containers ephemerally and using a minimum two node setup. You can technically run with a single node, but in any network you should never publish the RPC port (even firewalled through our proxy) of the voting representative that has a wallet unlocked on disk. 

First run the principle node:

```
docker run --rm -it \
 -e CLI_OPTIONS='--config node.enable_voting=true' \
 -p 7075:7075/udp \
 -p 7075:7075/tcp \
 linuxserver/nano bash
```

Then run a local peer to connect up to it acting as an RPC proxy:

```
docker run --rm -it \
 -p 7076:3000 \
 -p 7077:3001 \
 -e PEER_HOST=REPLACE_WITH_LOCAL_IP \
 linuxserver/nano bash
```

Once both are up and running send some wallet RPC commands inside the voting principle node to unlock the Genesis wallet:

```
curl -d '{ "action": "wallet_create" }' localhost:7076
curl -d '{ "action": "wallet_add", "wallet": "REPLACE_WITH_WALLET_ID", "key": "0000000000000000000000000000000000000000000000000000000000000000" }' localhost:7076
```

You can now use the default private key `0000000000000000000000000000000000000000000000000000000000000000` in the web wallet to manage the genesis funds. By acessing the hosted live wallet http://wallet.linuxserver.io/?node=REPLACE_WITH_LOCAL_IP or run a simple nginx container located [here](https://github.com/linuxserver/docker-nano-wallet) to host a wallet locally.

By default you will be running an insecure centralized network with a single voting representative and a zero security private key using the commands above. To spinup a standard private or even public network you should read up on Nano's documentation [HERE](https://docs.nano.org/) and continue reading the network design section below. 

### Network design
There are 4 main concepts to grasp from a network standpoint as far as types of endpoints. Before we get started here is a basic network diagram:

![image](https://raw.githubusercontent.com/linuxserver/image-docs/master/img/nano-network.png)

#### Principle nodes and voting representatives
Principle nodes are network representatives with the ability to vote due to having a certain threshold of funds unlocked on that node or pointed to that unlocked address. These nodes should be as airgapped as possible while still being an active 24/7 peer of the network. From a tecnical perspective this is a node with an account private key that either has the funds it needs itself or enough users have pointed their accounts to it as a representative. In a live and secure configuration to protect the funds of this account you would use an inactive private key account with the funds in it and locally sign a change of representative block to point to the always online representative.

These nodes should never process external RPC calls even on a local network, the same rules go for any node with a local unlocked wallet.

Keep in mind the key to the security of the network is that 51% of the funds are pointed to trusted representatives that will generally not argue about chain forks. 

In most deployments the best bet is to heavily centralize your voting nodes, this is unless you are intentionally trying to build a distributed ledger and security model like the main Nano live net. Achieving that will be a long and difficult task.

#### Network peers

To a normal user simply transacting on the network using off the shelf tools like a web wallet and web based block explorers is generally all that is required. They get a number in a ledger somewhere and are able to locally sign and publish blocks using their private key using your published RPC endpoints.

For advanced users and just to generally make the network more robust, network operators should promote people running their own nodes. Using this image a network peer simply needs to run a docker run command with your pre-configured variables. IE given the generation example from above in the `Your Genesis account` section:

```
docker create \
  --name=nano \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e PEER_HOST=peering.mydomain.com \
  -e LIVE_GENESIS_PUB=2D057DF2EB09E918D3F95B5FCA69A5FD3EA406EF7D1810106324CD7A99FAA32D \
  -e LIVE_GENESIS_ACCOUNT=nano_1da7hqsgp4hb55bzkptzsbntdzbyni5gyzar41a88b8fhcezoasfjkgmyk5y \
  -e LIVE_GENESIS_WORK=7fd88e48684600b7 \
  -e LIVE_GENESIS_SIG=D1DF3A64BB43C131944401632215569A40AAE858ACF6CB59D5C77070E69DBF6435D93807877628A8B142DBF1AC4C562CD2F4CEBEB7D15486BDB7494A6146E007 \
  -p 7075:7075/udp \
  -p 7075:7075/tcp \
  -p 7076:3000 \
  -p 7077:3001 \
  -v /path/to/data:/config \
  --restart unless-stopped \
  linuxserver/nano
```

When the container spins up it will reach out to the node to bootstrap it's local ledger from peering.mydomain.com . This node once fully synced will be able to run local RPC commands to plug into a wallet and default Nano node wallet commands for automated pocketing of transactions etc. It will also get a list of other peers on the network from it's initial network peering and start participating in your distributed cryptocurrency network.

#### Public RPC endpoints
The key to users going to a webpage and managing the funds on your network is the ability to get blockchain information and publish new blocks to theirs. As mentioned earlier we bundle a basic firewall with a core set of RPC functions whitelisted that should be safe to expose publically. 

From a network design perspective these nodes should be purely what you would consider client peers and never have any wallets registered or private keys stored on them. Also for redundancy optmimally these peers should be run in a cluster behind a load balancer. For standard nodes you are building out a large P2P network, but in the case of the RPC endpoint and specifically the URL the end user is going to pass when accessing their wallet it is up to you to make that resilient.

#### Clientside javascript wallet
Currently we publish a pure javascript clientside wallet located here:  

https://github.com/linuxserver/nano-wallet

It is designed to be run 100% clientside in any web browser and use public RPC endpoints to hook into any network and conduct transactions by locally signing then publishing the result.
This can be hosted locally with any simple webserver and pointed to a locally run peer, but for full functionality we reccomend providing a public Https URL with these files along with plugging in legitamite SSL certificates into your RPC endpoints running on 7077.


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27nano%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=nano "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it nano /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f nano`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' nano`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/nano`

## Versions

* **17.05.20:** - Initial Release.
