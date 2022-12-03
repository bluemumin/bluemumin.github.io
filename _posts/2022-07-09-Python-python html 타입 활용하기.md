---
layout: post
title:  "python html 활용하기"
subtitle:   "python html 활용하기"
categories: Python
tags: Tip
comments: true
---

## python으로 html 타입을 활용하는 방법을 공유하려 합니다.

해당 코드를 실습할수 있는 데이터는

[캐글 데이터 페이지](https://www.kaggle.com/datasets/bluemumin/kbo-baseball-for-kaggle)를 통해서 다운로드 부탁드리겠습니다.

<br/>

```python
import warnings
warnings.filterwarnings(action='ignore')

import numpy as np

import pandas as pd
from pandas import DataFrame

import os
```


```python
data = pd.read_csv("2019_kbo_for_kaggle_v2.csv")
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

table을 엑셀로 저장하는 경우가 일반적이지만,

필요에 따라 html로 바꿔서 저장해야되는 경우가 있습니다.

아래는 테이블을 html로 변환해주는 함수입니다.


```python
from IPython.display import HTML

def getTableHTML(df):

    styles = [
        # table properties
        dict(selector=" ",
             props=[("margin", "0"),
                    ("font-family", '"Helvetica", "Arial", sans-serif'),
                    ("border-collapse", "collapse"),
                    ("border", "none"),
                    ]),

        # background shading
        dict(selector="tbody tr:nth-child(even)",
             props=[("background-color", "#fff")]),
        dict(selector="tbody tr:nth-child(odd)",
             props=[("background-color", "#eee")]),

        # cell spacing
        dict(selector="td",
             props=[("padding", ".5em")]),

        # header cell properties
        dict(selector="th",
             props=[("font-size", "100%"),
                    ("text-align", "center")]),
    ]
    return (df.style.set_table_styles(styles)).render()
```

<br/>

html 생성을 위해서 테스트용 폴더를 생성하고 이를 경로로 지정하였습니다.


```python
from pathlib import Path

test_path = os.getcwd() + '/test' #테스트 폴더 생성용 경로

Path(test_path).mkdir(parents=True, exist_ok=True) #테스트 폴더 생성(기존에 있으면 자동으로 패스됨)

os.chdir(test_path) #새로운 테스트 폴더로 이동
```


<br/>

테이블에서 html을 변환하는 것을 테스트하기 위해

head, tail을 통해서 앞부분과 뒷 부분만 추출 하였습니다.


```python
html_file = open('html_file_front.html', 'w')
html_file.write(getTableHTML(data.head(2)))
html_file.close()
```


```python
html_file = open('html_file_tail.html', 'w')
html_file.write(getTableHTML(data.tail(2)))
html_file.close()
```

<img data-action="zoom" src='{{ "/assets/img/html_test/image1.PNG" | relative_url }}' alt='absolute'>   

<br/>

다음으로는 이러한 html 파일들을 하나로 모으는 함수 입니다.

빈 html 파일을 만들고 그 안에 현재 모아야되는 html 파일들이 있는 경로,

새로운 파일 명을 넣으면, merge라는 하위 폴더가 만들어지고

자동으로 해당 파일 명으로 html이 모아집니다.


```python
def multiple_html_to_one(contain_path, file_name):
    empty_html = '<html><head></head><body></body></html>' #빈 html

    contain_path = contain_path + '/' #현재 경로 설정용

    for file in os.listdir(contain_path):
        if file.endswith(".html"):
            print(file)
            with open(contain_path + file, 'r') as f:
                html = f.read()
                empty_html = empty_html.replace(
                    '</body></html>', html + '<br></br><br></br>' + '</body></html>') #<br></br> 2번으로 공백 2번 생성

    #새로 merge되는 하위 폴더 생성
    merge_path = contain_path + '/merge'
    Path(merge_path).mkdir(parents=True, exist_ok=True)
    merge_file = merge_path + '/' + file_name

    #merge된 html을 생성
    with open(merge_file, 'w') as f:
        f.write(empty_html)
```

<br/>

해당 함수를 실행시키면, 

현재 경로에 있는 html 파일들 목록을 print 해주게 됩니다.


```python
multiple_html_to_one(os.getcwd(), 'merged.html')
```

    html_file_front.html
    html_file_tail.html

merge 파일이 생성된 것을 확인하실 수 있습니다.

<img data-action="zoom" src='{{ "/assets/img/html_test/image2.PNG" | relative_url }}' alt='absolute'>   

설정한 파일 이름대로 나온 것을 볼 수 있습니다.
    
<img data-action="zoom" src='{{ "/assets/img/html_test/image3.PNG" | relative_url }}' alt='absolute'>   

<br/>

마지막으로 두 html 파일이 합쳐진 예시입니다.

중간 사이의 공백은 '<br></br><br></br>'을 통해 만든 것입니다.

<img data-action="zoom" src='{{ "/assets/img/html_test/merged.PNG" | relative_url }}' alt='absolute'>   