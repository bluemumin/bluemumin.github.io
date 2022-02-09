---
layout: post
title:  "Oracle sql DDL 테이블, 뷰 정리"
subtitle: "Oracle sql DDL 테이블, 뷰 정리"
categories: SQL
comments: true
tags: Oracle
---

## oracle DB의 DDL구문 중 테이블, 뷰를 정리하려고 합니다

### 1.테이블

데이터를 저장할 수 있는 기본적인 오브젝트로,

행과 열로 구성되어있고, 오브젝트 안에다가 제약조건과 인덱스를 생성할 수 있다.

만드는 과정인 CREATE, 수정이 가능한 ALTER,

테이블을 삭제하는 DROP, 테이블 내 데이터를 전부 지우는 TRUNCATE가 있다.

    CREATE TABLE table_name1(
        column_1 number
        , column2 number(2) default 200
        , column3 number(10) default 10 not null
    );

테이블 안에 컬럼 명칭과 타입, 경우에 따라서 기본 값과

not null이라는 컬럼 내에 값이 존재해야된다는 설정을 추가 할 수 있다.

    CREATE TABLE table_name1 select * from table_name2 where 0=1;

또한 기존 테이블을 활용하여 서브쿼리로 생성하는 것도 가능하며 

이러한 방식을 축약해서 CTAS라고 부른다.

다만 이러한 방식은 열 타입과 NOT NULL 제약조건은 들고오지만

기본 값 설정은 가져오지 않는다.

<br/>

ALTER 쿼리는 테이블 이름 변경, 읽기 전용 테이블로 변경이 가능해진다.

    ALTER TABLE table_name1 RENAME TO new_table1;

DROP 쿼리는 테이블을 삭제할 수 있으며, 추가적으로 

PURGE를 통해 휴지통 기능을 사용하지 않고 바로 삭제할 수 있고(데이터 복구 불가)

CASCADE CONSTRAINTS 를 통해 FK조건을 함께 삭제가 가능하다.

    DROP TABLE new_table1 CASCADE CONSTRAINTS PURGE;

마지막으로 TRUNCATE의 경우, 테이블을 초기화 하는데 

테이블 저장 공간을 해제 하므로 DELETE와 다르게 롤백이 불가능하다

    TRUNCATE TABLE new_table1;

<br/>

### 2.테이블 구조

위에서 테이블 생성, 수정, 삭제를 보았는데

이러한 테이블들에도 여러 가지 유형들이 존재한다.

위에서 CREATE를 통해서 만들어진 테이블 모두 힙 테이블이라는

임의의 위치에 데이터를 저장하는 테이블이다.

<br/>

다음 테이블은 인덱스 구조 테이블로, 

pk 제약 조건의 열 순서에 따라 데이터가 정렬되어 저장된다.

    CREATE TABLE table_name1(
        column_1 NUMBER
        , column2 NUMBER
        , CONSTRAINT table_name1_pk PRIMARY KEY (column1)
    )
    ORGANIZATION INDEX ;

<br/>

그리고 트랜잭션 종료되면 초기화 되는 임시 테이블이 있다.

    CREATE GLOBAL TEMPORARY TABLE table_name1(
        column_1 NUMBER
        , column2 NUMBER
    )
    ON COMMIT DELETE ROWS;

마지막에 DELETE ROWS는 트랜젝션 레벨로 데이터를 저장하며

PRESERVE ROWS는 세션 레벨로 데이터를 저장한다.(다시 접속시 사라짐)

<br/>

### 3.뷰

간단하게 이야기 하면 SELECT문을 DB에 저장하는 오브젝트이다

테이블 처럼 사용이 가능하고 JOIN, UNION ALL등 결합해서 만드는 방식이 대부분이다.

    CREATE OR REPLACE VIEW view1 AS
    SELECT * FROM table_name1 WHERE column1 >= 1;

테이블 처럼 데이터 UPDATE, DELETE 등이 가능하지만

이러한 기능은 테이블에도 있으므로, 테이블을 참조해서 뷰를 만드는 경우

데이터를 직접 VIEW에 넣기보다는 테이블에 넣는 방식을 사용한다.

<br/>

뷰의 가장 큰 장점은 데이터 보안성 그리고 독립성이다.

사용자에게 일부만 공개를 해야되는 데이터의 경우,

일부 컬럼만 들어있는 VIEW를 생성 한 다음, 

해당 VIEW에 접근할 수 있는 권한만 부여하면 된다.

기존에 테이블을 수정하면 이를 바라보는 사용자들이 이에 맞춰서 수정을 하여야 하지만

뷰를 바라보게 하면, 뷰 안의 쿼리를 수정 후에 

as를 통해서 컬럼 명을 그대로 유지하는 방식으로 수정을 하지 않게 해도 된다.