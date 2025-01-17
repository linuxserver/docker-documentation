# How to get support

1. Join our [Discord server](https://linuxserver.io/discord), read our [Support Policy](../misc/support-policy.md), and read the description of each channel before asking for support.
2. SSH to your server and run the following command to create an alias that gathers the information we require:

   ```bash
   alias lsiosupport='function _lsiosupport(){ uname -a > lsiosupport.txt; docker -v >> lsiosupport.txt; cat /etc/os-release >> lsiosupport.txt; docker inspect --format "$(wget -qO- https://docs.linuxserver.io/assets/run.tpl)" $1 >> lsiosupport.txt; docker logs $1 >> lsiosupport.txt; }; _lsiosupport'
   ```

   The alias gathers the following information: OS details, docker version, run command, and container logs.
3. Execute the alias with a container name:

   ```bash
   lsiosupport <container-name>
   ```

   Add `sudo` in the beginning if your user can't access docker.
4. A file called `lsiosupport.txt` will be created in the current folder, open it with a text editor.
5. Redact sensitive information such as: passwords, domains, emails, personal information, etc.
   **Don't redact information we need for troubleshooting such as: IPs, volumes, local paths, etc.**
6. Upload the file to a pastebin like [PrivateBin](https://privatebin.net/) or [Gist](https://gist.github.com/).
7. Post the link along with a detailed description of your issue in the appropriate discord support channel.
