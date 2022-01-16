---
layout: post
title:  "Oracle sql 함수, 프로시저 작성 정리"
subtitle:   "Oracle sql 함수, 프로시저 작성 정리"
categories: SQL
tags: Oracle
comments: true
---

## oracle DB에 있는 함수, 프로시저 작성법에 대해서 정리하려 합니다.

DB를 사용하다 보면, 자신이 원하는 방식으로

컬럼을 변형하고, 여러번 사용을 해야되는 경우가 있다.

파이썬에서의 함수처럼 sql에서도 이러한 사용자 지정 함수가 존재한다.

<br/>

### 1.함수 작성법

하나의 값만 return을 받을 때는 아래와 같은 방식을 사용하면 된다.

    CREATE OR REPLACE FUNCTION function1 (parameter1 NUMBER) 
        RETURN VARCHAR2 
    IS 
        output1 VARCHAR2(14); 
    BEGIN 
        SELECT column1 
        INTO output1 
        FROM table1 
        WHERE column2 = parameter1; 

        RETURN output1; 
    END;

함수 명칭을 지정하고 필요한 파라미터가 있으면 소괄호 안에 넣는다,

이후에 return을 받아야될 값을 지정하고

begin ~ end 구문 안에다가 원하는 내용을 넣고 반환을 수행하면 된다.

<br/>

다만 여러 개의 컬럼을 반환하는 경우에는

이러한 함수를 여러 개 만드는 것 보다는

파이프라인 테이블 함수라는 테이블로 반환을 하는 것이 가능한

함수를 만들어서 하는 것을 추천한다.

<br/>

    -- A. 타입 지정(object)
    CREATE OR REPLACE TYPE type_make AS OBJECT 
    ( 
        column1 NUMBER, 
        column2 VARCHAR2(14), 
        column3 VARCHAR2(13) 
    ); 

    -- B. 타입 지정(테이블)
    CREATE OR REPLACE TYPE table_make  
    AS TABLE OF type_make; 

먼저 컬럼들을 object로서 지정하고

그 다음에 그 컬럼들로 이루어진 테이블을 지정한다.

<br/>

    -- 3. 파이프라인 테이블 함수 생성
    CREATE OR REPLACE FUNCTION function2 (parameter1 NUMBER) 
        RETURN table_make 
        PIPELINED 
    IS 
        output1 type_make; 
    BEGIN 
        FOR rec IN ( 
            SELECT column1 
                , column2 
                , column3 
            FROM table1 
            WHERE column1 >= parameter1 
        ) LOOP 
            output1 := type_make(rec.column1, rec.column2, rec.column3);         
            PIPE ROW(output1); 
        END LOOP; 
        
        RETURN; 
    END;

마지막으로 이전처럼 함수를 작성하는데

return이 되는 곳에 테이블을 넣고 PIPELINED를 추가로 넣는다.

begin 구절에는 for문을 넣어 루프를 수행하게 하고

해당 결과들이 모여서 테이블이 될 수 있도록 한다.

마지막에 해당 테이블이 반환이 된다.

<br/>

    SELECT * FROM TABLE(function2(123));

실행 방법은 테이블 형태로 나오기 때문에, from 절에 사용하거나

테이블이 들어가도 오류가 나지 않을 위치에 넣어서 활용하면 된다.

<br/>

### 2.프로시저 작성법

필요할때마다 호출, 사용할 수 있게 특정 로직만 처리하고

결과값은 반환하지 않게 할 수 있는 서브 프로그램이다.

단, 레퍼런스 변수를 사용하면 결과 값 리턴이 가능하다.

    CREATE OR REPLACE PROCEDURE procedure1 
    (
        column1 IN VARCHAR2,
        column2 IN VARCHAR2
    )
    IS

    BEGIN

        UPDATE table1
            SET c1 = column2
        WHERE t1 = column1;

    EXCEPTION
        WHEN OTHERS THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('SQL ERROR MESSAGE: ' || SQLERRM);

    END procedure1;

예시는 특정 조건에 맞는 컬럼 값을 update 하는 프로시저이다.

    EXEC procedure1('example1', 'example2')

로 실행이 가능하다.

update를 진행하기에 리턴이 없지만

<br/>

이를 cursor를 추가로 해서 리턴을 받거나

varchar2등을 넣어서 리턴을 받을 수 있다.

    CREATE OR REPLACE PROCEDURE procedure2 
    (
        column1 IN VARCHAR2,
        column2 IN VARCHAR2,
        output1 OUT VARCHAR2
    )
    IS
        TEMP_COLUMN VARCHAR2(1);

    BEGIN

        UPDATE table1
            SET c1 = column2
        WHERE t1 = column1;

        TEMP_COLUMN := TO_CHAR(SQL%ROWCOUNT);

        output1 := TEMP_COLUMN;

    EXCEPTION
        WHEN OTHERS THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('SQL ERROR MESSAGE: ' || SQLERRM);

    END procedure2;

이전 프로시저와 다르게 업데이트가 실행된 행 갯수를

반환 받을 수 있도록 프로시저를 작성하였다.

    variable real_output VARCHAR2;
    exec procedure2('test1','test2,:real_output);
    print real_output;

로 결과를 반환 받을 수 있게 된다.
