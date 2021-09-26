---
title: "Github Pages 만들기"
categories: 
    - "github-pages" 
tags: 
    - "ruby"
    - "jekyll"
    - "minimal-mistakes"
excerpt: 깃허브 페이지를 만들어보자
header:
  teaser: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
---

연구하면서 이것저것 잡다하게 얻은 지식을 정리해보려고 블로그를 시작하게 되었다. 내친 김에 github page를 만들게 되었다.

## 1. *minimal_mistakes* 테마 가져오기

github page를 처음 만들게 되면 정말 아무것도 없다. 그래서 남이 만들어 놓은 밥상에 숟가락을 올려야 편하다.

1. [이 깃헙 링크](https://github.com/mmistakes/minimal-mistakes)를 내 repo로 fork한다. 참고로 fork와 clone의 차이점은 [여기](https://www.toolsqa.com/git/difference-between-git-clone-and-git-fork/)에 있다.
2. 가져온 repo의 이름을 `{username}.github.io`로 바꾼다. 이름 형식을 통해 Page임을 판별하는 것 같다.
3. 깃허브 repo 페이지 옆에 Deployment를 클릭해서 내가 만든 Page에 접속한다. 또는 걍 [*https://`username`.github.io*](https://siheon-park.github.io/404)로 들어가도 된다.

## 2. 로컬에서 보기

테마를 가져온 것은 가져온 거고, 수정을 해야한다. github에서 수정할 수도 있지만, 수정 후 랜더링하는데 딜레이가 있어서 로컬에서 돌리는 것이 편하다. *minimal_mistake*는 *jekyll*을 이용하는데, 이게 `ruby`로 작성되었다. 그래서 `ruby`를 설치해야한다. 다행이 Mac에는 루비가 기본적으로 설치되있지만, 시스템 기본을 사용하게 되면 앞의 과정에서 `Gem::FilePermissionError`가 발생한다. 해결방법은 [이 포스트](https://jojoldu.tistory.com/288)를 참고한다.

1. `ruby` 환경 만들기

    `brew`로 `rbenv` (conda같은 거)를 설치한다.

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % brew update
    (base) shaun@shaunui-MacBookPro ~ % brew install rbenv
    ```

    잘 설치되었는지 확인한다.
    시스템 기본 ruby를 사용중일 것이다.

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % rbenv versions  
    * system (set by /Users/shaun/.ruby-version)
    ```

    상위 버전의 Ruby가 설치 가능한지 알아본다.

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % rbenv install -l
    2.6.8
    2.7.4
    3.0.2
    jruby-9.3.0.0
    mruby-3.0.0
    rbx-5.0
    truffleruby-21.2.0.1
    truffleruby+graalvm-21.2.0
    ```

    나는 `3.0.2` 버전을 선택했다.

    ```zsh
    rbenv install 3.0.2
    ````

    설치된 버전을 확인하자

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % rbenv versions  
    *  system
    3.0.2 (set by /Users/shaun/.ruby-version)
    ```

    이제 시스템 기본 ruby를 바꾼다. (c.f. `local`로 해도 되는듯?)

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % rbenv global 3.0.2
    (base) shaun@shaunui-MacBookPro ~ % rbenv versions    
    system
    * 3.0.2 (set by /Users/shaun/.ruby-version)
    ```

    마지막으로 `PATH`에 추가하기 위해 쉘 설정파일을 고친다. 나는 **맥북프로**이기 때문에 zsh를 사용해서 `.zshrc`를 수정했다.

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % vim ~/.zshrc
    ````

    이 문장을 추가한다.

    ```zsh
    [[ -d ~/.rbenv  ]] && \
      export PATH=${HOME}/.rbenv/bin:${PATH} && \
      eval "$(rbenv init -)"
    ```

    쉘 재시작

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % source ~/.zshrc
    ````

2. `bundle`, &nbsp;`jekyll` 설치하기

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % gem install bundle jekyll
    ```

    여기서 `Gem::FilePermissionError`가 발생했다면 [위 부분](#2-로컬에서-보기)를 다시 읽어보자

    (c.f. 만약 추후에 이상하게 안되면 `gem 'github-pages'`를 시도해보자)

3. remote에서 가져오기

    [위](#1-minimal_mistake-테마-가져오기)에서 만든 repo를 로컬로 가져와야 한다.

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % git clone https://github.com/{username}/{username}.github.io.git
    ````

4. 로컬 서버로 미리보기

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % bundle install
    (base) shaun@shaunui-MacBookPro ~ % bundle exec jekyll serve --livereload
    ```

    만약 `ruby`버전이 3 이상이라면 `Load error: cannot load such file – webrick`가 발생할 것이다. `ruby3`부터는 `bundle install`했을때 자동으로 `webrick`이 설치되자 않아서 발생하는 문제이다. 이것만 추가로 설치해준다.

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % bundle install
    (base) shaun@shaunui-MacBookPro ~ % bundle add webrick
    (base) shaun@shaunui-MacBookPro ~ % bundle exec jekyll serve --livereload
    ```

    브라우저 주소창에 [localhost:4000](http://localhost:4000) 으로 접속하면 페이지 미리보기가 가능하다.

## 3. 로컬에서 수정하기

기본적으로 _config.yml 파일을 수정하여 프로필을 만드는 등의 설정을 할 수 있다.
포스트를 추가하고 싶으면_post 폴더에 `.md` 형식의 문서를 작성하면 된다. 기본적으로 `.md`의 제목은 `YYYY-MM-DD-TITLE.md`의 형식으로 주어여 `jekyll`이 알아듣는다. 뭐 다른 사소한 것들은 [내 github.io repo](https://github.com/Siheon-Park/Siheon-Park.github.io)를 탐구해봐라.

수정한 파일을 `git` 으로 remote 저장소에 올리면 끝!

```zsh
    (base) shaun@shaunui-MacBookPro ~ % git add --all
    (base) shaun@shaunui-MacBookPro ~ % git commit -m "init"
    (base) shaun@shaunui-MacBookPro ~ % git push
```

## 4. 느낀점

어찌보면 편하고 어찌보면 불편하다... 깃허브의 네임벨류를 믿고 쓰고 있지만 `HTML`, `MARKDOWN`, `RUBY` 등에 익숙하지 않은 사람이면 참 어렵다. 솔직히 markdown 형식도 vscode로 보는 것과 비교하면 너무 못생겼다?
