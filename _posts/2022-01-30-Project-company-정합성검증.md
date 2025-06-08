---
layout: post
title:  "데이터 정합성 자동 검증 파이프라인 구축"
subtitle:   "데이터 정합성 자동 검증 파이프라인 구축"
categories: Project
tags: Company
comments: true
---

### 이기종 DB 간 데이터 마이그레이션 시, 

### 정합성 검증을 자동화한 파이썬 파이프라인 구축 프로젝트입니다.

[public version github link](https://github.com/bluemumin/python_another_db_check)

<br/>

### 1. 프로젝트 개요

- Member : 김경록
- Status : Complete
- 사용언어 : Python
- 핵심 라이브러리 : pandas, cx_Oracle, pyodbc, psycopg2 등
- DBMS 환경 : Oracle, MS SQL, PostgreSQL, DB2

<br/>

### 2. Why

데이터 웨어하우스(DW) 구축 과정에서, 

이기종 DB 간 대규모 데이터 마이그레이션이 자주 발생합니다. 

이때 데이터가 정확히 옮겨졌는지를 검증하는 작업은 필수입니다.  

하지만, 수동 검증은 비효율적이며 오류 발생 가능성이 높습니다. 

이에 따라 **정합성 검증을 자동화**하여, 

**데이터 정확성과 마이그레이션 품질**을 동시에 확보하는 

파이프라인을 개발하게 되었습니다.

<br/>

### 3. 주요 기능 및 구조

<img data-action="zoom" src='{{ "/assets/img/projects/db_check.png" | relative_url }}' alt='absolute'> 

<br/>

#### (1) DB 연결 및 데이터 불러오기
- 다양한 DBMS 간 통신을 위해 Python에서 DB 커넥터 통합
- Oracle, MSSQL, PostgreSQL, DB2 
  
  → 모두 pandas DataFrame으로 변환하여 처리 일관성 확보

#### (2) Too Big Table 필터링
- 레코드 수가 100만 건 이상인 대용량 테이블에 대해 효율적인 사전 필터링 수행
- 필요 시 사용자 정의 기준으로 검증 테이블 범위 설정 가능

#### (3) 컬럼 비교 및 정합성 검토
- 컬럼 이름 및 개수 비교
- 동일 테이블 구조가 아닐 경우 별도 알림 후 검증 중단 처리

#### (4) 데이터 타입 일치 확인 및 공백문자 정제
- 각 컬럼의 데이터 타입 일치 여부 확인
- DB별로 상이한 공백 처리, 문자열 포맷 등을 통일하여 비교 가능하도록 전처리

#### (5) 데이터 정합성 비교
- Source/Target 테이블 조인 후, 레코드 개수와 일치 여부 판단
- 네 가지 케이스로 결과 도출:
  - Case1: Source = Target (정합)
  - Case2: Source > Target (불일치)
  - Case3: Source < Target (불일치)
  - Case4: Source ≠ Target & 교집합 외 불일치 구간 존재

#### (6) 인코딩 문제 여부 탐지
- 한글/특수문자 등의 인코딩 문제 유무 자동 확인
- 문제 문자는 별도 리스트화하여 사용자 후처리 가능

<br/>

### 4. 결과 예시 및 반환 방식

- 결과는 JSON 및 Excel 형태로 반환 가능
- 검증 실패 시 에러 로그 및 실패 항목 자동 기록
- 주요 출력 예시:
  - `Source only count`, `Target only count`, `인코딩 문제 유무`, `검증 시간`

```text
ex Case : Source 1000건, Target 500건 → SRC 테이블 인코딩 문제 존재
→ SRC 인코딩 확인 필요, 검증 일시: 2021-04-14 18:00:00
```

<br/>

### 5. 프로젝트 한계 및 향후 개선 방향


기술적 개선

    Spark, Dask 등 분산 처리 도구와 연계하여 대용량 테이블 검증 속도 향상 가능

    Airflow 기반 스케줄링 도입으로 주기적 자동 검증 및 모니터링 확장

비즈니스 관점 개선

    CI/CD 파이프라인에 통합하여 배포 전 정합성 자동 점검 수행

    Data Catalog 및 Quality Report 자동 생성으로 사용자 신뢰도 향상 가능

사회적/윤리적 방향

    민감 데이터 이동 시 비식별화 처리 여부 검증 기능 추가 가능

    정합성 검증 결과에 대한 감사 로그 기능 확보로 컴플라이언스 준수 강화