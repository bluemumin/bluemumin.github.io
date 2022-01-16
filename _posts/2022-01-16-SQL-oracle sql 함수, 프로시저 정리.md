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


### 2.프로시저 작성법

필요할때마다 호출, 사용할 수 있게 특정 로직만 처리하고

결과값은 반환하지 않게 할 수 있는 서브 프로그램

in 다음에 out을 잘 적으면 out도 가능

CREATE OR REPLACE PROCEDURE 프로시저명(파라미터)

IS -- 프로시저에서 선언할 변수

BEGIN ~ 내용 END; (여러 작업 단위별로 가능, 예외 처리 가능)

-> EXEC 프로시저명(파라미터);

CURSOR를 쓰면 리턴도 가능
