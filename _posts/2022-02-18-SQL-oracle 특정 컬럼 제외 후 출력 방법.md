---
layout: post
title:  "Oracle 특정 컬럼 제외 select 방법"
subtitle: "Oracle 특정 컬럼 제외 select 방법"
categories: SQL
comments: true
tags: Oracle
---

## oracle에서 SELECT를 할 때, 특정 컬럼을 제외하고 하는 방법을 공유 합니다.

보통 파이썬을 활용한다면 DataFrame에서 컬럼 하나를 빼는 것은 간단하다.

하지만 이러한 방법은 sql에서 활용하려고 하면 방법을 찾는 것이 어려워진다.

주로 SELECT에서 컬럼 상관없이 다 가지고 올 때는 SELECT * 을 사용한다.

그러다 쿼리 작성 도중에 몇 개의 컬럼이 필요 없는 상황이 되었을 때,

SELECT * 에서 컬럼 한 두 개 빼고 하는 방법을 찾아보면 없다고 나온다

정확히는 컬럼을 다 기술하는 방식으로 해결을 하라고 한다.

<br/>

물론 컬럼 수가 적다면 괜찮지만 컬럼 수가 100개 이상이 된다면

SELECT 문에 테이블 컬럼을 붙여놓고, CTRL + F로 찾아서 제거 하게 될 것이다.

그래서 이번 포스팅에서는

해당 SELECT 문에 원하지 않는 컬럼만 제외된 상태로

컬럼을 나열할 수 있는 방법을 소개하고자 한다.

<br/>

    SELECT rtrim(xmlagg(xmlelement(e,column_name, ', ').extract('//text()')).getclobval()) x
    FROM all_tab_columns
    WHERE 1=1 
    AND TABLE_NAME = '쓰려는_테이블_이름'
    AND column_name NOT IN ('column3', 'column4')

결과는 컬럼들을 column1, column2, ... 방식으로 나열 되는 것입니다.

그러면 이제 해당 쿼리 결과로 나온 문구를 다음에 사용할 SELECT문에 넣어주면 되는 것이고요.

핵심 아이디어는 해당 컬럼들을 나열하기 위해, 일시적으로 XML 타입을 활용하는 것입니다.

XML로 바꾸꿔주는 이유는, 컬럼들을 나열했을때 4000 byte가 넘는 경우에는 

CLOB 타입으로 바꿔줘야 컬럼이 중간에 짤리는 현상이 생기지 않기 때문입니다.

<br/>

처음에 xmlelement로 xml화 시켜줍니다.

xmlelement(e,column_name, ', ') 는

    <E>column1, </E>
    <E>column2, </E>

아래와 같은 형태로 나오게 해주며

뒤에 붙은 .extract('//text()')는

<E>, </E>  이런식으로 붙은 xml 태그를 없애준다.

    column1, 
    column2, 

형태로 나오게 되면 이제 이 컬럼들을 합쳐주면 과정이 남게 된다.

xmlagg( xmlelement...) 를 사용해서 xml을 합쳐주게 되면

column1, column2, ...로 값들이 합쳐지게 된다.

마지막으로 .getclobval()을 붙여서 xml 타입을 clob 타입으로 바꿔준다.

그리고 rtrim으로 오른쪽 공백을 제거해주는 것으로 마무리 하는 방식입니다.