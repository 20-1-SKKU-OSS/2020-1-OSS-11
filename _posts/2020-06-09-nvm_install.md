---
title: "nvm install rules 추가"
date: 2020-06-08 15:30:00 -0400
categories: thefuck
author: Jokuna
---

### nvm install rules 추가

#### 추가적인 NVM 명령어 보완

nvm에서 지원하는 명령어들은 많으나, 현재 nvm 명령어를 사용할 시, 오직 `nvm` 명령어만을 추천하고 있습니다. 따라서 이들 중 `nvm install <version>` 명령어를 지원하도록 rules를 추가하겠습니다.

#### 1. install 명령어 추천하도록 보완

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

그러면 다음과 같이 이제 `nvm install` 명령어를 추천해줍니다.(우선적으로는 `nvm` 명령어를 추천합니다.)

관련 커밋은 [여기서](https://github.com/20-1-SKKU-OSS/2020-1-OSS-11/commit/7c218f037b99c9eef829dbf85d395c86001ec935) 확인하실 수 있습니다.

&nbsp;&nbsp;&nbsp;&nbsp;
