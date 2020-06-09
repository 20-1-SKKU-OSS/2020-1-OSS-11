---
title: "cat not exist file rule 추가"
date: 2020-06-09 20:30:00 -0400
categories: thefuck
---

## cat [not exist file] 

사용자가 cat 명령어를 존재하지 않는 파일에 대해 수행할 경우 다음과 같은 에러가 발생합니다.

fuck 명령어를 쳐도 cat을 존재하지 않는 파일에 하는 경우에 대한 rule이 없기 때문에 다음과 같이 "No fucks given" 이라는 메세지를 출력합니다.

<img width="357" alt="스크린샷 2020-06-09 오후 8 33 04" src="https://user-images.githubusercontent.com/63663300/84142815-70a38a80-aa90-11ea-9e52-9498f2ca4dd0.png">

리눅스 환경에서 코딩을 하다가 존재하는줄 알았던 파일에 대해 cat 명령어를 수행했다가 존재하지 않는 파일일 경우 바로 vim 에디터로 해당 파일을 생성하고 편집할 수 있도록 rule을 추가하였습니다.

## Code

<img width="531" alt="스크린샷 2020-06-09 오후 8 33 41" src="https://user-images.githubusercontent.com/63663300/84142875-8dd85900-aa90-11ea-9c16-2e1f1be691a4.png">

사용자가 입력한 커맨드에 대한 에러 메세지가 cat으로 시작되고 "No such file or directory"라는 메세지가 포함되는 경우 fuck으로 주어진 rule이 실행됩니다.

cat 명령어를 vim으로 바꿔줍니다.


## Result

<img width="361" alt="스크린샷 2020-06-09 오후 8 34 57" src="https://user-images.githubusercontent.com/63663300/84143113-f45d7700-aa90-11ea-82ad-b68f375af0c9.png">

다음과 같이 cat 명령어를 존재하지 않는 파일에 대해 수행할 경우 vim 에디터로 바로 그 파일을 생성하고 편집할 수 있게 해줍니다.
