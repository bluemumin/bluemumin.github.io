---
layout: post
title:  "Oracle sql DDL 기타 내용 정리"
subtitle: "Oracle sql DDL 기타 내용 정리"
categories: SQL
comments: true
tags: Oracle
---

## oracle DB의 DDL구문 중 시너님, DBLINK, COMMENT를 정리 하려고 합니다

### 1.SYNONYM(시너님)

오브젝트에 동의어를 부여하는 오브젝트로

주로 긴 이름을 짧게 축약하거나 스키마를 기술하지 않고 사용할 수 있게 해준다.

PUBLIC SYNONYM, PRIVATE SYNONYM 두 가지로 나뉘는데

    GRANT CREATE SYNONYM TO user1; --제거는 REVOKE

SYNONYM 생성은 해당 계정에 SYNONYM 권한 부여가 된 이후에 가능하다.

<br/>

    CREATE OR REPLACE PUBLIC SYNONYM table_name1 FOR schema.table_name1

    CREATE OR REPLACE SYNONYM table_name2 FOR schema.table_name2

주로 스키마가 많은 db라 테이블 명칭만 가지고 바로 사용할 수 있도록 하는 경우가 많다.

PUBLIC을 붙이면 공용으로 사용할 수 있는 SYNONYM이 되고

붙이지 않는다면 PRIVATE이 된다.

PRIAVATE SYNONYM은 PUBLIC SYNONYM과 달리, 

사용자마다 만드는 것이기 때문에 사용하는 것이기 때문에

    CREATE OR REPLACE SYNONYM abc FOR user1.table_name2

    CREATE OR REPLACE SYNONYM abc FOR user2.table_name2

PUBLIC과 다르게 SYNONYM 이름이 같더라도 에러가 발생되지 않는다.

<br/>

### 2.DBLINK

다른 DB에서 현재 DB로 오브젝트를 엑세스 할 수 있도록 하는 오브젝트이다.

SYNONYM과 같이 권한이 있어야 생성이 가능하다.

    CREATE PUBLIC DATABASE LINK db_link1 CONNECT TO user_name IDENTIFIED BY password USING 'oracle_sid';

    CREATE DATABASE LINK db_link1
    CONNECT TO user_name
    IDENTIFIED BY "password"
    USING '(DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = db_ip_입력)(PORT = 1521))
    (CONNECT_DATA =
        (SERVER = DEDICATED)
        (SERVICE_NAME = oracle_sid)
    )
    )';

SYNONYM과 마찬가지로 PUBLIC, PRIVATE가 존재합니다.

db_link1은 DB LINK 명칭, user_name는 연결하고자 하는 USER,

password는 연결하고자 하는 USER의 PASSWORD를 대체해서 입력하면 됩니다.

생성은 어렵지만 사용법은 간단한 것이 원하는 테이블 명칭 뒤에 @db_link1 같이

DB LINK 명칭을 적으면 됩니다.

    SELECT * FROM other_db_table@db_link1;

<br/>

### 3.COMMENT

쿼리문에서는 주로 주석을 달 때, --를 사용하거나 /* */ 을 사용한다.

오브젝트에는 간단하게 테이블, 뷰, 열 등에 COMMENT ON 으로 주석을 입력한다.

    COMMENT ON TABLE table_name1 IS '테이블 주석 내용';

    COMMENT ON COLUMN table_name1.column1 IS '컬럼 주석 내용';    

가장 큰 장점은 해당 주석들을 문서로 관리하지 않아도 되고,

테이블이나 컬럼에 대해서 모르는 사용자가 보고, 이해를 할 수 있도록 도와줄 수 있다.