---
title: "nvm install rules 추가 (2편)"
date: 2020-06-09 15:40:00 -0400
categories: thefuck
---

### nvm install 명령어 rules 추가

#### `<version>` 입력 시 `<version>`도 추천하도록 보완

이제 `nvm install`을 추천하게 되었지만, `<version>` 인자가 입력시에도 여전히 `nvm install` 만을 추천합니다. 

따라서 `<version>` 입력 시

- `nvm install <version>`와 같은 형식으로 추천하도록 합니다.

- 만약 `<version>`에 적절한 인자가 입력되지 않는 경우에는 예외처리를 합니다.

```python
def get_new_command(command):
	new_cmds = ["nvm"]
	nextcommand = []
	for e in command.script_parts[2:]:
		if e.replace('.', '', 2).isdigit():
		    nextcommand.append(e)
		else:
		    nextcommand = ["node"]
		    break	
	return [' '.join([new_command] + ["install"] + nextcommand) for new_command in new_cmds] 
```

[Node.js의 버전](https://nodejs.org/ko/download/releases/)들을 참고하면, 모두 `int.int.int` 형태를 띄고 있습니다. 따라서 `<version>` 입력시 .를 지우고 isdigit 함수를 사용하여 정수형이 맞는지를 확인합니다. 만약 오탈자가 입력된 경우, `nvm install node` 명령어를 추천하여 Node.js 최신 버전을 설치할 수 있도록 설계하였습니다.


관련 커밋은 [여기서](https://github.com/20-1-SKKU-OSS/2020-1-OSS-11/commit/c5edace794e2e06a7649e1ee6cc3103b972e3c82) 확인하실 수 있습니다.

&nbsp;&nbsp;&nbsp;&nbsp;
