---
title: "nvm install rules 추가 (1편)"
date: 2020-06-09 15:30:00 -0400
categories: thefuck
---

### nvm install 명령어 rules 추가

#### 추가적인 NVM 명령어 보완

```bash
kuna@server:~$ nvm installl 12.18.0

Node Version Manager (v0.35.3)

Note: <version> refers to any version-like string nvm understands. This includes:
  - full or partial version numbers, starting with an optional "v" (0.10, v0.1.2, v1)
  - default (built-in) aliases: node, stable, unstable, iojs, system
  - custom aliases you define with `nvm alias foo`

  ...
  (중략)
  ...

Note:
  to remove, delete, or uninstall nvm - just remove the `$NVM_DIR` folder (usually `~/.nvm`)

kuna@server:~$ fuck
nvm [enter/↑/↓/ctrl+c]
```

nvm에서 지원하는 명령어들은 많으나, 현재 nvm 명령어를 사용할 시, 오직 `nvm` 명령어만을 추천하고 있습니다. 따라서 이들 중 `nvm install <version>` 명령어를 지원하도록 보완하겠습니다.

#### 1. nvm install 추천하도록 만들기

`nvm install` 명령어를 추천하기 위해 다음과 같이 nvm_install.py에 추가합니다.

```python
from difflib import SequenceMatcher

def match(command):
	if SequenceMatcher(None, command.script_parts[0], "nvm").ratio() > 0.6:
		return 1
	else:
	    return 0

def get_new_command(command):
	new_cmds = ["nvm"]
	return [' '.join([new_command] + ["install"]) for new_command in new_cmds]
```
입력 받은 명령어가 `nvm`과 유사도가 60% 이상일때 부터 `nvm install`가 추천됩니다.

```bash
kuna@server:~$ nvm installl 12.18.0

Node Version Manager (v0.35.3)

Note: <version> refers to any version-like string nvm understands. This includes:
  - full or partial version numbers, starting with an optional "v" (0.10, v0.1.2, v1)
  - default (built-in) aliases: node, stable, unstable, iojs, system
  - custom aliases you define with `nvm alias foo`

...
(중략)
...

Note:
  to remove, delete, or uninstall nvm - just remove the `$NVM_DIR` folder (usually `~/.nvm`)

kuna@server:~$ fuck
nvm install [enter/↑/↓/ctrl+c]
```


그러면 다음과 같이 이제 `nvm install` 명령어를 추천해줍니다.(우선적으로는 `nvm` 명령어가 추천되고 그 다음에 `nvm intall` 이 추천됩니다.)

위의 코드관련 커밋은 [여기서](https://github.com/20-1-SKKU-OSS/2020-1-OSS-11/commit/7c218f037b99c9eef829dbf85d395c86001ec935) 확인하실 수 있습니다.

&nbsp;&nbsp;&nbsp;&nbsp;
