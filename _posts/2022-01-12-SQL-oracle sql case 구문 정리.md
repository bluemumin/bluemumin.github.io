---
layout: post
title:  "Oracle sql CASE 구문 정리"
subtitle:   "Oracle sql CASE 구문 정리"
categories: SQL
tags: Oracle
comments: true
---

## oracle DB의 CASE 구문을 정리하려고 합니다.

<br/>

case 구문은 case 바로 뒤에 컬럼을 넣고 조건을 추가하는 단일 case 표현식,

case 뒤에 when을 넣고 조건들을 넣는 검색 case가 존재한다.

<br/>

### 1.단일 CASE 표현식

SELECT CASE 컬럼1 

WHEN 10 THEN 1

WHEN 20 THEN 2

ELSE 9 --ELSE 생략하면 해당 경우에 NULL 반환

END AS C1 ~

<br/>

이런식으로 CASE 다음에 바로 컬럼이 들어가고 그 컬럼과 값의 일치여부를 확인하여

값을 반환하는 방식이다.

컬럼 하나로 정하기 때문에, 컬럼 타입과 WHEN 다음에 입력되는 값의 타입이 다르다면

오류가 발생하게 된다.

<br/>

### 2.검색 CASE 표현식

SELECT CASE

WHEN 컬럼1 BETWEEN 10 AND 20 THEN 1

WHEN 컬럼1 BETWEEN 20 AND 30 THEN 2

ELSE 9

END AS C1 ~

<br/>

이런 식으로 CASE 다음의 WHEN에 다양한 조건들을 기입하고

그 조건에 해당되면 값을 반환하는 방식이다.

<br/>

### 3.응용 방법

이러한 CASE 구문은 조건에 내장함수, 사용자 정의 함수 등 다양하게

사용을 하는 것이 가능하다.

CASE 구문 안에 또 다른 CASE 구문을 넣을 수 있다.

<br/>

SELECT CASE

WHEN 컬럼1 = 10 THEN

    CASE WHEN 컬럼2 >= 1000 THEN '1위'

         WHEN 컬럼2 >= 500 THEN '2위' END

WHEN 컬럼1 = 20 THEN

    CASE WHEN 컬럼2 >= 3000 THEN '1위'

         WHEN 컬럼2 >= 2500 THEN '2위' END

END AS LAST_COLUMN ~

<br/>

이런 방식으로 CASE ~ END로 구분을 잘 지어주고

추가로 들여쓰기를 통해서 CASE 구문 안에 CASE 구문이 있는 구조로

쿼리를 작성해주면 보기에도 좋고

추가로 중첩 CASE 구문을 작성할 수 있게 된다.
