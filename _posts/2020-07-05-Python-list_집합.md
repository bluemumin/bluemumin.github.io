---
layout: post
title:  "list간의 집합 관계 표현 방법"
subtitle:   "list간의 집합 관계 표현 방법"
categories: Python
tags: Tip
comments: true
---

#### 여러 리스트 간의 단순 비교가 아닌 집합 처럼의 비교를 할 때 사용하는 방법입니다.

<br/>

실제 실행된 결과를 ipynb 파일로 보고 싶으시다면 다음 링크로 이동해주시면 됩니다!

<https://github.com/bluemumin/bluemumin.github.io/blob/master/_posts/html/intersection%20%ED%8F%AC%EC%8A%A4%ED%8C%85%EC%9A%A9.ipynb>

<br/>

파이썬에서는 단순히 a in b 혹은 a == b를 통해서 비교를 하는 경우도 있겠지만

이는 True, False로 반환이 되며, 이를 다시 원 값으로 반환하려면 한 번의 치환 과정이 굳이 필요합니다.

하지만 이를, 두 리스트 간의 포함관계를 이용하여서 해당 값으로 바로 반환이 가능하며,

또한 집합의 성질을 이용하여서, 공통되는 것, 한 쪽의 list에만 있는 것 등으로 자유롭게 표현이 가능합니다.

먼저 두 숫자 list를 통해서 일반적으로 사용하는 방법입니다.

```python
b1 = [1, 2, 3, 4, 5, 9, 11, 15]
b2 = [5, 4, 6 ,7, 8, 8]

list( set(b1).intersection(b2) ) #교집합

list( set().union(b1, b2) ) #합집합

list( set( b1 + b2) ) # 합집합 다른 버전

list( set(b1).difference(b2) ) #차집합

list( set(b1).symmetric_difference(b2) ) #대칭 차집합
```

<br/>

intersection, union, difference, symmetric_diffecence로

두 리스트 간의 교집합, 합집합, 차집합, 대칭 차집합을 표현이 가능하고 이러한 집합이

모두 원 값으로 반환이 되기 때문에 바로 활용이 가능합니다.

만약 True, False로 활용을 하고자 한다면, len()에서 나오는 값이 0인지 아닌지를 통해서

굳이 추가적인 변환이 없이 조건으로서 활용이 가능합니다.

다음은 실제 실행된 결과 입니다.

<img data-action="zoom" src='{{ "/bluemumin.github.io/assets/img/list/post1.PNG" | relative_url }}' alt='absolute'>

<br/>

다음은 이를 함수로 해서 활용한 방법입니다.

```python
# 두 리스트가 주어졌을 때, 해당되는 리스트에서 교집합이 있으면 해당되는 것을 리스트 형태로 반환하는 함수

def intersection(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3

intersection(b1, b2) # 함수버전 교집합

b3 = intersection(b1, b2)
' '.join( [str(i) for i in b3])

def diff (list1, list2):
    list3 = [value for value in list1 if value not in list2]
    return list3

diff(b1, b2) #함수버전 차집합

diff(b2, b1) # [6, 7, 8, 8] #단 이렇게 하면 중복되는 것이 제거가 되지 않음

list( set( diff(b2, b1) ) ) # 고유한 것만 남겨주는 set를 이용한 뒤, 리스트를 통해 다시 리스트로 만들면 됨 # [6, 7, 8]

list( set( diff(b1, b2) + diff(b2, b1) ) ) #대칭 차집합은 굳이 함수를 만들지 않아도 간단히 가능하다.
```

<br/>

한 번 함수로 만들어 놓으면 굳이 list(set())을 통해서 쓸 필요가 없으며,

이러한 함수는 나중에 class로 만들어두어 필요할 때 불러와서 사용할 수 있습니다.

다음은 실제 실행된 결과 입니다.

<img data-action="zoom" src='{{ "/bluemumin.github.io/assets/img/list/post2.PNG" | relative_url }}' alt='absolute'>

<br/>

그렇다면 문자 list에서도 동일하게 되는 지 확인해보겠습니다.

```python
c1 = ['abc', 'edb', 'aacc', 'e', 'ed', 'ed']
c2 = ['abc', 'etc', 'fdc', 'c', 'e']

list( set(c1).intersection(c2) )

list( set().union(c1, c2) )

list( set( c1 + c2 ) )

intersection(c1, c2)

c3 = list( set(c1).intersection(c2) )
' '.join(c3)

diff(c1, c2)
```
<br/>

문자 list에서도 똑같이 작동을 하는 모습을 볼 수 있었습니다.

다음은 실제 실행된 결과 입니다.

<img data-action="zoom" src='{{ "/bluemumin.github.io/assets/img/list/post3.PNG" | relative_url }}' alt='absolute'>

<br/>
