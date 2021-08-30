---
layout: post
title:  "Oracle varchar2 to CLOB"
subtitle:   "Oracle varchar2 to CLOB"
categories: SQL
tags: Oracle
comments: true
---

## oracle에서 varchar2 타입을  CLOB로 바꾸는 방법을 포스팅 하려 합니다.

### 개요

oracle에서 하나의 varchar2 컬럼을 만들었을 때, 해당 컬럼의 하나의 값에 최대 입력 가능한

바이트의 수는 4000바이트이다. 보통 영어로는 4000자, 한글로는 2바이트로 취급해 2천자로

간단히 계산한다.

하지만, 해당 값에는 영어, 한글만 존재할 수 없다.(ex- 띄어쓰기, !, ? 등 특수 키)

그렇기에, varchar2로 컬럼을 만들었을 때, 너무 긴 값을 입력하고자 한다면,

varchar2가 아닌, 보통은 clob 컬럼으로 만들어서, 해당 4천 바이트 제한을 해결한다.

하지만, 보통은 varchar2로 만들어놓고, 문제가 생기면 그 때, 해결을 하는 방식을 선호한다.

clob로만 테이블 구성을 하면 당연히 편리하지만, 길이가 길지도 않은 테이블에 clob 방식으로

컬럼을 생성하는 것은 낭비가 아닐 수 없다.

### 본론

그렇기에, varchar2 -> clob로 바꿔야 하는 경우, 보통은 

"ORA-00910: 데이터형에 지정된 길이가 너무 깁니다."

를 보고 해결하는 경우 일 것이다.

먼저, 테이블 내에, 데이터 존재 유무에 따라 방법이 달라진다.

해당 컬럼의 파티션 설정, pk설정, 인덱스 설정 등은 배제하고 진행하고자 한다.

(경우의 수가 너무 많아진다.)

1. 테이블 내에 데이터가 없을 때

테이블에 데이터가 없다면, 구조만 있기에, 바로 clob 컬럼 타입으로 바꿔주면 된다.

보통은 varchar2 -> clob가 가능하다고 생각하겠지만,

varchar2 -> long -> clob로 바꿔줘야지 정상적으로 변경이 가능하다.

ALTER TABLE (스키마.)테이블명 modify 타입변경_컬럼 long; --varchar2 -> long

ALTER TABLE (스키마.)테이블명 modify 타입변경_컬럼 clob; --long -> clob

해당 쿼리를 실행시키면, varchar2는 clob 컬럼 타입으로 변경이 되게 된다.

<br/>

2. 테이블 내에 데이터가 있을 때,

데이터가 있는 상태에서 해당 1번 방식처럼 컬럼을 바꾸게 되면, 데이터에 문제가 발생할 수 있다.

그렇기에, 임시 컬럼을 만들고, 여기에 덮어 씌워야한다.

ALTER TABLE (스키마.)테이블명 ADD 타입변경_컬럼_temp clob; --임시 컬럼 생성

UPDATE (스키마.)테이블명 SET 타입변경_컬럼_temp = 기존_컬럼; --데이터 복제

ALTER TABLE (스키마.)테이블명 drop column 기존_컬럼; -- 기존 컬럼 및 데이터 drop

ALTER TABLE (스키마.)테이블명 rename column 타입변경_컬럼_temp to 기존_컬럼; --기존 컬럼 명으로 대체

이렇게 하게 되면 다 해결 된 것 처럼 보인다.

<br/>

하지만 이렇게 하면, 임시 컬럼은 맨 뒤에 위치하게 되므로,

테이블내, 컬럼 순서까지 똑같이 하려면 다음의 과정이 필요하다.

물론 데이터가 작다면, 테이블을 백업 방식으로 다시 만드는게 좋지만, 

그러면 pk, index 등의 작업은 다시 해야되고, 데이터가 크면 시도조차 하지 못한다.

(오라클 11이하 버전은 밑에 방법을 사용하지 못하니, 테이블 재생성을 하여야 한다.)

그렇기에, 컬럼 숨기기/숨김 해제로 처리를 하는 것이 좋다.("오라클 12c vesrion 이상만 가능")

ALTER TABLE (스키마.)테이블명 modify 기존_컬럼의_뒷컬럼1 INVISIBLE;

ALTER TABLE (스키마.)테이블명 modify 기존_컬럼의_뒷컬럼2 INVISIBLE;

....

ALTER TABLE (스키마.)테이블명 modify 기존_컬럼의_뒷컬럼1 VISIBLE;

ALTER TABLE (스키마.)테이블명 modify 기존_컬럼의_뒷컬럼2 VISIBLE;

....

mysql은 alter table 테이블명 modify column 신규_컬럼 after 이동할_위치의_앞_컬럼;

으로 해결이 되는데, oracle은 아직까지 invisible/visible로 해결 하여야 하는 듯 하다.

### 추가 사항(ALTER TABLE... INVISIBLE 쿼리 반복 작업 해결)

이러면 컬럼이 많을 때, 매 번 해야되는게 문제인데

이건 그냥, 문자 값들을 이어 붙여서 해결을 하는게 좋다.

(하단 추가 작성 중, 아직 수정 전임)

cf) (shift + \) 사용시, 표로 생성 되어 임시로 ii로 대체함.

select 'ALTER TABLE (스키마.)테이블명 modify ' ii column ii ' INVISIBLE;' as job1

from all_tab_columns

where 1=1 and table_name = "테이블명";

이런 식으로 ALTER TABLE 쿼리를 만들어서 사용하면 해결 된다.
