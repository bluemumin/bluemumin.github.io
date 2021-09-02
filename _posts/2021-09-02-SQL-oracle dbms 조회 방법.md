---
layout: post
title:  "Oracle dbms 조회 방법"
subtitle:   "Oracle dbms 조회 방법"
categories: SQL
tags: Oracle
comments: true
---

## oracle에서 dba, all, user_을 활용하여 계정별로 접속한 DB 내의 정보를 찾아내는 방법입니다.

<br/>

수 많은 DB에 접속하면서, 해당 DB안에 어떠한 테이블들이 존재하는지, 테이블 안에 컬럼이 무엇이 있는지

일일히 기억을 하기에는 어려움이 있고, 이를 위해서 oracle안에서는

테이블, 컬럼, 파티션 등을 다양하게 조회할 수 있는 방법이 있다.

예를 들어, 접속한 DB 안에서 테이블들을 전부 확인하는 방법은

all_objects, all_table, dba_tables, user_objects등 다양하다.

<br/>

이러한 조회 쿼리들에서 사용되는 from 절의 내용물들은

dba_, all_, user_ 들을 계정 안에 부여된 권한에 한해서 볼 수 있다.

dba_로 시작되는 것은 DBA 계정으로 접속을 했을 때, 모든 것을 제대로 볼 수 있고

보통은 all_로 보는게 일반적이며(user 접근 가능), 

접속한 계정 소유의 내용은 user_을 붙이는 것으로 보인다.

이번 포스팅에서는 각 조회 정보들의 자세한 내용을 소개하기 보다는

이러한 방법으로 조회가 가능하고, 대체가 가능함을 보이고 싶다.

<br/>

1.테이블 정보 조회

-\- 테이블 모든 정보 (대체 가능 : DBA_OBJECTS, ALL_OBJECTS, DBA_TABLES, ALL_ALL_TABLES)

select * from ALL_TABLES; 

-\- 접속 계정 내 소유 항목 조회 (대체 가능 : user_object)

select * from tabs;

-\- 파티션 된 테이블 정보

select * from all_part_tables;

<br/>

2.column 조회

-\- 전체 컬럼 조회 (대체 가능 : all_tab_columns 등)

select * from cols;

-\- 파티션 컬럼 조회

select * from all_part_key_columns;

-\- 컬럼별 constraint 정보 조회 (대체 가능 : DBA_CONS_COLUMN, USER_CONS_COLUMN(접속 계정 소유))

select * from all_cons_columns;

<br/>

3.comment 조회

comment 에는 테이블 자체에 대한 설명을 적은 comment(tab_comments)와

테이블 내 각 컬럼에 적은 comment(col_comments)가 있다. 

-\- 테이블 자체 comment(대체 가능 : DBA_TAB_COMMENTS, USER_TAB_COMMENTS(접속 계정 소유))

select * from all_tab_comments;

-\- 테이블 내 column comment(대체 가능 : DBA_COL_COMMENTS, USER_COL_COMMENTS(접속 계정 소유))

select * from all_col_comments;

<br/>

4.기타 정보

-\- 파티션 정보 조회

select * from all_tab_partitions;

-\- 파티션 된 테이블의 index 조회

select * from all_part_indexes;

-\- constraint 정보 조회

select * from all_constraints;

-\- 접속 계정 보유 권한 조회

select * from user_tab_privs;

<br/>

이런식으로 원하는 정보를 찾아보고 dba_, all_, user_등으로 바꿔 가면서

자신에게 허용이 되는 선에서의 정보를 찾거나

자신이 소유한 것에 대한 정보를 찾을 수 있다.

