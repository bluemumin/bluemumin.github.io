---
layout: post
title:  "python matplotlib text 및 legend 등" 
subtitle:   "python matplotlib text 및 legend 등"
categories: Python
tags: Graph
comments: true
---

## python 그래프를 그릴 때 text를 입력하는 방법, legend 입력 방법 등을 포스팅 합니다.

<br/>

해당 코드를 실습할수 있는 데이터는

[캐글 데이터 페이지](https://www.kaggle.com/datasets/bluemumin/kbo-baseball-for-kaggle)를 통해서 다운로드 부탁드리겠습니다.


```python
#기본 설정 및 데이터 불러오기
import warnings
warnings.filterwarnings(action='ignore')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("2019_kbo_for_kaggle_v2.csv")
#data = data[data.columns[27:]]
print(data.shape)
```

    (1913, 37)

<br/>    
    
이전 포스팅과 동일하게 선수들의 기록에 연차를 부여하고

이 연차들을 그룹화 하여, 연차별 차기 시즌 OPS의 평균, 표준편차를 구하였습니다.


```python
data = data.sort_values(by=['batter_name', 'year'])  # 이름과 연도 별로 sort

# 각 관측치마다 연차를 부여하기 위해서 생성
batter_name_first = [i for i in data['batter_name'][1:]]
batter_name_zero = [i for i in data['batter_name'][0:]]

work_year = list()  # 해당 관측치와 다음 관측치의 이름이 같으면 1년차 -> 2년차의 방식을 빠르게 수행하기 위해서 시행
work_year.append(1)

for i in range(len(batter_name_first)):
    if batter_name_first[i] == batter_name_zero[i]:
        work_year.append(work_year[i]+1)
    else:
        work_year.append(1)

data['work_year'] = work_year

work_group_total = data.groupby(['work_year'])['YOPS'].aggregate(['mean', 'std', 'count']).reset_index()
one_to_nineteen = list(work_group_total['work_year'])
work_group_total.tail(3)
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
      <th>work_year</th>
      <th>mean</th>
      <th>std</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>0.734583</td>
      <td>0.093955</td>
      <td>12</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>0.689000</td>
      <td>0.165181</td>
      <td>8</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>0.702333</td>
      <td>0.214219</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>

<br/>

먼저 그래프에 텍스트를 삽입하는 방법입니다.

plt.text를 쓸때는 x좌표, y좌표, 텍스트 입력 내용으로 입력하면 됩니다.


```python
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(one_to_nineteen, work_group_total['mean'])

plt.text(10, 0.85, "text check \n like like \n this", 
         fontsize=20, color='blue', horizontalalignment="center")
plt.text(8, 0.77, "checking point", ha="right", weight="heavy")
plt.text(8, 0.77, "x = %0.2f \n y = %0.2f" % (8, 0.77),
         rotation=30, color='gray');
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_text/output_5_0.png" | relative_url }}' alt='absolute'> 
    
<br/>

annotate도 동일한 기능을 하는데,

이 경우에는 실제 표시할 점의 위치와

텍스트가 표시될 위치를 다르게 하고

이를 화살표로 연결하는 것이 가능합니다.


```python
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(one_to_nineteen, work_group_total['mean'])

arrowprops = {
    'arrowstyle': '->'
}

ax.annotate(text="max_point",  # 입력할 텍스트
            xy=(15, 0.825),  # 시작점 위치
            xytext=(20, 0.85),  # 텍스트가 표시 될 위치
            color='green', fontfamily='serif', fontstyle='italic', fontsize=15,
            arrowprops=arrowprops #xy, xytext가 있으면 화살표로 연결함
            )
plt.show()
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_text/output_7_0.png" | relative_url }}' alt='absolute'> 

<br/>

다음으로는 legend(범례)를 설정하는 방법입니다.

seaborn의 경우는 한 번에 그리고 hue로 범례를 만드는게 가능하지만

그냥 matplotlib의 경우는 그림을 여러 번 그리고

그 그림에 대해서 라벨을 표시하는 식으로 legend를 생성합니다.

먼저 각 그림 마다 label을 지정하고 legend를 생성하는 방식입니다.


```python
fig, ax = plt.subplots(figsize=(5, 3))

data_30_under = data[data['age']<=30]
ax.scatter(data_30_under['age'], data_30_under['YOPS'], s=5, color='blue', label='age_under_30')

data_30_over = data[data['age']>30]
ax.scatter(data_30_over['age'], data_30_over['YOPS'], s=5, color='black', label='age_over_30')

ax.legend(loc="best");
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_text/output_9_0.png" | relative_url }}' alt='absolute'> 

<br/>

일일히 지정을 하는 것이 아닌

한 번에 그림을 그린 이후에 

마지막에 legend에 labels를 통해서 표시하는 것도 가능합니다.


```python
fig, ax = plt.subplots(figsize=(5, 3))

data_30_under = data[data['age']<=30]
ax.scatter(data_30_under['age'], data_30_under['YOPS'], s=5, color='blue')

data_30_over = data[data['age']>30]
ax.scatter(data_30_over['age'], data_30_over['YOPS'], s=5, color='black')

ax.legend(labels = ['age_under_30', 'age_over_30'], loc="best");
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_text/output_11_0.png" | relative_url }}' alt='absolute'> 

<br/>

legend 박스의 위치를 지정하는 것도 가능하고 

기준은 그림의 좌표를 0 ~ 1 사이로 해두고 

bbox_to_anchor를 통해서 조정하는 방식입니다.

바깥에 놔두고 싶은 경우는 1보다 크게 하면 되며

기준점은 왼쪽 위를 기준으로 하는 듯 합니다.


```python
fig, ax = plt.subplots(figsize=(5, 3))

data_30_under = data[data['age']<=30]
ax.scatter(data_30_under['age'], data_30_under['YOPS'], s=5, color='blue')

data_30_over = data[data['age']>30]
ax.scatter(data_30_over['age'], data_30_over['YOPS'], s=5, color='black')
  
ax.legend(labels = ['age_under_30', 'age_over_30'], loc="upper left", 
          bbox_to_anchor=(1, 1));
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_text/output_13_0.png" | relative_url }}' alt='absolute'> 

<br/>

서브플롯간의 간격을 가능한 최적의 수치로 자동 조정해주는 것도 가능합니다.

```python
#fig, ax = plt.subplots(constrained_layout=True)
plt.rcParams['figure.constrained_layout.use'] = True

data_30_under = data[data['age']<=30]
plt.scatter(data_30_under['age'], data_30_under['YOPS'], s=5, color='blue')

data_30_over = data[data['age']>30]
plt.scatter(data_30_over['age'], data_30_over['YOPS'], s=5, color='black')
  
plt.legend(labels = ['age_under_30', 'age_over_30']);
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_text/output_15_0.png" | relative_url }}' alt='absolute'> 

<br/>

마지막으로 지금까지의 matplotlib의 기능들을

정리하기로 마음을 먹었던 시각화 코드로 마무리를 해보려고 합니다.

연차별 차기시즌 OPS에 대한 평균과 표준편차의 0.5배만큼 정도를 신뢰구간을 만들고

이를 범위로 표시해 보았습니다.

중간 중간 주석을 달아서 해당 항목에 대해서 설명하였습니다.


```python
from matplotlib import rc
rc('font', family='Malgun Gothic')
```


```python
checking = 0.5

f, ax = plt.subplots(figsize=(18, 6))

#평균, 신뢰구간 하한/상한 선 그래프 그리기
plt.plot(one_to_nineteen, work_group_total['mean'], color='b',
         marker='o',  markerfacecolor='black', linewidth=3)
plt.plot(one_to_nineteen,
         work_group_total['mean'] - checking * work_group_total['std'], 'k.')
plt.plot(one_to_nineteen,
         work_group_total['mean'] + checking * work_group_total['std'], 'k.')

# 신뢰구간 지정 범위 색깔 칠하기
plt.fill(np.concatenate([one_to_nineteen, one_to_nineteen[::-1]]),
         np.concatenate([work_group_total['mean'] - checking * work_group_total['std'],
                         (work_group_total['mean'] + checking * work_group_total['std'])[::-1]]),
         alpha=.5, fc='grey', ec='None', label='95% confidence interval')

#x축 좌,우 구간 줄이기 및 y축 눈금 삭제
ax.spines['left'].set_position(('axes', 0.045))
ax.spines['right'].set_position(('axes', 0.955))
ax.tick_params(axis="y", length=0)

#x축 이름 라벨링, 축 제목 설정
plt.xticks(one_to_nineteen, one_to_nineteen)
plt.xlabel('연차', size=18)
plt.ylabel('다음 시즌 OPS', size=18)
plt.title('신뢰구간 포함 연차당 YOPS 그래프', size=25)

#x, y축 라벨 세부 설정
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(18)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

# 점 마다 text 입력으로 YOPS 값 입력
tk = [round(i, 2) for i in work_group_total['mean']]
for x, y in zip(one_to_nineteen, tk):
    plt.text(x+0.04, y+0.01, tk[x-1], size=15)

tk2 = [round(i, 2) for i in work_group_total['mean'] - checking * work_group_total['std']]
for x, y in zip(one_to_nineteen, tk2):
    plt.text(x+0.04, y-0.01, tk2[x-1], size=15)

tk3 = [round(i, 2) for i in work_group_total['mean'] + checking * work_group_total['std']]
for x, y in zip(one_to_nineteen, tk3):
    plt.text(x+0.04, y-0.01, tk3[x-1], size=15)

# 신뢰 구간에 대한 legend 설정
plt.legend( bbox_to_anchor=(0.25, 0.9), fontsize=15);
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_text/output_18_0.png" | relative_url }}' alt='absolute'> 