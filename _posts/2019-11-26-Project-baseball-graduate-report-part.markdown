---
layout: post
title:  "학사 졸업 논문(kbo 다음시즌 OPS 예측 모델링)"
subtitle:   "학사 졸업 논문(kbo 다음시즌 OPS 예측 모델링)"
categories: Project
tags: school
comments: true
---

##### 현재 학사 졸업 논문으로 제작이 된 RandomForest Regressor 모형의 설명 및 코드 일부입니다

##### 모형 설명

모형 구축 데이터명(날짜) :  KBO_player_data_2019(2019.10)(스탯티즈 크롤링)

모형 구축 기간 : 2019.10 ~ 2019.11

목적 : KBO 다음 시즌 타자 성적(OPS) 예측

제안 목표 고객 : KBO팀 스카우터, KBO 선수, 야구 관계자

목적 변수 : YOPS(다음 시즌 타자 OPS)

변수 중요도 상위 6개 : 총 루타 수(TB), wOBA, 타점(RBI), 홈런(HR), isop, 현재 시즌 OPS

요약 : 선수들의 개인 성향 및 특징, 현재 시즌 타자들의 성적,

다음 시즌 공의 반발계수 등의 다음 시즌 특징 들을 활용하여

YOPS를 예측하고 MAE를 통해 확인한 RandomForest Regressor 모형입니다.


##### 사용 프로그램 : Python (Jupyter notebook)

##### 사용 방법 (시각화)

타석 위치 및 포지션 통합 작업 용 boxplot and bar plot

예상 핵심 변수(타수, 나이, war, 홈런) histogram and YOPS와의 scatter plot

목적변수에 대한 독립변수들의 상관계수 시각화 및 각 변수들 상관계수 heatmap

RandomForest Regressor 변수 중요도 세로 막대 그래프

##### 사용 방법 (모델링)

선수명 수집 -> 스탯티즈 크롤링 <http://www.statiz.co.kr/> 및 목적 변수(YOPS 생성)

-> 선수 성적 관련 변수 추가, 포지션 & 타석 위치 그룹화, 다음 시즌 공의 반발계수 반영

-> eda를 통한 OPS+ 일정 값 이하 이상치 제거, 

-> 모델링 비교 작업(linear regressor, RandomForest Regressor, XGBoost regressor)

-> 평가 방법 : MAE, 타수(AB) 가중치 RMSE, 50타수 이상 선수들 기준 MAE



### 코드 작성 링크 공유

- 코드 작성 인증 링크 공유

(코드가 너무 길어 깃허브 블로그에는 포스팅 하지 않습니다.)

<https://github.com/bluemumin/dongguk_university_graduate_report_baseball_OPS>

- 작성 학사 논문 (설명) 공개 여부 : x

- 데이터 수집 방법 및 크롤링 코드 공개 여부 : x

- 검색용 태그 :  isnull(), boxplot, barplot, hist, scatter, corr(), heatmap, MinMaxScaler(), itemgetter, .set_bbox, np.where, pd.get_dummies, .drop, grid_search.best_params_, mean_absolute_error, rmse, best_grid.feature_importances_, plt.barh
