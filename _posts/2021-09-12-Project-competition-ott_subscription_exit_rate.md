---
layout: post
title:  "OTT 신규 구독자, 1달 뒤 재구독 여부 분류"
subtitle:  "OTT 신규 구독자, 1달 뒤 재구독 여부 분류"
categories: Project
tags: Competition
comments: true
---

## 1. Competition - ott 재구독 여부 분류

  - Member : 김경록

  - Status : Complete
  
  - Tag : Competition

  - 사용언어 : python(3.8)
  
  - 핵심 라이브러리 : Pandas, LightGBM

## 2. Why

OTT 플랫폼에 신규 가입한 구독자의 3주간의 시청 기록을 활용하여, 

1개월 뒤 OTT 서비스를 다시 결제를 할 것인지를 사전 분류함.

## 3. Data

[그룹사 경진대회 데이터 제공] 

(데이터 외부 유출 금지 -> 미 업로드, 관련 결과 삭제)

## 4. 분석 방법

(a). Data Preprocessing 

	- EDA : 고객 결제 사항 + 시청 기록 데이터

	- 변수 내 항목 간소화 : 결제 코드, 결제 등록 기기, 컨텐츠별 시청 기기

	- 파생변수 생성 : 최신 컨텐츠 시청 기간 그룹화, 컨텐츠 길이 대비 시청 퍼센트, 
	
	  		 결제 후 마지막 시청일자 gap 계산

	- Data Reduction : 유저별 과도한 컨텐츠 시청 수 및 최신 컨텐츠 과다 시청 수 절삭

(b). Model & Algorithms

	- LightGBM 1차, 2차 수행 
	
	  --> 최적의 parameter 확인(with gridsearch + 5-fold) 
	  
	  --> 최적의 threshold 확인(with 5-fold)

	- Extra Try : Xgboost, Randomforest 모델링 후, ensemble 수행 
	
	   --> 예측률 저하로 최종 제외

(c). Report & Review

	- 최종 등수 : 27등/248팀 (1등과 f1-score 0.01 차이)

	- 긍정적 사항 : 컨텐츠 길이 대비 시청 퍼센트(시청 시간/컨텐츠 길이) 
	
			파생 변수 생성으로 모델 성능 향상

	- 피드백 : 결제 후, 마지막 시청일자 gap 파생변수 영향도 << 주차별 시청 시간 증가/감소 여부

	- Futher Research : 해당 주차 드라마/영화 순위(외부 데이터) 활용한 인기 콘텐츠 선호도,

		+ (ott내 영화 추가 구매 여부, 코인 추가 거래 내역 등) 
	
		플랫폼 적극적 이용 수치 인사이트 개발 가능 예상
		
*보러가기: [ott 재구독 여부 분류 코드](https://github.com/bluemumin/ott_subscription_exit_rate/blob/main/ott_%EC%9E%AC%EA%B5%AC%EB%8F%85%EC%97%AC%EB%B6%80_%EB%B6%84%EB%A5%98.ipynb)*