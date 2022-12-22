---
layout: post
title:  "약물 분자 코드로 약물 독성 여부 분류"
subtitle:   "약물 분자 코드로 약물 독성 여부 분류"
categories: Project
tags: Competition
comments: true
---

## 1. Competition - 약물 독성 분류

  - Member : 김경록

  - Status : Complete

  - Tag : Competition

  - 사용언어 / 핵심 라이브러리 : python / Pandas, 
  
  	rdkit(분자구조 변환 라이브러리), LightGBM, sklearn

## 2. Why

 최근 제약 회사들은 신규 약 개발 시, 
 
 다양한 시물레이션 실행을 통해서 비용을 절감하고자 한다.
 
 이러한 시물레이션을 통해서 만들어진 약물의 분자구조로 
 
 약물의 독성 여부를 분류할 수 있는 모델이 있다면
 
 위험한 실제 약을 만드는 과정이 줄어들어 비용과 위험성을 줄어들게 할 수 있다.
 
## 3. Data

[사내 경진대회 데이터 제공] 

(데이터 외부 유출 금지 -> 미 업로드, 관련 결과 삭제)

## 4. 분석 방법

(a). Data Preprocessing
 
	- 데이터 도메인 공부 : SMILES CODE 공부, 분자구조 벡터화 방식, 약물 성분 컬럼 내용
	
	- 파생변수 추가 : 분자 구조 벡터화 방식 2종 추가, rdkit 라이브러리 활용 변수 추가
	
 (b). Model & Algorithms
 
	- LightGBM --> 10-fold + parameter 추가 설정
	
	- 모델 성능 검증 --> binary cross entropy 대신 
	
	  f1_score 함수 구현 후 LightGBM 성능 개선에 사용
	
 (c). Report & Review
 
	- 최종 등수 : 2등/97팀
	
	- 긍정적 사항 : 단일 LGBM 구조로, 앙상블 활용 수상작들과 f1_score가 차이 없는 모델 구현
	
	  + 관련 도메인 없지만 충분한 리서치 후, 관련 라이브러리를 활용한 파생 변수 생성
	
	- 피드백 : 데이터 부족 -> overfitting 상태 미 해결로 대회 종료
		
*보러가기: [약물 독성 분류 코드](https://github.com/bluemumin/smiles_toxicity/blob/main/smiles_code_to_toxicity.ipynb)*