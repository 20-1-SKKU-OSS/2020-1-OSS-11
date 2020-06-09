# 2020-1-OSS-11
## Project : The Fuck
**Original project** : https://github.com/nvbn/thefuck

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
```


## Team Members
**권태완** (Team Leader)
- Student ID : 2015310434
- E-mail : tae6ae@gmail.com
- Github ID: tae6ae

**김민철**
- Student ID : 2019310854
- E-mail : sdasasq@gmail.com
- Github ID: sdasasqkim

**안영태**
- Student ID : 2015313102
- E-mail : youngtea93@gmail.com
- Github ID: youngtae47

**인진영**
- Student ID : 2017311575
- E-mail : sara_in@naver.com
- Github ID: injinyoung

**조건희**
- Student ID : 2018313255
- E-mail : rafik57@g.skku.edu
- Github ID: Jokuna


## Contribution
**Add New Rules**
- "nvm" command rule
- "gcc" command rule
- "nvm install" command rule
- "head" and "tail" command rule
- "cat" command rule

**Fix Bug Issues**
- Resolve an issue about "dirs" command
- Modification code for "dirs" command
- Resolve an issue about "free" command

## Static Page
https://20-1-skku-oss.github.io/2020-1-OSS-11/

## Requirements

- python (3.4+)
- pip
- python-dev

## Installation

On OS X, you can install *The Fuck* via [Homebrew][homebrew] (or via [Linuxbrew][linuxbrew] on Linux):

```bash
brew install thefuck
```

On Ubuntu / Mint, install *The Fuck* with the following commands:
```bash
sudo apt update
sudo apt install python3-dev python3-pip python3-setuptools
sudo pip3 install thefuck
```

On FreeBSD, install *The Fuck* with the following commands:
```bash
pkg install thefuck
```

On ChromeOS, install *The Fuck* using [chromebrew](https://github.com/skycocker/chromebrew) with the following command:
```bash
crew install thefuck
```

On other systems, install *The Fuck*  by using `pip`:

```bash
pip install thefuck
```

[Alternatively, you may use an OS package manager (OS X, Ubuntu, Arch).](https://github.com/nvbn/thefuck/wiki/Installation)

<a href='#manual-installation' name='manual-installation'>#</a>
It is recommended that you place this command in your `.bash_profile`,
`.bashrc`, `.zshrc` or other startup script:

```bash
eval $(thefuck --alias)
# You can use whatever you want as an alias, like for Mondays:
eval $(thefuck --alias FUCK)
```

[Or in your shell config (Bash, Zsh, Fish, Powershell, tcsh).](https://github.com/nvbn/thefuck/wiki/Shell-aliases)

Changes are only available in a new shell session. To make changes immediately
available, run `source ~/.bashrc` (or your shell config file like `.zshrc`).

To run fixed commands without confirmation, use the `--yeah` option (or just `-y` for short, or `--hard` if you're especially frustrated):

```bash
fuck --yeah
```

To fix commands recursively until succeeding, use the `-r` option:

```bash
fuck -r
```
