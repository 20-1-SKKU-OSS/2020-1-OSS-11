---
title: "The Fuck 설치 가이드"
date: 2020-05-23 12:00:00 -0400
categories: thefuck
---

### 설치 가이드

이번 설치가이드는 Ubuntu 18.04을 기준으로 작성이 되었습니다.

Ubuntu에서 다음과 같은 명령어를 통해 설치를 진행할 수 있습니다.

```bash
sudo apt update
sudo apt install python3-dev python3-pip python3-setuptools
sudo pip3 install thefuck`
```

그 후 `eval "$(thefuck --alias)"` 문구를 `.bashrc` 파일에 작성한 후

마지막으로 
```bash
source ~/.bashrc
```
명령어를 치면 바로 사용할 수 있습니다.

### 최신 버전으로 업데이트

최신 버전으로 업데이트 하기 위해서는 

```bash
pip3 install thefuck --upgrade
```


참고 문헌 [The Fuck installation](https://github.com/nvbn/thefuck#installation)