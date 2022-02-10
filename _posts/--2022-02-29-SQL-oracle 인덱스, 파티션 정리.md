---
layout: post
title:  "Oracle sql DDL 인덱스, 파티션 정리"
subtitle: "Oracle sql DDL 인덱스, 파티션  정리"
categories: SQL
comments: true
tags: Oracle
---

### 1.INDEX

데이터를 빠르게 검색하기 위한 오브젝트로 테이블에 종속 되어 있으며

하나의 테이블에 여러 개의 인덱스를 생성 할 수 있다

    CREATE UNIQUE INDEX table1_u1 ON table_name1 (column1, column2);

앞에 UNIQUE가 붙으면 고유한 값으로 구성이 된 인덱스이다.

<br/>

이러한 인덱스를 비할성화 시키는 방법이 있는데

    ALTER INDEX table1_u1 UNUSABLE;

해당 방법을 사용하게 되면, 해당 인덱스는 UNIQUE 인덱스이기 때문에

비활성화가 되면 데이터를 INSERT 할 수 없게 된다.

<br/>

    ALTER INDEX table1_u1 REBUILD;

해당 쿼리는 단편화 해소나 테이블 스페이스 변경을 위해 주로 사용하며,

인덱스가 재 구축 된다.

<br/>

그리고 PK와 UNIQUE 조건은 내부적으로 인덱스를 사용하기에

생성할 때, 해당 제약조건에서 사용할 수 있는 인덱스가 없으면 자동으로 생성 된다

그리고 수동으로 해당 조건을 지정할 수 있는데 

    ALTER TABLE table_name1 ADD CONSTRAINT table1_pk PRIMARY KEY (column1, column2) USING INDEX table1_pk;

USING을 이용해서 지정할 수 있다.

<br/>

### 2.파티션

다수의 물리적 파티션이 하나의 논리적 오브젝트로 관리되는 것으로

주로 테이블에서는 파티션 키를 통해서 분할이 되며 테이블과 동일한 구조로 생성이 된다.

파티션에는 주로 RANGE 파티션, HASH 파티션이 있는데

먼저 RANGE 파티션의 경우

    CREATE TABKE table_name1 (column1 NUMBER, column2 DATE)
    PARTITION BY RANGE(column2) (
        PARTITION p_name1 VALUES LESS THEN (DATE '2022-02-01')
        , PARTITION p_name2 VALUES LESS THEN (DATE '2022-03-01')
        , PARTITION p_name3 VALUES LESS THEN (DATE '2022-04-01')
        , PARTITION p_name4 VALUES LESS THEN (MAXVALUE)
    );

방식으로 생성이 되며, 주로 마지막 값을 지정하기 힘들기 때문에

MAXVALUE를 넣는 방식으로 마무리 한다.

<br/>

이러한 파티션은 SELECT 구문에서도 활용이 가능한데

    SELECT * FROM table_name1 PARTITION FOR ('2022-04-03')

'2022-04-03'에 해당하는 테이블의 파티션을 조회하는 방식이다.

또한 파티션은 컬럼을 다중으로 활용하여 생성이 가능하며, 

RANGE() 에서 쉼표만 추가해서 넣어주면 된다.

<br/>

HASH 파티션의 경우, 범위를 지정하지 않고

데이터가 무작위로 분산되는데, OLTP 시스템의 블록 경합을 해소하기 위해 주로 사용 된다.

이외에도, LIST를 활용하는 파티션, 파티션 키 없이 임의로 데이터를 분할하는 SYSTEM 파티션 등이 있다.

<br/>

파티션 테이블 말고도 파티션 인덱스가 존재하는데

이는 다수의 물리적 인덱스 파티션을 하나의 논리적 인덱스로 사용할 수 있다.

파티션 테이블과 동일한 구조로 파티셔닝이 되는 로컬 파티션 인덱스,

테이블과 관계없이 파티셔닝 되는 글로벌 파티션 인덱스가 있다.

관리 방법 정리
