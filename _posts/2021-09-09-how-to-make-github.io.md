---
title: "github.io 만들기"
categories: 
    - "setup" 
tags: 
    - "github"
    - "github-pages"
excerpt: 깃허브 페이지를 만들어보자
---

연구하면서 이것저것 잡다하게 얻은 지식을 정리해보려고 블로그를 시작하게 되었다. 내친 김에 github page를 만들게 되었다.

## 1. *minimal_mistake* 테마 가져오기

github page를 처음 만들게 되면 정말 아무것도 없다. 그래서 남이 만들어 놓은 밥상에 숟가락을 올려야 편하다. 

1. [이 깃헙 링크](https://github.com/mmistakes/minimal-mistakes)를 내 repo로 fork한다. 참고로 fork와 clone의 차이점은 [여기](https://www.toolsqa.com/git/difference-between-git-clone-and-git-fork/)에 있다.
2. 가져온 repo의 이름을 `{username}.github.io`로 바꾼다. 이름 형식을 통해 Page임을 판별하는 것 같다.
3. 깃허브 repo 페이지 옆에 Deployment를 클릭해서 내가 만든 Page에 접속한다. 또는 걍 [*https://{username}.github.io*]()로 들어가도 된다.

## 2. Ruby 설치하기

테마를 가져온 것은 가져온 거고, 수정을 해야한다. github에서 수정할 수도 있지만, 수정 후 랜더링하는데 딜레이가 있어서 로컬에서 돌리는 것이 편하다. *minimal_mistake*는 *jekyll*을 이용하는데, 이게 `ruby`로 작성되었다. 그래서 `ruby`를 설치해야한다. 다행이 Mac에는 루비가 기본적으로 설치되있지만, 시스템 기본을 사용하게 되면 오류가 난다. 그래서

1. `brew`로 `rbenv` (conda같은 거)를 설치한다.

    ```shell
    $ brew update
    $ brew install rbenv
    ```

2. asdf

    ```python
    for i in range(10):
        print(i)
    ```
