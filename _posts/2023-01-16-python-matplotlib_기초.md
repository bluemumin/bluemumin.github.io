---
layout: post
title:  "python matplotlib 설정 및 subplot"
subtitle:   "python matplotlib 설정 및 subplot"
categories: Python
tags: Graph
comments: true
---

## python 그래프 축 설정 법, subplot에 대해 아는 대로 포스팅 합니다.

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
    
이번 예시 데이터는, 선수들의 기록에 연차를 부여하고

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
work_group_total.head(3)

one_to_nineteen = list(work_group_total['work_year'])
```

<br/>

matplotlib은 python의 대표적인 시각화 라이브러리인데

세세하게 다루면 끝이 없습니다.

이번 포스팅에서는 기본 설정을 하는 방법과

subplot으로 그래프를 한 번에 여러 개를 그리는 것을 정리하려고 합니다.

<br/>

먼저 rcParams를 이용한 기본 설정 방법입니다.

'plt.rcParams' 에는 default로 설정된 사항들이 있습니다.

이는 dictionary 구성으로 되어있으며

사용자가 변경이 가능합니다.

예시로 그래프의 크기, 선 굵기 등을 변경하였습니다.


```python
plt.rcParams['figure.figsize'] = (5,5) #그래프 사이즈 설정
plt.rcParams['figure.dpi'] = 72 #인치당 도트수(그림 구성 픽셀 수) #기본 100
plt.rcParams['lines.linewidth'] = 5 #선 굵기
plt.rcParams['axes.grid'] = True #격자무늬 설정
plt.rcParams['axes.edgecolor'] =  'red' #외각 선 색깔

plt.rcParams['savefig.dpi'] = 200 #저장시 도트 수
plt.rcParams['savefig.transparent'] = True #투명 배경 #기본 false

plt.rcParams['font.family'] = 'Dejavu Sans' #폰트 설정
plt.rcParams['font.size'] = 14 #폰트 크기

plt.plot(one_to_nineteen, work_group_total['mean']);
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_basic/output_6_0.png" | relative_url }}' alt='absolute'> 

<br/>
    
해당 rcParams의 설정과 동일한 것이 

matplotlib 안에 있는 rc를 import하면 가능합니다.

rcParams와 다르게, 하나의 줄에 여러 요소를 동시에 적용가능하게 할 수 있습니다.

차이도 크게 없는게 rcParams의 'figure.figsize', 'figure.dpi'는

rc에서 'figure'인 구분 안에서 figsize, dpi로 나누어 지는 것을 볼 수 있습니다.


```python
from matplotlib import rc

rc('figure', figsize = (8,8), dpi=72) #그래프 사이즈 설정 #인치당 도트수
rc('axes', grid = False) #격자무늬 미 설정
rc('axes', edgecolor = 'red') #외각 선 색깔
rc('lines', linewidth = 1) #선 굵기
rc('savefig', dpi = 200, transparent = True) #저장시 도트 수 #투명 배경 여부
rc('font', family = 'DejaVu Sans', size = 20, weight = 'bold') #폰트 설정, #폰트 크기, #폰트 굵기

plt.plot(one_to_nineteen, work_group_total['mean']);
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_basic/output_8_0.png" | relative_url }}' alt='absolute'> 

<br/>
    
아래의 방식은 dictoinary로 만든 다음에,

폰트 양식을 적용시키는 방식입니다.


```python
import seaborn as sns
plt.style.use('ggplot')

rc2 = {
    "axes.facecolor":"#FFF9ED",
    "figure.facecolor":"#FFF9ED",
    "axes.edgecolor":"#383838"
}

sns.set(rc=rc2)

plt.plot(one_to_nineteen, work_group_total['mean']);
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_basic/output_10_0.png" | relative_url }}' alt='absolute'> 

<br/>
    
```python
font_dict = {'family' : 'DejaVu Sans',
        'size' : 14,
        'weight' : 'normal'
       }

rc('font', **font_dict)

plt.plot(one_to_nineteen, work_group_total['mean']);
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_basic/output_11_1.png" | relative_url }}' alt='absolute'> 
    
<br/>

이렇게 plt.rcParams, rc를 통해서 적용을 하게 되면,

다음 설정에서도 해당 사항들이 그대로 적용이 되게 됩니다.

이번에는 matplotlib의 font_manager를 통해 

title에만 폰트 양식을 적용시켜보겠습니다.

기존 사항들에 대해서 초기화를 하지 않았기에

title의 폰트만 바뀌게 됩니다.


```python
from matplotlib import font_manager as fm

# font setting
font_setting0 = fm.FontProperties() #기본 설정 저장
font_setting0.set_family('Dejavu Sans') # 'serif' 'sans-serif', 'cursive', 'fantasy', 'monospace' #폰트 스타일

font_setting0.set_size(20) #크기
font_setting0.set_style('normal') # 'normal', 'oblique', 'italic' #기울임 설정 등
font_setting0.set_weight('bold') #강조표시

plt.plot(one_to_nineteen, work_group_total['mean'])
plt.title('title', fontproperties=font_setting0);
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_basic/output_13_0.png" | relative_url }}' alt='absolute'> 

<br/>

해당 설정은 동일하게 dictionary를 통해서도 가능합니다.

```python
# font setting
fontdict = {
    'family': 'serif', #스타일
    'style' : 'italic',
    'size': 20, #크기
    'weight': 'bold', #강조표시
}

plt.plot(one_to_nineteen, work_group_total['mean'])
plt.title('title', fontproperties=fontdict);
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_basic/output_15_0.png" | relative_url }}' alt='absolute'> 
    
<br/>

다음은 subplot을 활용해서 각 칸마다 그림을 그리는 방법입니다.

전체 구간을 지정하는 방법은 크게 2가지로

plt.figure(figsize=(3, 3))이라는 위에서 설명이 된

plt의 'figure.figsize' 지정을 통해서 전체 구간을 지정하는 방법과

plt.subplots를 통해 figsize를 지정하는 방법입니다.

두 방법에 큰 차이는 없고, 그림이 그려질 전체 구간의 크기를 지정하는 방식입니다.

<br/>

```python
plt.style.use('default') #rcParams 설정 초기화
```

그림의 구간을 나누는 방법은 여러개로

하나는 plt.subplot(행 열 index)입력하는 방법입니다.

아래의 예시는 2행 3열로 된 칸에 순서대로 그림을 그리는 방법입니다.


```python
plt.figure(figsize=(12, 6))

plt.subplot(231)  # 2행 3열 중 첫번째
plt.plot(one_to_nineteen, work_group_total['mean'])
plt.subplot(232)  # 2행 3열 중 두번째
plt.plot(one_to_nineteen, work_group_total['mean']**2)
plt.subplot(233)  # 2행 3열 중 세번째
plt.plot(one_to_nineteen, work_group_total['mean']**3)
plt.subplot(234)  # 2행 3열 중 네번째
plt.plot(one_to_nineteen, work_group_total['mean']**4)
plt.subplot(235)  # 2행 3열 중 다섯번째
plt.plot(one_to_nineteen, work_group_total['mean']**5)
plt.subplot(236)  # 2행 3열 중 여섯번째
plt.plot(one_to_nineteen, work_group_total['mean']**6);
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_basic/output_19_0.png" | relative_url }}' alt='absolute'> 
    
<br/>

위와 동일한 방법으로 하는 대신에

각 subplot에 객체 지정을 하고, 

sharey를 통해 1번째, 4번째 그래프의 y축을 공유하는 코드를 작성해 보았습니다.

```python
fig, axes = plt.subplots(figsize=(12, 6))

ax1 = plt.subplot(231)  # 2행 3열 중 첫번째
ax1.plot(one_to_nineteen, work_group_total['mean'])
ax2 = plt.subplot(232, sharey=ax1)  # 2행 3열 중 두번째
ax2.plot(one_to_nineteen, work_group_total['mean']**2)
ax3 = plt.subplot(233, sharey=ax1)  # 2행 3열 중 세번째
ax3.plot(one_to_nineteen, work_group_total['mean']**3)
ax4 = plt.subplot(234)  # 2행 3열 중 네번째
ax4.plot(one_to_nineteen, work_group_total['mean']**4)
ax5 = plt.subplot(235, sharey=ax4)  # 2행 3열 중 다섯번째
ax5.plot(one_to_nineteen, work_group_total['mean']**5)
ax6 = plt.subplot(236, sharey=ax4)  # 2행 3열 중 여섯번째
ax6.plot(one_to_nineteen, work_group_total['mean']**6);
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_basic/output_21_0.png" | relative_url }}' alt='absolute'> 
    
<br/>

subplot의 두 번째 방법은 행 열 index를 한 번에 적는 것이 아닌

쉼표를 이용해 나누어서 적는 방법입니다.

for문을 통해서 그린다면 해당 방법이 효과적이라고 생각됩니다.


```python
plt.subplot(2, 2, 1)  # 2 행 2 열 크기의 격자 중 첫 번째 부분 그래프 = 좌측 상단 # nrows=2, ncols=2, index=1
plt.plot(one_to_nineteen, work_group_total['mean'])
plt.subplot(2, 2, 2)  # 2 행 2 열 크기의 격자 중 두 번째 부분 그래프 = 우측 상단
plt.plot(one_to_nineteen, work_group_total['mean']**2)
plt.subplot(2, 2, 3)  # 2 행 2 열 크기의 격자 중 세 번째 부분 그래프 = 좌측 하단
plt.plot(one_to_nineteen, work_group_total['mean']**3)
plt.subplot(2, 2, 4)  # 2 행 2 열 크기의 격자 중 네 번째 부분 그래프 = 우측 하단
plt.plot(one_to_nineteen, work_group_total['mean']**4);
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_basic/output_23_0.png" | relative_url }}' alt='absolute'> 

<br/>

subplots를 ax로 객제 치정하고, 

이를 좌표처럼 활용해서, 그래프를 집어 넣을 수도 있습니다.


```python
fig, ax = plt.subplots(2, 2) # 순서대로 row의 갯수, col의 갯수입니다. nrows=2, cols=2로 지정할 수도 있습니다.

# plot위치는 ax[row, col] 또는 ax[row][col]로 지정합니다.
ax[0, 0].plot(one_to_nineteen, work_group_total['mean'])      # 2 행 2 열 크기의 격자 중 첫 번째 부분 그래프 = 좌측 상단
ax[0, 1].plot(one_to_nineteen, work_group_total['mean']**2)   # 2 행 2 열 크기의 격자 중 두 번째 부분 그래프 = 우측 상단
ax[1, 0].plot(one_to_nineteen, work_group_total['mean']**3)   # 2 행 2 열 크기의 격자 중 세 번째 부분 그래프 = 좌측 하단
ax[1, 1].plot(one_to_nineteen, work_group_total['mean']**4);   # 2 행 2 열 크기의 격자 중 네 번째 부분 그래프 = 우측 하단
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_basic/output_25_0.png" | relative_url }}' alt='absolute'> 

<br/>

아니면 GridSpec이라는 subplots와 유사한 기능의 격자를 준비하고

grid를 좌표처럼 활용해서 그릴 수도 있습니다.

이렇게 하게 되면 위에서는 하나씩만 지정해서 그릴 수 있지만

ax3번 처럼, 여러 칸을 활용해서 그릴 수도 있게 됩니다.


```python
grid = plt.GridSpec(2, 2)  # 2행 2열 크기의 격자를 준비합니다.

ax1 = plt.subplot(grid[0, 0])  # 2행 2열 크기의 격자 중 첫 번째 부분 그래프 = 좌측 상단
ax2 = plt.subplot(grid[0, 1])  # 2행 2열 크기의 격자 중 두 번째 부분 그래프 = 우측 상단
ax3 = plt.subplot(grid[1, 0:]) # 2행 *1*열의 두 번째 부분 그래프 = 하단
                               # 범위를 [1, 0:]으로 설정하여 2행 전체를 지정함.
    
ax1.plot(one_to_nineteen, work_group_total['mean']) 
ax2.plot(one_to_nineteen, work_group_total['mean']**2) 
ax3.plot(one_to_nineteen, work_group_total['mean']**3);
```

<img data-action="zoom" src='{{ "/assets/img/matplotlib_basic/output_27_0.png" | relative_url }}' alt='absolute'> 