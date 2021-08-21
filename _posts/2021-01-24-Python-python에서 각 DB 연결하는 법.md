---
layout: post
title:  "python에서 Oracle, MS SQL, DB2, Postgre DB 연동 하는 법"
subtitle:   "python에서 Oracle, MS SQL, DB2, Postgre DB 연동 하는 법"
categories: Python
tags: Tip
comments: true
---

## python에서 Oracle, MS SQL, DB2, Postgre DB connection 하는 법을 소개하려 합니다.

최근에 여러 DBMS들을 통해서 데이터를 추출하고 이를 활용하는 작업을 하고 있는데

하나의 DB에 접속하는 것이라면 DBeaver 같은걸로 접속정보 미리 넣어두는 것이 가능하기에

넣어두고 연결해서 하면 되지만

지금 거의 30개가 넘는 DB들이 있는데 이걸 언제 사람이 수작업으로 하고 있겠는가

당장 1000개가 넘는 테이블들의 SQL문을 실행하여야 되기 때문에

python으로 자동화를 하는 방법을 고안하는 것이 필수적이었던 상황이라

pd.read_sql("SQL문장", con = "SQL 문장 실행 DB 연결 구조")

에 들어가는 DB 연결 구조를 편하게 연결하기 위한 방법을 찾게 되었고

이를 소개하려고 한다.

<br/>

사용하려는 python 패키지와 기본 설정 방법입니다

oracle은 사용자 컴퓨터에 설치가 된 oracle의 경로를 추가로 지정해주어야

oracle DB에 연결이 가능합니다.

```python
import os
oracle_install_space = "C:\oracle\instantclient_19_8" #oracle 설치 위치

import cx_Oracle  #oracle 연결용
import pymssql  #mssql 연결용
from psycopg2 import connect  #postgre 연결용
import ibm_db_dbi as db  #db2 연결용
```

예시로 보여드리려는 각 DB의 임시 설정 값들입니다.

ID = python_user / 
PW = love@! / 
IP = 1.1.1.1 / 
PORT = 8888 / 
SHCEMA = dbo

<br/>

## Oracle 연결방법


```python
def oracle_con(SCHEMA, IP, PORT, ID, PW, oracle_install_space):
    #oracle과 instant cleint있어야만 실행이 가능함
    location = oracle_install_space
    os.environ["PATH"] = location + ";" + os.environ["PATH"]

    oracle_connection = cx_Oracle.connect(
        str(ID) + "/" + str(PW) + "@" + str(IP) + ":" + str(PORT) + "/" +
        str(SCHEMA))
    return oracle_connection
```

cx_Oracle.connect("python_user/love@!@1.1.1.1:8888/dbo")

## MS sql 연결방법


```python
def mssql_con(SCHEMA, IP, PORT, ID, PW, charset='utf8'):
    sql_server_connection = pymssql.connect(database=str(SCHEMA),
                                            server=str(IP),
                                            port=int(PORT),
                                            user=str(ID),
                                            password=str(PW),
                                            charset=charset)
    return sql_server_connection
```

pymssql.connect(database="dbo",
                server="1.1.1.1",
                port=8888,
                user="python_user",
                password="love@!",
                charset=charset)

## postgre 연결방법


```python
def postgre_con(SCHEMA, IP, PORT, ID, PW):
    postgre_connection = connect(database=str(SCHEMA),
                                 host=str(IP),
                                 port=int(PORT),
                                 user=str(ID),
                                 password=str(PW))
    return postgre_connection
```

connect(database="dbo",
         host="1.1.1.1",
         port=8888,
         user="python_user",
         password="love@!")

## DB2 연결방법


```python
def db2_con(SCHEMA, IP, PORT, ID, PW):
    db_connection = db.connect(
        "DATABASE=" + str(SCHEMA) + ";"
        "HOSTNAME=" + str(IP) + ";"
        "PORT=" + str(PORT) + ";"
        "UID = " + str(ID) + ";"
        "PWD= " + str(PW) + ";", "", " ")
    return db_connection
```

db.connect(
    "DATABASE=dbo;
    HOSTNAME=1.1.1.1;
    PORT=8888;
    UID=python_user;
    PWD=love@!;" , "", " ")
    
<br/>

코드들을 보다보면 사용되는 패키지들도 서로 다르고

어떤 DBMS는 hostname, host, server 이런식으로 다르게 표현하고

이를 함수화 하지 않으면 직접 입력을 해주어야 한다.

만약 각 DBMS 연결 함수 밑에 있는 것들은 이를 직접 입력하고자 할 때

복사해서 붙여놓고 본인이 사용할 DBMS 정보값으로 바꿔서 넣어주면 된다.

함수에 들어가는 순서는 SCHEMA, IP(Host), PORT, ID, PW순으로 해두었고

oracle의 경우, 미리 지정해놓은 oracle_install_space만 추가로 넣어주면

oracle 연결이 가능하도록 되어있다.

엑셀 같은 곳에 접속정보를 모아놓는다면, 함수 형태로 이렇게 먼저 만들어 놓고

나중에 접속 정보를 수정할 일이 생기더라도

엑셀에서만 변경해주면 되기 때문에 이렇게 함수 형태로 된 것들은 수정하지 않아도 된다.



