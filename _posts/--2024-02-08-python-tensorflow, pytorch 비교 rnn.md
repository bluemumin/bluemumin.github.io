---
layout: post
title:  "Tensorflow & Pytorch 비교 RNN" 
subtitle:   "Tensorflow & Pytorch 비교 RNN"
categories: Python
tags: DL
comments: true
---

## RNN 기본 모델 코드를 Tensorflow와 Pytorch에서 비교한 게시물 입니다.

<br/>

tensorflow와 pytorch를 동시에 사용하기 위해서, 

Main Base : [Tensorflow 실습 코드 출처](https://github.com/deeplearningzerotoall/TensorFlow/tree/master/tf_2.x)

비교용 Base : [Pytorch 실습 코드 출처](https://github.com/hunkim/PyTorchZeroToAll/tree/master)

or pytorch 2.2.0+cpu version에서 오류 수정 한 버전으로 비교.

전체 파일 내용은 [tensorflow_pytorch_comaprison](https://github.com/bluemumin/tensorflow_pytorch_comparison) 확인 가능.

해당 블로그에는 비교 내용 작성.

<br/>

### 1. RNN 기초

먼저 tensorflow에서의 RNN 코드이다.

<br/>

 in tensorflow

```python

num_classes = 2
hidden_dims = [10, 10]

input_dim = len(char2idx)
output_dim = len(char2idx)
one_hot = np.eye(len(char2idx)) #N×N 크기의 단위 행렬(identity matrix)을 생성

model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(input_dim = input_dim, output_dim = output_dim,
                                   trainable=False, mask_zero=True, input_length=max_sequence,
                                   embeddings_initializer=tf.keras.initializers.Constant(one_hot)))
#trainable은 임베딩 가중치를 훈련 가능하게 할지 여부를 결정, False로 설정 -> 훈련 중에 업데이트되지 않음. 
model.add(tf.keras.layers.SimpleRNN(units=hidden_dims[0], return_sequences=True))
model.add(tf.keras.layers.TimeDistributed(tf.keras.layers.Dropout(rate=0.2))) #dropout을 시간 단계별로 적용
model.add(tf.keras.layers.SimpleRNN(units=hidden_dims[1]))
model.add(tf.keras.layers.Dropout(rate=0.2))
model.add(tf.keras.layers.Dense(units=num_classes))
```

<br/>

만약 tensorflow에서 순환신겸망을 양방향으로 구축하고 싶다면 아래와 같이

Bidirectional 층을 추가해주어야 합니다.

```python
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(input_dim = input_dim, output_dim = output_dim, mask_zero = True,
                                   trainable=False, input_length = max_sequence,
                                   embeddings_initializer = tf.keras.initializers.Constant(one_hot)))
model.add(tf.keras.layers.Bidirectional(tf.keras.layers.SimpleRNN(units=hidden_dim, return_sequences=True))) #양방향 순환 신경망
model.add(tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(units=num_classes)))
```

<br/>

그 다음은 pytorch에서의 모델 구축이다.

순환신겸망을 양방향으로 구축하고 싶다면 

bidirectional=True 옵션을 지정하면 된다.

 in pytorch

```python

class RNN(torch.nn.Module):
    
    def __init__(self, num_classes, input_size, hidden_size, num_layers):
        super(RNN, self).__init__()
        
        self.num_classes = num_classes
        self.num_layers = num_layers
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.sequence_length = sequence_length
        
        self.rnn = torch.nn.RNN(input_size = 5,
                               hidden_size = 5,
                               batch_first = True) #bidirectional=True
        
    def forward(self, x):
        h_0 = torch.zeros(
            self.num_layers, x.size(0), self.hidden_size)
        
        x.view(x.size(0), self.sequence_length, self.input_size) # Reshape input (batch, sequence, input)
        
        out, _ = self.rnn(x, h_0)
        return out.view(-1, num_classes)
```

<br/>

### 1-2. 모델 학습 코드

그리고 학습을 원한다면, epoch 수 만큼 반복해가면서 gradient를 감소시키는 방향으로

모델을 학습시키면 된다.

in tensorflow

```python
tr_loss_hist = []

for epoch in range(epochs):
    avg_tr_loss = 0
    tr_step = 0
    
    for x_mb, y_mb in tr_dataset:
        with tf.GradientTape() as tape:
            tr_loss = loss_fn(model, x=x_mb, y=y_mb, training=True)
        grads = tape.gradient(target=tr_loss, sources=model.variables)
        opt.apply_gradients(grads_and_vars=zip(grads, model.variables))
        avg_tr_loss += tr_loss
        tr_step += 1
    else:
        avg_tr_loss /= tr_step
        tr_loss_hist.append(avg_tr_loss)
```

in pytorch

```python
rnn = RNN(num_classes, input_size, hidden_size, num_layers)  

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(rnn.parameters(), lr=0.1)

for epoch in range(20):
    outputs = rnn(inputs)
    optimizer.zero_grad()
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
    _, idx = outputs.max(1)
    idx = idx.data.numpy()
    result_str = [idx2char[c] for c in idx.squeeze()] 
    # .squeeze( : 텐서 크기 줄이기 -> 차원크기 1인 차원 제거
    # ex) (1, 2, 3)과 같은 크기의 텐서를 (2, 3)으로 변경.
```

### cf) 양방향 순환 신경망 학습 방식