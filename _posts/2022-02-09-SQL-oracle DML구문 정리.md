---
layout: post
title:  "Oracle sql DML구문 정리"
subtitle:   "Oracle DML구문 정리"
categories: SQL
comments: true
tags: Oracle
---

## oracle DB의 DML구문을 정리하려고 합니다

DML구문의 가운데 M은 manipulation을 의미하는데, 이는 조작을 의미한다. 

그렇기에 해당 구문은 테이블 내부를 조작하는 구문들로 구성 되어있다.

<br/>

### 1.INSERT 문

기존 테이블에 행을 삽입하는 구문으로 아래와 같이 사용되게 된다.

    INSERT INTO table_name (column1, column2, ...) 
    VALUES (7777, 'SAM', ...);
    
방식으로 컬럼을 지정하고 해당 컬럼에 값을 집어넣는 방식이다.

하나의 행, 그리고 특정 컬럼에 값을 집어 넣기에,

빈 열에는 값이 들어가지 않거나, DEFAULT 설정이 되어있으면 해당 값이 들어간다.

데이터 값을 직접 집어넣는 방식이기에,

여러 데이터를 넣을때는 잘 사용되는 방식이 아니다.

그리고 INSERT INTO 뒤에 열을 기술하지 않는다면

values 처럼 데이터가 들어오는 항목에는

전체 열과 같은 갯수의 데이터가 들어와야지 된다.

<br/>

그리고 만약 기존 테이블에 데이터가 있다면,

서브 쿼리를 통해서 여러 행의 값을 삽입하는 것이 가능하다.

    INSERT INTO table_name --(column1, column2) 
    SELECT column1, column2 from table_name2 where ...;
    
<br/>

그리고 INSERT구문은 INSERT ~ INTO 사이에 ALL을 기술하느냐, 

FIRST ~ WHEN을 쓰느냐에 따라 INTO 뒤에 모두 삽입하는 것이 가능하거나

조건적으로 삽입하는 것이 가능하다.

    INSERT ALL
    WHEN column1 >= 5 THEN INTO table_name1 
    WHEN column1 >=105 THEN INTO table_name2
    ELSE INTO table_name3
    SELECT column1, column2
    FROM table_name3;

<br/>

첫 구문 처럼 ALL을 넣으면 table_name1, table_name2에 

모두 데이터가 들어가지만

    INSERT FIRST
    WHEN column1 >= 5 THEN INTO table_name1 
    WHEN column1 >=105 THEN INTO table_name2
    ELSE INTO table_name3
    SELECT column1, column2
    FROM table_name3;

두 번째 처럼 FIRST를 넣게되면 5이상의 값은 

table_name1에만 들어가게 된다.
    
<br/>

### 2.UPDATE , DELETE 문

기존 테이블 행의 값을 갱신하기 위해 사용하는 구문으로 아래와 같이 사용된다.

    UPDATE table_name1 
    SET column1 = 1000, column2 = 2000 
    WHERE column3 = 70;
    
쉼표로 구분을 해주면 한 번에 여러 열 갱신도 가능하며

인라인 뷰를 통해서, null로 갱신되는 경우가 있는 case를 방지할 수 있다.

    UPDATE table_name1 a 
    SET (a.column1, a.column2) = 
    (SELECT SUM(x.column1), SUM(x.column2) 
    FROM table_name2 x 
    WHERE x.column3 = a.column3)

해당 쿼리는 table_name1에만 존재하는 column3과 같이 있는 행의

column1, column2의 값을 null로 갱신한다.

    WHERE EXISTS 
    (SELECT 1 
    FROM table_name2 x 
    WHERE x.column3 = a.column3);

하지만 맨 뒤에 WHERE절로 exists를 추가하면 

null로 갱신되는 것을 방지할 수 있다.

해당 쿼리는 대신, table_name2를 2번 사용하기에

더 효율적인 쿼리를 소개하려고 한다.

    UPDATE
    (SELECT a.column1, a.column2, b.column1 as col_n, b.column2 as col2_n
    FROM table_name1 a
    , (SELECT column3, SUM(x.column1) as column1, SUM(x.column2) as column2 
    FROM table_name2 
    GROUP BY column3) b 
    WHERE b.column3 = a.column3)
    SET column1 = col_n, column2 = col2_n;

table_name2를 inner join으로 해서 column3끼리 대응되는 테이블들로 먼저 만들고

해당 값들을 바꾸는 방식이다.

테이블을 한 번씩만 사용하기에 훨씬 효율적이다.

<br/>

다만 에러가 발생하는 경우는 여러개 있다.

MERGE를 통해서, 조인 차수가 1:M의 구조가 된다면

여러번 갱신이 되기 때문에 이러한 경우에는 에러가 발생한다.

추가로 PK 제약조건으로 1번만 갱신되는 것이 보장되지 않는다면

에러가 발생하게 된다.

즉 UPDATE구문은 값이 1번만 변경되지 않고 여러번 변경이 된다면 에러를 발생 시킨다.

<br/>

DELETE구문은 단순하게 테이블의 기존 행을 삭제하는 것으로 

만약 WHERE절이 없다면 전체 행을 삭제되고, 서브쿼리 사용이 가능합니다.

    DELETE 
    FROM table_name1 
    WHERE column1 = 100; --조건부 삭제

    DELETE 
    FROM table_name1; --전체 삭제

    DELETE 
    FROM table_name1 a 
    WHERE not exists(
        SELECT 1
        FROM table_name2 x 
        WHERE x.column1 = a.column1
        ); --서브쿼리에 없는 항목 삭제

그렇기에 UPDATE와 DELETE구문은 사용시에는, 

미리 SELECT절로 자세히 다 확인 후에 해당 SELECT를

UPDATE, DELETE로 간단히 변경하는 것을 권장합니다.

<br/>

### 3.MERGE 구문

MERGE구문은 위에서 언급된 삽입, 갱신, 삭제가 모두 가능한 구문입니다.

대신 JOIN구문 처럼 사용이 되기에, 해당 구문에 대한 숙지가 중요하다고 생각된다.

    MERGE
    INTO table_name1 t
    USING table_name2 s
    ON (t.column1 = s.column2)
    WHEN MATCHED THEN
    UPDATE
    SET t.column2 = s.column2 - 500
    WHERE t.column4 = 500
    WHEN NOT MATCHED THEN
    INSERT (t.column1, t.column3, t.column4)
    VALUES (s.column1, s.column3, s.column4);

MERGE 구문의 핵심은 USING절, ON절이다.

어떤 테이블을 이용할 것인지, 그리고 그 기준이 어떤 것인지

정확히 나타내야되기 때문이다.

<br/>

게다가 ON절에 기술된 열은 일반적으로 갱신할 수 없다.

하지만, ROWID, ROW_NUMBER등을 사용하면 갱신이 가능하다.

    MERGE 
    INTO table_name1 t
    USING 
    (SELECT a.column1_n, b.ROWID as rid
    FROM 
    (SELECT column1, column1 + ROW_NUMBER () OVER (ORDER BY column1) AS column1_n 
    FROM table_name2) a
    , table_name1 b
    WHERE b.column1 = a.column1) s
    ON (t.ROWID = s.rid)
    WHEN MATCHED THEN
    UPDATE SET t.column1 = s.column1_n ;

정확히는 ROWID들끼리 이용해서 하는 것이에,

쿼리가 길어지고 복잡해진다는 단점이 존재한다.

<br/>

### 4.ERROR 로깅

DML구문은 공통적으로 중간에 에러가 발생하면 이전에 사항들을 모두 롤백시킨다.

이를 방지하기 위해, DML 수행 중 에러 발생시, 

에러를 기록하고 다음 행에 대해서 진행을 할 수 있다.

    BEGIN
    DBMS_ERRLOG.CREATE_ERROR_LOG (dml_table_name => 'T1'
    , err_log_table_name => 'E1');

PL/SQL 처리를 수행 한 이후,

    INSERT INTO table_name (column1, column2, ...) VALUES (7777, 'SAM')
    LOG ERRORS INTO e1('1') REJECT LIMIT UNLIMITED;

수행하는 DML 쿼리 뒤에 LOG ERRORS를 추가하면

e1 테이블에서 해당 에러 결과를 확인할 수 있게 된다.

이러한 테이블은 에러 체킹이 끝나서 더 이상 활용을 하지 않는다면

DROP TABLE을 통해서 삭제를 하면 된다.