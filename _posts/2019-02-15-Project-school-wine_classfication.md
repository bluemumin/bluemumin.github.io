---
layout: post
title:  "와인 성분 데이터로 와인 품질 분류"
subtitle:   "와인 성분 데이터로 와인 품질 분류"
categories: Project
tags: University
comments: true
---

## 1. Toy Project - 와인 품질 분류

  - Member : 김경록

  - Status : Complete

  - 사용언어 : python 
  
  - 핵심 라이브러리 : Pandas, matplotlib, seaborn, sklearn, LightGBM

## 2. Why

와인의 성분에 따라서 맛이 변하고, 

이를 평가하는 사람들에게서 평가가 달라진다

그렇다면 최상급의 와인을 만들기 위해서 필요한 성분은 무엇이며,

사람이 아닌 시물레이션을 통해서 

이러한 품질을 분류할 수 있게 한다면

비용이 절감되지 않을까 라는 생각으로 출발하였다.

## 3. Data

[Kaggle 데이터](https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009) : 레드 와인 성분 + 와인 품질

## 4. 분석 방법

(a). Data Preprocessing

	- EDA (독립변수 correlation plot, histogram, boxplot)

	- 반응 변수 그룹화 : (와인품질 3~8점) / 5점 이하 -> low rank, 6점 이상 -> high rank

	- Data Reduction : EDA 시각화 이후, 각 변수의 상위 5%의 이상치 값 제거

(b). Model & Algorithms

	- Logistic Regression, RandomForest, LightGBM

	  --> 기본 버전 및 paramter 개선을 통해 정확도, auc 개선 사항 확인

(c). Report & Review

	- 기본 버전 및 paramter 개선을 통해 정확도, auc 개선 사항 확인

	- 전반적인 머신러닝 flow 학습 및 파이썬 기초 코딩 능력 습득

	- 피드백 : 모델링 이전 part에 집중하여, 
	
	  실제 머신러닝 개선을 복잡하고 다양하게 시도하는 방법은 미 시도 한채로 종료함.
		
*보러가기: [와인 품질 분류 코드](https://github.com/bluemumin/wine_quality_classfication/blob/master/wine_quality_simple_classfication.ipynb)*

- 요약 내용

<img data-action="zoom" src='{{ "/assets/img/wine/summary.png" | relative_url }}' alt='absolute'>