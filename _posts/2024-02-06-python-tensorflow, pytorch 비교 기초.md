---
layout: post
title:  "Tensorflow & Pytorch 비교 기초 단계" 
subtitle:   "Tensorflow & Pytorch 비교 기초 단계"
categories: Python
tags: DL
comments: true
---

## Tensorflow와 Pytorch에서 동일하게 사용되는 기능의 문법을 비교한 게시물 입니다.

<br/>

tensorflow와 pytorch를 동시에 사용하기 위해서, 

Main Base : [Tensorflow 실습 코드 출처](https://github.com/deeplearningzerotoall/TensorFlow/tree/master/tf_2.x)

비교용 Base : [Pytorch 실습 코드 출처](https://github.com/hunkim/PyTorchZeroToAll/tree/master)

or pytorch 2.2.0+cpu version에서 오류 수정 한 버전으로 비교.

전체 파일 내용은 [tensorflow_pytorch_comaprison](https://github.com/bluemumin/tensorflow_pytorch_comparison) 확인 가능.

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

#### A. 단순 선형 회귀를 tensorflow와 pytorch에서 재현할때의 주요 차이점.

pytorch에서는 torch.tensor에서 requires_grad라는 매개변수로 기울기를 추적할지의 여부를 결정할 수 있다.

단순한 선형 회귀의 매개변수를 갱신하기 위한 예제를 하는 아래의 코드에서

그래서 매개변수를 갱신할때도, tensorflow는 with tf.GradientTape() as tape:를 써서

식 -> cost -> 개별 미분값 -> assign_sub를 통한, 기울기 * 개별 미분값 반영을 반복하지만

pytorch에서는 그래디언트를 자동으로 추적하기에, 이를 굳이 재현하자면은

with torch.no_grad():를 써서 추적하지 않도록 설정하고 이를 직접 빼는 방식을 사용한다.

<br/>

in tensorflow

```python
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
```
<br/>

in pytorch

```python
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

    W_grad, b_grad = torch.autograd.grad(cost, [W, b]) # 자동 미분으로 그래디언트 계산 autograd.grad 

    with torch.no_grad(): #pytorch에서 파라미터 업데이트 시, 그레디언트를 추적하지 않도록 설정하는 블록
    # 모델의 파라미터 값을 테스트하거나 평가할 때는 그래디언트를 추적할 필요가 없음.
      W -= lr * W_grad #torch에서는 assign_sub 기능이 없어, 직접 빼는 방법 사용함.
      b -= lr * b_grad
```

<br/>

#### B. 실제 모델 활용시 차이점.

전체 비교 작업을 한 코드의 경우,

tensorflow 예시 코드가 전반적인 딥러닝 구조를 이해하기 위해, 

직접 함수를 생성해서 구현한 경우가 많아서

pytorch가 더 간결해 보일수 있다.

예시 데이터는 MNIST 데이터에 대한 softmax 방식 구현 내용 중 일부이다.

<br/>

in pytorch

```python
  import torch.nn.functional as F 

  class Net(torch.nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.l1 = torch.nn.Linear(784,520)
        self.l2 = torch.nn.Linear(520,320)
        self.l3 = torch.nn.Linear(320,240)
        self.l4 = torch.nn.Linear(240,120)
        self.l5 = torch.nn.Linear(120,10)
        
    def forward(self, x):
        x = x.view(-1, 784) # Flatten the data (n, 1, 28, 28)-> (n, 784)
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        x = F.relu(self.l3(x))
        x = F.relu(self.l4(x))
        return self.l5(x)

  model = Net()
  model.to(device)
  criterion = torch.nn.CrossEntropyLoss() # Softmax + CrossEntropy (logSoftmax + NLLLoss)
  optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.5)

```
in tensorflow

```python

  class Net(tf.keras.Model):
      def __init__(self):
          super(Net, self).__init__()
          self.flatten = tf.keras.layers.Flatten(input_shape=(28, 28))
          self.l1 = tf.keras.layers.Dense(520, activation='relu')
          self.l2 = tf.keras.layers.Dense(320, activation='relu')
          self.l3 = tf.keras.layers.Dense(240, activation='relu')
          self.l4 = tf.keras.layers.Dense(120, activation='relu')
          self.l5 = tf.keras.layers.Dense(10)

      def call(self, x):
          x = self.flatten(x)
          x = self.l1(x)
          x = self.l2(x)
          x = self.l3(x)
          x = self.l4(x)
          return self.l5(x)

  # Instantiate the model
  model = Net()

  # Compile the model
  model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.5),
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

```
일단 해당 버전에서는 pytorch에서는 모델을 생성하고, 

device라는 사전에 cpu인지 gpu 인지 지정한 장치로 이동을 시켜서 향후 모델을 구동한다.

반면에 tensorflow는 model을 할당하고 compile을 통해서, 

모델의 구성 요소를 지정할 수 있도록 한다.

그리고 모델 구축의 경우도, pytorch는 먼저 Linear를 통해서 차원변환을 정의하고

그 층을 forward를 할 때 relu를 추가하지만

tensorflow에서는 층 구성 당시에, activation까지 정의할 수 있다. 

마지막으로 tensorflow는 Flatten층을 이용해서, input_shape를 넣고 펴줄수 있다.

torch에서는 .view(-1, 원하는 값) 을 통해 변환이 가능한 듯 하다.

<br/>

그 다음으로는 모델 학습 코드 중 일부이다.

마찬가지로 tensorflow에서는 해당 방법을 직접 구현하는 방식을 사용했기에

pytorch보다는 코드가 길다.


in pytorch

```python

  optimizer.zero_grad()  # 이전에 계산된 그래디언트를 초기화
  output = model(data)
  loss = criterion(output, target)
  loss.backward()  # 손실에 대한 역전파 수행
  optimizer.step()  # 옵티마이저를 사용하여 파라미터 업데이트

```

in tensorflow

```python

  logits = model(images, training=True) #dropout 적용
  loss = tf.reduce_mean(tf.keras.losses.categorical_crossentropy(y_pred = logits,
                                                                y_true = labels, from_logits = True))
  def grad(model, images, labels):
    with tf.GradientTape() as tape:
      loss = loss_fn(model, images, labels)
    return tape.gradient(loss, model.variables)             

  def train(model, images, labels):
    grads = grad(model, images, labels)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))                                                 

```
pytorch에서는 이전 그래디언트를 초기화하고, 모델을 통해 예측하고,

해당 값을 통해 loss 계산 후, 역전파를 수행한다.

그리고 이를 옵티마이저를 통해 업데이트 하면서 이를 반복한다.

tensorflow의 경우는, 이를 직접 구현한 예시이지만

동일하게 예측 후, loss를 구하고, 이 그래디언트를 apply_gradients를 통해서 반영한다.

