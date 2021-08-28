---
layout: post
title:  "Oracle SQL VS ANSI SQL"
subtitle:   "Oracle SQL VS ANSI SQL"
categories: SQL
tags: Oracle
comments: true
---

## 표준 문법 SQL과 Oracle SQL간의 문법 차이에 대해서 간단히 나타내고자 합니다.

해당 글을 포스팅 하는데 굉장히 오랜 시간이 들었네요

테이블 형식으로 된 글을 포스팅 하려고, 해당 글을 만들어 놓고

해야지 해야지 생각은 다른 글들을 포스팅 할 때마다 했는데

ADP하면서 밀리고, 사내 경진대회 나가면서 밀리고, 쉬면서 밀리고

좀 많이 밀렸었네요.

막상 또 테이블 형식으로 포스팅 해보니, 만드는데 엄청 힘들고

다 만들고 테스트 해보니 모양도 안 이쁘네요.

<br/>

첫 번째 - 줄은 Oracle, 두 번째 - 줄은 ANSI SQL입니다.

세번째 - 줄은 비고 설명입니다.


1.  NULL 확인 방법

- NVL(컬럼,'')

- IFNULL(컬럼,'')

2. 현재 날짜 입력

- SYSDATE

- NOW()

3. 날짜포맷 -> string

- TO_CHAR(컬럼,'YYYYMMDDHH24MISS')

- DATE_FORMAT(컬럼,'%Y%m%d%H%i%s')

- ANSI(%y = 2자리)

4. 요일 숫자 범위

- 일요일=1, 토요일=7

- 일요일=0, 토요일=6

- oracle은 보통 -1해서 ANSI와 동일하게 사용

5. 문자 합칠때

- '%'||'k'||'*'

- concat('%','k','*')

6. 문자형으로 변환

- TO_CHAR(632)

- CAST(632 AS CHAR)

7. 페이징 처리

- where rownum between 0 and 10

- from table limit 0,10

8. 시퀀스 사용시, 다음 번호 호출

- 시퀀스명.NEXTVAL

- 시퀀스명.CURRVAL

9. alias 사용
- as 'alias명' or alias명 or as alias명

- as alias명 or alias명

- ANSI는 alias명 자동 대문자

10. 문자형 자르기

- SUBSTR(문자열,1,10)

- SUBSTR(문자열,1,10) + left(문자열,3), right(문자열,3)

- (+는 추가 기능)

11. 저장프로시저 있는지 파악 후, create

- create or replace procedure 프로시저명

- drop procedure if exists 프로시저명; create procedure 프로시저명

- 12. 예약어가 컬럼명 일때

- 컬럼명을 따옴표로 감싸기(select "column" from tab)

- 컬럼명을 tab 위 ' ` '키로 감싸기

13. IF구문

- DECODE(조건식,일치 조건 값, 참 반환 값,거짓 반환 값)

- IF(조건식,참 반환 값, 거짓 반환 값)

- (다중 조건인 CASE는 동일하게 사용)

14. JOIN 방법

일반적 join  

- inner join(두 테이블 내 일치)

- outer join (left, right, full)

- cross (모든 경우의 수 고려)(조건 기술 필요 없음)

- self (자기자신과 join, alias로 지정 반드시 권유)

  이유 : Hierachical structure -> flat structure 변경) (성능 고려 x 가능)

차이점 :

- ANSI는 테이블을 하나씩 붙임.

  select * from A inner join B on A.column1 = B.column1

  inner join C on A.column2 = C.column2

- Oracle은 모든 table은 from절, 조건은 where

  join 당하는 테이블은 (+) 표기

  ex) from I1, I2 where I1.column1 = I2.column1(+)

이번 연도에는 Oracle sql만 주구장창 사용을 해와서

가끔씩 표준 형식 sql을 사용하는 DBMS들을 사용할 때 불편함이 있어서

차이점을 찾아보고 정리를 해보았습니다.

간단히 요약만 해본 것이고, 제가 다른 블로그들을 보고 해보긴 해보았지만, 

엄청 자세하게 조사를 해보지는 못하여 잘못된 정보가 있을 수 있으니

참고용으로 보시는 것을 추천드립니다.

감사합니다.
