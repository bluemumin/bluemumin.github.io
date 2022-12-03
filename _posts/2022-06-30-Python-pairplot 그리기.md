---
layout: post
title:  "python pairplot 그리기"
subtitle:   "python pairplot 그리기"
categories: Python
tags: Graph
comments: true
---

## python pairplot 그리는 법을 상세히 소개하려 합니다.

<br/>

해당 코드를 실습할수 있는 데이터는

[캐글 데이터 페이지](https://www.kaggle.com/datasets/bluemumin/kbo-baseball-for-kaggle)를 통해서 다운로드 부탁드리겠습니다.


<br/>

```python
import warnings
warnings.filterwarnings(action='ignore')

import numpy as np
import pandas as pd
from pandas import DataFrame

import seaborn as sns

%matplotlib inline
import matplotlib.pyplot as plt
```


```python
data = pd.read_csv("2019_kbo_for_kaggle_v2.csv")
data['YOPS']=data['YOPS'].fillna(0.00000)
print(data.shape)
data.head()
```

    (1913, 37)
    




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
      <th>0</th>
      <td>백용환</td>
      <td>24.0</td>
      <td>26.0</td>
      <td>58.0</td>
      <td>52.0</td>
      <td>4.0</td>
      <td>9.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>포수</td>
      <td>5.0</td>
      <td>6.0</td>
      <td>0.173</td>
      <td>0.259</td>
      <td>0.250</td>
      <td>0.509</td>
      <td>2014</td>
      <td>79.0</td>
      <td>0.580</td>
    </tr>
    <tr>
      <th>1</th>
      <td>백용환</td>
      <td>25.0</td>
      <td>47.0</td>
      <td>86.0</td>
      <td>79.0</td>
      <td>8.0</td>
      <td>14.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>...</td>
      <td>포수</td>
      <td>8.0</td>
      <td>5.0</td>
      <td>0.177</td>
      <td>0.226</td>
      <td>0.354</td>
      <td>0.580</td>
      <td>2015</td>
      <td>154.0</td>
      <td>0.784</td>
    </tr>
    <tr>
      <th>2</th>
      <td>백용환</td>
      <td>26.0</td>
      <td>65.0</td>
      <td>177.0</td>
      <td>154.0</td>
      <td>22.0</td>
      <td>36.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>...</td>
      <td>포수</td>
      <td>20.0</td>
      <td>20.0</td>
      <td>0.234</td>
      <td>0.316</td>
      <td>0.468</td>
      <td>0.784</td>
      <td>2016</td>
      <td>174.0</td>
      <td>0.581</td>
    </tr>
    <tr>
      <th>3</th>
      <td>백용환</td>
      <td>27.0</td>
      <td>80.0</td>
      <td>199.0</td>
      <td>174.0</td>
      <td>12.0</td>
      <td>34.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>...</td>
      <td>포수</td>
      <td>23.0</td>
      <td>20.0</td>
      <td>0.195</td>
      <td>0.276</td>
      <td>0.305</td>
      <td>0.581</td>
      <td>2017</td>
      <td>17.0</td>
      <td>0.476</td>
    </tr>
    <tr>
      <th>4</th>
      <td>백용환</td>
      <td>28.0</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>17.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>포수</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>0.176</td>
      <td>0.300</td>
      <td>0.176</td>
      <td>0.476</td>
      <td>2018</td>
      <td>47.0</td>
      <td>0.691</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 37 columns</p>
</div>


<br/>

```python
from matplotlib import rc
import platform
if platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    rc('font', family='AppleGothic')
else: #linux
    rc('font', family='NanumGothic')
    
plt.rcParams['axes.unicode_minus'] = False
```

<br/>

먼저 기본적인 틀 입니다. 

PairGrid는 주어진 데이터 컬럼에 대한 모든 조합을 만들어주는 빈 틀을 위한 코드라고 보시면 됩니다.

여기서 corner=True를 설정하시면 위쪽이 없는 삼각형의 모양으로 나오게 됩니다.

단 이 설정을 하게 되면 첫 컬럼인 age 컬럼이 입력되어 있지 않습니다.

이러한 case가 생기기 때문에, 이는 다른 함수 설정을 통해서 살리는 방법을 나중에 소개하도록 하겠습니다.


```python
temp = data[['age','HR','war','YAB','YOPS']]

g = sns.PairGrid(temp, diag_sharey=False, corner=True)
g.fig.suptitle("pair plot 그리기", x=0.25, y=1.02, size=20)
```




    Text(0.25, 1.02, 'pair plot 그리기')




    
<img data-action="zoom" src='{{ "/assets/img/pairplot/output_5_1.png" | relative_url }}' alt='absolute'>   


<br/>
    


이러한 빈 틀에다가 하단, 상단, 중앙을 나눠서 각각 그림을 채워 넣을 수 있습니다.

먼저 아래쪽은 map_lower를 통해서 지정할 수 있으며

하단에 scatter plot을 그려보도록 하겠습니다.


```python
temp = data[['age','HR','war','YAB','YOPS']]

g = sns.PairGrid(temp, diag_sharey=False)
g.fig.suptitle("pair plot 그리기", x=0.25, y=1.02, size=20)

g.map_lower(sns.scatterplot, data=temp, alpha=0.5)
```




    <seaborn.axisgrid.PairGrid at 0x1ac527efa00>




    
<img data-action="zoom" src='{{ "/assets/img/pairplot/output_7_1.png" | relative_url }}' alt='absolute'> 
    


<br/>


```python

```

그리고 이 pairgrid 안에서는 같은 영역이라도 중첩해서 그리는 것이 가능합니다.

그럼 먼저 하단에 scatter plot을 그리고 

scatter plot을 제외한 상관관계선을 추가한 그래프를 그려보겠습니다.


```python
temp = data[['age','HR','war','YAB','YOPS']]

g = sns.PairGrid(temp, diag_sharey=False)
g.fig.suptitle("pair plot 그리기", x=0.25, y=1.02, size=20)

g.map_lower(sns.scatterplot, data=temp, alpha=0.5)
g.map_lower(sns.regplot, data=temp, scatter=False, color=sns.color_palette("rocket")[3])
```




    <seaborn.axisgrid.PairGrid at 0x1ac535dc700>




    
<img data-action="zoom" src='{{ "/assets/img/pairplot/output_10_1.png" | relative_url }}' alt='absolute'> 
    

<br/>



추가로 각 컬럼간의 상관관계와 해당 두 컬럼이 중첩되는 갯수를 계산해서

이를 텍스트로 입력 하는 함수를 구현해보겠습니다.}


```python
def corrdot(*args, **kwargs):
    temp2 = DataFrame([args[0], args[1]]).T #두 컬럼을 dataframe화
    
    #텍스트를 강조하기 위한 원 만들기
    ax = plt.gca()
    marker_size = 1500 #원 사이즈
    corr_r = args[0].corr(args[1], 'pearson') #각 컬럼간 상관관계 구하기
    ax.scatter([.85], [.85], marker_size, [corr_r], alpha=0.6, cmap="coolwarm",
               vmin=-1, vmax=1, transform=ax.transAxes)
    
    #원 안에 넣을 텍스트 만들기, corr 값 입력 및 두 컬럼 중 na가 하나라도 있는 것을 제외함
    corr_text = f"{corr_r:2.2f}" + "\n" + "[" + str(temp2.dropna().shape[0]) + "]" 
    
    #안에 넣을 텍스트를 삽입
    font_size = 12
    ax.annotate(corr_text, [.85, .85,], xycoords="axes fraction",
               ha='center', va='center', fontsize=font_size)
```

<br/>

```python
temp = data[['age','HR','war','YAB','YOPS']]

g = sns.PairGrid(temp, diag_sharey=False)
g.fig.suptitle("pair plot 그리기", x=0.25, y=1.02, size=20)

g.map_lower(sns.scatterplot, data=temp, alpha=0.5)
g.map_lower(sns.regplot, data=temp, scatter=False, color=sns.color_palette("rocket")[3])
g.map_lower(corrdot)
```




    <seaborn.axisgrid.PairGrid at 0x2b12141cb50>




    
<img data-action="zoom" src='{{ "/assets/img/pairplot/output_14_1.png" | relative_url }}' alt='absolute'> 
    

<br/>



원래는 pairgrid에 corner를 통해서 위쪽을 지우는 방식이 있습니다만,

처음에 언급 드렸다시피 첫 번째 컬럼이 표기가 되지 않는 점이 있었습니다.

그리고 상단, 하단, 중간을 사용자가 지정해서 지울수 있게

해당 영역을 지우는 함수를 작성하고 이번에는 하단을 지워보도록 하겠습니다.


```python
def hide_current_axis(*args, **kwds):
    plt.gca().set_visible(False)
```


```python
temp = data[['age','HR','war','YAB','YOPS']]

g = sns.PairGrid(temp, diag_sharey=False)
g.fig.suptitle("pair plot 그리기", x=0.25, y=1.02, size=20)

g.map_upper(sns.scatterplot, data=temp, alpha=0.5)
g.map_upper(sns.regplot, data=temp, scatter=False, color=sns.color_palette("rocket")[3])
g.map_upper(corrdot)

g.map_lower(hide_current_axis)
```




    <seaborn.axisgrid.PairGrid at 0x1ac575b6160>




    
<img data-action="zoom" src='{{ "/assets/img/pairplot/output_18_1.png" | relative_url }}' alt='absolute'> 
    
<br/>


가운데 영역은 map_diag를 통해서 사용이 가능하며 

주로 histogram 혹은 distplot을 넣는 영역입니다.


```python
temp = data[['age','HR','war','YAB','YOPS']]

g = sns.PairGrid(temp, diag_sharey=False)
g.fig.suptitle("pair plot 그리기", x=0.25, y=1.02, size=20)

g.map_lower(sns.scatterplot, data=temp, alpha=0.5)
g.map_lower(sns.regplot, data=temp, scatter=False, color=sns.color_palette("rocket")[3])
g.map_lower(corrdot)

g.map_upper(hide_current_axis)

g.map_diag(sns.histplot)
```




    <seaborn.axisgrid.PairGrid at 0x1ac592bf340>


  
<img data-action="zoom" src='{{ "/assets/img/pairplot/output_20_1.png" | relative_url }}' alt='absolute'> 
    
<br/>

마지막으로 x축과 y축의 컬럼의 크기를 조절하는 방법을 소개하려고 합니다.

plotting_context에서 axes.labelsize는 말 그대로 축의 라벨 사이즈를 조절하는 방식입니다.

해당 방식을 통해 전보다 축에서의 컬럼 크기가 늘어난 것을 볼 수 있습니다.


```python
with sns.plotting_context(rc={"axes.labelsize":15}):

    temp = data[['age','HR','war','YAB','YOPS']]

    g = sns.PairGrid(temp, diag_sharey=False)
    g.fig.suptitle("pair plot 그리기", x=0.25, y=1.02, size=20)
    
    g.map_lower(sns.scatterplot, data=temp, alpha=0.5)
    g.map_lower(sns.regplot, data=temp, scatter=False, color=sns.color_palette("rocket")[3])
    g.map_lower(corrdot)
    
    g.map_upper(hide_current_axis)
    
    g.map_diag(sns.distplot)
```


    
<img data-action="zoom" src='{{ "/assets/img/pairplot/output_22_1.png" | relative_url }}' alt='absolute'> 