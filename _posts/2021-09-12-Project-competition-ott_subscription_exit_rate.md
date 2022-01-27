---
layout: post
title:  "OTT 신규 구독자, 1달 뒤 재구독 여부 분류"
subtitle:  "OTT 신규 구독자, 1달 뒤 재구독 여부 분류"
categories: Project
tags: Competition
comments: true
---

## Competition - ott 재구독 여부 분류

- 사용언어 / 핵심 라이브러리
 <p> python(3.8) / Pandas, LightGBM </p>

- Background 
 <p> ott 신규 구독자의 3주간 시청 기록 활용, 1개월 뒤 재구독 여부를 사전 분류함.(이후 이탈 방지 혜택 부여) </p>

- Summary
	<p>(1). Data Collection <br/>
		- 그룹사 경진대회 데이터 제공[OTT 서비스 중 하나](데이터 외부 유출 금지로 미 업로드 및 관련 결과 삭제) </p>
	<p>(2). Data Preprocessing <br/>
		- EDA (고객 결제 사항 + 시청 기록 데이터) <br/>
	        - 변수 내 항목 간소화 (결제 코드, 결제 등록 기기, 컨텐츠별 시청 기기) <br/>
		- 파생변수 생성 (최신 컨텐츠 시청 기간 그룹화, 유저 컨텐츠 시청 퍼센트, 결제 후, 마지막 시청일자 gap 계산) <br/>
		- Reduction (유저별 과도한 컨텐츠 시청 수, 최신 컨텐츠 과다 시청 수 절삭)</p>
	<p>(3). Model & Algorithms <br/>
		- LightGBM 1차, 2차 수행 --> 최적의 parameter 확인(gridsearch + 5-fold) --> 최적의 threshold 확인(5-fold)  <br/>
		- Xgboost, Randomforest 모델링 후, ensemble 수행 --> 예측률 저하로 최종 제외 <br/>
	<p>(4). Report <br/>
		- LightGBM 결과 기반, 재구독 여부에 효과적인 변수 list 작성 <br/>
	        - 최종 등수 27/248(팀) 기록 (1등과 f1-score 0.01 차이) <br/>
		- 두 평가 기준인 f1-score와 accuracy의 차이가 없는 균형적 모델 작성</p>
	<p>(5). Review <br/>
		- 긍정적 사항 : 유저의 컨텐츠 시청 퍼센트(시청 시간/컨텐츠 길이) 파생 변수가 모델 개선에 효과적 <br/>
	        - 피드백 : 결제 후, 마지막 시청일자 gap보다, 1주차별 시청 시간의 증가/감소 여부가 더 효과적임을 예상함 <br/>
		- Futher Research : 해당 주차 드라마/영화 순위(외부 데이터) 활용한 인기 콘텐츠 선호도, <br/>
		&nbsp;+ (ott내 영화 추가 구매 여부, 코인 추가 거래 내역 등) 플랫폼 적극적 이용 수치 인사이트 개발 가능 예상 </p>
		
*보러가기: [ott 재구독 여부 분류 코드](https://github.com/bluemumin/ott_subscription_exit_rate/blob/main/ott_%EC%9E%AC%EA%B5%AC%EB%8F%85%EC%97%AC%EB%B6%80_%EB%B6%84%EB%A5%98.ipynb)*