# 2020-1-OSS-11
## Project : The Fuck
*The Fuck* is a magnificent app, inspired by a [@liamosaur](https://twitter.com/liamosaur/)
[tweet](https://twitter.com/liamosaur/status/506975850596536320),
that corrects errors in previous console commands.

![texture theme preview](https://raw.githubusercontent.com/nvbn/thefuck/master/example.gif)

More examples:

```bash
➜ apt-get install vim
E: Could not open lock file /var/lib/dpkg/lock - open (13: Permission denied)
E: Unable to lock the administration directory (/var/lib/dpkg/), are you root?

➜ fuck
sudo apt-get install vim [enter/↑/↓/ctrl+c]
[sudo] password for nvbn:
Reading package lists... Done
...
