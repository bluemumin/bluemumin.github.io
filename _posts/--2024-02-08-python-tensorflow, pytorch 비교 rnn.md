---
layout: post
title:  "Tensorflow & Pytorch 비교 RNN" 
subtitle:   "Tensorflow & Pytorch 비교 RNN"
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

### 1. RNN 기초

in tensorflow

```python

hidden_size = 2
rnn = tf.keras.layers.SimpleRNN(units=hidden_size, return_sequences=True, return_state=True)
outputs, states = rnn(x_data)

```

<br/>

in pytorch

```python

cell = torch.nn.RNN(input_size=4, hidden_size=2, batch_first=True)

hidden = torch.randn(1,1,2)


#하나만 넣어보는 버전
inputs = torch.Tensor([h,e,l,l,o])

for one in inputs:
    one = one.view(1,1,-1)
    out, hidden = cell(one, hidden)

```

<br/>


 in tensorflow


```python

num_classes = 2
hidden_dims = [10, 10]

input_dim = len(char2idx)
output_dim = len(char2idx)
one_hot = np.eye(len(char2idx))

model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(input_dim = input_dim, output_dim = output_dim,
                                   trainable=False, mask_zero=True, input_length=max_sequence,
                                   embeddings_initializer=tf.keras.initializers.Constant(one_hot)))
model.add(tf.keras.layers.SimpleRNN(units=hidden_dims[0], return_sequences=True))
model.add(tf.keras.layers.TimeDistributed(tf.keras.layers.Dropout(rate=0.2)))
model.add(tf.keras.layers.SimpleRNN(units=hidden_dims[1]))
model.add(tf.keras.layers.Dropout(rate=0.2))
model.add(tf.keras.layers.Dense(units=num_classes))


model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(input_dim = input_dim, output_dim = output_dim, mask_zero = True,
                                   trainable=False, input_length = max_sequence,
                                   embeddings_initializer = tf.keras.initializers.Constant(one_hot)))
model.add(tf.keras.layers.Bidirectional(tf.keras.layers.SimpleRNN(units=hidden_dim, return_sequences=True)))
model.add(tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(units=num_classes)))




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

class Model(torch.nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.rnn = torch.nn.RNN(input_size=input_size,
                                hidden_size=hidden_size,
                                batch_first=True)
        
    def forward(self, hidden, x):
        x = x.view(batch_size, sequence_length, input_size) # Reshape input (batch first)
        
        out, hidden = self.rnn(x, hidden) # hidden: (num_layers * num_directions, batch, hidden_size)
        return hidden, out.view(-1, num_classes)
    
    def init_hidden(self): 
        return torch.zeros(num_layers, batch_size, hidden_size) 
    '''
    num_layers x batch_size x hidden_size인 모든 요소가 0인 텐서를 생성
    순환 신경망의 초기 hidden state 나타내는데 사용
    일반적으로 모든 값을 0으로 초기화 후, 시작하는 것이 일반적인 초기화 방법.
    모델의 학습이 시작되면서 역전파에 의해 이 값이 조정될 것.
    '''

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
                               batch_first = True)
        
    def forward(self, x):
        h_0 = torch.zeros(
            self.num_layers, x.size(0), self.hidden_size)
        
        x.view(x.size(0), self.sequence_length, self.input_size) # Reshape input (batch, sequence, input)
        
        out, _ = self.rnn(x, h_0)
        return out.view(-1, num_classes)
    
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
    # ex) (1, 2, 3)과 같은 크기의 텐서를 (2, 3)으로 바꿔줍니다.



```