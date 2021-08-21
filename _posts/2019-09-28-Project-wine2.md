---
layout: post
title:  "캐글 와인 프로젝트 포스팅_part1"
subtitle:   "캐글 와인 프로젝트 포스팅_part1"
categories: Project
tags: school
comments: true
---

[캐글 데이터 링크](https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009)

0.변수설명(한글)

고정 산도   : 포도주에 고정되어 있는 산미 정도

휘발성 산도 : 높은 수준에서는 불쾌한 식초 맛을 초래할 수있는 와인의 아세트산의 양

구연산     : 소량으로 발견되는 경우 와인에 신선함과 맛을 추가하는 구연산 양.

잔류 설탕   : 와인 발효 후 잔류하는 설탕의 양, ex) 1g / L 미만의 와인은 드물며. 45g / L 이상의 와인은 단맛으로 여겨짐.

염화물     : 와인에 들어있는 소금의 양

자유 황산   : 미생물 성장과 포도주의 산화를 방지하는 황산 값.

총 이산화황  : 자유황산등으로 인해 때문에 생기는 이산화황, 저농도에서 SO2는 와인에서는 거의 검출되지 않지만, 50ppm 이상에서는 이산화황의 향과 맛이 느껴짐.

밀도        : 알코올과 설탕 퍼센트 함량으로 결정됨.

pH         : 와인의 산성,염기성 정도. 대부분의 와인은 pH 가늠자에 3-4 사이에서있다

황산염      : 와인 첨가제로서 항균 및 항산화 작용 수행

알코올      : 와인의 알콜 함량 퍼센트

품질출력 변수 (감각 데이터를 기반으로 0과 10 사이의 점수)  -> 실제로는 red는 3~8 정수값만 가지고있음 -> 퍼센트대로 등급을 나누어서 분류 수행


1.필요한 패키지 불러오기


```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
```


```python
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plt

#그래프에 한글 안깨지게 하는 함수 포함
import matplotlib
from matplotlib import font_manager, rc
import platform
matplotlib.rc('font', family='NanumBarunGothic')

if platform.system()=='Windows':
    font_name=font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font',family=font_name)
else:
    rc('font',family='AppleGothic')
    
matplotlib.rcParams['axes.unicode_minus']=False #그래프 마이너스 표시

import pandas as pd

import seaborn as sns
```

2.이산형 반응변수인 y변수를 목적에 맞게 변형(이산형->범주형)


```python
#wine=pd.read_csv(r"C:\Users\bluedice\Desktop\winedata.csv")
wine=pd.read_csv(r"C:\Users\bluedice\Desktop\winedata.csv")
```
데이터를 불러오는 과정입니다.

```python
wine['quality']=wine['quality'].replace(3,'low rank')
wine['quality']=wine['quality'].replace(4,'low rank')
wine['quality']=wine['quality'].replace(5,'low rank')
wine['quality']=wine['quality'].replace(6,'high rank')
wine['quality']=wine['quality'].replace(7,'high rank')
wine['quality']=wine['quality'].replace(8,'high rank')
```
와인의 등급은 앞서 설명이 된 대로 3~8의 값으로 이루어져있었고

이 값을 그대로 예측하는 모델링을 하기에는 3,4,7,8점의 값을 가지고 있는 와인의 등급들의 값은 너무 작았습니다.

그렇기 때문에 해당 값들 중 3~5점은 낮은 등급으로 묶고, 6~8점은 높은 등급으로 묶어 그룹화를 진행 하였습니다.

```python
wine.rename(columns={'fixed acidity':'fixacid', 'volatile acidity':'volacid', 'citric acid':'citacid', 
         'residual sugar':'rsugar', 'chlorides':'salt', 
                    'free sulfur dioxide':'freedioxid', 'total sulfur dioxide':'totaldioxid'  },   inplace=True)
```
사용하기 편하기 위해 열 이름을 다음과 같이 변경하였습니다.

3.전체적인 사항 파악하기


```python
wine.head()
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
      <th>fixacid</th>
      <th>volacid</th>
      <th>citacid</th>
      <th>rsugar</th>
      <th>salt</th>
      <th>freedioxid</th>
      <th>totaldioxid</th>
      <th>density</th>
      <th>pH</th>
      <th>sulphates</th>
      <th>alcohol</th>
      <th>quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7.4</td>
      <td>0.70</td>
      <td>0.00</td>
      <td>1.9</td>
      <td>0.076</td>
      <td>11.0</td>
      <td>34.0</td>
      <td>0.9978</td>
      <td>3.51</td>
      <td>0.56</td>
      <td>9.4</td>
      <td>low rank</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7.8</td>
      <td>0.88</td>
      <td>0.00</td>
      <td>2.6</td>
      <td>0.098</td>
      <td>25.0</td>
      <td>67.0</td>
      <td>0.9968</td>
      <td>3.20</td>
      <td>0.68</td>
      <td>9.8</td>
      <td>low rank</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.8</td>
      <td>0.76</td>
      <td>0.04</td>
      <td>2.3</td>
      <td>0.092</td>
      <td>15.0</td>
      <td>54.0</td>
      <td>0.9970</td>
      <td>3.26</td>
      <td>0.65</td>
      <td>9.8</td>
      <td>low rank</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11.2</td>
      <td>0.28</td>
      <td>0.56</td>
      <td>1.9</td>
      <td>0.075</td>
      <td>17.0</td>
      <td>60.0</td>
      <td>0.9980</td>
      <td>3.16</td>
      <td>0.58</td>
      <td>9.8</td>
      <td>high rank</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7.4</td>
      <td>0.70</td>
      <td>0.00</td>
      <td>1.9</td>
      <td>0.076</td>
      <td>11.0</td>
      <td>34.0</td>
      <td>0.9978</td>
      <td>3.51</td>
      <td>0.56</td>
      <td>9.4</td>
      <td>low rank</td>
    </tr>
  </tbody>
</table>
</div>

```python
wine.describe()
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
      <th>fixacid</th>
      <th>volacid</th>
      <th>citacid</th>
      <th>rsugar</th>
      <th>salt</th>
      <th>freedioxid</th>
      <th>totaldioxid</th>
      <th>density</th>
      <th>pH</th>
      <th>sulphates</th>
      <th>alcohol</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1599.000000</td>
      <td>1599.000000</td>
      <td>1599.000000</td>
      <td>1599.000000</td>
      <td>1599.000000</td>
      <td>1599.000000</td>
      <td>1599.000000</td>
      <td>1599.000000</td>
      <td>1599.000000</td>
      <td>1599.000000</td>
      <td>1599.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>8.319637</td>
      <td>0.527821</td>
      <td>0.270976</td>
      <td>2.538806</td>
      <td>0.087467</td>
      <td>15.874922</td>
      <td>46.467792</td>
      <td>0.996747</td>
      <td>3.311113</td>
      <td>0.658149</td>
      <td>10.422983</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.741096</td>
      <td>0.179060</td>
      <td>0.194801</td>
      <td>1.409928</td>
      <td>0.047065</td>
      <td>10.460157</td>
      <td>32.895324</td>
      <td>0.001887</td>
      <td>0.154386</td>
      <td>0.169507</td>
      <td>1.065668</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.600000</td>
      <td>0.120000</td>
      <td>0.000000</td>
      <td>0.900000</td>
      <td>0.012000</td>
      <td>1.000000</td>
      <td>6.000000</td>
      <td>0.990070</td>
      <td>2.740000</td>
      <td>0.330000</td>
      <td>8.400000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>7.100000</td>
      <td>0.390000</td>
      <td>0.090000</td>
      <td>1.900000</td>
      <td>0.070000</td>
      <td>7.000000</td>
      <td>22.000000</td>
      <td>0.995600</td>
      <td>3.210000</td>
      <td>0.550000</td>
      <td>9.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>7.900000</td>
      <td>0.520000</td>
      <td>0.260000</td>
      <td>2.200000</td>
      <td>0.079000</td>
      <td>14.000000</td>
      <td>38.000000</td>
      <td>0.996750</td>
      <td>3.310000</td>
      <td>0.620000</td>
      <td>10.200000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>9.200000</td>
      <td>0.640000</td>
      <td>0.420000</td>
      <td>2.600000</td>
      <td>0.090000</td>
      <td>21.000000</td>
      <td>62.000000</td>
      <td>0.997835</td>
      <td>3.400000</td>
      <td>0.730000</td>
      <td>11.100000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>15.900000</td>
      <td>1.580000</td>
      <td>1.000000</td>
      <td>15.500000</td>
      <td>0.611000</td>
      <td>72.000000</td>
      <td>289.000000</td>
      <td>1.003690</td>
      <td>4.010000</td>
      <td>2.000000</td>
      <td>14.900000</td>
    </tr>
  </tbody>
</table>
</div>

4.각 변수의 분포 확인 및 변수 시각화 작업


```python
sns.set(style="white")

cor=wine.corr()

mask=np.zeros_like(cor,dtype=np.bool)
mask[np.triu_indices_from(mask)]=True

f,ax=plt.subplots(figsize=(15,9))
cmap=sns.diverging_palette(200,10,as_cmap=True)
sns.heatmap(cor,mask=mask,cmap=cmap,center=0,square=True,linewidths=0.5,cbar_kws={"shrink":1},annot=True)
plt.title('wine data correlation',size=20)
ax.set_xticklabels(['fixacid', 'volacid','citacid','rsugar','salt','free','total','density','ph','sul','alcohol'],size=12)
ax.set_yticklabels(['fixacid', 'volacid','citacid','rsugar','salt','free','total','density','ph','sul','alcohol'],size=12)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_12_1.png" | relative_url }}' alt='absolute'>

가장 먼저 확인을 한 것은 모든 변수들 간의 상관관계를 확인하고 주의할만한 사항이 있는지 확인하는 것이었습니다.


```python
wine['fixacid'].hist(figsize=(9,6))
plt.title('fixacid',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('value',size=18)
plt.ylabel('count',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_13_1.png" | relative_url }}' alt='absolute'>



```python
wine['volacid'].hist(figsize=(9,6))
plt.title('volacid',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('value',size=18)
plt.ylabel('count',size=18)
```
<img data-action="zoom" src='{{ "/assets/img/wine/output_14_1.png" | relative_url }}' alt='absolute'>



```python
wine['citacid'].hist(figsize=(9,6))
plt.title('citacid',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('value',size=18)
plt.ylabel('count',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_15_1.png" | relative_url }}' alt='absolute'>



```python
wine['rsugar'].hist(bins=20,figsize=(9,6))
plt.title('rsugar',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('value',size=18)
plt.ylabel('count',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_16_1.png" | relative_url }}' alt='absolute'>



```python
wine['salt'].hist(figsize=(9,6))
plt.title('salt',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('value',size=18)
plt.ylabel('count',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_17_1.png" | relative_url }}' alt='absolute'>



```python
wine['freedioxid'].hist(bins=20,figsize=(9,6))
plt.title('freedioxid',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('value',size=18)
plt.ylabel('count',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_18_1.png" | relative_url }}' alt='absolute'>



```python
wine['totaldioxid'].hist(bins=30,figsize=(9,6))
plt.title('totaldioxid',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('value',size=18)
plt.ylabel('count',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_19_1.png" | relative_url }}' alt='absolute'>



```python
wine['density'].hist(figsize=(9,6))
plt.title('density',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('value',size=18)
plt.ylabel('count',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_20_1.png" | relative_url }}' alt='absolute'>



```python
wine['pH'].hist(figsize=(9,6))
plt.title('ph',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('value',size=18)
plt.ylabel('count',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_21_1.png" | relative_url }}' alt='absolute'>



```python
wine['sulphates'].hist(figsize=(9,6))
plt.title('sulphates',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('value',size=18)
plt.ylabel('count',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_22_1.png" | relative_url }}' alt='absolute'>



```python
wine['alcohol'].hist(figsize=(9,6))
plt.title('alcohol',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('value',size=18)
plt.ylabel('count',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_23_1.png" | relative_url }}' alt='absolute'>



```python
f,ax=plt.subplots(figsize=(9,6))
sns.boxplot(x="quality",  y="fixacid", data=wine)
plt.title('등급별 fixacid 차이',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('quality',size=18)
plt.ylabel('fixacid',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_24_1.png" | relative_url }}' alt='absolute'>


```python
f,ax=plt.subplots(figsize=(9,6))
sns.boxplot(x="quality",  y="volacid", data=wine)
plt.title('등급별 volacid 차이',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('quality',size=18)
plt.ylabel('volacid',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_25_1.png" | relative_url }}' alt='absolute'>



```python
f,ax=plt.subplots(figsize=(9,6))
sns.boxplot(x="quality",  y="citacid", data=wine)
plt.title('등급별 citacid 차이',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('quality',size=18)
plt.ylabel('citacid',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_26_1.png" | relative_url }}' alt='absolute'>


```python
f,ax=plt.subplots(figsize=(9,6))
sns.boxplot(x="quality",  y="rsugar", data=wine)
plt.title('등급별 rsugar 차이',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('quality',size=18)
plt.ylabel('rsugar',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_27_1.png" | relative_url }}' alt='absolute'>



```python
f,ax=plt.subplots(figsize=(9,6))
sns.boxplot(x="quality",  y="salt", data=wine)
plt.title('등급별 salt 차이',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('quality',size=18)
plt.ylabel('salt',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_28_1.png" | relative_url }}' alt='absolute'>



```python
f,ax=plt.subplots(figsize=(9,6))
sns.boxplot(x="quality",  y="freedioxid", data=wine)
plt.title('등급별 freedioxid 차이',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('quality',size=18)
plt.ylabel('freedioxid',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_29_1.png" | relative_url }}' alt='absolute'>



```python
f,ax=plt.subplots(figsize=(9,6))
sns.boxplot(x="quality",  y="totaldioxid", data=wine)
plt.title('등급별 totaldioxid 차이',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('quality',size=18)
plt.ylabel('totaldioxid',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_30_1.png" | relative_url }}' alt='absolute'>



```python
f,ax=plt.subplots(figsize=(9,6))
sns.boxplot(x="quality",  y="density", data=wine)
plt.title('등급별 density 차이',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('quality',size=18)
plt.ylabel('density',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_31_1.png" | relative_url }}' alt='absolute'>



```python
f,ax=plt.subplots(figsize=(9,6))
sns.boxplot(x="quality",  y="pH", data=wine)
plt.title('등급별 ph 차이',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('quality',size=18)
plt.ylabel('ph',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_32_1.png" | relative_url }}' alt='absolute'>



```python
f,ax=plt.subplots(figsize=(9,6))
sns.boxplot(x="quality",  y="sulphates", data=wine)
plt.title('등급별 sulphates 차이',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('quality',size=18)
plt.ylabel('sulphates',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_33_1.png" | relative_url }}' alt='absolute'>



```python
f,ax=plt.subplots(figsize=(9,6))
sns.boxplot(x="quality",  y="alcohol", data=wine)
plt.title('등급별 alcohol 차이',size=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('quality',size=18)
plt.ylabel('alcohol',size=18)
```

<img data-action="zoom" src='{{ "/assets/img/wine/output_34_1.png" | relative_url }}' alt='absolute'>


5.시각화에서 발견된 이상치 제거작업(파이썬)


```python
tk=2*wine.quantile(0.95) 
```


```python
tk #0~10
```




    fixacid         23.6000
    volacid          1.6800
    citacid          1.2000
    rsugar          10.2000
    salt             0.2522
    freedioxid      70.0000
    totaldioxid    224.2000
    density          2.0000
    pH               7.1400
    sulphates        1.8600
    alcohol         25.0000
    Name: 0.95, dtype: float64




```python
wine=wine[wine['fixacid']<=tk[0]]
wine=wine[wine['volacid']<=tk[1]]
wine=wine[wine['citacid']<=tk[2]]
wine=wine[wine['rsugar']<=tk[3]]
wine=wine[wine['salt']<=tk[4]]
wine=wine[wine['freedioxid']<=tk[5]]
wine=wine[wine['totaldioxid']<=tk[6]]
wine=wine[wine['density']<=tk[7]]
wine=wine[wine['pH']<=tk[8]]
wine=wine[wine['sulphates']<=tk[9]]
wine=wine[wine['alcohol']<=tk[10]]
```


```python
wine.describe()
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
      <th>fixacid</th>
      <th>volacid</th>
      <th>citacid</th>
      <th>rsugar</th>
      <th>salt</th>
      <th>freedioxid</th>
      <th>totaldioxid</th>
      <th>density</th>
      <th>pH</th>
      <th>sulphates</th>
      <th>alcohol</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1558.000000</td>
      <td>1558.000000</td>
      <td>1558.000000</td>
      <td>1558.000000</td>
      <td>1558.000000</td>
      <td>1558.000000</td>
      <td>1558.000000</td>
      <td>1558.000000</td>
      <td>1558.000000</td>
      <td>1558.000000</td>
      <td>1558.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>8.316367</td>
      <td>0.528665</td>
      <td>0.265777</td>
      <td>2.465629</td>
      <td>0.082319</td>
      <td>15.721438</td>
      <td>45.643774</td>
      <td>0.996719</td>
      <td>3.316560</td>
      <td>0.647766</td>
      <td>10.443742</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.752520</td>
      <td>0.179674</td>
      <td>0.191676</td>
      <td>1.065970</td>
      <td>0.024106</td>
      <td>10.252484</td>
      <td>31.557502</td>
      <td>0.001862</td>
      <td>0.150953</td>
      <td>0.143165</td>
      <td>1.063866</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.600000</td>
      <td>0.120000</td>
      <td>0.000000</td>
      <td>0.900000</td>
      <td>0.012000</td>
      <td>1.000000</td>
      <td>6.000000</td>
      <td>0.990070</td>
      <td>2.860000</td>
      <td>0.330000</td>
      <td>8.400000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>7.100000</td>
      <td>0.390000</td>
      <td>0.090000</td>
      <td>1.900000</td>
      <td>0.070000</td>
      <td>7.000000</td>
      <td>22.000000</td>
      <td>0.995585</td>
      <td>3.212500</td>
      <td>0.550000</td>
      <td>9.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>7.900000</td>
      <td>0.520000</td>
      <td>0.250000</td>
      <td>2.200000</td>
      <td>0.079000</td>
      <td>13.000000</td>
      <td>37.000000</td>
      <td>0.996710</td>
      <td>3.310000</td>
      <td>0.620000</td>
      <td>10.200000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>9.200000</td>
      <td>0.640000</td>
      <td>0.420000</td>
      <td>2.600000</td>
      <td>0.089000</td>
      <td>21.000000</td>
      <td>61.000000</td>
      <td>0.997820</td>
      <td>3.400000</td>
      <td>0.720000</td>
      <td>11.100000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>15.900000</td>
      <td>1.580000</td>
      <td>0.790000</td>
      <td>9.000000</td>
      <td>0.250000</td>
      <td>68.000000</td>
      <td>165.000000</td>
      <td>1.003200</td>
      <td>4.010000</td>
      <td>1.620000</td>
      <td>14.900000</td>
    </tr>
  </tbody>
</table>
</div>


```python
wine.to_csv('C:/Users/bluedice/Desktop/wine2.csv', index=False)
```