---
layout: post
title:  "Oracle sql DDL 컬럼, 제약 조건 정리"
subtitle:   "Oracle DDL 컬럼, 제약 조건 정리"
categories: SQL
comments: true
tags: Oracle
---

### 1.열

테이블을 구성하는 기본 단위로 테이블이 만들어진 다음에

새로 추가하거나, 변경, 삭제 등을 가능하게 할 수 있다.

    ALTER TABLE table_name1 ADD (column2 NUMBER DEFAULT 11 NOT NULL, column3 VARCHAR2(14)); --컬럼 추가

    ALTER TABLE table_name1 ADD (column2 NUMBER(2), column3 VARCHAR2(14)); --컬럼 추가

    ALTER TABLE table_name1 MODIFY (column1 DEFAULT 11); --컬럼 DEFAULT 값 변경

    ALTER TABLE table_name1 RENAME COLUMN column22 TO column2; --컬럼 이름 변경

    ALTER TABLE table_name1 DROP (column3, column5); --컬럼 삭제

    ALTER TABLE table_name1 SET UNUSED (column2, column4); --미 사용 열로 변경

ALTER 쿼리 뒤에 테이블 이름을 넣고 원하는 동작을 수행하면 되는 방식으로

여러 개의 컬럼을 다룰 경우 ()가 들어가게 된다.

RENAME의 경우, COLUMN이 변경 되는 것을 인지시켜주기 위해 COLUMN이 추가 되고

원래 이름에서 나중 이름을 지정해주기 위해 TO가 추가 된다.

SET UNUSED와 다르게 테이블에서 컬럼을 안 보이게 하는 INVISIBLE도 존재한다.

주로 열 순서를 변경할 때 사용한다.

<br/>

### 2.열 타입

컬럼의 데이터 타입은 크게 문자, 숫자, 날짜, 이진 분류로 나뉜다.

먼저 문자 중에 제일 가장 많이 쓰이는 VARCHAR2이다.

최대 길이는 4000바이트 이며, 그 이상으로 하고 싶은 경우 보통 CLOB를 사용한다.

VARCHAR2 컬럼 타입에서 CLOB 타입으로 바꾸고 싶은 경우는

이전에 [해당 포스팅](https://bluemumin.github.io/sql/2021/08/30/SQL-oracle-varchar2-to-clob/) 에서 설명하여, 생략하도록 하겠다.

한 가지 생각이 들 수 있는게, 그러면 문자 타입은 다 CLOB만 사용해도 되는거 아니냐 라고 들 수 있다.

하지만, CLOB 타입은 WHERE 조건과 같은 비교 조건을 쓸 수가 없다.

(ex WHERE column = 'A') --> ERROR

단, LIKE는 ERROR가 발생하지 않는다.

<br/>

숫자 컬럼은 NUMBER가 가장 많이 쓰이며, 괄호 안에 정수, 소수 부문으로 나뉜다

그렇기에 보통 NUMBER(3,2)로 되어있으면, 뒤에 소수점은 2번째 자리까지만 허용되고

앞의 정수 부문은 1개의 숫자만 들어간다

그렇기에 총 범위는 -9.99 ~ 9.99 사이의 값만 들어간다.

추가 예시로 NUMBER(2,-2)는 -9900 ~ 9900의 정수 값이 들어가게 된다.

<br/>

DATE, TIMESTAMP 타입은 [해당 포스팅](https://bluemumin.github.io/sql/2022/01/09/SQL-oracle-sql-%EB%82%A0%EC%A7%9C-%ED%83%80%EC%9E%85-%EC%A0%95%EB%A6%AC/)으로 대체 하도록 하겠다.

<br/>

### 3.제약조건

데이터 무결성 보장을 위한 기능으로 NOT NULL, UNIQUE, PK, FK, CHECK 제약 조건이 있다.

CONSTRAINT를 통해 설정이 가능하거나, ALTER TABLE을 통해서 추가/제거하면 된다.

NOT NULL은 열에 NULL 값이 들어가지 않도록 보장하는 기능이다.

UNIQUE는 이와 다른 것이, NOT NULL은 NULL이 들어오는 것을 방지하는 것이지만

UNIQUE는 값이 중복해서 들어오는 것을 방지해준다.

전체 열에 NULL이 들어오면 중복 검사를 하지 않는다는 점도 있다.

<br/>

PK는 NOT NULL과 UNIQUE의 제약 조건들이 합쳐진 제약 조건으로

ORACLE에서는 PK가 설정되어 있다면 NOT NULL 설정이 되어있다.

또한 테이블 당 하나의 PK만 설정이 가능하다.

    ALTER TABLE table_name1 ADD CONSTRAINT table1_pk PRIMARY KEY (column1);

이런 식으로, PK를 추가 할수도 있다.

<br/>

마지막으로 FK는 참조 무결성을 보장하는 제약조건으로

부모 테이블의 갱신/삭제시 수행 규칙을 지정할 수 있다.

NO ACTION은 에러가 발생하고, CASCADE는 자식 테이블에 내용이 반영되고

SET NULL, SET DEFAULT는 자식 테이블의 값을 해당 값으로 변경 한다.

RESTRICT는 참조하는 행을 갱신, 삭제할 수 없게 한다.

    ALTER TABLE table_name2 
    ADD CONSTRAINT table2_fk1 FOREIGN KEY (column1) 
    REFEREBCE table_name1 (column2)
    ON DELETE CASCADE;

단, 참조하는 부모 테이블의 열은 UNIQUE 혹은 PK 설정이 되어있어야 한다.

만약 설정시에 특별한 조건을 설정하지 않았을때,

자식 테이블이 참조하고 있는 값이 있다면 부모 테이블은 값을 갱신/삭제 할 수가 없다.

마지막으로 FK 제약조건을 생성한 열은(자식 테이블) 인덱스를 필수로 생성하여야 한다.

UPDATE 등으로 인한 블로킹으로 인한 장애 발생이 일어날 수 있다.