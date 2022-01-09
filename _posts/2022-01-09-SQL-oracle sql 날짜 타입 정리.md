---
layout: post
title:  "Oracle sql 날짜 타입 정리"
subtitle:   "Oracle sql 날짜 타입 정리"
categories: SQL
tags: Oracle
comments: true
---

## oracle DB에 사용 되는 날짜 관련 사항들을 정리하려 합니다.

<br/>

저는 python을 하면서도 날짜 컬럼을 다루는 것을 다른 컬럼들에 비해서

한 번 더 찾아보고 하는 경우가 많습니다.

그러한 이유가 생각보다 날짜 컬럼들은 세밀한 경우가 많습니다.

시간 없이 날짜만 담는 경우도 있고, 시간 초까지 다 같이 담는 경우가 있어서 입니다.

게다가 다른 컬럼들 보다는 나오는 빈도가 적기도 합니다.

하지만 시계열 데이터에서는 필수적으로 들어가야되는 컬럼 타입이고

DB에서는 이 컬럼을 기반으로 파티션을 만들거나, 데이터를 관리하기도 합니다.

그렇기에, 오늘 포스팅에서는 oracle DB에서 사용되는 날짜 타입들을 정리해보려고 합니다.

<br/>

### 1.DATE, TIMESTAMP

기본적인 날짜 컬럼 타입은 DATE입니다.

여기에 TIMESTAMP는 DATE 타입의 초까지가 아닌 초의 소수점까지 추가로 제어할 수 있는 타입입니다.

소숫점 단위로 하려면 보통 타입 지정 뒤에 FF를 더 붙여주면 됩니다.

ex) YYYY-MM-DD HH:MM:SS.FF4 (소숫점 4자리까지 표현)

만약 현재 시간을 입력할때는 DATE는 SYSDATE를

TIMSTAMP는 SYSTIMESTAMP를 사용하면 됩니다.

<br/>

### 2. 연산 방법

날짜타입의 기본적인 연산 방법은 숫자 타입과 동일합니다.

ex1) SYSDATE + 1/24/60/60 --1초 (=1일/24시간/60분/60초) 이런식 입니다.

대신 TIMESTAMP는 INTERVAL이라는 키워드로 해야 됩니다.

ex2) SYSTIMESTAMP + INTERVAL '10' SECOND

(MINUTE, HOUR, DAY 등으로도 변경해서 가능)

<br/>

### 3.함수 종류

날짜 타입의 경우 함수가 다양합니다.

NEXT_DAY(입력된 date 이후, 지정된 요일에 해당되는 값 반환),  / CF) 일 ~ 토 : 1 ~7 배정됨

ex1) select NEXT_DAY(DATE '2050-01-01', '화') -> 2050-01-04 00:00:00

ex2) select NEXT_DAY(DATE '2050-01-01', 3) -> 2050-01-04 00:00:00

<br/>

LAST_DAY(해당 date의 월말 반환),

<br/>

ADD_MONTHS(date, integer) (지정한 개월수 가감한 값 반환 / 단 월말일이면 월말일 반환함),

ex1) select ADD_MONTHS(DATE '2050-02-28', 1) -> 2050-03-31 00:00:00

<br/>

EXTRACT(YEAR, MONTH 등 원하는 날짜 정보 추출) 등이 있습니다.

<br/>

### 4.타입 변환 방법

다른 타입에서 날짜 타입으로 바꾸는 경우는 주로 TO_DATE, TO_TIMESTAMP를 사용해야 합니다.

여기서 이 다른 타입은 문자타입인 char 타입이어야되고, 포맷 지정이 필수입니다.

포맷지정이 되지 않으면 정확히 어느 날짜인지 인지를 못하기 때문 입니다.

ex1) SELECT TO_DATE('20050102', 'YYYYMMDD') -> 2005-01-02 00:00:00

ex2) SELECT TO_DATE('20050102123456', 'YYYYMMDD24MISS') -> 2005-01-02 12:34:56

<br/>

연도, 월 등 시간 format은 다음과 같습니다.

YYYY(연도 4글자), YY(2글자)

MM(월), DD(일), DAY(요일)

HH(12시간 단위), HH24(24시간 단위), MI(분), SS(초)

<br/>

그리고 주로 사용되는 다른 포맷들은 아래와 같습니다.

'YYYYMMDD', 'YYYYMMDD24MISS', 'YYYY-MM-DD HH24:MI:SS' (- 대신에 .으로도 가능)