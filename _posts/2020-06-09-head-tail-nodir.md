---
title: "head, tail dir rule 추가"
date: 2020-06-09 20:17:00 -0400
categories: thefuck
---

## head [directory] 

사용자가 head나 tail 명령어를 directory에 수행 할 경우 다음과 같은 에러가 발생합니다.

fuck 명령어를 쳐도 head나 tail을 directory에 하는 경우에 대한 rule이 없기 때문에 다음과 같이 "No fucks given" 이라는 메세지를 출력합니다.

<img width="346" alt="스크린샷 2020-06-09 오후 8 20 09" src="https://user-images.githubusercontent.com/63663300/84141773-a778a100-aa8e-11ea-9225-17fffe2dcfaf.png">

기존 vanilla the fuck 코드를 보면 rule에 cat을 directory에 수행 할 경우 ls 명령어로 대체하여 해결하였습니다.

이 점을 참고하여 head와 tail도 마찬가지로 단순히 명령어를 ls로 변경시켜주는 rule을 추가하였습니다.

## Code

<img width="510" alt="스크린샷 2020-06-09 오후 8 23 16" src="https://user-images.githubusercontent.com/63663300/84142154-41d8e480-aa8f-11ea-93c9-65123e6b127b.png">

<img width="503" alt="스크린샷 2020-06-09 오후 8 23 32" src="https://user-images.githubusercontent.com/63663300/84142157-456c6b80-aa8f-11ea-92c9-c508ee3babb6.png">

사용자가 입력한 커맨드에 대한 에러 메세지가 head나 tail로 시작되고 첫번째 아규먼트가 directory인 경우 fuck으로 주어진 rule이 실행됩니다.

단순히 head, tail을 ls 명령어로 바꿔줍니다.

## Result

<img width="344" alt="스크린샷 2020-06-09 오후 8 24 27" src="https://user-images.githubusercontent.com/63663300/84142220-5ddc8600-aa8f-11ea-8c12-bac74d317256.png">

다음과 같이 head 명령어를 directory에 대해 수행할 경우 ls directory로 변경하여 수행해줍니다.
