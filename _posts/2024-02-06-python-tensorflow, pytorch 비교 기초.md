---
layout: post
title:  "Tensorflow & Pytorch 비교 기초 단계" 
subtitle:   "Tensorflow & Pytorch 비교 기초 단계"
categories: Python
tags: Deep Learning
comments: true
---

## Tensorflow와 Pytorch에서 동일하게 사용되는 기능의 문법을 비교한 게시물 입니다.

<br/>

tensorflow와 pytorch를 동시에 사용하기 위해서, 

Main Base : [Tensorflow 실습 코드 출처](https://github.com/hunkim/DeepLearningZeroToAll/tree/master/tf2)

비교용 Base : [Pytorch 실습 코드 출처](https://github.com/hunkim/PyTorchZeroToAll/tree/master)

or pytorch 2.x version 따로 작성 후 비교.

전체 파일 내용은 [추후 추가 링크]() 확인 가능.

해당 블로그에는 비교 내용 작성.

<br/>

### 1. 기초 Operations

사칙연산 및 여러 계산법은 pytorch와 tensorflow가 대부분 비슷한 명령어를 공유한다.

다만 tensorflow는 일부 명령어가 tf.ceil 이런식으로 사용시 사용이 되지 않는다.

현재 사용하는 2.5.3 version에서는 tf.math.명령어를 사용하면 전부 다 사용이 가능하다.

이 코드들 중 기존 값에 음수 부호를 추가하는 torch.neg의 경우

tensorflow에서는 tensorflow.math.negative로 사용된다.

하단 python 코드는 pytorch version에서 작성된 계산 방법.

```python

torch_add = torch.add(torch.tensor([1.0, 2.0]), torch.tensor([3.0, 4.0])) # 덧셈

torch_subtract = torch.subtract(torch.tensor([5.0, 6.0]), torch.tensor([2.0, 1.0])) # 뺄셈

torch_multiply = torch.multiply(torch.tensor([2.0, 3.0]), torch.tensor([4.0, 5.0])) # 곱셈

torch_divide = torch.divide(torch.tensor([10.0, 15.0]), torch.tensor([2.0, 3.0])) # 나눗셈

torch_pow = torch.pow(torch.tensor([2.0, 3.0]), 3) # n-제곱

torch_negative = torch.neg(torch.tensor([4.0, -5.0])) # 음수 부호 추가 --> # tensor([-4.,  5.])

torch_abs = torch.abs(torch.tensor([-2.0, 3.0])) # 절대값

torch_sign = torch.sign(torch.tensor([-2.0, 3.0])) # 부호  --> tensor([-1.,  1.])

torch_round = torch.round(torch.tensor([1.6, 2.4])) # 반올림

torch_ceil = torch.ceil(torch.tensor([1.6, 2.4])) # 올림

torch_floor = torch.floor(torch.tensor([1.6, 2.4])) # 내림

torch_square = torch.square(torch.tensor([2.0, 3.0])) # 제곱

torch_sqrt = torch.sqrt(torch.tensor([4.0, 9.0])) # 제곱근

torch_maximum = torch.maximum(torch.tensor([1.0, 2.0]), torch.tensor([3.0, 1.0])) #최대값 -> tensor([3., 2.])

torch_minimum = torch.minimum(torch.tensor([1.0, 2.0]), torch.tensor([3.0, 1.0])) # 최소값 -> tensor([1., 1.])

x = torch.tensor([2.0, 3.0, 4.0]) #예시 값

result_cumsum = torch.cumsum(x, dim=0) # 누적합 -> tensor([2., 5., 9.])

result_cumprod = torch.cumprod(x, dim=0) #누적곱 -> tensor([ 2.,  6., 24.])

result_log = torch.log(x) #로그값
```

### 2. 주요 비교사항

A. 단순 선형 회귀를 tensorflow와 pytorch에서 재현할때의 주요 차이점.

pytorch에서는 torch.tensor에서 requires_grad라는 매개변수로 기울기를 추적할지의 여부를 결정할 수 있다.

그래서 매개변수를 갱신할때도, tensorflow는 with tf.GradientTape() as tape:를 써서

식 -> cost -> 개별 미분값 -> assign_sub를 통한, 기울기 * 개별 미분값 반영을 반복하지만

pytorch에서는 그래디언트를 자동으로 추적하기에, with torch.no_grad():를 써서 추적하지 않도록 설정하고

이를 직접 빼는 방식을 사용한다.

<br/>

in tensorflow

  #값 지정시
  tf.constant(3.0, tf.float32) 
  tf.constant([1.0, 3.0])

  #linear regression 매개변수 초기 값 지정 및 평균 계산
  W = tf.Variable(2.9)
  cost = tf.reduce_mean(tf.square(hyp - y_train)) #에러 제곱의 평균

  #매개변수 갱신시, 
  for ii in range(100):
    with tf.GradientTape() as tape:
      hyp = W * x_train + b
      cost = tf.reduce_mean(tf.square(hyp - y_train))

      W_grad, b_grad = tape.gradient(cost, [W,b]) #gradeint method를 불러서 개별 미분값을 구해서 반환함.
      W.assign_sub(lr*W_grad) #현재 매개변수 값에, 학습률 * 매개변수 개별 미분값 빼기
      b.assign_sub(lr*b_grad)

<br/>

in pytorch

  #값 지정시
  torch.tensor(3.0, dtype=torch.float32)
  torch.tensor([3.0, 4.0], dtype=torch.float32)

  #linear regression 매개변수 초기 값 지정 및 평균 계산
  W = torch.tensor(2.9, requires_grad=True) # requires_grad = 기울기를 추적할것인지 나타내는 매개변수
  cost = torch.mean((hyp - y_train)**2)

  #매개변수 갱신시, 
  for ii in range(100):
    hyp = W * x_train + b
    cost = torch.mean((hyp - y_train)**2)

    W_grad, b_grad = torch.autograd.grad(cost, [W, b]) # 그래디언트 계산 autograd.grad

    with torch.no_grad(): #pytorch에서 파라미터 업데이트 시, 그레디언트를 추적하지 않도록 설정하는 블록
    # 모델의 파라미터 값을 테스트하거나 평가할 때는 그래디언트를 추적할 필요가 없음.
      W -= lr * W_grad #torch에서는 assign_sub 기능이 없어, 직접 빼는 방법 사용함.
      b -= lr * b_grad