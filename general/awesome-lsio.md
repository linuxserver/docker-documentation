# Awesome LSIO

## Administration

| Container | Description |
| --------- | ----------- |
| [doublecommander](https://github.com/linuxserver/docker-doublecommander/) | [Double Commander](https://doublecmd.sourceforge.io/) is a free cross platform open source file manager with two panels side by side. It is inspired by Total Commander and features some new ideas. |
| [endlessh](https://github.com/linuxserver/docker-endlessh/) | [endlessh](https://github.com/skeeto/endlessh) is an SSH tarpit that very slowly sends an endless, random SSH banner. It keeps SSH clients locked up for hours or even days at a time. The purpose is to put your real SSH server on another port and then let the script kiddies get stuck in this tarpit instead of bothering a real server. |
| [ldap-auth](https://github.com/linuxserver/docker-ldap-auth/) | [ldap-auth](https://github.com/nginxinc/nginx-ldap-auth) software is for authenticating users who request protected resources from servers proxied by nginx. It includes a daemon (ldap-auth) that communicates with an authentication server, and a webserver daemon that generates an authentication cookie based on the user’s credentials. The daemons are written in Python for use with a Lightweight Directory Access Protocol (LDAP) authentication server (OpenLDAP or Microsoft Windows Active Directory 2003 and 2012). |
| [netbootxyz](https://github.com/linuxserver/docker-netbootxyz/) | [netbootxyz](https://netboot.xyz) is a way to PXE boot various operating system installers or utilities from one place within the BIOS without the need of having to go retrieve the media to run the tool. iPXE is used to provide a user friendly menu from within the BIOS that lets you easily choose the operating system you want along with any specific types of versions or bootable flags. |
| [netbox](https://github.com/linuxserver/docker-netbox/) | [netbox](https://github.com/netbox-community/netbox) is an IP address management (IPAM) and data center infrastructure management (DCIM) tool. Initially conceived by the network engineering team at DigitalOcean, NetBox was developed specifically to address the needs of network and infrastructure engineers. It is intended to function as a domain-specific source of truth for network operations. |
| [openssh-server](https://github.com/linuxserver/docker-openssh-server/) | [openssh-server](https://www.openssh.com/) is a sandboxed environment that allows ssh access without giving keys to the entire server. |
| [snipe-it](https://github.com/linuxserver/docker-snipe-it/) | [snipe-it](https://github.com/snipe/snipe-it) makes asset management easy. It was built by people solving real-world IT and asset management problems, and a solid UX has always been a top priority. Straightforward design and bulk actions mean getting things done faster. |

## Audiobooks

| Container | Description |
| --------- | ----------- |
| [booksonic-air](https://github.com/linuxserver/docker-booksonic-air/) | [booksonic-air](http://booksonic.org) is a platform for accessing the audiobooks you own wherever you are. At the moment the platform consists of |

## Automation

| Container | Description |
| --------- | ----------- |
| [domoticz](https://github.com/linuxserver/docker-domoticz/) | [domoticz](https://www.domoticz.com) is a Home Automation System that lets you monitor and configure various devices like: Lights, Switches, various sensors/meters like Temperature, Rain, Wind, UV, Electra, Gas, Water and much more. Notifications/Alerts can be sent to any mobile device. |
| [habridge](https://github.com/linuxserver/docker-habridge/) | [habridge](http://bwssystems.com/#/habridge) emulates Philips Hue API to other home automation gateways such as an Amazon Echo/Dot Gen 1 (gen 2 has issues discovering ha-bridge) or other systems that support Philips Hue. The Bridge handles basic commands such as "On", "Off" and "brightness" commands of the hue protocol. This bridge can control most devices that have a distinct API. |
| [homeassistant](https://github.com/linuxserver/docker-homeassistant/) | [Home Assistant Core](https://www.home-assistant.io/) - Open source home automation that puts local control and privacy first. Powered by a worldwide community of tinkerers and DIY enthusiasts. Perfect to run on a Raspberry Pi or a local server.  |
| [kanzi](https://github.com/linuxserver/docker-kanzi/) | [kanzi](https://lexigr.am/), formerly titled Kodi-Alexa, this custom skill is the ultimate voice remote control for navigating Kodi. It can do anything you can think of (100+ intents).  This container also contains lexigram-cli to setup Kanzi with an Amazon Developer Account and automatically deploy it to Amazon. |

## Backup

| Container | Description |
| --------- | ----------- |
| [duplicati](https://github.com/linuxserver/docker-duplicati/) | [duplicati](https://www.duplicati.com/) works with standard protocols like FTP, SSH, WebDAV as well as popular services like Microsoft OneDrive, Amazon Cloud Drive & S3, Google Drive, box.com, Mega, hubiC and many others. |
| [resilio-sync](https://github.com/linuxserver/docker-resilio-sync/) | [resilio-sync](https://www.resilio.com/individuals/) (formerly BitTorrent Sync) uses the BitTorrent protocol to sync files and folders between all of your devices. There are both free and paid versions, this container supports both. There is an official sync image but we created this one as it supports user mapping to simplify permissions for volumes. |
| [rsnapshot](https://github.com/linuxserver/docker-rsnapshot/) | [rsnapshot](http://www.rsnapshot.org/) is a filesystem snapshot utility based on rsync. rsnapshot makes it easy to make periodic snapshots of local machines, and remote machines over ssh. The code makes extensive use of hard links whenever possible, to greatly reduce the disk space required." |
| [syncthing](https://github.com/linuxserver/docker-syncthing/) | [syncthing](https://syncthing.net) replaces proprietary sync and cloud services with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet. |

## Books

| Container | Description |
| --------- | ----------- |
| [calibre](https://github.com/linuxserver/docker-calibre/) | [calibre](https://calibre-ebook.com/) is a powerful and easy to use e-book manager. Users say it’s outstanding and a must-have. It’ll allow you to do nearly everything and it takes things a step beyond normal e-book software. It’s also completely free and open source and great for both casual users and computer experts. |
| [calibre-web](https://github.com/linuxserver/docker-calibre-web/) | [calibre-web](https://github.com/janeczku/calibre-web) is a web app providing a clean interface for browsing, reading and downloading eBooks using an existing Calibre database.   It is also possible to integrate google drive and edit metadata and your calibre library through the app itself. |
| [cops](https://github.com/linuxserver/docker-cops/) | [cops](http://blog.slucas.fr/en/oss/calibre-opds-php-server) by Sébastien Lucas, stands for Calibre OPDS (and HTML) Php Server. |
| [lazylibrarian](https://github.com/linuxserver/docker-lazylibrarian/) | [lazylibrarian](https://lazylibrarian.gitlab.io/) is a program to follow authors and grab metadata for all your digital reading needs. It uses a combination of Goodreads Librarything and optionally GoogleBooks as sources for author info and book info.  This container is based on the DobyTang fork. |
| [mylar3](https://github.com/linuxserver/docker-mylar3/) | [mylar3](https://github.com/mylar3/mylar3) is an automated Comic Book downloader (cbr/cbz) for use with NZB and torrents written in python. It supports SABnzbd, NZBGET, and many torrent clients in addition to DDL. |
| [readarr](https://github.com/linuxserver/docker-readarr/) | [readarr](https://github.com/Readarr/Readarr) - Book Manager and Automation (Sonarr for Ebooks) |
| [ubooquity](https://github.com/linuxserver/docker-ubooquity/) | [ubooquity](https://vaemendis.net/ubooquity/) is a free, lightweight and easy-to-use home server for your comics and ebooks. Use it to access your files from anywhere, with a tablet, an e-reader, a phone or a computer. |

## Cloud

| Container | Description |
| --------- | ----------- |
| [nextcloud](https://github.com/linuxserver/docker-nextcloud/) | [nextcloud](https://nextcloud.com/) gives you access to all your files wherever you are. |

## Crypto

| Container | Description |
| --------- | ----------- |
| [gmail-order-bot](https://github.com/linuxserver/docker-gmail-order-bot/) | [gmail-order-bot](https://developers.google.com/gmail/api) - A bot used to leverage a Gmail account as an order messaging service to consume email orders from [Nano Checkout](https://github.com/linuxserver/nano-checkout) and process them using any custom logic you choose. |
| [nano](https://github.com/linuxserver/docker-nano/) | [nano](https://nano.org/) is a digital payment protocol designed to be accessible and lightweight, with a focus on removing inefficiencies present in other cryptocurrencies. With ultrafast transactions and zero fees on a secure, green and decentralized network, this makes Nano ideal for everyday transactions. |
| [nano-discord-bot](https://github.com/linuxserver/docker-nano-discord-bot/) | [nano-discord-bot](https://discord.com/developers/docs/intro) - A bot used to hook into a [self hosted Nano RPC endpoint](https://hub.docker.com/r/linuxserver/nano) and discord server to Distribute funds from a faucet account. |
| [nano-wallet](https://github.com/linuxserver/docker-nano-wallet/) | [nano-wallet](https://nano.org/) is a digital payment protocol designed to be accessible and lightweight, with a focus on removing inefficiencies present in other cryptocurrencies. With ultrafast transactions and zero fees on a secure, green and decentralized network, this makes Nano ideal for everyday transactions. |

## DNS

| Container | Description |
| --------- | ----------- |
| [adguardhome-sync](https://github.com/linuxserver/docker-adguardhome-sync/) | [adguardhome-sync](https://github.com/bakito/adguardhome-sync/) is a tool to synchronize AdGuardHome config to replica instances. |
| [ddclient](https://github.com/linuxserver/docker-ddclient/) | [ddclient](https://github.com/ddclient/ddclient) is a Perl client used to update dynamic DNS entries for accounts on Dynamic DNS Network Service Provider. It was originally written by Paul Burry and is now mostly by wimpunk. It has the capability to update more than just dyndns and it can fetch your WAN-ipaddress in a few different ways. |
| [duckdns](https://github.com/linuxserver/docker-duckdns/) | [duckdns](https://duckdns.org/) is a free service which will point a DNS (sub domains of duckdns.org) to an IP of your choice. The service is completely free, and doesn't require reactivation or forum posts to maintain its existence. |

## Dashboard

| Container | Description |
| --------- | ----------- |
| [heimdall](https://github.com/linuxserver/docker-heimdall/) | [heimdall](https://heimdall.site) is a way to organise all those links to your most used web sites and web applications in a simple way. |

## Databases

| Container | Description |
| --------- | ----------- |
| [mariadb](https://github.com/linuxserver/docker-mariadb/) | [mariadb](https://mariadb.org/) is one of the most popular database servers. Made by the original developers of MySQL. |
| [mysql-workbench](https://github.com/linuxserver/docker-mysql-workbench/) | [MySQL Workbench](https://www.mysql.com/products/workbench/) is a unified visual tool for database architects, developers, and DBAs. MySQL Workbench provides data modeling, SQL development, and comprehensive administration tools for server configuration, user administration, backup, and much more. |
| [phpmyadmin](https://github.com/linuxserver/docker-phpmyadmin/) | [phpmyadmin](https://github.com/phpmyadmin/phpmyadmin/) is a free software tool written in PHP, intended to handle the administration of MySQL over the Web. phpMyAdmin supports a wide range of operations on MySQL and MariaDB. |
| [sqlitebrowser](https://github.com/linuxserver/docker-sqlitebrowser/) | [DB Browser for SQLite](https://sqlitebrowser.org/) is a high quality, visual, open source tool to create, design, and edit database files compatible with SQLite. |

## Docker

| Container | Description |
| --------- | ----------- |
| [docker-compose](https://github.com/linuxserver/docker-docker-compose/) | No description |
| [fleet](https://github.com/linuxserver/docker-fleet/) | [fleet](https://github.com/linuxserver/fleet) provides an online web interface which displays a set of maintained images from one or more owned repositories. |

## Documents

| Container | Description |
| --------- | ----------- |
| [libreoffice](https://github.com/linuxserver/docker-libreoffice/) | [LibreOffice](https://www.libreoffice.org/) is a free and powerful office suite, and a successor to OpenOffice.org (commonly known as OpenOffice). Its clean interface and feature-rich tools help you unleash your creativity and enhance your productivity. |
| [paperless-ng](https://github.com/linuxserver/docker-paperless-ng/) | [paperless-ng](https://github.com/jonaswinkler/paperless-ng) is an application by Daniel Quinn and contributors that indexes your scanned documents and allows you to easily search for documents and store metadata alongside your documents." |
| [paperless-ngx](https://github.com/linuxserver/docker-paperless-ngx/) | [paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) is an application by Daniel Quinn and contributors that indexes your scanned documents and allows you to easily search for documents and store metadata alongside your documents." |
| [papermerge](https://github.com/linuxserver/docker-papermerge/) | [papermerge](https://www.papermerge.com/) is an open source document management system (DMS) primarily designed for archiving and retrieving your digital documents. Instead of having piles of paper documents all over your desk, office or drawers - you can quickly scan them and configure your scanner to directly upload to Papermerge DMS." |

## Downloaders

| Container | Description |
| --------- | ----------- |
| [deluge](https://github.com/linuxserver/docker-deluge/) | [deluge](http://deluge-torrent.org/) is a lightweight, Free Software, cross-platform BitTorrent client. |
| [nntp2nntp](https://github.com/linuxserver/docker-nntp2nntp/) | [nntp2nntp](https://github.com/linuxserver/nntp2nntp) proxy allow you to use your NNTP Account from multiple systems, each with own user name and password. It fully supports SSL and you can also limit the access to proxy with SSL certificates. nntp2nntp proxy is very simple and pretty fast. |
| [nzbget](https://github.com/linuxserver/docker-nzbget/) | [nzbget](http://nzbget.net/) is a usenet downloader, written in C++ and designed with performance in mind to achieve maximum download speed by using very little system resources. |
| [pyload-ng](https://github.com/linuxserver/docker-pyload-ng/) | [pyLoad](https://pyload.net/) is a Free and Open Source download manager written in Python and designed to be extremely lightweight, easily extensible and fully manageable via web. |
| [qbittorrent](https://github.com/linuxserver/docker-qbittorrent/) | The [qbittorrent](https://www.qbittorrent.org/) project aims to provide an open-source software alternative to µTorrent. qBittorrent is based on the Qt toolkit and libtorrent-rasterbar library. |
| [sabnzbd](https://github.com/linuxserver/docker-sabnzbd/) | [sabnzbd](http://sabnzbd.org/) makes Usenet as simple and streamlined as possible by automating everything we can. All you have to do is add an .nzb. SABnzbd takes over from there, where it will be automatically downloaded, verified, repaired, extracted and filed away with zero human interaction. |
| [transmission](https://github.com/linuxserver/docker-transmission/) | [transmission](https://www.transmissionbt.com/) is designed for easy, powerful use. Transmission has the features you want from a BitTorrent client: encryption, a web interface, peer exchange, magnet links, DHT, µTP, UPnP and NAT-PMP port forwarding, webseed support, watch directories, tracker editing, global and per-torrent speed limits, and more. |

## FTP

| Container | Description |
| --------- | ----------- |
| [davos](https://github.com/linuxserver/docker-davos/) | [davos](https://github.com/linuxserver/davos) is an FTP automation tool that periodically scans given host locations for new files. It can be configured for various purposes, including listening for specific files to appear in the host location, ready for it to download and then move, if required. It also supports completion notifications as well as downstream API calls, to further the workflow. |
| [filezilla](https://github.com/linuxserver/docker-filezilla/) | [FIleZilla](https://filezilla-project.org/) Client is a fast and reliable cross-platform FTP, FTPS and SFTP client with lots of useful features and an intuitive graphical user interface. |

## Family

| Container | Description |
| --------- | ----------- |
| [babybuddy](https://github.com/linuxserver/docker-babybuddy/) | [babybuddy](https://github.com/babybuddy/babybuddy) is a buddy for babies! Helps caregivers track sleep, feedings, diaper changes, tummy time and more to learn about and predict baby's needs without (as much) guess work. |

## File Sharing

| Container | Description |
| --------- | ----------- |
| [projectsend](https://github.com/linuxserver/docker-projectsend/) | [projectsend](http://www.projectsend.org) is a self-hosted application that lets you upload files and assign them to specific clients that you create yourself. Secure, private and easy. No more depending on external services or e-mail to send those files. |
| [pwndrop](https://github.com/linuxserver/docker-pwndrop/) | [pwndrop](https://github.com/kgretzky/pwndrop) is a self-deployable file hosting service for sending out red teaming payloads or securely sharing your private files over HTTP and WebDAV. |
| [pydio-cells](https://github.com/linuxserver/docker-pydio-cells/) | [pydio-cells](https://pydio.com/) is the nextgen file sharing platform for organizations. It is a full rewrite of the Pydio project using the Go language following a micro-service architecture. |
| [snapdrop](https://github.com/linuxserver/docker-snapdrop/) | [snapdrop](https://github.com/RobinLinus/snapdrop) A local file sharing in your browser. Inspired by Apple's Airdrop. |
| [xbackbone](https://github.com/linuxserver/docker-xbackbone/) | [xbackbone](https://github.com/SergiX44/XBackBone) is a simple, self-hosted, lightweight PHP file manager that support the instant sharing tool ShareX and *NIX systems. It supports uploading and displaying images, GIF, video, code, formatted text, and file downloading and uploading. Also have a web UI with multi user management, past uploads history and search support. |

## Finance

| Container | Description |
| --------- | ----------- |
| [budge](https://github.com/linuxserver/docker-budge/) | [budge](https://github.com/linuxserver/budge) is an open source 'budgeting with envelopes' personal finance app. |

## Games

| Container | Description |
| --------- | ----------- |
| [emulatorjs](https://github.com/linuxserver/docker-emulatorjs/) | [emulatorjs](https://github.com/linuxserver/emulatorjs) - In browser web based emulation portable to nearly any device for many retro consoles. A mix of emulators is used between Libretro and EmulatorJS. |
| [minetest](https://github.com/linuxserver/docker-minetest/) | [minetest](http://www.minetest.net/) (server) is a near-infinite-world block sandbox game and a game engine, inspired by InfiniMiner, Minecraft, and the like. |

## Graphics

| Container | Description |
| --------- | ----------- |
| [blender](https://github.com/linuxserver/docker-blender/) | [Blender](https://www.blender.org/) is a free and open-source 3D computer graphics software toolset used for creating animated films, visual effects, art, 3D printed models, motion graphics, interactive 3D applications, virtual reality, and computer games. **This image does not support GPU rendering out of the box only accelerated workspace experience** |
| [kdenlive](https://github.com/linuxserver/docker-kdenlive/) | [Kdenlive](https://kdenlive.org/) is a powerful free and open source cross-platform video editing program made by the KDE community. Feature rich and production ready. |

## IRC

| Container | Description |
| --------- | ----------- |
| [limnoria](https://github.com/linuxserver/docker-limnoria/) | [limnoria](https://github.com/ProgVal/limnoria) A robust, full-featured, and user/programmer-friendly Python IRC bot, with many existing plugins. Successor of the well-known Supybot. |
| [ngircd](https://github.com/linuxserver/docker-ngircd/) | [ngircd](https://ngircd.barton.de/) is a free, portable and lightweight Internet Relay Chat server for small or private networks, developed under the GNU General Public License (GPL). It is easy to configure, can cope with dynamic IP addresses, and supports IPv6, SSL-protected connections as well as PAM for authentication. It is written from scratch and not based on the original IRCd. |
| [pidgin](https://github.com/linuxserver/docker-pidgin/) | [Pidgin](https://pidgin.im/) is a chat program which lets you log into accounts on multiple chat networks simultaneously. This means that you can be chatting with friends on XMPP and sitting in an IRC channel at the same time. |
| [quassel-core](https://github.com/linuxserver/docker-quassel-core/) | [quassel-core](http://quassel-irc.org/) is a modern, cross-platform, distributed IRC client, meaning that one (or multiple) client(s) can attach to and detach from a central core. |
| [quassel-web](https://github.com/linuxserver/docker-quassel-web/) | [quassel-web](https://github.com/magne4000/quassel-webserver) is a web client for Quassel.  Note that a Quassel-Core instance is required, we have a container available [here.](https://hub.docker.com/r/linuxserver/quassel-core/)  |
| [thelounge](https://github.com/linuxserver/docker-thelounge/) | [thelounge](https://thelounge.github.io/) (a fork of shoutIRC) is a web IRC client that you host on your own server. |
| [znc](https://github.com/linuxserver/docker-znc/) | [znc](http://wiki.znc.in/ZNC) is an IRC network bouncer or BNC. It can detach the client from the actual IRC server, and also from selected channels. Multiple clients from different locations can connect to a single ZNC account simultaneously and therefore appear under the same nickname on IRC. |

## Indexers

| Container | Description |
| --------- | ----------- |
| [jackett](https://github.com/linuxserver/docker-jackett/) | [jackett](https://github.com/Jackett/Jackett) works as a proxy server: it translates queries from apps (Sonarr, SickRage, CouchPotato, Mylar, etc) into tracker-site-specific http queries, parses the html response, then sends results back to the requesting software. This allows for getting recent uploads (like RSS) and performing searches. Jackett is a single repository of maintained indexer scraping & translation logic - removing the burden from other apps. |
| [nzbhydra2](https://github.com/linuxserver/docker-nzbhydra2/) | [nzbhydra2](https://github.com/theotherp/nzbhydra2) is a meta search application for NZB indexers, the "spiritual successor" to NZBmegasearcH, and an evolution of the original application [NZBHydra](https://github.com/theotherp/nzbhydra). |
| [prowlarr](https://github.com/linuxserver/docker-prowlarr/) | [prowlarr](https://github.com/Prowlarr/Prowlarr) is a indexer manager/proxy built on the popular arr .net/reactjs base stack to integrate with your various PVR apps. Prowlarr supports both Torrent Trackers and Usenet Indexers. It integrates seamlessly with Sonarr, Radarr, Lidarr, and Readarr offering complete management of your indexers with no per app Indexer setup required (we do it all). |

## Media Management

| Container | Description |
| --------- | ----------- |
| [bazarr](https://github.com/linuxserver/docker-bazarr/) | [bazarr](https://www.bazarr.media/) is a companion application to Sonarr and Radarr. It can manage and download subtitles based on your requirements. You define your preferences by TV show or movie and Bazarr takes care of everything for you. |
| [medusa](https://github.com/linuxserver/docker-medusa/) | [medusa](https://pymedusa.com/) is an automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic. |
| [plex-meta-manager](https://github.com/linuxserver/docker-plex-meta-manager/) | [plex-meta-manager](https://github.com/meisnate12/Plex-Meta-Manager) is a Python 3 script that can be continuously run using YAML configuration files to update on a schedule the metadata of the movies, shows, and collections in your libraries as well as automatically build collections based on various methods all detailed in the wiki. |
| [radarr](https://github.com/linuxserver/docker-radarr/) | [radarr](https://github.com/Radarr/Radarr) - A fork of Sonarr to work with movies à la Couchpotato. |
| [sickchill](https://github.com/linuxserver/docker-sickchill/) | [sickchill](https://github.com/SickChill/SickChill) is an Automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.  |
| [sickgear](https://github.com/linuxserver/docker-sickgear/) | [SickGear](https://github.com/sickgear/sickgear) provides management of TV shows and/or Anime, it detects new episodes, links downloader apps, and more.. |
| [sonarr](https://github.com/linuxserver/docker-sonarr/) | [sonarr](https://sonarr.tv/) (formerly NZBdrone) is a PVR for usenet and bittorrent users. It can monitor multiple RSS feeds for new episodes of your favorite shows and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available. |

## Media Players

| Container | Description |
| --------- | ----------- |
| [emby](https://github.com/linuxserver/docker-emby/) | [emby](https://emby.media/) organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server. |
| [jellyfin](https://github.com/linuxserver/docker-jellyfin/) | [jellyfin](https://jellyfin.github.io/) is a Free Software Media System that puts you in control of managing and streaming your media. It is an alternative to the proprietary Emby and Plex, to provide media from a dedicated server to end-user devices via multiple apps. Jellyfin is descended from Emby's 3.5.2 release and ported to the .NET Core framework to enable full cross-platform support. There are no strings attached, no premium licenses or features, and no hidden agendas: just a team who want to build something better and work together to achieve it. |
| [plex](https://github.com/linuxserver/docker-plex/) | [plex](https://plex.tv) organizes video, music and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone Plex Media Server. has always been a top priority. Straightforward design and bulk actions mean getting things done faster. |

## Media Requesters

| Container | Description |
| --------- | ----------- |
| [doplarr](https://github.com/linuxserver/docker-doplarr/) | [doplarr](https://github.com/kiranshila/Doplarr) is an *arr request bot for Discord." |
| [ombi](https://github.com/linuxserver/docker-ombi/) | [ombi](https://ombi.io) allows you to host your own Plex Request and user management system. |
| [overseerr](https://github.com/linuxserver/docker-overseerr/) | [overseerr](https://overseerr.dev/) is a request management and media discovery tool built to work with your existing Plex ecosystem. |

## Media Tools

| Container | Description |
| --------- | ----------- |
| [embystat](https://github.com/linuxserver/docker-embystat/) | [embystat](https://github.com/mregni/EmbyStat) is a personal web server that can calculate all kinds of statistics from your (local) Emby server. Just install this on your server and let him calculate all kinds of fun stuff. |
| [ffmpeg](https://github.com/linuxserver/docker-ffmpeg/) | No description |
| [htpcmanager](https://github.com/linuxserver/docker-htpcmanager/) | [htpcmanager](https://github.com/HTPC-Manager/HTPC-Manager) is a front end for many htpc related applications. |
| [minisatip](https://github.com/linuxserver/docker-minisatip/) | [minisatip](https://github.com/catalinii/minisatip) is a multi-threaded satip server version 1.2 that runs under Linux and it was tested with DVB-S, DVB-S2, DVB-T, DVB-T2, DVB-C, DVB-C2, ATSC and ISDB-T cards. |
| [oscam](https://github.com/linuxserver/docker-oscam/) | [oscam](http://www.streamboard.tv/oscam/) is an Open Source Conditional Access Module software used for descrambling DVB transmissions using smart cards. It's both a server and a client. |
| [synclounge](https://github.com/linuxserver/docker-synclounge/) | [synclounge](https://github.com/samcm/synclounge) is a third party tool that allows you to watch Plex in sync with your friends/family, wherever you are. |
| [tautulli](https://github.com/linuxserver/docker-tautulli/) | [tautulli](http://tautulli.com) is a python based web application for monitoring, analytics and notifications for Plex Media Server. |
| [tvheadend](https://github.com/linuxserver/docker-tvheadend/) | [tvheadend](https://www.tvheadend.org/) works as a proxy server: is a TV streaming server and recorder for Linux, FreeBSD and Android supporting DVB-S, DVB-S2, DVB-C, DVB-T, ATSC, ISDB-T, IPTV, SAT>IP and HDHomeRun as input sources. |
| [webgrabplus](https://github.com/linuxserver/docker-webgrabplus/) | [webgrabplus](http://www.webgrabplus.com) is a multi-site incremental xmltv epg grabber. It collects tv-program guide data from selected tvguide sites for your favourite channels. |

## Monitor

| Container | Description |
| --------- | ----------- |
| [apprise-api](https://github.com/linuxserver/docker-apprise-api/) | [apprise-api](https://github.com/caronc/apprise-api) Takes advantage of [Apprise](https://github.com/caronc/apprise) through your network with a user-friendly API. |
| [healthchecks](https://github.com/linuxserver/docker-healthchecks/) | [healthchecks](https://github.com/healthchecks/healthchecks) is a watchdog for your cron jobs. It's a web server that listens for pings from your cron jobs, plus a web interface. |
| [librespeed](https://github.com/linuxserver/docker-librespeed/) | [librespeed](https://github.com/librespeed/speedtest) is a very lightweight Speedtest implemented in Javascript, using XMLHttpRequest and Web Workers. |
| [smokeping](https://github.com/linuxserver/docker-smokeping/) | [smokeping](https://oss.oetiker.ch/smokeping/) keeps track of your network latency. For a full example of what this application is capable of visit [UCDavis](http://smokeping.ucdavis.edu/cgi-bin/smokeping.fcgi). |
| [syslog-ng](https://github.com/linuxserver/docker-syslog-ng/) | [syslog-ng](https://www.syslog-ng.com/products/open-source-log-management/) allows you to flexibly collect, parse, classify, rewrite and correlate logs from across your infrastructure and store or route them to log analysis tools. |

## Music

| Container | Description |
| --------- | ----------- |
| [airsonic-advanced](https://github.com/linuxserver/docker-airsonic-advanced/) | [airsonic-advanced](https://github.com/airsonic-advanced/airsonic-advanced) is a free, web-based media streamer, providing ubiquitious access to your music. Use it to share your music with friends, or to listen to your own music while at work. You can stream to multiple players simultaneously, for instance to one player in your kitchen and another in your living room. |
| [audacity](https://github.com/linuxserver/docker-audacity/) | [Audacity](https://www.audacityteam.org/) is an easy-to-use, multi-track audio editor and recorder. Developed by a group of volunteers as open source. |
| [beets](https://github.com/linuxserver/docker-beets/) | [beets](http://beets.io/) is a music library manager and not, for the most part, a music player. It does include a simple player plugin and an experimental Web-based player, but it generally leaves actual sound-reproduction to specialized tools. |
| [daapd](https://github.com/linuxserver/docker-daapd/) | [daapd](https://owntone.github.io/owntone-server/) (iTunes) media server with support for AirPlay devices, Apple Remote (and compatibles), Chromecast, MPD and internet radio. |
| [headphones](https://github.com/linuxserver/docker-headphones/) | [headphones](https://github.com/rembo10/headphones) is an automated music downloader for NZB and Torrent, written in Python. It supports SABnzbd, NZBget, Transmission, µTorrent and Blackhole. |
| [lidarr](https://github.com/linuxserver/docker-lidarr/) | [lidarr](https://github.com/lidarr/Lidarr) is a music collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new tracks from your favorite artists and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available. |
| [mstream](https://github.com/linuxserver/docker-mstream/) | [mstream](https://mstream.io/) is a personal music streaming server. You can use mStream to stream your music from your home computer to any device, anywhere.  There are mobile apps available for both Android and iPhone. |

## Network

| Container | Description |
| --------- | ----------- |
| [unifi-controller](https://github.com/linuxserver/docker-unifi-controller/) | The [unifi-controller](https://www.ubnt.com/enterprise/#unifi) software is a powerful, enterprise wireless software engine ideal for high-density client deployments requiring low latency and high uptime performance. |
| [wireshark](https://github.com/linuxserver/docker-wireshark/) | [Wireshark](https://www.wireshark.org/) is the world’s foremost and widely-used network protocol analyzer. It lets you see what’s happening on your network at a microscopic level and is the de facto (and often de jure) standard across many commercial and non-profit enterprises, government agencies, and educational institutions. Wireshark development thrives thanks to the volunteer contributions of networking experts around the globe and is the continuation of a project started by Gerald Combs in 1998.  |

## Photos

| Container | Description |
| --------- | ----------- |
| [chevereto](https://github.com/linuxserver/docker-chevereto/) | [chevereto](https://github.com/rodber/chevereto-free) is an image hosting software that allows you to create a beautiful and full-featured image hosting website on your own server. It's your hosting and your rules, so say goodbye to closures and restrictions. |
| [darktable](https://github.com/linuxserver/docker-darktable/) | [darktable](https://www.darktable.org/) is an open source photography workflow application and raw developer. A virtual lighttable and darkroom for photographers. It manages your digital negatives in a database, lets you view them through a zoomable lighttable and enables you to develop raw images and enhance them. |
| [digikam](https://github.com/linuxserver/docker-digikam/) | [digiKam](https://www.digikam.org/): Professional Photo Management with the Power of Open Source |
| [lychee](https://github.com/linuxserver/docker-lychee/) | [lychee](https://lycheeorg.github.io/) is a free photo-management tool, which runs on your server or web-space. Installing is a matter of seconds. Upload, manage and share photos like from a native application. Lychee comes with everything you need and all your photos are stored securely." |
| [photoshow](https://github.com/linuxserver/docker-photoshow/) | [photoshow](https://github.com/thibaud-rohmer/PhotoShow) is gallery software at its easiest, it doesn't even require a database. |
| [piwigo](https://github.com/linuxserver/docker-piwigo/) | [piwigo](http://piwigo.org/) is a photo gallery software for the web that comes with powerful features to publish and manage your collection of pictures. |
| [pixapop](https://github.com/linuxserver/docker-pixapop/) | [pixapop](https://github.com/bierdok/pixapop) is an open-source single page application to view your photos in the easiest way possible. |

## Programming

| Container | Description |
| --------- | ----------- |
| [cloud9](https://github.com/linuxserver/docker-cloud9/) | [cloud9](https://github.com/c9/core) Cloud9 is a complete web based IDE with terminal access. This container is for running their core SDK locally and developing plugins. |
| [code-server](https://github.com/linuxserver/docker-code-server/) | [code-server](https://coder.com) is VS Code running on a remote server, accessible through the browser. |
| [openvscode-server](https://github.com/linuxserver/docker-openvscode-server/) | [openvscode-server](https://github.com/gitpod-io/openvscode-server) provides a version of VS Code that runs a server on a remote machine and allows access through a modern web browser. |
| [pylon](https://github.com/linuxserver/docker-pylon/) | [pylon](https://github.com/pylonide/pylon) is a web based integrated development environment built with Node.js as a backend and with a supercharged JavaScript/HTML5 frontend, licensed under GPL version 3. This project originates from Cloud9 v2 project. |

## RSS

| Container | Description |
| --------- | ----------- |
| [freshrss](https://github.com/linuxserver/docker-freshrss/) | [freshrss](https://freshrss.org/) is a free, self-hostable aggregator for rss feeds. |

## Recipes

| Container | Description |
| --------- | ----------- |
| [grocy](https://github.com/linuxserver/docker-grocy/) | [grocy](https://github.com/grocy/grocy) is an ERP system for your kitchen! Cut down on food waste, and manage your chores with this brilliant utility. |

## Remote

| Container | Description |
| --------- | ----------- |
| [guacd](https://github.com/linuxserver/docker-guacd/) | [guacd](https://guacamole.apache.org/) - Apache Guacamole is a clientless remote desktop gateway. It supports standard protocols like VNC, RDP, and SSH. This container is only the backend server component needed to use The official or 3rd party HTML5 frontends. |
| [rdesktop](https://github.com/linuxserver/docker-rdesktop/) | [rdesktop](http://xrdp.org/) - Containers containing full desktop environments in many popular flavors for Alpine, Ubuntu, Arch, and Fedora accessible via RDP. |
| [remmina](https://github.com/linuxserver/docker-remmina/) | [Remmina](https://remmina.org/) is a remote desktop client written in GTK, aiming to be useful for system administrators and travellers, who need to work with lots of remote computers in front of either large or tiny screens. Remmina supports multiple network protocols, in an integrated and consistent user interface. Currently RDP, VNC, SPICE, NX, XDMCP, SSH and EXEC are supported. |
| [webtop](https://github.com/linuxserver/docker-webtop/) | [webtop](https://github.com/linuxserver/gclient) - Alpine, Ubuntu, Fedora, and Arch based containers containing full desktop environments in officially supported flavors accessible via any modern web browser. |

## Science

| Container | Description |
| --------- | ----------- |
| [boinc](https://github.com/linuxserver/docker-boinc/) | [BOINC](https://boinc.berkeley.edu/) is a platform for high-throughput computing on a large scale (thousands or millions of computers). It can be used for volunteer computing (using consumer devices) or grid computing (using organizational resources). It supports virtualized, parallel, and GPU-based applications. |
| [foldingathome](https://github.com/linuxserver/docker-foldingathome/) | [Folding@home](https://foldingathome.org/) is a distributed computing project for simulating protein dynamics, including the process of protein folding and the movements of proteins implicated in a variety of diseases. It brings together citizen scientists who volunteer to run simulations of protein dynamics on their personal computers. Insights from this data are helping scientists to better understand biology, and providing new opportunities for developing therapeutics. |

## Storage

| Container | Description |
| --------- | ----------- |
| [diskover](https://github.com/linuxserver/docker-diskover/) | [diskover](https://github.com/diskoverdata/diskover-community) is an open source file system indexer that uses Elasticsearch to index and manage data across heterogeneous storage systems. |
| [qdirstat](https://github.com/linuxserver/docker-qdirstat/) | [QDirStat](https://github.com/shundhammer/qdirstat) Qt-based directory statistics: KDirStat without any KDE -- from the author of the original KDirStat. |
| [scrutiny](https://github.com/linuxserver/docker-scrutiny/) | [scrutiny](https://github.com/AnalogJ/scrutiny) WebUI for smartd S.M.A.R.T monitoring. Scrutiny is a Hard Drive Health Dashboard & Monitoring solution, merging manufacturer provided S.M.A.R.T metrics with real-world failure rates from Backblaze. |

## Tools

| Container | Description |
| --------- | ----------- |
| [yq](https://github.com/linuxserver/docker-yq/) | No description |

## VPN

| Container | Description |
| --------- | ----------- |
| [wireguard](https://github.com/linuxserver/docker-wireguard/) | [WireGuard®](https://www.wireguard.com/) is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPsec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable. It is currently under heavy development, but already it might be regarded as the most secure, easiest to use, and simplest VPN solution in the industry. |

## Web

| Container | Description |
| --------- | ----------- |
| [firefox](https://github.com/linuxserver/docker-firefox/) | [Firefox](https://www.mozilla.org/en-US/firefox/) Browser, also known as Mozilla Firefox or simply Firefox, is a free and open-source web browser developed by the Mozilla Foundation and its subsidiary, the Mozilla Corporation. Firefox uses the Gecko layout engine to render web pages, which implements current and anticipated web standards. |
| [grav](https://github.com/linuxserver/docker-grav/) | [grav](https://github.com/getgrav/grav/) is a Fast, Simple, and Flexible, file-based Web-platform. |
| [nginx](https://github.com/linuxserver/docker-nginx/) | [nginx](https://nginx.org/) is a simple webserver with php support. The config files reside in `/config` for easy user customization. |
| [swag](https://github.com/linuxserver/docker-swag/) | SWAG - Secure Web Application Gateway (formerly known as letsencrypt, no relation to Let's Encrypt™) sets up an Nginx webserver and reverse proxy with php support and a built-in certbot client that automates free SSL server certificate generation and renewal processes (Let's Encrypt and ZeroSSL). It also contains fail2ban for intrusion prevention. |

## Wiki

| Container | Description |
| --------- | ----------- |
| [bookstack](https://github.com/linuxserver/docker-bookstack/) | [bookstack](https://github.com/BookStackApp/BookStack) is a free and open source Wiki designed for creating beautiful documentation. Featuring a simple, but powerful WYSIWYG editor it allows for teams to create detailed and useful documentation with ease. |
| [dillinger](https://github.com/linuxserver/docker-dillinger/) | [dillinger](https://github.com/joemccann/dillinger) is a cloud-enabled, mobile-ready, offline-storage, AngularJS powered HTML5 Markdown editor. |
| [dokuwiki](https://github.com/linuxserver/docker-dokuwiki/) | [dokuwiki](https://www.dokuwiki.org/dokuwiki/) is a simple to use and highly versatile Open Source wiki software that doesn't require a database. It is loved by users for its clean and readable syntax. The ease of maintenance, backup and integration makes it an administrator's favorite. Built in access controls and authentication connectors make DokuWiki especially useful in the enterprise context and the large number of plugins contributed by its vibrant community allow for a broad range of use cases beyond a traditional wiki. |
| [hedgedoc](https://github.com/linuxserver/docker-hedgedoc/) | [HedgeDoc](https://hedgedoc.org/) gives you access to all your files wherever you are. |
| [raneto](https://github.com/linuxserver/docker-raneto/) | [raneto](http://raneto.com/) - is an open source Knowledgebase platform that uses static Markdown files to power your Knowledgebase. |
| [wikijs](https://github.com/linuxserver/docker-wikijs/) | [wikijs](https://github.com/Requarks/wiki) A modern, lightweight and powerful wiki app built on NodeJS. |
