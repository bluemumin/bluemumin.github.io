---
layout: post
title:  "python dictionary 사용 팁"
subtitle:   "python dictionary 사용 팁"
categories: Python
tags: Study
comments: true
---

## python dictionary 타입을 주로 사용하는 방식과 팁을 공유하려 합니다.

<br/>

dictionary를 key, value 기반이기에

key는 찾기 편하게 혹은 단순하게

value에는 하나의 값이 아닌 dataframe 같은 

데이터 하나가 통째로 들어가도 상관이 없기에

객체를 일일히 만들고 싶지 않을때 주로 사용합니다.

그렇기에 저는 주로 key에는 loop로 수행되는 index번호를 넣고

이에 맞는 작업을 각각 수행하게 하고 마지막에 concat을 하게 합니다.

이렇게 하면 pd.concat([df1, df2, df3], axis=0)

이런 방식으로 일일히 나열을 하지 않아도 되고

dictionary가 key는 index로 

value는 하나의 dataframe으로 합쳐지게 됩니다.

아래는 예시입니다.

<br/>

해당 코드를 실습할수 있는 데이터는

[캐글 데이터 페이지](https://www.kaggle.com/datasets/bluemumin/kbo-baseball-for-kaggle)를 통해서 다운로드 부탁드리겠습니다.


```python
#기본 설정 및 데이터 불러오기
import warnings
warnings.filterwarnings(action='ignore')

import pandas as pd

data = pd.read_csv("2019_kbo_for_kaggle_v2.csv")
print(data.shape)
data.tail(3)
```

    (1913, 37)
    

|      | batter_name |  age |     G |    PA |    AB |     R |     H |   2B |  3B |   HR | ... |     tp |   1B |  FBP |   avg |   OBP |   SLG |   OPS | p_year |   YAB |  YOPS |  YOPS |
|-----:|------------:|-----:|------:|------:|------:|------:|------:|-----:|----:|-----:|----:|-------:|-----:|-----:|------:|------:|------:|------:|-------:|------:|------:|------:|
| 1910 |      조용호 | 29.0 |  16.0 |  14.0 |  13.0 |   4.0 |   1.0 |  0.0 | 0.0 |  0.0 | ... | 우익수 |  1.0 |  0.0 | 0.077 | 0.077 | 0.077 | 0.154 |   2019 | 188.0 | 0.720 | 0.720 |
| 1911 |    히메네스 | 27.0 |  70.0 | 299.0 | 279.0 |  37.0 |  87.0 | 17.0 | 2.0 | 11.0 | ... |  3루수 | 57.0 | 16.0 | 0.312 | 0.344 | 0.505 | 0.849 |   2016 | 523.0 | 0.889 | 0.889 |
| 1912 |    히메네스 | 28.0 | 135.0 | 579.0 | 523.0 | 101.0 | 161.0 | 36.0 | 0.0 | 26.0 | ... |  3루수 | 99.0 | 49.0 | 0.308 | 0.363 | 0.526 | 0.889 |   2017 | 181.0 | 0.769 | 0.769 |


예시이기 때문에 간단하게

선수의 이름들로 슬라이싱을 하고

이름을 key, 슬라이싱 된 dataframe을 value로 저장시켜 주겠습니다.


```python
unique_name = list(data['batter_name'].unique())

agg = {}

for one_name in unique_name:
    agg[one_name] = data[data['batter_name'] == one_name]
    
agg[unique_name[-1]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>batter_name</th>
      <th>age</th>
      <th>G</th>
      <th>PA</th>
      <th>AB</th>
      <th>R</th>
      <th>H</th>
      <th>2B</th>
      <th>3B</th>
      <th>HR</th>
      <th>...</th>
      <th>tp</th>
      <th>1B</th>
      <th>FBP</th>
      <th>avg</th>
      <th>OBP</th>
      <th>SLG</th>
      <th>OPS</th>
      <th>p_year</th>
      <th>YAB</th>
      <th>YOPS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1911</th>
      <td>히메네스</td>
      <td>27.0</td>
      <td>70.0</td>
      <td>299.0</td>
      <td>279.0</td>
      <td>37.0</td>
      <td>87.0</td>
      <td>17.0</td>
      <td>2.0</td>
      <td>11.0</td>
      <td>...</td>
      <td>3루수</td>
      <td>57.0</td>
      <td>16.0</td>
      <td>0.312</td>
      <td>0.344</td>
      <td>0.505</td>
      <td>0.849</td>
      <td>2016</td>
      <td>523.0</td>
      <td>0.889</td>
    </tr>
    <tr>
      <th>1912</th>
      <td>히메네스</td>
      <td>28.0</td>
      <td>135.0</td>
      <td>579.0</td>
      <td>523.0</td>
      <td>101.0</td>
      <td>161.0</td>
      <td>36.0</td>
      <td>0.0</td>
      <td>26.0</td>
      <td>...</td>
      <td>3루수</td>
      <td>99.0</td>
      <td>49.0</td>
      <td>0.308</td>
      <td>0.363</td>
      <td>0.526</td>
      <td>0.889</td>
      <td>2017</td>
      <td>181.0</td>
      <td>0.769</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 37 columns</p>
</div>




```python
agg2 = pd.concat(agg)

agg2.tail(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>batter_name</th>
      <th>age</th>
      <th>G</th>
      <th>PA</th>
      <th>AB</th>
      <th>R</th>
      <th>H</th>
      <th>2B</th>
      <th>3B</th>
      <th>HR</th>
      <th>...</th>
      <th>tp</th>
      <th>1B</th>
      <th>FBP</th>
      <th>avg</th>
      <th>OBP</th>
      <th>SLG</th>
      <th>OPS</th>
      <th>p_year</th>
      <th>YAB</th>
      <th>YOPS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>조용호</th>
      <th>1910</th>
      <td>조용호</td>
      <td>29.0</td>
      <td>16.0</td>
      <td>14.0</td>
      <td>13.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>우익수</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.077</td>
      <td>0.077</td>
      <td>0.077</td>
      <td>0.154</td>
      <td>2019</td>
      <td>188.0</td>
      <td>0.720</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">히메네스</th>
      <th>1911</th>
      <td>히메네스</td>
      <td>27.0</td>
      <td>70.0</td>
      <td>299.0</td>
      <td>279.0</td>
      <td>37.0</td>
      <td>87.0</td>
      <td>17.0</td>
      <td>2.0</td>
      <td>11.0</td>
      <td>...</td>
      <td>3루수</td>
      <td>57.0</td>
      <td>16.0</td>
      <td>0.312</td>
      <td>0.344</td>
      <td>0.505</td>
      <td>0.849</td>
      <td>2016</td>
      <td>523.0</td>
      <td>0.889</td>
    </tr>
    <tr>
      <th>1912</th>
      <td>히메네스</td>
      <td>28.0</td>
      <td>135.0</td>
      <td>579.0</td>
      <td>523.0</td>
      <td>101.0</td>
      <td>161.0</td>
      <td>36.0</td>
      <td>0.0</td>
      <td>26.0</td>
      <td>...</td>
      <td>3루수</td>
      <td>99.0</td>
      <td>49.0</td>
      <td>0.308</td>
      <td>0.363</td>
      <td>0.526</td>
      <td>0.889</td>
      <td>2017</td>
      <td>181.0</td>
      <td>0.769</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 37 columns</p>
</div>




```python
agg2.index[-2:]
```




    MultiIndex([('히메네스', 1911),
                ('히메네스', 1912)],
               )



pd.concat를 활용해서 dictonary를 합쳐보았습니다.

앞에 선수들의 이름이 index로 붙은 것을 확인할 수 있습니다.

이는 현재 dictionary의 key가 선수 이름이기에

해당 부분이 dataframe의 index가 된 것입니다.

이렇게 MultiIndex가 생성되는게 싫다면

values만 concat을 해주던가

아니면 합쳐진 뒤에 reset_index로 없애주면 해결 됩니다.


```python
agg3 = pd.concat(agg.values())

agg3.tail(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>batter_name</th>
      <th>age</th>
      <th>G</th>
      <th>PA</th>
      <th>AB</th>
      <th>R</th>
      <th>H</th>
      <th>2B</th>
      <th>3B</th>
      <th>HR</th>
      <th>...</th>
      <th>tp</th>
      <th>1B</th>
      <th>FBP</th>
      <th>avg</th>
      <th>OBP</th>
      <th>SLG</th>
      <th>OPS</th>
      <th>p_year</th>
      <th>YAB</th>
      <th>YOPS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1910</th>
      <td>조용호</td>
      <td>29.0</td>
      <td>16.0</td>
      <td>14.0</td>
      <td>13.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>우익수</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.077</td>
      <td>0.077</td>
      <td>0.077</td>
      <td>0.154</td>
      <td>2019</td>
      <td>188.0</td>
      <td>0.720</td>
    </tr>
    <tr>
      <th>1911</th>
      <td>히메네스</td>
      <td>27.0</td>
      <td>70.0</td>
      <td>299.0</td>
      <td>279.0</td>
      <td>37.0</td>
      <td>87.0</td>
      <td>17.0</td>
      <td>2.0</td>
      <td>11.0</td>
      <td>...</td>
      <td>3루수</td>
      <td>57.0</td>
      <td>16.0</td>
      <td>0.312</td>
      <td>0.344</td>
      <td>0.505</td>
      <td>0.849</td>
      <td>2016</td>
      <td>523.0</td>
      <td>0.889</td>
    </tr>
    <tr>
      <th>1912</th>
      <td>히메네스</td>
      <td>28.0</td>
      <td>135.0</td>
      <td>579.0</td>
      <td>523.0</td>
      <td>101.0</td>
      <td>161.0</td>
      <td>36.0</td>
      <td>0.0</td>
      <td>26.0</td>
      <td>...</td>
      <td>3루수</td>
      <td>99.0</td>
      <td>49.0</td>
      <td>0.308</td>
      <td>0.363</td>
      <td>0.526</td>
      <td>0.889</td>
      <td>2017</td>
      <td>181.0</td>
      <td>0.769</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 37 columns</p>
</div>




```python
agg4 = pd.concat(agg).reset_index(drop=True)

agg4.tail(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>batter_name</th>
      <th>age</th>
      <th>G</th>
      <th>PA</th>
      <th>AB</th>
      <th>R</th>
      <th>H</th>
      <th>2B</th>
      <th>3B</th>
      <th>HR</th>
      <th>...</th>
      <th>tp</th>
      <th>1B</th>
      <th>FBP</th>
      <th>avg</th>
      <th>OBP</th>
      <th>SLG</th>
      <th>OPS</th>
      <th>p_year</th>
      <th>YAB</th>
      <th>YOPS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1910</th>
      <td>조용호</td>
      <td>29.0</td>
      <td>16.0</td>
      <td>14.0</td>
      <td>13.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>우익수</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.077</td>
      <td>0.077</td>
      <td>0.077</td>
      <td>0.154</td>
      <td>2019</td>
      <td>188.0</td>
      <td>0.720</td>
    </tr>
    <tr>
      <th>1911</th>
      <td>히메네스</td>
      <td>27.0</td>
      <td>70.0</td>
      <td>299.0</td>
      <td>279.0</td>
      <td>37.0</td>
      <td>87.0</td>
      <td>17.0</td>
      <td>2.0</td>
      <td>11.0</td>
      <td>...</td>
      <td>3루수</td>
      <td>57.0</td>
      <td>16.0</td>
      <td>0.312</td>
      <td>0.344</td>
      <td>0.505</td>
      <td>0.849</td>
      <td>2016</td>
      <td>523.0</td>
      <td>0.889</td>
    </tr>
    <tr>
      <th>1912</th>
      <td>히메네스</td>
      <td>28.0</td>
      <td>135.0</td>
      <td>579.0</td>
      <td>523.0</td>
      <td>101.0</td>
      <td>161.0</td>
      <td>36.0</td>
      <td>0.0</td>
      <td>26.0</td>
      <td>...</td>
      <td>3루수</td>
      <td>99.0</td>
      <td>49.0</td>
      <td>0.308</td>
      <td>0.363</td>
      <td>0.526</td>
      <td>0.889</td>
      <td>2017</td>
      <td>181.0</td>
      <td>0.769</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 37 columns</p>
</div>

<br/>

dictionary여도 기존 pd.concat 방식을 따르기에

어느 dataframe에 컬럼이 없어도 NaN으로 대체해줍니다.


```python
agg['조용호'] = agg['조용호'].drop(['OPS','YOPS'], axis=1)

agg5 = pd.concat(agg).reset_index(drop=True)

agg5.tail(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>batter_name</th>
      <th>age</th>
      <th>G</th>
      <th>PA</th>
      <th>AB</th>
      <th>R</th>
      <th>H</th>
      <th>2B</th>
      <th>3B</th>
      <th>HR</th>
      <th>...</th>
      <th>tp</th>
      <th>1B</th>
      <th>FBP</th>
      <th>avg</th>
      <th>OBP</th>
      <th>SLG</th>
      <th>OPS</th>
      <th>p_year</th>
      <th>YAB</th>
      <th>YOPS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1910</th>
      <td>조용호</td>
      <td>29.0</td>
      <td>16.0</td>
      <td>14.0</td>
      <td>13.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>우익수</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.077</td>
      <td>0.077</td>
      <td>0.077</td>
      <td>NaN</td>
      <td>2019</td>
      <td>188.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1911</th>
      <td>히메네스</td>
      <td>27.0</td>
      <td>70.0</td>
      <td>299.0</td>
      <td>279.0</td>
      <td>37.0</td>
      <td>87.0</td>
      <td>17.0</td>
      <td>2.0</td>
      <td>11.0</td>
      <td>...</td>
      <td>3루수</td>
      <td>57.0</td>
      <td>16.0</td>
      <td>0.312</td>
      <td>0.344</td>
      <td>0.505</td>
      <td>0.849</td>
      <td>2016</td>
      <td>523.0</td>
      <td>0.889</td>
    </tr>
    <tr>
      <th>1912</th>
      <td>히메네스</td>
      <td>28.0</td>
      <td>135.0</td>
      <td>579.0</td>
      <td>523.0</td>
      <td>101.0</td>
      <td>161.0</td>
      <td>36.0</td>
      <td>0.0</td>
      <td>26.0</td>
      <td>...</td>
      <td>3루수</td>
      <td>99.0</td>
      <td>49.0</td>
      <td>0.308</td>
      <td>0.363</td>
      <td>0.526</td>
      <td>0.889</td>
      <td>2017</td>
      <td>181.0</td>
      <td>0.769</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 37 columns</p>
</div>

<br/>

다음은 dictionary 입력을 편하게 하는 방식입니다.

setdefault는 기존 dictionary에 key가 중복되지 않으면

key, value로 나누어서 저장을 해줍니다.

중복되는 key가 있다면 해당 key를 반환합니다.

예시로 선수들의 연도별 YOPS의 평균값을 

단순하게 key, value 형태로 바꿔보도록 하겠습니다.


```python
name_ops_mean = pd.DataFrame(data.groupby(['batter_name'])['YOPS'].mean()).reset_index()
name_ops_mean.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>batter_name</th>
      <th>YOPS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강경학</td>
      <td>0.620600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동관</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강동우</td>
      <td>0.665846</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강민국</td>
      <td>0.372667</td>
    </tr>
    <tr>
      <th>4</th>
      <td>강민호</td>
      <td>0.807733</td>
    </tr>
  </tbody>
</table>
</div>




```python
temp_dict = {}

for i,j in list(zip(name_ops_mean['batter_name'] ,name_ops_mean['YOPS'])):
    temp_dict.setdefault(i, j) 
```


```python
temp_dict['강경학']
```




    0.6205999999999999

<br/>

그리고 미세한 팁이지만

update를 수행할때는 key에는 '' 표시를 하지 않습니다.


```python
temp_dict2 = temp_dict.copy()

temp_dict2.update(강경학 = 4, 강동우 = 2)

temp_dict['강경학'], temp_dict2['강경학'], temp_dict['강동우'], temp_dict2['강동우']
```




    (0.6205999999999999, 4, 0.6658461538461539, 2)

<br/>

다음으로는 dictionary를 copy하는 방법입니다.

일반적인 .copy를 해도 되지만

dictionary안에 dictionary가 있는 경우라면

다른 방법을 사용하여야 합니다.

먼저 예시 dictionary 입니다.


```python
orig = {'a' : {'b' : 111, 'c' : 222},
        'd' : 333, 'e' : 444,
        'f' : {'g' : 555, 'h' : 666}}
```

'a' key안에 있는 'b'의 value를 변경해보고

'd' key안에 있는 value 값을 변경해보았습니다


```python
renew1 = orig.copy()

renew1['a']['b'] = 777
renew1['d'] = 888
renew1
```




    {'a': {'b': 777, 'c': 222}, 'd': 888, 'e': 444, 'f': {'g': 555, 'h': 666}}




```python
orig
```




    {'a': {'b': 777, 'c': 222}, 'd': 333, 'e': 444, 'f': {'g': 555, 'h': 666}}



단순 원본이었던 dictionary에도 값이 변경되는 것이 확인 되었습니다.

그런데 이상하게도 dictionary 안에 바로 key가 있으면

이 값은 변경되지가 않았습니다.

그렇다면 dictionary 안에 dictionary 자체를 변경해보겠습니다.


```python
orig = {'a' : {'b' : 111, 'c' : 222},
        'd' : 333, 'e' : 444,
        'f' : {'g' : 555, 'h' : 666}}
```


```python
renew2 = orig.copy()

renew2['a'] = {'i' : 123, 'j' : 456}
renew2['d'] = 888
renew2
```




    {'a': {'i': 123, 'j': 456}, 'd': 888, 'e': 444, 'f': {'g': 555, 'h': 666}}




```python
orig
```




    {'a': {'b': 111, 'c': 222}, 'd': 333, 'e': 444, 'f': {'g': 555, 'h': 666}}

<br/>

맨 위의 key 값에 변경사항을 적용하면

원본에는 영향을 미치지 않지만

dictionary 안에 dictionary가 있는 경우에는

마치 a=b 이후에 b의 값을 바꾸면 a에도 영향을 주는 방식처럼

.copy 가 잘 동작하지 않는 것 같습니다.

이를 해결하기 위해서는 copy 패키지의 deepcopy를 사용하여야 합니다


```python
orig = {'a' : {'b' : 111, 'c' : 222},
        'd' : 333, 'e' : 444,
        'f' : {'g' : 555, 'h' : 666}}
```


```python
import copy

renew3 = copy.deepcopy(orig)

renew3['a']['b'] = 777
renew3['e'] = 888

renew3
```




    {'a': {'b': 777, 'c': 222}, 'd': 333, 'e': 888, 'f': {'g': 555, 'h': 666}}




```python
orig
```




    {'a': {'b': 111, 'c': 222}, 'd': 333, 'e': 444, 'f': {'g': 555, 'h': 666}}



deepcopy를 사용하여 원본에도 영향을 주지 않고

새로 copy한 dictionary에서 값을 변경할 수 있게 되었습니다.