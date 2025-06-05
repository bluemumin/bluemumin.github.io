---
layout: post
title:  "한 장으로 보는 LightGBM 논문 요약"
subtitle:   "한 장으로 보는 LightGBM 논문 요약"
categories: Python
tags: ML
comments: true
---

## LightGBM 논문을 한 장으로 요약해본 게시물입니다.

개인적으로 모델링을 해야 할 때, 무조건 한 번은 사용해보는 알고리즘 이며,

캐글에서 핫했던 XGBoost의 가벼운 버전이라고 불리우는 LightGBM의 논문을 분석하고

한 장으로 요약을 해보는 시간을 가져보았습니다.

먼저 [논문 링크](https://papers.nips.cc/paper/2017/file/6449f44a102fde848669bdd9eb6b76fa-Paper.pdf) 입니다.

해당 논문을 읽으면서 보았던 참고 블로그들이 있는데 같이 게시합니다.

<br/>

[첫 번째 블로그](https://greeksharifa.github.io/machine_learning/2019/12/09/Light-GBM/) 의 경우, 핵심 알고리즘인 EFB에 대해서 이해가 처음에는 안됬었는데

해당 블로그를 보면서 이해를 하는데 도움을 많이 받았습니다.

<br/>

[두번째 블로그](https://aldente0630.github.io/data-science/2018/06/29/highly-efficient-gbdt.html) 의 경우는 아예 번역을 해놓으셔서 

제가 해석을 한 것과 번역된 것과 얼마나 차이가 있는지 보면서

읽을 수 있어서 좋았습니다.

<br/>

마지막으로 제가 논문을 읽은 이후에, 요약해서 만든 파일입니다.

<img data-action="zoom" src='{{ "/assets/img/one_picture/lgbm/한장lgbm.jpg" | relative_url }}' alt='absolute'>

대부분의 머신러닝, 딥러닝 계열 논문들이 영어이고

특히 각 모델별 핵심 알고리즘의 경우에는 시간이 지나면 헷갈리는 경우가 많기에

이렇게 한 장으로 요약을 해놓으면 어떨까 라는 생각으로 시작하게 되었습니다.

NP-Hard, 랭킹쪽을 평가하는 방법 중 하나인 NDCG도 추가로 공부할 수 있었고

AdaBoost기반이 왜 Down Sampling이 안 되는지 공부할 수 있었습니다.

AdaBoost의 경우는 이 [블로그](https://bkshin.tistory.com/entry/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-14-AdaBoost) 가 정말 정리가 잘 되어 있다고 생각하였습니다.

다음은 XGBoost 논문 요약을 할 계획이며, 일주일에 한 번 정도는 요약하는 게시물을 작성하려고 합니다.

감사합니다.
