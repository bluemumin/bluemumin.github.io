---
layout: post
title:  "Oracle sql JOIN, 집합 연산자 정리"
subtitle:   "Oracle sql JOIN, 집합 연산자 정리"
categories: SQL
tags: Oracle
comments: true
---

## oracle DB에 있는 JOIN, 집합 연산자들을 정리하려 합니다.

오라클 DB는 기본적으로 ANSI SQL을 지원해줍니다.

이유는 사용자들이 oracle DB 안에서 ansi sql 구문으로 많이 쓰다보니...

저도 사실 ansi sql이 더 편하지만, oracle DB를 썼던 입장에서

oracle DB의 JOIN 구문을 알아야겠다고 생각해서 공부를 했었습니다.

<br/>

### 1.JOIN 구문

일반적으로 FROM table1, table2 이후에

WHERE 조건절에 조인 조건이 없으면 카티션 곱으로 쿼리가 발생한다

간단하게 말해서 각 테이블 행의 곱 만큼 행이 반환 되는 것으로

첫 테이블에 행 3개, 두 번째 테이블에 행이 2개면

총 6개의 행이 반환이 되는 것이다.(즉 모든 경우의 수 반환)

<br/>

inner JOIN, outer JOIN 등은 ansi sql에서도 있지만

가장 큰 차이는 inner JOIN, outer JOIN 등을 기술하지 않아도 된다는 점이다.

ansi sql 같은 경우

    SELECT a.c1, b.t1

    FROM table1 a

    INNER

    JOIN table2 b

    ON b.t1 = a.c1;

이지만 oracle은

    SELECT a.c1, b.t1

    FROM table1 a, table2 b

    WHERE b.t1 = a.c1;

로 JOIN을 굳이 적지 않아도 된다는 점

그리고 WHERE 조건에 바로 JOIN 조건을 기술한다는 점이다.

<br/>

대신 이렇게 적지 않아도 되기에, inner, outer의 구분이 힘들기에

outer JOIN일 경우에는

    SELECT a.c1, b.t1

    FROM table1 a, table2 b

    WHERE b.t1(+) = a.c1;

로 아우터 기준이 아닌 테이블에는 무조건 (+)가 붙어야 한다.

그렇게 처리를 하지 않으면 이너 조인으로 인식이 된다.

<br/>

WHERE 조건에는 일반적으로

첫번째 기술 테이블 일반 조건 -> 조인 조건 -> 두번째 테이블... 등으로

순서를 맞춰주는 것이 가독성이 좋다고 한다.

<br/>

### 2.집합 연산자

JOIN 구문은 테이블간에 조건에 맞춰서 행, 열이 늘어나는 개념이라면

집합 연산자는 모든 열이 동일한 상황에서, 행의 갯수가 달라진다.

조건도 제한적인 것이 열의 갯수, 데이터 타입이 동일해야된다.

order by가 추가되는 경우에는 각 구문에 적는 것이 아닌

마지막에 1번만 기술해도 order by가 처리 된다.

<br/>

UNION ALL(중복포함 전체 합집합), 

UNION(중복 제외, 합집합 반환, sort 발생),

INTERSECT(중복값 제거 교집합 반환, sort 발생),

MINUS(중복값 제거,차집합 반환 sort 발생)

가 있으며 이 중에서 UNION 계열을 사용할 때, 중복이 없는걸 안다면

불필요한 sort가 진행되지 않도록 UNION all을 사용하는 것이 좋다.

<br/>

그리고 UNION all을 제외하고는 sort가 발생하지만

데이터가 적은 상황이라면 상관이 없지만

데이터가 많다면 굉장히 오래 걸리게 되기에

이를 똑같이 대체할 수 있는 쿼리를 소개하려고 한다.

<br/>

INTERSECT 구문의 경우

    SELECT c1, c2 FROM table1

    INTERSECT

    SELECT c1, c2 FROM table2

해당 쿼리를 DISTINCT(중복값 제거) 와 EXISTS 조건, 

LNNVL 함수(NULL 허용해야되는 열 있을 경우) 를 사용해서 대체할 수 있다.

    SELECT DISTINCT a.c1, a.c2
    
    FROM table1 a

    WHERE EXISTS

    (SELECT 1
    
    FROM table2 b
    
    WHERE b.c1 = a.c1
    
    AND LNNVL (b.c2 <> a.c2));

MINUS의 경우에는 EXISTS가 있는 항목에 NOT EXISTS로

바꿔주면 대체가 가능하게 된다.

<br/>

하지만 해당 쿼리를 사용하게 되면, 서브쿼리를 사용하게 되기에

쿼리의 길이가 길어지게 되는 단점또한 존재한다.