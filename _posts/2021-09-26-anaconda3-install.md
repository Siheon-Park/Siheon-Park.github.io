---
title: "Anaconda3 설치하기"
categories:
    - set-up
    - ksop
tags:
    - anaconda
    - python
    - windows

excerpt: "운영체제: Windows"
layout: single

header:
  teaser: https://devopstuto-docker.readthedocs.io/en/latest/_images/continuumio_logo.png
  overlay_image: https://assets-cdn.anaconda.com/assets/company/anaconda-logo.png?mtime=20200723150109&focal=none
  overlay_filter: 0.5
  actions:
    - label: "Documentation"
      url: https://docs.anaconda.com/
---

## 들어가며

내가 가르치는 학생들이 재미있어 할만한게 무엇이 있을까 생각해보니 `Python`이 있었다.
체질이 코딩이어서 그런지 나는 `Python`이 정말 유용하고 재미있는 도구라고 생각한다.
어디서 무엇을 하던지 `Python`이랑 컴퓨터만 있으면 효율이 정말 많이 늘어난다.
특히 연구를 하는데 있어서 정말 빠질 수 없다.

`Anaconda`는 `Python`배포판으로 `Python` 패키지를 다른 가상환경에 독립적으로 설치할 수 있도록 해준다.
때문에 데이터 사이언스나 머신러닝을 연구하면서 `Anaconda`는 필수적이다.

## Anaconda 설치

이 포스트는 [anaconda 공식 문서](https://docs.anaconda.com/anaconda/install/windows/)를 기반으로 작성하였다.

1. [아나콘다 설치자 다운로드](https://www.anaconda.com/download/#windows)
2. 더블 클릭해서 설치자 실행
3. "다음(Next)" 클릭
4. 라이선스에 "동의함(I Agree)" 선택
5. "나만 설치(Just Me)" 선택
6. 아아콘다 설치할 폴더 설정. 왠만하면 건들지 말고 다음
   ![설치화면](https://docs.anaconda.com/_images/win-install-destination.png)

7. `PATH`환경변수에 아나콘다를 추가할지 결정. Windows의 경우 추천하지 않는다. 또, 아나콘다를 기본 파이썬으로 설정한다.
    ![환경변수설정](https://docs.anaconda.com/_images/win-install-options.png)
8. "설치(Install)"를 시작한다. 시간이 좀 걸리는 듯.
9. "다음(Next)" 클릭
10. *PyCharm*을 설치하라고 나오는데, 유료이다. 대신에 무료 버전인 [커뮤니티 에디션](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)을 설치할 수 있다. 개인적으로 파이썬을 사용할 때는 파이참이 가장 나은 에디터라고 생각한다. 아니면 개발자들 사이에서 인기인 [VSCode](https://code.visualstudio.com/)도 좋다. 파이참보다 가볍고 다른 언어도 다룰 수 있어 편리하다.

11. "끝(Finish)"
    ![끝](https://docs.anaconda.com/_images/win-install-complete.png)

## 설치 확인

- 아나콘다 네비게이터를 실행해보자. "시작"에서 "Anaconda Nevigator"를 실행한다.
    ![navi](https://docs.anaconda.com/_images/win-navigator.png)
- 아나콘다 프롬프트를 실행해보자. "시작"에서 "Anaconda Prompt"를 실행한다.
    ![prompt](https://docs.anaconda.com/_images/win-anaconda-prompt.png)