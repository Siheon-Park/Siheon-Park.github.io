---
title: "conda 사용법"
categories:
    - set-up
    - ksop
tags:
    - anaconda
    - python
    - windows

excerpt: "conda 사용법"
layout: single

header:
  teaser: https://devopstuto-docker.readthedocs.io/en/latest/_images/continuumio_logo.png
  overlay_image: https://assets-cdn.anaconda.com/assets/company/anaconda-logo.png?mtime=20200723150109&focal=none
  overlay_filter: 0.5
  actions:
    - label: "Documentation"
      url: https://docs.anaconda.com/
---

## 선행 포스트

[아나콘다 설치방법]({% post_url 2021-09-26-anaconda3-install %})

## conda 사용법

1. `conda` 버전보기

   ```zsh
   (base) shaun@shaunui-MacBookPro ~ % conda -V
    conda 4.10.1
   ```

2. `conda` 업데이트

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % conda update conda
    Collecting package metadata (current_repodata.json): done
    Solving environment: done
    .
    .
    .
    ```

3. 새로운 가상환경 만들기/지우기

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % conda env create -n ksop
    Collecting package metadata (repodata.json): \ 
    .
    .
    .
    ```

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % conda env remove -n ksop
    
    Remove all packages in environment /Users/shaun/anaconda3/envs/ksop:
    ```

4. 만든 가상환경 보기

    ```zsh
    (base) shaun@shaunui-MacBookPro ~ % conda env list
    # conda environments:
    #
    base                  *  /Users/shaun/anaconda3
    ksop                     /Users/shaun/anaconda3/envs/ksop
    ```

5. 가상환경 활정화하기/비활성화하기

   ```zsh
   (base) shaun@shaunui-MacBookPro ~ % conda activate ksop
   # base 에서 ksop로 바뀜!!
   (ksop) shaun@shaunui-MacBookPro ~ % conda deactivate ksop
    ```
   
6. 패키지 설치하기/제거하기

    ```zsh
    (ksop) shaun@shaunui-MacBookPro ~ % conda install numpy
    ```

    ```zsh
    (ksop) shaun@shaunui-MacBookPro ~ % conda remove numpy
    ```

7. 주피터 노트북 실행

    ```zsh
    (ksop) shaun@shaunui-MacBookPro ~ % conda install jupyter notebook
    Collecting package metadata (current_repodata.json): done
    Solving environment: done
    .
    .
    .
    (ksop) shaun@shaunui-MacBookPro ~ % jupyter notebook
    ```

## (추가) jupyter kernel 설치/삭제

```zsh
# 설치
(ksop) shaun@shaunui-MacBookPro ~ % python -m ipykernel install --user --name ksop --display-name "KSOP"
Installed kernelspec ksop in /Users/shaun/Library/Jupyter/kernels/ksop
```

jupyter notebook 실행 후 화면

<img src = "/assets/images/Screen Shot 2021-10-08 at 6.13.17 PM.png" width="40%">

```zsh
# 삭제
(ksop) shaun@shaunui-MacBookPro ~ % jupyter kernelspec uninstall ksop
Kernel specs to remove:
ksop                	/Users/shaun/Library/Jupyter/kernels/ksop
Remove 1 kernel specs [y/N]: y
[RemoveKernelSpec] Removed /Users/shaun/Library/Jupyter/kernels/ksop
```

이렇게 하면 매번 `conda activate 가상환경이름` 을 명령하지 않아도 Jupyter Notebook에서 Kernel만 바꾸어서 원하는 환경을 선택할 수 있다. 
