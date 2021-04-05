---
layout: post
title:  "프로젝트 외부 작업물 모음(Kaggle)"
subtitle:   "프로젝트 외부 작업물 모음(Kaggle)"
categories: Project
tags: etc
comments: true
---

## 현재 본인이 작업하였지만 외부에 게시된 프로젝트 모음입니다.

<br/>

### KBO 야구 OPS 예측 학사 논문 및 데이터

한국 프로 야구의 타자들의 연간 OPS를 예측하는 프로젝트

결과물 : <https://github.com/bluemumin/dongguk_university_graduate_report_baseball_OPS>

데이터 : <https://www.kaggle.com/bluemumin/kbo-baseball-for-kaggle>

6회때 진행되었던 KBO 데이터를 스탯티즈에서 크롤링 하는 방식으로 데이터를 가져온 뒤에,

학사 졸업 논문으로 작성하였던 결과물

일단 가장 큰 결론은 타수 적은 선수들을 빼고 한 50타수 정도 되는 선수들로 결론을 내야지

약 0.06정도의 OPS 차이를 보인다는 점

<br/>

### Wine 데이터 Python 모델링 비교

와인의 맛 평가를 성분을 통해서 분류해내는 toy proejct

결과물 : <https://github.com/bluemumin/baf_kaggle_wine_project>

데이터 : <https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009>

캐글 노트북 

단순 EDA : <https://www.kaggle.com/bluemumin/wine-eda-for-korean-user>

단순 모델링 비교 : <https://www.kaggle.com/bluemumin/wine-modeling-for-korean-user> 

19년도 1학기에 진행하였던 wine data를 이용하여서 회귀분석을 한 작업물 대신에,

캐글에서의 wine data를 활용하여, 높은 등급, 낮은 등급을 분류해내는 모델링을

단순한 튜토리얼 식으로 구성하였다. 설명이 자세한 튜토리얼은 아니지만

<https://www.kaggle.com/vishalyo990/prediction-of-quality-of-wine> 같은 튜토리얼도

특별히 많은 설명이 없기 때문에, 캐글 게시를 위해 가볍게 작업하여 결과물을 올렸다.

<br/>

### 텔레마케팅 데이터 활용 정기 예금 가입 분류

포르투갈의 2000년대 후반 텔레마케팅 가입 여부 분류를 위한 toy project

데이터 : <https://www.kaggle.com/yufengsui/code>

단순 EDA : <https://www.kaggle.com/bluemumin/bank-data-eda>

당시 실행 코드 (R + SAS) : <https://github.com/bluemumin/data_mining_telephone_marketing_with_R>

해당 토이 프로젝트의 경우, 4학년 1학기에 진행한 데이터 마이닝 수업에서의 내용으로

현재는 파이썬만 활용하기 때문에, 해당 코드를 수정하는데 시간을 할애하기가 힘들어

당시 내용만 깃허브에 게시하고, 캐글에는 EDA부분만 게시를 하였다.

train, test의 비율이 거의 9 : 1로 했을때 정확도는 거의 83%였으며,

다른 캐글 유저의 경우, 정확도가 더 높지만, 해당 데이터는 불균형이 좀 심한 상태이고

정확도 이외의 지표의 점수가 좋지 않기 때문에, 적절히 구축이 되었다고 판단이 된다.

<br/>

### SMILES Code to Toxicity

약물의 SMILES Code를 통해서 약물의 독성 여부를 판별해내는 toy project

추가 예정