---
layout: post
title:  "python DB 연결 함수 ver2"
subtitle:   "python DB 연결 함수 ver2"
categories: Python
tags: Study
comments: true
---

## python DB 연결 함수 version2를 올립니다.

이전에 DB2, Oracle, Postgre, MS-SQL 4개의 DBMS를 각각 함수형태로 불러오는 것을 소개하였습니다.

<https://bluemumin.github.io/ps/2021/01/24/Python&SQL-python%EC%97%90%EC%84%9C-%EA%B0%81-DB-%EC%97%B0%EA%B2%B0%ED%95%98%EB%8A%94-%EB%B2%95/>

해당 버전을 살펴보던 중, 4개 DBMS의 입력 순서가 똑같으니

이를 하나의 함수로 또 묶어서 만들면 더 간단하게 사용이 가능하지 않을까 라는 생각으로 출발하였습니다.

<https://github.com/bluemumin/python_db_connection>

제 깃허브에 python_db_con.py 파일로 올려놓은 상태입니다.

README 파일에 자세히 적어놓았지만,

4개 DBMS의 패키지를 불러오고, 각 DBMS연결 함수, DBMS 통합 함수를 불러와서 사용이 가능합니다.

당연히 DBMS 패키지 4개가 설치가 되야되기에, 만약에 안쓰는 DBMS라면 설명에 적힌대로 .py파일에서

주석처리를 한 이후에 사용하시거나, 따로 추출해서 사용하시기 바랍니다.

```python
# 실제 수행 코드

from python_db_con import python_db_connection

oracle_install_space = 'oracle_설치 경로'

python_db_connection('oracle', 'DB명칭', 'host', 'port', 'id', 'pw', oracle_install_space)

python_db_connection('db2', 'DB명칭', 'host', 'port', 'id', 'pw')
```

실제로 동작하는 모습까지 보여드리고 싶지만, 회사에서 구현한거라 보여드릴수 없어서 아쉬움이 따릅니다.