---
layout: post
title:  "Oracle sql 프로그래머스 문제 풀이"
subtitle:   "Oracle sql 프로그래머스 문제 풀이"
categories: SQL
tags: Oracle
comments: true
---

## oracle 쿼리를 사용해 프로그래머스 문제를 푼 내용을 정리합니다.

일을 하면서 쿼리를 자주 사용하기는 하지만

실제로 코딩 테스트때 sql이 나오거나

다른데서는 sql을 어떻게 예시로 드는지 보고 싶어서

프로그래머스에서의 sql 고득점 kit의 문제를 풀어보았습니다.

join 구문을 제외하고는 전반적인 난이도가 낮은 편이라는 생각이 들었습니다.

<br/>

[문제풀이 sql 전체 파일](https://github.com/bluemumin/solving_the_algorithm_problem/tree/main/programmers/sql) 에 문제들에 대한 쿼리는 올려 놓았습니다.

sql만 먼저 풀어보고 싶어서 언어 별로 문제를 고를 수 있는

프로그래머스에서 진행을 했습니다.

문제는 총 29개였는데

이 중에서 group by 쪽에서 괜찮았던 문제를 소개하려고 합니다.

<br/>

    -- 입양 시각 구하기(2)
    -- a에는 테이블에서의 시간별 count를 b에서는 connect by로 만든 임의 테이블에 0~23의 값 삽입
    -- 그 이후, b를 기준으로 a와 outer join 수행 하고 값이 없는 시간대는 case로 0을 삽입

    with a as (
    select to_char(DATETIME,'HH24') as hour , count(*) as COUNT
    from ANIMAL_OUTS 
    group by to_char(DATETIME,'HH24')
    ),
    b as (
    SELECT rownum - 1 as HOUR
    from dual
    connect by rownum <= 24
        ) 
    select b.hour,
    case when a.count >=1 then a.count
    else 0 end count
    from a, b
    where b.hour = a.hour(+)
    order by b.hour;

문제에서 주어진 테이블에 특정 시간대만 존재하였기에

값이 없는 시간대를 만들기 위해서 connect by를 사용해서

0시부터 23시로 만들수 있는 임시 테이블을 하나 만들었다

그 이후에, 주어진 테이블에서 시간만 추출해서 group by를 하였고

해당 작업들은 with 구문으로 묶어서 위쪽으로 배치하였다

그 다음으로 두 테이블 중에서 시간대만 있는 테이블을 기준으로

outer join을 수행하고, count가 없는 시간대는 case 구문으로 0을 추가하였다.