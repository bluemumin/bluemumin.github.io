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

### 1. with Attention

 attention 매커니즘의 경우, encoder에서는 추가되는 것이 없고

 Decoder에서 추가 된다.


<br/>

in tensorflow

```python

class Decoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, dec_units, batch_size):
        super(Decoder, self).__init__()
        self.batch_size = batch_size
        self.dec_units = dec_units
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = gru(self.dec_units)
        self.fc = tf.keras.layers.Dense(vocab_size)
        
        # used for attention (기존 이후 추가되는 영역)
        self.W1 = tf.keras.layers.Dense(self.dec_units)
        self.W2 = tf.keras.layers.Dense(self.dec_units)
        self.V = tf.keras.layers.Dense(1)
        
    def call(self, x, hidden, enc_output):
        
        #attention 위해서 추가됨
        hidden_with_time_axis = tf.expand_dims(hidden, 1)
        score = self.V(tf.nn.tanh(self.W1(enc_output) + self.W2(hidden_with_time_axis)))
        attention_weights = tf.nn.softmax(score, axis=1)
        
        context_vector = attention_weights * enc_output
        context_vector = tf.reduce_sum(context_vector, axis=1)
        
        #기존 영역
        x = self.embedding(x)
        x = tf.concat([tf.expand_dims(context_vector, 1), x], axis = -1) #임베딩과 attention 결합
        output, state = self.gru(x, initial_state = hidden)
        
        output = tf.reshape(output, (-1, output.shape[2])) # output shape == (batch_size * 1, hidden_size)
        
        x = self.fc(output) # output shape == (batch_size * 1, vocab)
        
        return x, state, attention_weights
    
    def initialize_hidden_state(self):
        return tf.zeros((self.batch_size, self.dec_units))

```

<br/>


in pytorch

```python


class AttnDecoderRNN(nn.Module):

    def __init__(self, hidden_size, output_size, n_layers=1, dropout_p=0.1):
        super(AttnDecoderRNN, self).__init__()

        # Linear for attention
        self.attn = nn.Linear(hidden_size, hidden_size)

        # Define layers
        self.embedding = nn.Embedding(output_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size,
                          n_layers, dropout=dropout_p)
        self.out = nn.Linear(hidden_size * 2, output_size)

    def forward(self, word_input, last_hidden, encoder_hiddens):
        rnn_input = self.embedding(word_input).view(1, 1, -1)  # S=1 x B x I
        rnn_output, hidden = self.gru(rnn_input, last_hidden)

        attn_weights = self.get_att_weight(rnn_output.squeeze(0), encoder_hiddens)
        context = attn_weights.bmm(encoder_hiddens.transpose(0, 1))  # B x S(=1) x I

        rnn_output = rnn_output.squeeze(0)  # S(=1) x B x I -> B x I
        context = context.squeeze(1)  # B x S(=1) x I -> B x I
        output = self.out(torch.cat((rnn_output, context), 1))

        return output, hidden, attn_weights

    def get_att_weight(self, hidden, encoder_hiddens):
        seq_len = len(encoder_hiddens)

        attn_scores = cuda_variable(torch.zeros(seq_len))  # B x 1 x S

        for i in range(seq_len):
            attn_scores[i] = self.get_att_score(hidden, encoder_hiddens[i])

        return F.softmax(attn_scores).view(1, 1, -1)

    def get_att_score(self, hidden, encoder_hidden):
        score = self.attn(encoder_hidden)
        return torch.dot(hidden.view(-1), score.view(-1))

```



<br/>







 in tensorflow


```python


```


<br/>

in pytorch

```python


```