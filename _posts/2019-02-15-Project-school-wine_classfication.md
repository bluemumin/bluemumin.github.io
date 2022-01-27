---
layout: post
title:  "와인 성분 데이터로 와인 품질 분류"
subtitle:   "와인 성분 데이터로 와인 품질 분류"
categories: Project
tags: University
comments: true
---

## Toy Project - 와인 품질 분류

- 사용언어 / 핵심 라이브러리
 <p> python / Pandas, matplotlib, seaborn, sklearn, LightGBM  </p>

- Background 
 <p> 와인 생산 중 더 좋은 품질의 와인을 생산하기 위해, 와인 성분 데이터로 와인의 품질 점수를 분류함</p>

- Summary
	<p>(1). Data Collection <br/>
		- 레드 와인 성분 + 와인 품질 [kaggle] </p>
	<p>(2). Data Preprocessing <br/>
		- EDA (독립변수 correlation plot, histogram, boxplot) <br/>
	        - binarization(와인품질 3~8점 / 5점 이하 -> low rank, 6점 이상 -> high rank) <br/>
		- Reduction (EDA 시각화 이후, 각 변수의 상위 5%의 이상치 값 제거)</p>
	<p>(3). Model & Algorithms <br/>
		- Logistic Regression, RandomForest, LightGBM <br/>
		  --> 기본 버전 및 paramter 개선을 통해 정확도, auc 개선 사항 확인 </p>
	<p>(4). Report & Review <br/>
		- 기본 버전 및 paramter 개선을 통해 정확도, auc 개선 사항 확인 <br/>
		- 전반적인 머신러닝 flow 학습 및 파이썬 기초 코딩 능력 습득 <br/>
		- 피드백 : 반응변수(와인 품질)에 대한 개선 방안 미 제시(ex - 변수 importance를 통한 변수 중요도 미 제시)<p/>
		
*보러가기: [와인 품질 분류 코드](https://github.com/bluemumin/wine_quality_classfication/blob/master/wine_quality_simple_classfication.ipynb)*

- 요약 내용

<img data-action="zoom" src='{{ "/assets/img/wine/summary.png" | relative_url }}' alt='absolute'>