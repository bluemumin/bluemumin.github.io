---
layout: post
title:  "Oracle sql 기초 함수 정리"
subtitle:   "Oracle sql 기초 함수 정리"
categories: SQL
tags: Oracle
comments: true
---

## oracle DB에 있는 sql 내장 함수들을 정리하려 합니다.

<br/>

오라클 DB안의 다양한 내장 함수들 중 단일 행에 사용되는 기초적인 함수들을 정리해보려고 합니다.

이미 사용법은 아는게 많아서 자세한 설명 보다는 정리된 모음 위주라고 봐주시면 됩니다.

<br/>

### 1.문자 함수

LOWER(소문자 변경), UPPER(대문자 변경), INITCAP(첫 글자만 대문자),

L,RPAD(값, 늘이는 길이, 채울 값) L,R 방향으로 1번 값을 2번의 길이만큼 채울때 

3번의 값으로 채운다(3번은 기본이 NULL)

EX1) LPAP('AB',5,'12) -> '121AB'

<br/>

L,RTRIM(값, 삭제하고 싶은 문자) L,R 방향으로 2번의 문자열이 있으면 제거, 기본은 공백만 제거

SUBSTR(글자 자르기), REPLACE(글자 변환), TRANSLATE(특정 위치에 대응되는 값 변환)

INSTR(선택한 문자의 시작 위치 반환, 없으면 0), LENGTH(길이 반환)

<br/>

### 2.숫자 함수

ABS(절대값 반환), SIGN(+, - 부호 반환, 0은 0), ROUNG(반올림), 

TRUNC(숫자1, 숫자2) 숫자1을 숫자2의 숫자 단위까지 버린다 

EX1) TRUNC(15.59, 1) -> 15.5,  TRUNC(15.59, -1) -> 10

<br/>

CEIL(올림), FLOOR(버림), MOD(나머지 반환, 분모가 0이면 첫 입력값 반환),

REMAINDER(나머지 반환, 분모가 0이면 에러 반환),

POWER(거듭제곱 값 반환), SQRT(제곱근), EXP(e의 N제곱 반환), 

LN(자연로그), LOG(로그 값 반환)

<br/>

### 3.NULL 관련 함수

NVL(값1, 값2) 값1이 NULL이 아니면 값1, NULL이 맞으면 값2 반환

NVL2(값1, 값2, 값3) 값1이 NULL이 아니면 값2, 맞으면 값3 반환

(단 NVL 함수는 모든 인수 평가로, 1/0 같은 게 있으면 오류 발생)

<br/>

COALESCE(NULL이 아닌 첫 번째 값을 반환), 

NULLIF(값1, 값2) 값1 != 값2 => 값1, 같으면 NULL 반환

<br/>

### 4.기타 함수

LEAST, GREATEST(최소(대)값 반환, 문자열도 가능, NULL이 있으면 NULL 반환, 데이터 타입 다르면 안됨),

USER(사용자 이름 반환), UID(사용자 ID 반환) 등등