---
layout: post
title:  "Tensorflow & Pytorch 비교 CNN" 
subtitle:   "Tensorflow & Pytorch 비교 CNN"
categories: Python
tags: DL
comments: true
---

## CNN 모델 코드를 Tensorflow와 Pytorch에서 비교한 게시물 입니다.

<br/>

tensorflow와 pytorch를 동시에 사용하기 위해서, 

Main Base : [Tensorflow 실습 코드 출처](https://github.com/hunkim/DeepLearningZeroToAll/tree/master/tf2)

비교용 Base : [Pytorch 실습 코드 출처](https://github.com/hunkim/PyTorchZeroToAll/tree/master)

or pytorch 2.x version 따로 작성 후 비교.

전체 파일 내용은 [추후 추가 링크]() 확인 가능.

해당 블로그에는 비교 내용 작성.

<br/>

### 1. CNN 기초

예시 데이터는 MNIST이며, input size는 28 * 28 입니다.

in tensorflow

```python
class MNISTModel(tf.keras.Model):
    def __init__(self):
        super(MNISTModel, self).__init__() #상위 init method call
        self.conv1 = tf.keras.layers.Conv2D(filters=32, kernel_size=[3,3], padding='SAME', activation=tf.nn.relu)
        self.pool1 = tf.keras.layers.MaxPool2D(padding='SAME')
        self.conv2 = tf.keras.layers.Conv2D(filters=64, kernel_size=[3,3], padding='SAME', activation=tf.nn.relu)
        self.pool2 = tf.keras.layers.MaxPool2D(padding='SAME')
        self.conv3 = tf.keras.layers.Conv2D(filters=128, kernel_size=[3,3], padding='SAME', activation=tf.nn.relu)
        self.pool3 = tf.keras.layers.MaxPool2D(padding='SAME') 
        self.pool3_flat = tf.keras.layers.Flatten()
        self.dense4 = tf.keras.layers.Dense(units=256, activation=tf.nn.relu)
        self.drop4 = tf.keras.layers.Dropout(rate=0.4)
        self.dense5 = tf.keras.layers.Dense(units=10)
        
    def call(self, inputs, training=False):
        net = self.conv1(inputs)
        net = self.pool1(net)
        net = self.conv2(net)
        net = self.pool2(net)
        net = self.conv3(net)
        net = self.pool3(net)
        net = self.pool3_flat(net)
        net = self.dense4(net)
        net = self.drop4(net)
        net = self.dense5(net)
        return net

```

<br/>


```python
class Net(torch.nn.Module):
    
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 10, kernel_size = 5, padding='same', padding_mode = 'zeros')
        self.conv2 = torch.nn.Conv2d(10, 20, kernel_size = 5, padding='same', padding_mode = 'zeros')
        self.mp = torch.nn.MaxPool2d(2)
        self.fc = torch.nn.Linear(980, 10) 
        
    def forward(self, x):
        in_size = x.size(0)
        x = F.relu(self.mp(self.conv1(x))) # (x, 1, 28, 28) -> (x, 10, 14, 14)
        x = F.relu(self.mp(self.conv2(x))) # (x, 10, 14, 14) -> (x, 20, 7, 7)
        x = x.view(in_size,-1) # (x, 20, 7, 7) -> (x, 980)
        x = self.fc(x) # (x, 980) -> (x, 10)
        return F.log_softmax(x)

```

<br/>

최대한 pytorch, tensorflow에서 유사하게 작성된 cnn 모델 구조를 가지고 왔다.

tensorflow는 이전이나 다음층에서 출력되는 필터의 수 까지 직접 지정하지 않아도 된다.

그리고 출력 크기를 고정시켜주는 same padding 기능의 경우도, 원활하게 사용이 가능하다.

하지만 pytorch에서는 해당 same padding 기능이 Conv2d에서는 존재하지만

stride가 1인 경우에서만 사용이 가능하다. 

(이것도 pytorch 1.9.1 이나 1.10.0 버전 이후에서 구현된 것)

<br/>

추가로 padding_mode가 있어 padding을 어떤 값으로 채울지 옵션이 있는데,

default는 zeros로 0으로 채운다.

reflect는 양끝에 거울처럼 반사된 값을,

replicate는 양 끝단 값을 padding 값으로 이용,

circular는 input 값을 순환하며 사용하는 기능이다.

다만, MaxPool2d에서 이러한 padding이 str 타입 지정으로는 되어있지 않아,

tensorflow보다는 번거롭다.

<br/>

그리고 flatten해서 torch.nn.Linear를 사용하고 싶은 경우라면

tensorflow는 해당 코드에서 Flatten만 하면 출력 크기에 상관없이

Dense에서 사용이 가능하다.

다만 pytorch에서는 이러한 출력 값 크기를 지정해줘야한다.

즉 직접 계산을 해야한다.

<br/>

위의 코드는 Conv2d에 same padding을 적용하여 

max pooling 과정에서의 출력 크기만 계산하면 되서

input : (1x28x28) -> (10x14x14) -> (20x7x7) 

flatten 후, 980이라는 값이 간단하게 나온다.

<br/>

만약 해당 same padding을 없앤다면 식을 통해 다음 출력을 직접 계산하면 됩니다.

높이(or 너비) = ((입력 높이 − 커널 높이 + 2 * 패딩) / 스트라이드) + 1

<br/>

(Conv2d : kernel_size = 5, padding = 미입력(default 0), stride = 미입력(default 1))

((28 - 5 + 2 * 0) / 1) + 1 ==> 24

<br/>

(MaxPool2d : kernel_size = 2, padding = 미입력(default 0), 

stride = 미입력 시, kernel_size와 동일 값 지정됨(default 1))

((24 - 2 + 2 * 0) / 2) + 1 ==> 12

if self.mp = torch.nn.MaxPool2d(kernel_size=2, stride=3) 이용시,

((24 - 2 + 2 * 0) / 3) + 1 ==> 7.333... + 1 => 올림처리로 9

<br/>

self.mp = torch.nn.MaxPool2d(kernel_size=3, stride=1, padding=1)

((28 - 3 + 2 * 1) / 1) + 1 ==> 27 + 1 => 올림처리로 9

<br/>

만약 pytorch로 class기반의 이전보다는 복잡한 CNN 모델을 작성하게 된다면

다음과 같이 작성이 되게 된다.

[코드 출처](https://github.com/hunkim/PyTorchZeroToAll/blob/master/11_1_toy_inception_mnist.py)

in pytorch

```python
class InceptionA(torch.nn.Module):
    
    def __init__(self, in_channels):
        super(InceptionA, self).__init__()
        self.branch1x1 = torch.nn.Conv2d(in_channels, 16, kernel_size=1)

        self.branch5x5_1 = torch.nn.Conv2d(in_channels, 16, kernel_size=1)
        self.branch5x5_2 = torch.nn.Conv2d(16, 24, kernel_size=5, padding=2)

        self.branch3x3dbl_1 = torch.nn.Conv2d(in_channels, 16, kernel_size=1)
        self.branch3x3dbl_2 = torch.nn.Conv2d(16, 24, kernel_size=3, padding=1)
        self.branch3x3dbl_3 = torch.nn.Conv2d(24, 24, kernel_size=3, padding=1)

        self.branch_pool = torch.nn.Conv2d(in_channels, 24, kernel_size=1)
            
    def forward(self, x):
        branch1x1 = self.branch1x1(x)
        
        branch5x5 = self.branch5x5_1(x)
        branch5x5 = self.branch5x5_2(branch5x5)
        
        branch3x3dbl = self.branch3x3dbl_1(x)
        branch3x3dbl = self.branch3x3dbl_2(branch3x3dbl)
        branch3x3dbl = self.branch3x3dbl_3(branch3x3dbl)
        
        branch_pool = F.avg_pool2d(x, kernel_size=3, stride=1, padding=1)
        branch_pool = self.branch_pool(branch_pool)
        
        outputs = [branch1x1, branch5x5, branch3x3dbl, branch_pool]
        
        return torch.cat(outputs,1)

class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = torch.nn.Conv2d(88, 20, kernel_size=5)
        
        self.incept1 = InceptionA(in_channels=10) # 16 + 24 + 24 + 24 = 88
        self.incept2 = InceptionA(in_channels=20)
        
        self.mp = torch.nn.MaxPool2d(2)
        self.fc = torch.nn.Linear(1408, 10) # 88 * 4 * 4
        
    def forward(self, x):
        in_size = x.size(0) #256 (batch_size)
        x = F.relu(self.mp(self.conv1(x))) # 28*28 -> 24*24 -> 12*12 ==> (x, 10, 12, 12)
        x = self.incept1(x) # (x, 10, 12, 12) => (x, 88, 12, 12)
        x = F.relu(self.mp(self.conv2(x))) # 12 * 12 -> 8 * 8 -> 4*4 ==> (x, 20, 4, 4)
        x = self.incept2(x) ## (x, 20, 4, 4) => (x, 88, 4, 4)
        x = x.view(in_size, -1) # (x, 88*4*4)
        x = self.fc(x) # (x, 88*4*4) => (x, 10)
        return F.log_softmax(x)

```
<br/>

다른 코드들 중에서, Linear(1408, 10)으로 하는 부분에서 가장 의문을 가진 것이

입력 크기를 계산하는 방법이 있을듯한 점이었다.

해당 부분은 추가로 찾은 뒤, 보충하는 방식으로 진행을 하여야 할 듯 하다.