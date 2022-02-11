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

이러한 파티션 인덱스는 파티션 키가 인덱스의 선두 열이면 PREFIXED 파티션 인덱스,

그게 아니라면 NONPREFIXED 파티션 인덱스가 된다.

이 중에서도 NONPREFIXED 글로벌 파티션 인덱스는 생성이 되지 않는다.

    CREATE UNIQUE INDEX table1_u1 ON table_name1 (column1, column2) LOCAL;

    CREATE UNIQUE INDEX table1_x1 ON table_name1 (column3, column2) GLOBAL PARTITION BY HASH (column3) PARTITIONS 2;

<br/>

이러한 파티션이 가장 중요하게 사용되는 이유는 데이터가 누적되고 많아지게 되어서 관리하게 되는 시점이다.

RANGE 파티션이 많이 쓰이는 이유는 일간, 월간 등으로 구간을 나누고

파티션 관리 정책을 내부에서 수립하게 되면, 그 이후에는

예전 데이터가 있는 파티션은 삭제하고 새로운 데이터를 위한 파티션을 새로 만들기만 하면 된다.

    ALTER TABLE table_name1 ADD PARTITION partition4 VALUES LESS THAN (MAXVALUE);

    ALTER TABLE table_name1 DROP PARTITION partition4;

다만 이러한 파티션 추가는 마지막 파티션 보다 키 값이 큰 파티션만 추가가 가능하다.

그렇기 때문에, 보통 마지막 파티션을 MAXVALUE로 설정하고

일반적인 RANGE 파티션이 LESS THEN으로 구간을 나누는 이유이다.

<br/>

    ALTER TABLE table_name1 MERGE PARTITIONS partition4, partition5 INTO PATITION partition5;

    ALTER TABLE table_name1 MERGE PARTITIONS partition4 TO partition5 INTO PATITION partition5;

파티션은 MERGE를 사용하면 병합이 가능한데

범위를 지정해서 병합을 할 수 있게 할 수 있다.

    ALTER TABLE table_name1 SPLIT PARTITIONS partition4 AT (4) INTO (PATITION partiton3, PARTITION partiton4);

    ALTER TABLE table_name1 SPLIT PARTITIONS partition4 INTO(
        PATITION partiton2 VALUES LESS THEN (2)
        , PATITION partiton3 VALUES LESS THEN (4)
        , PARTITION partiton4);

첫 코드는 4 값을 기준으로 파티션을 분할할 수 있게 해주는 코드이다.

하나의 파티션을 2개로 분할 할때는 AT으로 기준 값을 정해주고

INTO 안에는 파티션과 명칭을 설정해주면 된다.

3개 이상으로 할 때는 INTO 안에 파티션 기준 값을 넣어주고 분할을 진행하면 된다.

<br/>

    ALTER TABLE table_name1 EXCHANGE PARTITIONS partition1
    WITH TABLE table_name2 INCLUDING INDEXES WITHOUT VALIDATION;

table_name1의 partition1을 table_name2로 교체하는 작업입니다.

table_name1의 파티션 중 하나는 table_name2가 된다는 것을 의미하며

주로 파티션 일부만 작업 후, 다시 교체하려는 경우

로딩한 데이터를 파티션에 넣을때 사용합니다.

보통 운영중인 파티션 테이블을 바로 작업하게 되면 문제가 생기기 때문에

이러한 방식으로 사용을 하긴 하지만, 급한 경우가 아니라면

해당 방법 보다는 PM 작업시에, 다른 작업을 통해서 파티션 테이블의 문제를 해결합니다.

게다가 로컬 인덱스라면 크게 문제가 안되지만

글로벌 인덱스가 설정된 경우에는 REBULID를 해줘야되기 때문에

주의를 기울여서 작업을 수행하여야 한다.

    ALTER TABLE table_name1 RENAME PARTITION partition1 TO partition2; --로컬 파티션 인덱스의 파티션 명은 추가 작업 필요

    ALTER TABLE table_name1 TRUNCATE PARTITION partition1;

    ALTER TABLE table_name1 MODIFY PATITION p_name3 INDEXING ON;

파티션 이름 수정과 파티션 TRUNCATE는 다음과 같은 SQL 구문으로 수행이 가능하며,

INDEXING ON은 바로 다음에 설명 하도록 하겠다.

<br/>

파티션에는 설정에 따라 부분 인덱스를 설정이 가능한데,

    PARTITION BY RANGE(column2) (
        , PARTITION p_name3 VALUES LESS THEN (DATE '2022-04-01') INDEXING ON 
        , PARTITION p_name4 VALUES LESS THEN (MAXVALUE) INDEXING OFF
    );

파티션 생성 당시에 설정을 추가할 수 있다.

    CREATE INDEX table1_X1 ON table_name1 (column1, column2) INDEXING FULL;

    CREATE INDEX table1_X2 ON table_name1 (column1, column2) INDEXING PARTIAL;

이후에 INDEX 생성을 할 때, FULL 대신 PARTIAL을 넣어서

INDEXING ON 된 파티션들에만 인덱싱 설정할 수 있다.