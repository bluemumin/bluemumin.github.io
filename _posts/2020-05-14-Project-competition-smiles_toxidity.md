---
layout: post
title:  "약물 분자 코드로 약물 독성 여부 분류"
subtitle:   "약물 분자 코드로 약물 독성 여부 분류"
categories: Project
tags: Competition
comments: true
---

## Competition - 약물 독성 분류

- 사용언어 / 핵심 라이브러리
 <p> python / Pandas, rdkit(분자구조 변환 라이브러리), LightGBM, sklearn </p>

- Background 
 <p> 신규 약 개발 시, 다양한 시물레이션 실행 및 비용 감축을 위해, 약물 분자 구조 약칭 데이터로 약물의 독성 여부 분류함 </p>

- Summary
	<p>(1). Data Collection <br/>
		- 사내 경진대회 데이터 제공[의약 데이터](데이터 외부 유출 금지로 미 업로드 및 관련 결과 삭제) </p>
	<p>(2). Data Preprocessing <br/>
		- 데이터 도메인 공부 (SMILES CODE 공부, 분자구조 벡터화 방식, 약물 성분 컬럼 내용) <br/>
		- 파생변수 추가(분자 구조 벡터화 방식 2종 추가, rdkit 라이브러리 활용 변수 추가)</p>
	<p>(3). Model & Algorithms <br/>
		- LightGBM --> 10-fold + parameter 추가 설정 <br/>
		- 모델 성능 검증 --> binary cross entropy 대신 f1_score 함수 구현 후 LightGBM 성능 개선에 사용<p/>
	<p>(4). Report <br/>
		- 최대한 단순한 구조로, 앙상블을 사용한 다른 수상작들과 f1_score가 차이 없는 모델 구현 <br/>
		- 관련 도메인 없는 데이터임에도, 충분한 리서치 후, 관련 라이브러리를 활용하여 파생 변수 생성 <p/>
	<p>(5). Review <br/>
		- 피드백 : 데이터 부족으로 overfitting 상태를 대회 마지막까지 충분하게 극복 실패함 <br/>
		- Futher Research : 의약 관련 도메인 추가 습득시, 모델에 더 효과적인 파생변수 생성 가능<br/>
		- 사내 경진대회 2등 수상 <p/>
		
*보러가기: [약물 독성 분류 코드](https://github.com/bluemumin/smiles_toxicity/blob/main/smiles_code_to_toxicity.ipynb)*