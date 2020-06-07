---
title: "이전 dirs 코드 기여 보완 (modify)"
date: 2020-06-07 21:15:00 -0400
categories: thefuck
---

### 이전 dirs 코드 기여 보완 (modify)

```bash
from difflib import SequenceMatcher

def match(command):
    if SequenceMatcher(None, command.script_parts[0], "dirs").ratio() > 0.6:
        return 1
    else:
        return 0

def get_new_command(command):
    return "dirs"
```
전에 기존의 fuck 잡아내지 못하는 dirs 명령어를 찾는 코드를 commit 했었습니다.

dirs 명령어가 뒤에 argument를 가질 수 있다는 것을 인지하지 못했었고

dirs 명령어가 제대로 들어왔을 때 dirs를 추천하는 것이 아닌

다른 pool의 명령어를 추천해야한다고 판단했습니다.

따라서 이에 대한 반영 코드를 수정했습니다.

```bash

from difflib import SequenceMatcher

def match(command):
    if SequenceMatcher(None, command.script_parts[0], "dirs").ratio() == 1:
        return 0
    if SequenceMatcher(None, command.script_parts[0], "dirs").ratio() > 0.6:
        return 1
    else:
        return 0

def get_new_command(command):
    new_cmds = ["dirs"]
    return [' '.join([new_command] + command.script_parts[1:])
            for new_command in new_cmds]
```

코드에서 바뀐 점은 크게 두 가지입니다.

기존 단순히 dirs를 리턴했다면 위의 코드는

join과 command.script_parts[1:]를 이용한

완전한 명령어와 command form을 갖추게 했습니다.

두번째는 완전한 dirs가 들어올 경우로

이 경우는 return 0를 보내 다른 추천 명령어를 찾게 했습니다.

### dirs.py 수정 후 결과 화면

![11](https://user-images.githubusercontent.com/63634948/83968346-833c8900-a903-11ea-9f62-4f9675029935.png)

![22](https://user-images.githubusercontent.com/63634948/83968347-86377980-a903-11ea-86a3-dfc49e9c211a.png)

![33](https://user-images.githubusercontent.com/63634948/83968351-8899d380-a903-11ea-94e4-3e0d96034a64.png)

추가 인자를 정상적으로 받는 것을 확인할 수 있으며

dirs가 들어가는 경우는 다른 추천 명령어가 뜹니다.


[commit_dirs_link](https://github.com/20-1-SKKU-OSS/2020-1-OSS-11/commit/867109df6c8f601fe2b7a737b9d08ded2fa68a64)



