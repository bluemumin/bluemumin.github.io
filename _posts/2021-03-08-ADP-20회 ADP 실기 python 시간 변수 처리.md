---
layout: post
title:  "20회 ADP 실기 대비 python 시간 변수 처리"
subtitle:   "20회 ADP 실기 대비 python 시간 변수 처리"
categories: ADP
tags: ADP
comments: true
---

## 20회 ADP 실기를 python으로 준비한 과정 중 시간 변수를 처리 하는 방법에 대해서 포스팅 합니다.

## 시간 데이터 변환 포맷

포맷에 따른 출력(주로 쓰는 연,월,일 그리고 시간대를 위로, 부가적으로 본인이 원할 때 사용이 가능한 포맷을 아래에 배치하였다)

%y : 년(OO),
%Y : 년(OOOO)

%m : 월(숫자),
%d : 일(숫자)

%H : 시간,
%M : 분,
%S : 초

----------------------------------

%b : 월(Short) #영어로 된 월 문자열,
%B : 월(Full) #영어로 된 월 문자열

%D: 월/일/년

%a : 요일 #영어로 된 요일 문자열,
%A : 요일(FULL) #영어로 된 요일 문자열

## datetime 패키지 이용

time은 timestamp 타입과 관련이 되어있으며,

datetime에서의 datetime이 주로 활용이 되는 것이며, date는 잘 쓰이지는 않지만 알아두면 좋다.

그리고 timedelta가 시간 데이터에서의 덧셈, 뺏셈등을 수행하는데 유용하므로 알아두는 것이 좋다.

datetime.now()를 하면 현재 시간이 나오며, 이를 weekday, date, time등으로 분리해서 출력 가능하다.

weekday는 월요일이 0이고 일요일이 6의 값을 가진다. 7로 나눗셈 했을때 나머지의 값이라고 생각하면 편하다.

1부터 7까지 출력하는 방법도 있지만, 따로 찾기 보다는 그냥 weekday에 1을 더하는 것이 더 간편하다.


```python
import time
from datetime import datetime, date, timedelta

#월 = 0 ,일 = 6
datetime.now().weekday(), datetime.now().date(), datetime.now().time()
```




    (0, datetime.date(2021, 3, 8), datetime.time(20, 47, 55, 523297))



timedelta에 day, hour, minutes를 넣고 출력하면 day는 그대로 나오지만 나머지는 초로 계산이 된다.

이건 출력 방식이기에 크게 문제가 없고, weeks는 days=7과 동일하다.

date.today()와 timedelta를 활용하여서 원하는 날짜를 계산 가능하다.


```python
week = timedelta(weeks=1)
next_week = date.today() + week
timedelta(days=5, hours=17, minutes=30),  week,  date.today(),  next_week
```




    (datetime.timedelta(days=5, seconds=63000),
     datetime.timedelta(days=7),
     datetime.date(2021, 3, 8),
     datetime.date(2021, 3, 15))



## 시간 데이터 타입 변환

### str로 변환

먼저 str로 바꾸는 방법이다.

timestamp를 str로 바꾸는 것보다는, timestamp를 datetime으로 바꾸고 

그 datetime을 str로 바꾸는 것이 원하는 str 타입의 날짜 데이터를 얻는 방법이다.


```python
timestamp1 = time.time() #timestamp -> str
timestamp_to_str = str(timestamp1)
timestamp1, type(timestamp1), timestamp_to_str, type(timestamp_to_str)
```




    (1615212299.7269828, float, '1615212299.7269828', str)



timestamp에 str을 하면 단순히 숫자에 문자가 들어가는 것으로 끝난다.

하지만, datetime에 strftime을 이용하고 원하는 형태를 넣어주면 원하는 str타입의 형태로 반환이 되기에 굉장히 유용하다.


```python
datetime_to_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #dattime -> str

datetime.now(), type(datetime.now()), datetime_to_str, type(datetime_to_str)
```




    (datetime.datetime(2021, 3, 8, 20, 51, 20, 374326),
     datetime.datetime,
     '2021-03-08 20:51:20',
     str)



### timestamp로 변환

str에서 바로 timestamp로 변환을 하는 방법은 없다.

애초에 timestamp의 타입은 float인데, 원래 문자인 타입이 숫자로 반환이 되지 않기 때문에

str에 현재 입력된 타입을 기록하고, 그걸 strptime(<-> strftime)을 이용하여서 datetime으로 바꾸고

그 datetime에 timetuple을 이용하고 다시 time.mktime을 이용하여서 timestamp로 바꿔줘야 한다.


```python
str1 = '2018-05-16 12:00:00' #str
str_to_datetime = datetime.strptime(str1, '%Y-%m-%d %H:%M:%S') #str -> datetime 
datetime_to_timestamp = time.mktime(str_to_datetime.timetuple()) #str -> datetime -> timestamp
str1, type(str1), str_to_datetime, type(str_to_datetime), datetime_to_timestamp , type(datetime_to_timestamp)
```




    ('2018-05-16 12:00:00',
     str,
     datetime.datetime(2018, 5, 16, 12, 0),
     datetime.datetime,
     1526439600.0,
     float)



### datetime로 변환

주로 제일 많이 찾는 방법일 것이고, 앞에서 일부 방법이 미리 소개가 된 상태이다.

str에서 datetime은 strptime에 현재 str에 입력된 타입을 입력해주면 되고

timestamp에서 datetime은 fromtimestamp를 활용해주면 된다.

ADP 15회에 fromtimestamp를 활용해서 타입 변환을 먼저 해줘야 했다는 이야기가 있어서

알아두면 좋다고 생각된다.


```python
str1 = '2018-05-16 12:00:00' #str
str_to_datetime = datetime.strptime(str1, '%Y-%m-%d %H:%M:%S') #str -> datetime 
str1, type(str1), str_to_datetime, type(str_to_datetime)
```




    ('2018-05-16 12:00:00',
     str,
     datetime.datetime(2018, 5, 16, 12, 0),
     datetime.datetime)




```python
timestamp_to_datetime = datetime.fromtimestamp(time.time()) #timetsamp -> datetime
time.time(), type(time.time()), timestamp_to_datetime ,  type(timestamp_to_datetime )
```




    (1615212909.7644389,
     float,
     datetime.datetime(2021, 3, 8, 23, 15, 9, 764439),
     datetime.datetime)



## pandas 패키지 이용

pandas로 하는 방법을 알아둬야 하는 이유는 DataFrame을 사용할 때, 

해당 방식으로 날짜 타입들이 기록되어있을 가능성이 있기 때문이다.

이 포스팅 이후에 바로 진행되는 포스팅에서 pd.to_datetime을 이용해서, str을 datetime으로 변환을 해주고 진행을 한다.

앞에서와는 다르게 Timestamp가 숫자가 아닌 pandas에서의 고유한 타입으로 출력이 된다


```python
import pandas as pd
pd_ts = pd.Timestamp(2019, 12, 22, 13, 30, 59)

pd_ts, type(pd_ts)
```




    (Timestamp('2019-12-22 13:30:59'), pandas._libs.tslibs.timestamps.Timestamp)



고유한 타입으로 출력은 되지만, 해당 값에 .timestamp, .date, strftime 등을 한 번 더 해주면 

앞서 봤던 timestamp, datetime, str 타입들이 나오게 된다.


```python
pd_ts.timestamp(),pd_ts.date(), pd_ts.time()
```




    (1577021459.0, datetime.date(2019, 12, 22), datetime.time(13, 30, 59))




```python
pd_ts.strftime('%Y-%m-%d %H:%M:%S'), type(pd_ts.strftime('%Y-%m-%d %H:%M:%S'))
```




    ('2019-12-22 13:30:59', str)



pd.Timestamp에 now, today를 하면, 판다스 타임스탬프에 현재 날짜와 시간이 기록 되는 방식으로 나오게 된다.


```python
pd.Timestamp.now(), pd.Timestamp.today(), type(pd.Timestamp.today())
```




    (Timestamp('2021-03-08 20:47:54.559663'),
     Timestamp('2021-03-08 20:47:54.559663'),
     pandas._libs.tslibs.timestamps.Timestamp)



마지막으로, str 타입을 pd.to_datetime만 사용해서 판다스의 고유한 Tiemstamp 타입으로 변경한 모습이다.

이번 예시는 단순히 하나의 문자에서만 시행이 되었지만

당연하게 DataFrame의 한 컬럼에서도 똑같이 수행이 가능하다. 이건 바로 다음 포스팅에서 볼 수 있다.


```python
t1 = '2020-03-02 00:00:00'
t2 = pd.to_datetime(t1)
t1, type(t1),  t2,  type(t2)
```




    ('2020-03-02 00:00:00',
     str,
     Timestamp('2020-03-02 00:00:00'),
     pandas._libs.tslibs.timestamps.Timestamp)




20회 ADP 실기를 준비하면서 만든 notebook 파일에 대한 [깃허브 링크](https://github.com/bluemumin/ADP_certificate_preperation) 입니다.

