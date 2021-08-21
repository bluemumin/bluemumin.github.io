---
layout: post
title:  "python Counter 함수에서 value 값으로 key 값 찾는 방법"
subtitle:   "python Counter 함수에서 value 값으로 key 값 찾는 방법"
categories: Python
tags: Tip
comments: true
---

## 이번 게시물에 필요한 collections 패키지의 Counter 함수와 index 추출 함수입니다.


```python
from collections import Counter

#list(counter.key)에서 index 뽑기
def find_index(data, target):
    res = []
    lis = data
    while True:
        try:
            # +1의 이유 : 0부터 시작이니까
            res.append(lis.index(target) + (res[-1] + 1 if len(res) != 0 else 0)) 
            lis = data[res[-1] + 1:]
        except:
            break
    return res
```

대략 다음과 같은 방식으로 리스트에서 원하는 값에 대한 인덱스만 가져옵니다.

1. 빈 리스트 생성 + 데이터(리스트) 투입

2. while true에 try문을 수행시켜서 들어오는 리스트의 처음부터 끝까지 수행가능하도록 함

3. list.index(target)을 수행하면 가장 먼저나오는 target 값의 index 값이 나옴

4. 데이터를 가장 첫번째 target 값의 이후의 범위로 다시 인덱싱 하여서 이를 반복

5. error가 나온다는 것은 더이상 target 값이 없는 것이므로 종료 하고 원하는 값에 대한 index 값만 반환 됨


```python
aa = [1,7,2,3,7,5,3,7,1,2,3,7,7]

print(find_index(aa,7))
```

    [1, 4, 7, 11, 12]
    

DataFrame으로 만들고 index을 하는 방법도 있지만, list형태로 풀어나가야 된다면

해당 함수를 사용하시는 것을 추천합니다.

다음은 예제입니다.

a라는 list에 대해서 Counter(a)를 한 이후 객체 형태로 저장합니다.

Counter(a)는 dictionary 형태로 반환이 되기 때문에, key 값과 value 값을 각각 따로 저장해줍니다.


```python
a = ['a','a','a','b','b','c','c','c','d']
my_dict1 = Counter(a)
my_dict1_keys = list(my_dict1.keys())
my_dict1_values = list(my_dict1.values())
my_dict1
```




    Counter({'a': 3, 'b': 2, 'c': 3, 'd': 1})



value값을 list로 저장한 것을 활용하여 3번 나온 것을 찾고 index 값을 반환 하게 합니다.


```python
my_dict1_index = find_index(my_dict1_values, 3)
my_dict1_index
```




    [0, 2]



이를 list comprehension을 활용하여 key 값으로 반환합니다.


```python
[j for i,j in enumerate(my_dict1_keys) if i in my_dict1_index ]
```




    ['a', 'c']



3번 counting 된 것이 'a', 'c'인 것으로 잘 나온 것을 확인 할 수 있었습니다.

수치형 list에서도 마찬가지로 잘 수행이 됩니다.


```python
b = [7,2,3,7,5,3,7,1,2,3,7,7]
my_dict2 = Counter(b)
my_dict2_keys = list(my_dict2.keys())
my_dict2_values = list(my_dict2.values())
my_dict2
```




    Counter({7: 5, 2: 2, 3: 3, 5: 1, 1: 1})




```python
my_dict2_index = find_index(my_dict2_values, 1)
my_dict2_index
```




    [3, 4]




```python
[j for i,j in enumerate(my_dict2_keys) if i in my_dict2_index ]
```




    [5, 1]



Counter 함수 자체가 알파벳 순으로 key 값을 정렬하지 않기 때문에, 이를 유의해서 보아야 합니다.

그리고 만약에 dictionary 형태니까 Counter key 값과 value 값을 스위칭 해서 해도 되지 않을까 라고 생각하실 수 있습니다.

하지만 value 값이 모두 다른 경우에만 이러한 것이 가능하고

하나라도 같은 값이 존재하면, value 값이 key 값으로 넘어가는 과정에서 key가 중복된 것들은 하나를 제외하고 모두 사라지므로

원하시는 결과를 얻을 수 없습니다.


