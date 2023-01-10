---
layout: post
title:  "python Tabnet 리뷰"
subtitle:   "python Tabnet 리뷰"
categories: Python
tags: Deep Learning
comments: true
---

## 정형 데이터를 예측하는 딥러닝 모델인 Tabnet을 살펴보았습니다.

[이전 포스팅](https://bluemumin.github.io/python/2022/07/04/Python-plotly-%EC%86%8C%EA%B0%9C-%EB%B0%8F-radar-chart/) 

에서는 plotly 라이브러리를 통해 radar chart를 그리고 이를 그래프가 동적으로 움직이는 모습을 보여드렸습니다.

이런 plotly로 그린 그래프는 jupyter notebook에 결과만 출력해두고 그냥 놔두게 된다면

나중에 해당 그래프가 남아있지 않고 흰 바탕만 남게 되는 경우가 생기게 됩니다.

<br/>

그리고 이를 다른 사람들에게 공유하기 위해서 그래프가 출력된 창을

그대로 notebook에서 md 타입으로 변환 한다면, 수 많은 로그 기록만 남아있는 것을 보실 수 있습니다.

이번 포스팅에서는 plotly의 클라우드를 통해, 편하게 블로그에 업로드 하는 방법을 공유하려 합니다.

<br/>

먼저 설치가 되어야할 라이브러리는 chart_studio입니다.

보통은 설치가 안 되어 있으니 pip install chart_studio를 통해서 다운로드를 하시면 됩니다.

```python
import chart_studio
```

<br/>

그 다음에 저희는 이 그래프를 plotly의 클라우드에 저장하기 위해

plotly chart stuido에 회원가입을 진행하여야 합니다.

[해당 링크](https://chart-studio.plotly.com/Auth/login/#/) 클릭 후, 편하게 가입 하시면 됩니다.

그 이후, 오른쪽 위 가입자명 > Settings 클릭 후, 왼쪽에 있는 API Keys를 클릭 합니다.

그리고 API Settings의 두번째인 API key의 Regeberate Key를 클릭합니다.

그리고 username과 api_key를 입력하여 python 코드를 실행 시킵니다.

```python
username = 'username' # your username
api_key = 'regenerate key click 후 값' # your api key

chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
```

<br/>

plotly chart stuido 와의 연동을 완료하였으니, 

이전에 실행하였던 radar chart를 클라우드에 올리는 작업을 해보겠습니다.

보통 chart를 fig에 할당 해놓으니, filename만 따로 설정해주시면 됩니다.


```python
import chart_studio.plotly as py
py.plot(fig, filename = 'kbo_radar_chart_example', auto_open=True)
```

    '파이썬 실행 후 나오는 주소'

<br/>

블로그에 올리는 방법은 간단합니다.

이를 iframe 형태로 변환하여서 글의 원하는 위치에 넣으시면 됩니다.

여기서 iframe 전에 나오는 작은 따옴표는 제거하시면 됩니다.


```python
import chart_studio.tools as tls
tls.get_embed('파이썬 실행 후 나오는 주소') #change to your url
```


    '<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="파이썬 실행 후 나오는 주소.embed" height="525" width="100%"></iframe>'