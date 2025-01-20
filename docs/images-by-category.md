# Images by Category

## 3D Modeling

| Container | Description |
| --------- | ----------- |
| [blender](https://github.com/linuxserver/docker-blender/) | [Blender](https://www.blender.org/) is a free and open-source 3D computer graphics software toolset used for creating animated films, visual effects, art, 3D printed models, motion graphics, interactive 3D applications, virtual reality, and computer games. **This image does not support GPU rendering out of the box only accelerated workspace experience** |
| [freecad](https://github.com/linuxserver/docker-freecad/) | [FreeCAD](https://www.freecad.org/) is a general-purpose parametric 3D computer-aided design (CAD) modeler and a building information modeling (BIM) software application with finite element method (FEM) support. |
| [inkscape](https://github.com/linuxserver/docker-inkscape/) | [Inkscape](https://inkscape.org/) is professional quality vector graphics software which runs on Linux, Mac OS X and Windows desktop computers. |
| [kicad](https://github.com/linuxserver/docker-kicad/) | [KiCad](https://www.kicad.org/) - A Cross Platform and Open Source Electronics Design Automation Suite. |

## 3D Printing

| Container | Description |
| --------- | ----------- |
| [bambustudio](https://github.com/linuxserver/docker-bambustudio/) | [Bambu Studio](https://bambulab.com/en/download/studio) Bambu Studio is an open-source, cutting-edge, feature-rich slicing software. It contains project-based workflows, systematically optimized slicing algorithms, and an easy-to-use graphical interface, bringing users an incredibly smooth printing experience. |
| [cura](https://github.com/linuxserver/docker-cura/) | [UltiMaker Cura](https://ultimaker.com/software/ultimaker-cura/) is free, easy-to-use 3D printing software trusted by millions of users. Fine-tune your 3D model with 400+ settings for the best slicing and printing results. |
| [manyfold](https://github.com/linuxserver/docker-manyfold/) | [manyfold](https://github.com/manyfold3d/manyfold/)  is an open source, self-hosted web application for managing a collection of 3D models, particularly focused on 3D printing. |
| [orcaslicer](https://github.com/linuxserver/docker-orcaslicer/) | [Orca Slicer](https://github.com/SoftFever/OrcaSlicer) is an open source slicer for FDM printers. OrcaSlicer is fork of Bambu Studio, it was previously known as BambuStudio-SoftFever, Bambu Studio is forked from PrusaSlicer by Prusa Research, which is from Slic3r by Alessandro Ranellucci and the RepRap community |

## Administration

| Container | Description |
| --------- | ----------- |
| [doublecommander](https://github.com/linuxserver/docker-doublecommander/) | [Double Commander](https://doublecmd.sourceforge.io/) is a free cross platform open source file manager with two panels side by side. It is inspired by Total Commander and features some new ideas. |
| [hishtory-server](https://github.com/linuxserver/docker-hishtory-server/) | [hiSHtory](https://github.com/ddworken/hishtory) is a better shell history. It stores your shell history in context (what directory you ran the command in, whether it succeeded or failed, how long it took, etc). This is all stored locally and end-to-end encrypted for syncing to to all your other computers. |
| [ldap-auth](https://github.com/linuxserver/docker-ldap-auth/) | [ldap-auth](https://github.com/nginxinc/nginx-ldap-auth) software is for authenticating users who request protected resources from servers proxied by nginx. It includes a daemon (ldap-auth) that communicates with an authentication server, and a webserver daemon that generates an authentication cookie based on the user’s credentials. The daemons are written in Python for use with a Lightweight Directory Access Protocol (LDAP) authentication server (OpenLDAP or Microsoft Windows Active Directory 2003 and 2012). |
| [netbootxyz](https://github.com/linuxserver/docker-netbootxyz/) | [netbootxyz](https://netboot.xyz) is a way to PXE boot various operating system installers or utilities from one place within the BIOS without the need of having to go retrieve the media to run the tool. iPXE is used to provide a user friendly menu from within the BIOS that lets you easily choose the operating system you want along with any specific types of versions or bootable flags. |
| [netbox](https://github.com/linuxserver/docker-netbox/) | [netbox](https://github.com/netbox-community/netbox) is an IP address management (IPAM) and data center infrastructure management (DCIM) tool. Initially conceived by the network engineering team at DigitalOcean, NetBox was developed specifically to address the needs of network and infrastructure engineers. It is intended to function as a domain-specific source of truth for network operations. |
| [openssh-server](https://github.com/linuxserver/docker-openssh-server/) | [openssh-server](https://www.openssh.com/) is a sandboxed environment that allows ssh access without giving keys to the entire server. |
| [snipe-it](https://github.com/linuxserver/docker-snipe-it/) | [snipe-it](https://github.com/snipe/snipe-it) makes asset management easy. It was built by people solving real-world IT and asset management problems, and a solid UX has always been a top priority. Straightforward design and bulk actions mean getting things done faster. |

## Audio Processing

| Container | Description |
| --------- | ----------- |
| [ardour](https://github.com/linuxserver/docker-ardour/) | [Ardour](https://ardour.org/) is an open source, collaborative effort of a worldwide team including musicians, programmers, and professional recording engineers. |
| [audacity](https://github.com/linuxserver/docker-audacity/) | [Audacity](https://www.audacityteam.org/) is an easy-to-use, multi-track audio editor and recorder. Developed by a group of volunteers as open source. |

## Audiobooks

| Container | Description |
| --------- | ----------- |
| [emby](https://github.com/linuxserver/docker-emby/) | [emby](https://emby.media/) organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server. |
| [jellyfin](https://github.com/linuxserver/docker-jellyfin/) | [jellyfin](https://github.com/jellyfin/jellyfin) is a Free Software Media System that puts you in control of managing and streaming your media. It is an alternative to the proprietary Emby and Plex, to provide media from a dedicated server to end-user devices via multiple apps. Jellyfin is descended from Emby's 3.5.2 release and ported to the .NET Core framework to enable full cross-platform support. There are no strings attached, no premium licenses or features, and no hidden agendas: just a team who want to build something better and work together to achieve it. |
| [plex](https://github.com/linuxserver/docker-plex/) | [plex](https://plex.tv) organizes video, music and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone Plex Media Server. Straightforward design and bulk actions mean getting things done faster. |

## Backup

| Container | Description |
| --------- | ----------- |
| [duplicati](https://github.com/linuxserver/docker-duplicati/) | [duplicati](https://www.duplicati.com/) is a backup client that securely stores encrypted, incremental, compressed backups on local storage, cloud storage services and remote file servers. It works with standard protocols like FTP, SSH, WebDAV as well as popular services like Microsoft OneDrive, Amazon S3, Google Drive, box.com, Mega, B2, and many others. |
| [resilio-sync](https://github.com/linuxserver/docker-resilio-sync/) | [resilio-sync](https://www.resilio.com/individuals/) (formerly BitTorrent Sync) uses the BitTorrent protocol to sync files and folders between all of your devices. There are both free and paid versions, this container supports both. There is an official sync image but we created this one as it supports user mapping to simplify permissions for volumes. |
| [rsnapshot](https://github.com/linuxserver/docker-rsnapshot/) | [rsnapshot](http://www.rsnapshot.org/) is a filesystem snapshot utility based on rsync. rsnapshot makes it easy to make periodic snapshots of local machines, and remote machines over ssh. The code makes extensive use of hard links whenever possible, to greatly reduce the disk space required." |
| [syncthing](https://github.com/linuxserver/docker-syncthing/) | [syncthing](https://syncthing.net) replaces proprietary sync and cloud services with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet. |

## Books

| Container | Description |
| --------- | ----------- |
| [calibre](https://github.com/linuxserver/docker-calibre/) | [calibre](https://calibre-ebook.com/) is a powerful and easy to use e-book manager. Users say it's outstanding and a must-have. It'll allow you to do nearly everything and it takes things a step beyond normal e-book software. It's also completely free and open source and great for both casual users and computer experts. |
| [calibre-web](https://github.com/linuxserver/docker-calibre-web/) | [calibre-web](https://github.com/janeczku/calibre-web) is a web app providing a clean interface for browsing, reading and downloading eBooks using an existing Calibre database.   It is also possible to integrate google drive and edit metadata and your calibre library through the app itself. |
| [cops](https://github.com/linuxserver/docker-cops/) | [cops](https://github.com/mikespub-org/seblucas-cops) by Sébastien Lucas, now maintained by MikesPub, stands for Calibre OPDS (and HTML) Php Server. |
| [kavita](https://github.com/linuxserver/docker-kavita/) | [kavita](https://github.com/Kareadita/Kavita) is a fast, feature rich, cross platform reading server. Built with a focus for being a full solution for all your reading needs. Setup your own server and share your reading collection with your friends and family! |
| [lazylibrarian](https://github.com/linuxserver/docker-lazylibrarian/) | [lazylibrarian](https://lazylibrarian.gitlab.io/) is a program to follow authors and grab metadata for all your digital reading needs. It uses a combination of Goodreads Librarything and optionally GoogleBooks as sources for author info and book info.  This container is based on the DobyTang fork. |
| [mylar3](https://github.com/linuxserver/docker-mylar3/) | [mylar3](https://github.com/mylar3/mylar3) is an automated Comic Book downloader (cbr/cbz) for use with NZB and torrents written in python. It supports SABnzbd, NZBGET, and many torrent clients in addition to DDL. |
| [readarr](https://github.com/linuxserver/docker-readarr/) | [readarr](https://github.com/Readarr/Readarr) - Book Manager and Automation (Sonarr for Ebooks) |
| [ubooquity](https://github.com/linuxserver/docker-ubooquity/) | [ubooquity](https://vaemendis.net/ubooquity/) is a free, lightweight and easy-to-use home server for your comics and ebooks. Use it to access your files from anywhere, with a tablet, an e-reader, a phone or a computer. |

## Chat

| Container | Description |
| --------- | ----------- |
| [altus](https://github.com/linuxserver/docker-altus/) | [Altus](https://github.com/amanharwara/altus) is an Electron-based WhatsApp client with themes and multiple account support. |
| [ferdium](https://github.com/linuxserver/docker-ferdium/) | [Ferdium](https://ferdium.org/) is a desktop app that helps you organize how you use your favourite apps by combining them into one application. |
| [pidgin](https://github.com/linuxserver/docker-pidgin/) | [Pidgin](https://pidgin.im/) is a chat program which lets you log into accounts on multiple chat networks simultaneously. This means that you can be chatting with friends on XMPP and sitting in an IRC channel at the same time. |
| [thelounge](https://github.com/linuxserver/docker-thelounge/) | [thelounge](https://thelounge.github.io/) (a fork of shoutIRC) is a web IRC client that you host on your own server. |
| [webcord](https://github.com/linuxserver/docker-webcord/) | [WebCord](https://github.com/SpacingBat3/WebCord) can be summarized as a pack of security and privacy hardenings, Discord features reimplementations, Electron / Chromium / Discord bugs workarounds, stylesheets, internal pages and wrapped https://discord.com page, designed to conform with ToS as much as it is possible (or hide the changes that might violate it from Discord's eyes). |

## Cloud

| Container | Description |
| --------- | ----------- |
| [nextcloud](https://github.com/linuxserver/docker-nextcloud/) | [nextcloud](https://nextcloud.com/) gives you access to all your files wherever you are. |

## Content Management

| Container | Description |
| --------- | ----------- |
| [bookstack](https://github.com/linuxserver/docker-bookstack/) | [bookstack](https://github.com/BookStackApp/BookStack) is a free and open source Wiki designed for creating beautiful documentation. Featuring a simple, but powerful WYSIWYG editor it allows for teams to create detailed and useful documentation with ease. |
| [dokuwiki](https://github.com/linuxserver/docker-dokuwiki/) | [dokuwiki](https://www.dokuwiki.org/dokuwiki/) is a simple to use and highly versatile Open Source wiki software that doesn't require a database. It is loved by users for its clean and readable syntax. The ease of maintenance, backup and integration makes it an administrator's favorite. Built in access controls and authentication connectors make DokuWiki especially useful in the enterprise context and the large number of plugins contributed by its vibrant community allow for a broad range of use cases beyond a traditional wiki. |
| [grav](https://github.com/linuxserver/docker-grav/) | [grav](https://github.com/getgrav/grav/) is a Fast, Simple, and Flexible, file-based Web-platform. |
| [hedgedoc](https://github.com/linuxserver/docker-hedgedoc/) | [HedgeDoc](https://hedgedoc.org/) gives you access to all your files wherever you are. |
| [monica](https://github.com/linuxserver/docker-monica/) | [monica](https://github.com/monicahq/monica) is an open source personal relationship management system, that lets you document your life. |
| [obsidian](https://github.com/linuxserver/docker-obsidian/) | [Obsidian](https://obsidian.md) is a note-taking app that lets you create, link, and organize your notes on your device, with hundreds of plugins and themes to customize your workflow. You can also publish your notes online, access them offline, and sync them securely with end-to-end encryption. |
| [planka](https://github.com/linuxserver/docker-planka/) | [planka](https://github.com/plankanban/planka/) is an elegant open source project tracking tool. |
| [raneto](https://github.com/linuxserver/docker-raneto/) | [raneto](http://raneto.com/) - is an open source Knowledgebase platform that uses static Markdown files to power your Knowledgebase. |
| [wikijs](https://github.com/linuxserver/docker-wikijs/) | [wikijs](https://github.com/Requarks/wiki) A modern, lightweight and powerful wiki app built on NodeJS. |

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
| [fleet](https://github.com/linuxserver/docker-fleet/) | [fleet](https://github.com/linuxserver/fleet) provides an online web interface which displays a set of maintained images from one or more owned repositories. |
| [modmanager](https://github.com/linuxserver/docker-modmanager/) | Modmanager is a centralised tool for downloading and updating docker mods for all your other Linuxserver containers. |
| [qemu-static](https://github.com/linuxserver/docker-qemu-static/) | Run multiple architectures of Docker containers on an x86_64 or aarch64 host using QEMU static. |
| [socket-proxy](https://github.com/linuxserver/docker-socket-proxy/) | The Socket Proxy is a security-enhanced proxy which allows you to apply access rules to the Docker socket, limiting the attack surface for containers such as watchtower or Traefik that need to use it. |

## Documents

| Container | Description |
| --------- | ----------- |
| [calligra](https://github.com/linuxserver/docker-calligra/) | [Calligra](https://calligra.org/) is an office and graphic art suite by KDE. It is available for desktop PCs, tablet computers, and smartphones. It contains applications for word processing, spreadsheets, presentation, vector graphics, and editing databases. |
| [libreoffice](https://github.com/linuxserver/docker-libreoffice/) | [LibreOffice](https://www.libreoffice.org/) is a free and powerful office suite, and a successor to OpenOffice.org (commonly known as OpenOffice). Its clean interface and feature-rich tools help you unleash your creativity and enhance your productivity. |
| [nextcloud](https://github.com/linuxserver/docker-nextcloud/) | [nextcloud](https://nextcloud.com/) gives you access to all your files wherever you are. |
| [wps-office](https://github.com/linuxserver/docker-wps-office/) | [WPS Office](https://www.wps.com/) is a lightweight, feature-rich comprehensive office suite with high compatibility. As a handy and professional office software, WPS Office allows you to edit files in Writer, Presentation, Spreadsheet, and PDF to improve your work efficiency. |
| [zotero](https://github.com/linuxserver/docker-zotero/) | [Zotero](https://www.zotero.org/) is a free, easy-to-use tool to help you collect, organize, annotate, cite, and share research. |

## Downloaders

| Container | Description |
| --------- | ----------- |
| [deluge](https://github.com/linuxserver/docker-deluge/) | [deluge](http://deluge-torrent.org/) is a lightweight, Free Software, cross-platform BitTorrent client. |
| [nzbget](https://github.com/linuxserver/docker-nzbget/) | [nzbget](http://nzbget.com/) is a usenet downloader, written in C++ and designed with performance in mind to achieve maximum download speed by using very little system resources. |
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
| [pairdrop](https://github.com/linuxserver/docker-pairdrop/) | [PairDrop](https://github.com/schlagmichdoch/PairDrop) is a sublime alternative to AirDrop that works on all platforms. Send images, documents or text via peer to peer connection to devices in the same local network/Wi-Fi or to paired devices. |
| [projectsend](https://github.com/linuxserver/docker-projectsend/) | [projectsend](http://www.projectsend.org) is a self-hosted application that lets you upload files and assign them to specific clients that you create yourself. Secure, private and easy. No more depending on external services or e-mail to send those files. |
| [pwndrop](https://github.com/linuxserver/docker-pwndrop/) | [pwndrop](https://github.com/kgretzky/pwndrop) is a self-deployable file hosting service for sending out red teaming payloads or securely sharing your private files over HTTP and WebDAV. |
| [pydio-cells](https://github.com/linuxserver/docker-pydio-cells/) | [pydio-cells](https://pydio.com/) is the nextgen file sharing platform for organizations. It is a full rewrite of the Pydio project using the Go language following a micro-service architecture. |
| [snapdrop](https://github.com/linuxserver/docker-snapdrop/) | [snapdrop](https://github.com/snapdrop/snapdrop) A local file sharing in your browser. Inspired by Apple's Airdrop. |
| [xbackbone](https://github.com/linuxserver/docker-xbackbone/) | [xbackbone](https://github.com/SergiX44/XBackBone) is a simple, self-hosted, lightweight PHP file manager that support the instant sharing tool ShareX and *NIX systems. It supports uploading and displaying images, GIF, video, code, formatted text, and file downloading and uploading. Also have a web UI with multi user management, past uploads history and search support. |

## Finance

| Container | Description |
| --------- | ----------- |
| [budge](https://github.com/linuxserver/docker-budge/) | [budge](https://github.com/linuxserver/budge) is an open source 'budgeting with envelopes' personal finance app. |
| [kimai](https://github.com/linuxserver/docker-kimai/) | [kimai](https://kimai.org/) is a professional grade time-tracking application, free and open-source. |

## Games

| Container | Description |
| --------- | ----------- |
| [emulatorjs](https://github.com/linuxserver/docker-emulatorjs/) | [emulatorjs](https://github.com/linuxserver/emulatorjs) - In browser web based emulation portable to nearly any device for many retro consoles. A mix of emulators is used between Libretro and EmulatorJS. |
| [minetest](https://github.com/linuxserver/docker-minetest/) | [minetest](http://www.minetest.net/) (server) is a near-infinite-world block sandbox game and a game engine, inspired by InfiniMiner, Minecraft, and the like. |
| [steamos](https://github.com/linuxserver/docker-steamos/) | [SteamOS](https://www.steamdeck.com/) is an Arch based Linux distribution made by Valve Software. This container is a vanilla Arch install with Steam repositories added for software support. **This container will only work with modern AMD/Intel GPUs on a real Linux Host** |

## Home Automation

| Container | Description |
| --------- | ----------- |
| [habridge](https://github.com/linuxserver/docker-habridge/) | [habridge](https://github.com/bwssytems/ha-bridge/) emulates Philips Hue API to other home automation gateways such as an Amazon Echo/Dot Gen 1 (gen 2 has issues discovering ha-bridge) or other systems that support Philips Hue. The Bridge handles basic commands such as "On", "Off" and "brightness" commands of the hue protocol. This bridge can control most devices that have a distinct API. |
| [homeassistant](https://github.com/linuxserver/docker-homeassistant/) | [Home Assistant Core](https://www.home-assistant.io/) - Open source home automation that puts local control and privacy first. Powered by a worldwide community of tinkerers and DIY enthusiasts. Perfect to run on a Raspberry Pi or a local server |

## IRC

| Container | Description |
| --------- | ----------- |
| [limnoria](https://github.com/linuxserver/docker-limnoria/) | [limnoria](https://github.com/ProgVal/limnoria) A robust, full-featured, and user/programmer-friendly Python IRC bot, with many existing plugins. Successor of the well-known Supybot. |
| [ngircd](https://github.com/linuxserver/docker-ngircd/) | [ngircd](https://ngircd.barton.de/) is a free, portable and lightweight Internet Relay Chat server for small or private networks, developed under the GNU General Public License (GPL). It is easy to configure, can cope with dynamic IP addresses, and supports IPv6, SSL-protected connections as well as PAM for authentication. It is written from scratch and not based on the original IRCd. |
| [pidgin](https://github.com/linuxserver/docker-pidgin/) | [Pidgin](https://pidgin.im/) is a chat program which lets you log into accounts on multiple chat networks simultaneously. This means that you can be chatting with friends on XMPP and sitting in an IRC channel at the same time. |
| [thelounge](https://github.com/linuxserver/docker-thelounge/) | [thelounge](https://thelounge.github.io/) (a fork of shoutIRC) is a web IRC client that you host on your own server. |
| [znc](https://github.com/linuxserver/docker-znc/) | [znc](http://wiki.znc.in/ZNC) is an IRC network bouncer or BNC. It can detach the client from the actual IRC server, and also from selected channels. Multiple clients from different locations can connect to a single ZNC account simultaneously and therefore appear under the same nickname on IRC. |

## Image Editor

| Container | Description |
| --------- | ----------- |
| [gimp](https://github.com/linuxserver/docker-gimp/) | [GIMP](https://www.gimp.org/) is a free and open-source raster graphics editor used for image manipulation (retouching) and image editing, free-form drawing, transcoding between different image file formats, and more specialized tasks. It is extensible by means of plugins, and scriptable. |
| [krita](https://github.com/linuxserver/docker-krita/) | [Krita](https://krita.org/en/) is a professional FREE and open source painting program. It is made by artists that want to see affordable art tools for everyone. |
| [rawtherapee](https://github.com/linuxserver/docker-rawtherapee/) | [RawTherapee](https://rawtherapee.com/) is a free, cross-platform raw image processing program! |

## Indexers

| Container | Description |
| --------- | ----------- |
| [jackett](https://github.com/linuxserver/docker-jackett/) | [jackett](https://github.com/Jackett/Jackett) works as a proxy server: it translates queries from apps (Sonarr, SickRage, CouchPotato, Mylar, etc) into tracker-site-specific http queries, parses the html response, then sends results back to the requesting software. This allows for getting recent uploads (like RSS) and performing searches. Jackett is a single repository of maintained indexer scraping & translation logic - removing the burden from other apps. |
| [nzbhydra2](https://github.com/linuxserver/docker-nzbhydra2/) | [nzbhydra2](https://github.com/theotherp/nzbhydra2) is a meta search application for NZB indexers, the "spiritual successor" to NZBmegasearcH, and an evolution of the original application [NZBHydra](https://github.com/theotherp/nzbhydra). |
| [prowlarr](https://github.com/linuxserver/docker-prowlarr/) | [prowlarr](https://github.com/Prowlarr/Prowlarr) is a indexer manager/proxy built on the popular arr .net/reactjs base stack to integrate with your various PVR apps. Prowlarr supports both Torrent Trackers and Usenet Indexers. It integrates seamlessly with Sonarr, Radarr, Lidarr, and Readarr offering complete management of your indexers with no per app Indexer setup required (we do it all). |

## Machine Learning

| Container | Description |
| --------- | ----------- |
| [faster-whisper](https://github.com/linuxserver/docker-faster-whisper/) | [faster-whisper](https://github.com/SYSTRAN/faster-whisper) is a reimplementation of OpenAI's Whisper model using CTranslate2, which is a fast inference engine for Transformer models. This container provides a Wyoming protocol server for faster-whisper. |
| [piper](https://github.com/linuxserver/docker-piper/) | [piper](https://github.com/rhasspy/piper/) is a fast, local neural text to speech system that sounds great and is optimized for the Raspberry Pi 4. This container provides a Wyoming protocol server for Piper. |

## Media Management

| Container | Description |
| --------- | ----------- |
| [bazarr](https://github.com/linuxserver/docker-bazarr/) | [bazarr](https://www.bazarr.media/) is a companion application to Sonarr and Radarr. It can manage and download subtitles based on your requirements. You define your preferences by TV show or movie and Bazarr takes care of everything for you. |
| [flexget](https://github.com/linuxserver/docker-flexget/) | [flexget](http://flexget.com/) is a multipurpose automation tool for all of your media. |
| [kometa](https://github.com/linuxserver/docker-kometa/) | [kometa](https://github.com/Kometa-Team/Kometa) is a powerful tool designed to give you complete control over your media libraries. With kometa, you can take your customization to the next level, with granular control over metadata, collections, overlays, and much more. |
| [lidarr](https://github.com/linuxserver/docker-lidarr/) | [lidarr](https://github.com/lidarr/Lidarr) is a music collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new tracks from your favorite artists and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available. |
| [mediaelch](https://github.com/linuxserver/docker-mediaelch/) | [MediaElch](https://github.com/Komet/MediaElch) is a MediaManager for Kodi. Information about Movies, TV Shows, Concerts and Music are stored as nfo files. Fanarts are downloaded automatically from fanart.tv. Using the nfo generator, MediaElch can be used with other MediaCenters as well. |
| [medusa](https://github.com/linuxserver/docker-medusa/) | [medusa](https://pymedusa.com/) is an automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic. |
| [radarr](https://github.com/linuxserver/docker-radarr/) | [radarr](https://github.com/Radarr/Radarr) - A fork of Sonarr to work with movies à la Couchpotato. |
| [series-troxide](https://github.com/linuxserver/docker-series-troxide/) | [Series Troxide](https://github.com/MaarifaMaarifa/series-troxide) a Simple and Modern Series Tracker |
| [sickchill](https://github.com/linuxserver/docker-sickchill/) | [sickchill](https://github.com/SickChill/SickChill) is an Automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic. |
| [sickgear](https://github.com/linuxserver/docker-sickgear/) | [SickGear](https://github.com/sickgear/sickgear) provides management of TV shows and/or Anime, it detects new episodes, links downloader apps, and more.. |
| [sonarr](https://github.com/linuxserver/docker-sonarr/) | [sonarr](https://sonarr.tv/) (formerly NZBdrone) is a PVR for usenet and bittorrent users. It can monitor multiple RSS feeds for new episodes of your favorite shows and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available. |

## Media Requesters

| Container | Description |
| --------- | ----------- |
| [doplarr](https://github.com/linuxserver/docker-doplarr/) | [doplarr](https://github.com/kiranshila/Doplarr) is an *arr request bot for Discord." |
| [ombi](https://github.com/linuxserver/docker-ombi/) | [ombi](https://ombi.io) allows you to host your own Plex Request and user management system. |
| [overseerr](https://github.com/linuxserver/docker-overseerr/) | [overseerr](https://overseerr.dev/) is a request management and media discovery tool built to work with your existing Plex ecosystem. |

## Media Servers

| Container | Description |
| --------- | ----------- |
| [airsonic-advanced](https://github.com/linuxserver/docker-airsonic-advanced/) | [airsonic-advanced](https://github.com/kagemomiji/airsonic-advanced) is a free, web-based media streamer, providing ubiquitious access to your music. Use it to share your music with friends, or to listen to your own music while at work. You can stream to multiple players simultaneously, for instance to one player in your kitchen and another in your living room. |
| [emby](https://github.com/linuxserver/docker-emby/) | [emby](https://emby.media/) organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server. |
| [jellyfin](https://github.com/linuxserver/docker-jellyfin/) | [jellyfin](https://github.com/jellyfin/jellyfin) is a Free Software Media System that puts you in control of managing and streaming your media. It is an alternative to the proprietary Emby and Plex, to provide media from a dedicated server to end-user devices via multiple apps. Jellyfin is descended from Emby's 3.5.2 release and ported to the .NET Core framework to enable full cross-platform support. There are no strings attached, no premium licenses or features, and no hidden agendas: just a team who want to build something better and work together to achieve it. |
| [mstream](https://github.com/linuxserver/docker-mstream/) | [mstream](https://mstream.io/) is a personal music streaming server. You can use mStream to stream your music from your home computer to any device, anywhere.  There are mobile apps available for both Android and iPhone. |
| [plex](https://github.com/linuxserver/docker-plex/) | [plex](https://plex.tv) organizes video, music and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone Plex Media Server. Straightforward design and bulk actions mean getting things done faster. |

## Media Tools

| Container | Description |
| --------- | ----------- |
| [ffmpeg](https://github.com/linuxserver/docker-ffmpeg/) | A complete, cross-platform solution to record, convert and stream audio and video. |
| [htpcmanager](https://github.com/linuxserver/docker-htpcmanager/) | [htpcmanager](https://github.com/HTPC-Manager/HTPC-Manager) is a front end for many htpc related applications. |
| [minisatip](https://github.com/linuxserver/docker-minisatip/) | [minisatip](https://github.com/catalinii/minisatip) is a multi-threaded satip server version 1.2 that runs under Linux and it was tested with DVB-S, DVB-S2, DVB-T, DVB-T2, DVB-C, DVB-C2, ATSC and ISDB-T cards. |
| [oscam](https://github.com/linuxserver/docker-oscam/) | [oscam](https://git.streamboard.tv/common/oscam) is an Open Source Conditional Access Module software used for descrambling DVB transmissions using smart cards. It's both a server and a client. |
| [synclounge](https://github.com/linuxserver/docker-synclounge/) | [synclounge](https://github.com/samcm/synclounge) is a third party tool that allows you to watch Plex in sync with your friends/family, wherever you are. |
| [tautulli](https://github.com/linuxserver/docker-tautulli/) | [tautulli](http://tautulli.com) is a python based web application for monitoring, analytics and notifications for Plex Media Server. |
| [tvheadend](https://github.com/linuxserver/docker-tvheadend/) | [tvheadend](https://www.tvheadend.org/) works as a proxy server: is a TV streaming server and recorder for Linux, FreeBSD and Android supporting DVB-S, DVB-S2, DVB-C, DVB-T, ATSC, ISDB-T, IPTV, SAT>IP and HDHomeRun as input sources. |
| [webgrabplus](https://github.com/linuxserver/docker-webgrabplus/) | [webgrabplus](http://www.webgrabplus.com) is a multi-site incremental xmltv epg grabber. It collects tv-program guide data from selected tvguide sites for your favourite channels. |

## Monitoring

| Container | Description |
| --------- | ----------- |
| [apprise-api](https://github.com/linuxserver/docker-apprise-api/) | [apprise-api](https://github.com/caronc/apprise-api) Takes advantage of [Apprise](https://github.com/caronc/apprise) through your network with a user-friendly API. |
| [healthchecks](https://github.com/linuxserver/docker-healthchecks/) | [healthchecks](https://github.com/healthchecks/healthchecks) is a watchdog for your cron jobs. It's a web server that listens for pings from your cron jobs, plus a web interface. |
| [librespeed](https://github.com/linuxserver/docker-librespeed/) | [librespeed](https://github.com/librespeed/speedtest) is a very lightweight Speedtest implemented in Javascript, using XMLHttpRequest and Web Workers. |
| [smokeping](https://github.com/linuxserver/docker-smokeping/) | [smokeping](https://oss.oetiker.ch/smokeping/) keeps track of your network latency. For a full example of what this application is capable of visit [UCDavis](http://smokeping.ucdavis.edu/cgi-bin/smokeping.fcgi). |
| [speedtest-tracker](https://github.com/linuxserver/docker-speedtest-tracker/) | [speedtest-tracker](https://github.com/alexjustesen/speedtest-tracker) is a self-hosted internet performance tracking application that runs speedtest checks against Ookla's Speedtest service. |
| [syslog-ng](https://github.com/linuxserver/docker-syslog-ng/) | [syslog-ng](https://www.syslog-ng.com/products/open-source-log-management/) allows you to flexibly collect, parse, classify, rewrite and correlate logs from across your infrastructure and store or route them to log analysis tools. |

## Music

| Container | Description |
| --------- | ----------- |
| [airsonic-advanced](https://github.com/linuxserver/docker-airsonic-advanced/) | [airsonic-advanced](https://github.com/kagemomiji/airsonic-advanced) is a free, web-based media streamer, providing ubiquitious access to your music. Use it to share your music with friends, or to listen to your own music while at work. You can stream to multiple players simultaneously, for instance to one player in your kitchen and another in your living room. |
| [beets](https://github.com/linuxserver/docker-beets/) | [beets](http://beets.io/) is a music library manager and not, for the most part, a music player. It does include a simple player plugin and an experimental Web-based player, but it generally leaves actual sound-reproduction to specialized tools. |
| [emby](https://github.com/linuxserver/docker-emby/) | [emby](https://emby.media/) organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server. |
| [jellyfin](https://github.com/linuxserver/docker-jellyfin/) | [jellyfin](https://github.com/jellyfin/jellyfin) is a Free Software Media System that puts you in control of managing and streaming your media. It is an alternative to the proprietary Emby and Plex, to provide media from a dedicated server to end-user devices via multiple apps. Jellyfin is descended from Emby's 3.5.2 release and ported to the .NET Core framework to enable full cross-platform support. There are no strings attached, no premium licenses or features, and no hidden agendas: just a team who want to build something better and work together to achieve it. |
| [lidarr](https://github.com/linuxserver/docker-lidarr/) | [lidarr](https://github.com/lidarr/Lidarr) is a music collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new tracks from your favorite artists and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available. |
| [lollypop](https://github.com/linuxserver/docker-lollypop/) | [Lollypop](https://wiki.gnome.org/Apps/Lollypop) is a lightweight modern music player designed to work excellently on the GNOME desktop environment. |
| [mstream](https://github.com/linuxserver/docker-mstream/) | [mstream](https://mstream.io/) is a personal music streaming server. You can use mStream to stream your music from your home computer to any device, anywhere.  There are mobile apps available for both Android and iPhone. |
| [plex](https://github.com/linuxserver/docker-plex/) | [plex](https://plex.tv) organizes video, music and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone Plex Media Server. Straightforward design and bulk actions mean getting things done faster. |
| [spotube](https://github.com/linuxserver/docker-spotube/) | [Spotube](https://spotube.krtirtho.dev/) is an open source, cross-platform Spotify client compatible across multiple platforms utilizing Spotify's data API and YouTube, Piped.video or JioSaavn as an audio source, eliminating the need for Spotify Premium |
| [your_spotify](https://github.com/linuxserver/docker-your_spotify/) | [your_spotify](https://github.com/Yooooomi/your_spotify) is a self-hosted application that tracks what you listen and offers you a dashboard to explore statistics about it! It's composed of a web server which polls the Spotify API every now and then and a web application on which you can explore your statistics. |

## Network

| Container | Description |
| --------- | ----------- |
| [adguardhome-sync](https://github.com/linuxserver/docker-adguardhome-sync/) | [adguardhome-sync](https://github.com/bakito/adguardhome-sync/) is a tool to synchronize AdGuardHome config to replica instances. |
| [ddclient](https://github.com/linuxserver/docker-ddclient/) | [ddclient](https://github.com/ddclient/ddclient) is a Perl client used to update dynamic DNS entries for accounts on Dynamic DNS Network Service Provider. It was originally written by Paul Burry and is now mostly by wimpunk. It has the capability to update more than just dyndns and it can fetch your WAN-ipaddress in a few different ways. |
| [duckdns](https://github.com/linuxserver/docker-duckdns/) | [duckdns](https://duckdns.org/) is a free service which will point a DNS (sub domains of duckdns.org) to an IP of your choice. The service is completely free, and doesn't require reactivation or forum posts to maintain its existence. |
| [fail2ban](https://github.com/linuxserver/docker-fail2ban/) | [fail2ban](http://www.fail2ban.org/) is a daemon to ban hosts that cause multiple authentication errors. |
| [unifi-network-application](https://github.com/linuxserver/docker-unifi-network-application/) | The [unifi-network-application](https://ui.com/) software is a powerful, enterprise wireless software engine ideal for high-density client deployments requiring low latency and high uptime performance. |
| [wireguard](https://github.com/linuxserver/docker-wireguard/) | [WireGuard®](https://www.wireguard.com/) is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPsec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable. It is currently under heavy development, but already it might be regarded as the most secure, easiest to use, and simplest VPN solution in the industry. |
| [wireshark](https://github.com/linuxserver/docker-wireshark/) | [Wireshark](https://www.wireshark.org/) is the world’s foremost and widely-used network protocol analyzer. It lets you see what’s happening on your network at a microscopic level and is the de facto (and often de jure) standard across many commercial and non-profit enterprises, government agencies, and educational institutions. Wireshark development thrives thanks to the volunteer contributions of networking experts around the globe and is the continuation of a project started by Gerald Combs in 1998.  |

## Password Manager

| Container | Description |
| --------- | ----------- |
| [keepassxc](https://github.com/linuxserver/docker-keepassxc/) | [KeePassXC](https://keepassxc.org/) is a free and open-source password manager. It started as a community fork of KeePassX (itself a cross-platform port of KeePass). |

## Photos

| Container | Description |
| --------- | ----------- |
| [darktable](https://github.com/linuxserver/docker-darktable/) | [darktable](https://www.darktable.org/) is an open source photography workflow application and raw developer. A virtual lighttable and darkroom for photographers. It manages your digital negatives in a database, lets you view them through a zoomable lighttable and enables you to develop raw images and enhance them. |
| [digikam](https://github.com/linuxserver/docker-digikam/) | [digiKam](https://www.digikam.org/): Professional Photo Management with the Power of Open Source |
| [lychee](https://github.com/linuxserver/docker-lychee/) | [lychee](https://lycheeorg.github.io/) is a free photo-management tool, which runs on your server or web-space. Installing is a matter of seconds. Upload, manage and share photos like from a native application. Lychee comes with everything you need and all your photos are stored securely." |
| [piwigo](https://github.com/linuxserver/docker-piwigo/) | [piwigo](http://piwigo.org/) is a photo gallery software for the web that comes with powerful features to publish and manage your collection of pictures. |

## Programming

| Container | Description |
| --------- | ----------- |
| [code-server](https://github.com/linuxserver/docker-code-server/) | [code-server](https://coder.com) is VS Code running on a remote server, accessible through the browser. |
| [github-desktop](https://github.com/linuxserver/docker-github-desktop/) | [Github Desktop](https://desktop.github.com/) is an open source Electron-based GitHub app. It is written in TypeScript and uses React. |
| [gitqlient](https://github.com/linuxserver/docker-gitqlient/) | [GitQlient](https://github.com/francescmm/GitQlient) is a multi-platform Git client originally forked from QGit. Nowadays it goes beyond of just a fork and adds a lot of new functionality. |
| [openvscode-server](https://github.com/linuxserver/docker-openvscode-server/) | [openvscode-server](https://github.com/gitpod-io/openvscode-server) provides a version of VS Code that runs a server on a remote machine and allows access through a modern web browser. |
| [pylon](https://github.com/linuxserver/docker-pylon/) | [pylon](https://github.com/pylonide/pylon) is a web based integrated development environment built with Node.js as a backend and with a supercharged JavaScript/HTML5 frontend, licensed under GPL version 3. This project originates from Cloud9 v2 project. |
| [vscodium](https://github.com/linuxserver/docker-vscodium/) | [VSCodium](https://vscodium.com/) is a community-driven, freely-licensed binary distribution of Microsoft’s editor VS Code. |
| [yaak](https://github.com/linuxserver/docker-yaak/) | [yaak](https://yaak.app/) is a desktop API client for organizing and executing REST, GraphQL, and gRPC requests. It's built using [Tauri](https://tauri.app/), [Rust](https://www.rust-lang.org/), and [ReactJS](https://react.dev/). |

## RSS

| Container | Description |
| --------- | ----------- |
| [feed2toot](https://github.com/linuxserver/docker-feed2toot/) | [feed2toot](https://gitlab.com/chaica/feed2toot) automatically parses rss feeds, identifies new posts and posts them on the Mastodon social network. |
| [freshrss](https://github.com/linuxserver/docker-freshrss/) | [freshrss](https://freshrss.org/) is a free, self-hostable aggregator for rss feeds. |

## Recipes

| Container | Description |
| --------- | ----------- |
| [grocy](https://github.com/linuxserver/docker-grocy/) | [grocy](https://github.com/grocy/grocy) is an ERP system for your kitchen! Cut down on food waste, and manage your chores with this brilliant utility. |

## Remote Desktop

| Container | Description |
| --------- | ----------- |
| [kali-linux](https://github.com/linuxserver/docker-kali-linux/) | [kali-linux](https://github.com/linuxserver/docker-kali-linux) - is an Advanced Penetration Testing Linux distribution used for Penetration Testing, Ethical Hacking and network security assessments. KALI LINUX ™ is a trademark of OffSec. |
| [kasm](https://github.com/linuxserver/docker-kasm/) | [kasm](https://www.kasmweb.com/?utm_campaign=LinuxServer&utm_source=listing) Workspaces is a docker container streaming platform for delivering browser-based access to desktops, applications, and web services. Kasm uses devops-enabled Containerized Desktop Infrastructure (CDI) to create on-demand, disposable, docker containers that are accessible via web browser. Example use-cases include Remote Browser Isolation (RBI), Data Loss Prevention (DLP), Desktop as a Service (DaaS), Secure Remote Access Services (RAS), and Open Source Intelligence (OSINT) collections. |
| [rdesktop](https://github.com/linuxserver/docker-rdesktop/) | [rdesktop](http://xrdp.org/) - Containers containing full desktop environments in many popular flavors for Alpine, Ubuntu, Arch, and Fedora accessible via RDP. |
| [remmina](https://github.com/linuxserver/docker-remmina/) | [Remmina](https://remmina.org/) is a remote desktop client written in GTK, aiming to be useful for system administrators and travellers, who need to work with lots of remote computers in front of either large or tiny screens. Remmina supports multiple network protocols, in an integrated and consistent user interface. Currently RDP, VNC, SPICE, SSH and EXEC are supported. |
| [rustdesk](https://github.com/linuxserver/docker-rustdesk/) | [RustDesk](https://rustdesk.com/) is a full-featured open source remote control alternative for self-hosting and security with minimal configuration. |
| [webtop](https://github.com/linuxserver/docker-webtop/) | [webtop](https://github.com/linuxserver/docker-webtop) - Alpine, Ubuntu, Fedora, and Arch based containers containing full desktop environments in officially supported flavors accessible via any modern web browser. |

## Reverse Proxy

| Container | Description |
| --------- | ----------- |
| [nginx](https://github.com/linuxserver/docker-nginx/) | [nginx](https://nginx.org/) is a simple webserver with php support. The config files reside in `/config` for easy user customization. |
| [swag](https://github.com/linuxserver/docker-swag/) | SWAG - Secure Web Application Gateway (formerly known as letsencrypt, no relation to Let's Encrypt™) sets up an Nginx webserver and reverse proxy with php support and a built-in certbot client that automates free SSL server certificate generation and renewal processes (Let's Encrypt and ZeroSSL). It also contains fail2ban for intrusion prevention. |

## Science

| Container | Description |
| --------- | ----------- |
| [boinc](https://github.com/linuxserver/docker-boinc/) | [BOINC](https://boinc.berkeley.edu/) is a platform for high-throughput computing on a large scale (thousands or millions of computers). It can be used for volunteer computing (using consumer devices) or grid computing (using organizational resources). It supports virtualized, parallel, and GPU-based applications. |
| [foldingathome](https://github.com/linuxserver/docker-foldingathome/) | [Folding@home](https://foldingathome.org/) is a distributed computing project for simulating protein dynamics, including the process of protein folding and the movements of proteins implicated in a variety of diseases. It brings together citizen scientists who volunteer to run simulations of protein dynamics on their personal computers. Insights from this data are helping scientists to better understand biology, and providing new opportunities for developing therapeutics. |

## Security

| Container | Description |
| --------- | ----------- |
| [fail2ban](https://github.com/linuxserver/docker-fail2ban/) | [fail2ban](http://www.fail2ban.org/) is a daemon to ban hosts that cause multiple authentication errors. |

## Social

| Container | Description |
| --------- | ----------- |
| [mastodon](https://github.com/linuxserver/docker-mastodon/) | [mastodon](https://github.com/mastodon/mastodon/) is a free, open-source social network server based on ActivityPub where users can follow friends and discover new ones.. |

## Storage

| Container | Description |
| --------- | ----------- |
| [diskover](https://github.com/linuxserver/docker-diskover/) | [diskover](https://github.com/diskoverdata/diskover-community) is an open source file system indexer that uses Elasticsearch to index and manage data across heterogeneous storage systems. |
| [qdirstat](https://github.com/linuxserver/docker-qdirstat/) | [QDirStat](https://github.com/shundhammer/qdirstat) Qt-based directory statistics: KDirStat without any KDE -- from the author of the original KDirStat. |

## VPN

| Container | Description |
| --------- | ----------- |
| [wireguard](https://github.com/linuxserver/docker-wireguard/) | [WireGuard®](https://www.wireguard.com/) is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPsec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable. It is currently under heavy development, but already it might be regarded as the most secure, easiest to use, and simplest VPN solution in the industry. |

## Video Editor

| Container | Description |
| --------- | ----------- |
| [kdenlive](https://github.com/linuxserver/docker-kdenlive/) | [Kdenlive](https://kdenlive.org/) is a powerful free and open source cross-platform video editing program made by the KDE community. Feature rich and production ready. |
| [openshot](https://github.com/linuxserver/docker-openshot/) | [OpenShot](https://openshot.org/) Video Editor is an award-winning free and open-source video editor for Linux, Mac, and Windows, and is dedicated to delivering high quality video editing and animation solutions to the world. |
| [shotcut](https://github.com/linuxserver/docker-shotcut/) | [shotcut](https://www.shotcut.org/) is a free, open source, cross-platform video editor. |

## Video Streaming

| Container | Description |
| --------- | ----------- |
| [freetube](https://github.com/linuxserver/docker-freetube/) | [FreeTube](https://freetubeapp.io/) is a feature-rich and user-friendly YouTube client with a focus on privacy. |

## Web Browser

| Container | Description |
| --------- | ----------- |
| [chromium](https://github.com/linuxserver/docker-chromium/) | [Chromium](https://www.chromium.org/chromium-projects/) is an open-source browser project that aims to build a safer, faster, and more stable way for all users to experience the web. |
| [firefox](https://github.com/linuxserver/docker-firefox/) | [Firefox](https://www.mozilla.org/en-US/firefox/) Browser, also known as Mozilla Firefox or simply Firefox, is a free and open-source web browser developed by the Mozilla Foundation and its subsidiary, the Mozilla Corporation. Firefox uses the Gecko layout engine to render web pages, which implements current and anticipated web standards. |
| [librewolf](https://github.com/linuxserver/docker-librewolf/) | [LibreWolf](https://librewolf.net/) is a custom and independent version of Firefox, with the primary goals of privacy, security and user freedom. LibreWolf also aims to remove all the telemetry, data collection and annoyances, as well as disabling anti-freedom features like DRM. |
| [msedge](https://github.com/linuxserver/docker-msedge/) | [Microsoft Edge](https://www.microsoft.com/edge) is a cross-platform web browser developed by Microsoft and based on Chromium. |
| [mullvad-browser](https://github.com/linuxserver/docker-mullvad-browser/) | The [Mullvad Browser](https://mullvad.net/en/browser) is a privacy-focused web browser developed in a collaboration between Mullvad VPN and the Tor Project. It’s designed to minimize tracking and fingerprinting. You could say it’s a Tor Browser to use without the Tor Network. Instead, you can use it with a trustworthy VPN. |
| [opera](https://github.com/linuxserver/docker-opera/) | [Opera](https://www.opera.com/) is a multi-platform web browser developed by its namesake company Opera. The browser is based on Chromium, but distinguishes itself from other Chromium-based browsers (Chrome, Edge, etc.) through its user interface and other features. |
| [ungoogled-chromium](https://github.com/linuxserver/docker-ungoogled-chromium/) | [Ungoogled Chromium](https://github.com/ungoogled-software/ungoogled-chromium) is Google Chromium, sans dependency on Google web services. |

## Web Tools

| Container | Description |
| --------- | ----------- |
| [changedetection.io](https://github.com/linuxserver/docker-changedetection.io/) | [changedetection.io](https://github.com/dgtlmoon/changedetection.io) provides free, open-source web page monitoring, notification and change detection. |


