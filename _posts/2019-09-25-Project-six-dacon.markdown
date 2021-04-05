---
layout: post
title:  "데이콘 6회 KBO 타자 OPS 모델링/시각화 대회"
subtitle:   "데이콘 6회 KBO 타자 OPS 모델링/시각화 대회"
categories: Project
tags: etc
comments: true
---

## 처음으로 수상한 개인 프로젝트 입니다

### 대회 진행 기간

2019/02/15 ~ 2019/03/31 (모델링)

2019/07/20 ~ 2019/07/30 (시각화)

### 수상 내역 : 데이콘 6회 KBO 타자 OPS 모델링/시각화 대회 시각화 부문 1등

### 사용 프로그램 : Python (Jupyter notebook)

### 사용 방법 (모델링)

스탯티즈 사이트 크롤링 <http://www.statiz.co.kr/> 및 결측치 제거, 모델링 용도 목적변수 생성,

경기수 미달 선수 이상치 처리 작업

모델링 비교 작업(회귀, 랜덤포레스트 회귀, SVR, XGBoost regressor) 등

### 사용 방법 (시각화)

사용 데이터 결측치 현황 시각화, 각 변수 boxplot or histogram, 

다음 시즌 OPS와 선수 개인 변수 간의 인사이트 구축

### 수상 관련 사항

- 수상 인터뷰 및 등수 공유

	인터뷰 : <https://dacon.io/more/interview/43>

	(public ranking) (18/94등) (19.07.19)

	(Final Visualization Ranking) (1/17등) (19.08.29)
    
### 기타 사항

사이트가 개편되면서 이전에 6회 대회가 나누어지면서 코드를 본인들도 잃어버렸는지

해당 대회를 들어가보면 1등으로 기록은 되어있지만, 코드는 없는 상황이다.

문제는 나도 노트북이 고장이 나서 포맷하느라 plotly로 해놓은 1등 자료는 다 날아가버린 상황이다.

해당 plotly를 이용하여서 시각화 하는 방법은 

나중에 KBO 예측 논문 자료를 작성한 것을 바탕으로 그나마 살려볼 생각이다.