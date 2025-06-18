---
layout: post
title:  "Tensorflow & Pytorch 비교 RNN Seq2Seq Attention" 
subtitle:   "Tensorflow & Pytorch 비교 RNN Seq2Seq Attention"
categories: Python
tags: DL
comments: true
---

## Seq2Seq with Attention 모델을 Tensorflow와 Pytorch에서 비교한 게시물입니다.

<br/>

tensorflow와 pytorch를 동시에 사용하기 위해서, 

Main Base : [Tensorflow 실습 코드 출처](https://github.com/deeplearningzerotoall/TensorFlow/tree/master/tf_2.x)

비교용 Base : [Pytorch 실습 코드 출처](https://github.com/hunkim/PyTorchZeroToAll/tree/master)

or pytorch 2.2.0+cpu version에서 오류 수정 한 버전으로 비교.

전체 파일 내용은 [tensorflow_pytorch_comaprison](https://github.com/bluemumin/tensorflow_pytorch_comparison) 확인 가능.

해당 블로그에는 비교 내용 작성.

<br/>

### 1. Attention 모델 구조 메커니즘

기존 Seq2Seq 모델은 Encoder의 마지막 hidden state만을 

context vector로 사용하여 디코딩을 수행하지만, 문장이 길어질수록 정보 손실이 발생합니다.

이를 해결하기 위해 **Attention**은 **Decoder가 매 step마다 Encoder의 출력 전체를 참고**하여, 

입력 시퀀스에서 어느 부분을 "집중(attend)"할지를 스스로 학습합니다.

<br/>

### 2. Encoder (TensorFlow & PyTorch)

#### In TensorFlow

```python
class Encoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, enc_units, batch_size):
        super(Encoder, self).__init__()
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = tf.keras.layers.GRU(enc_units, return_sequences=True,
                                       return_state=True, recurrent_initializer='glorot_uniform')
        
    def call(self, x, hidden):
        x = self.embedding(x)
        output, state = self.gru(x, initial_state=hidden)
        return output, state
    
    def initialize_hidden_state(self):
        return tf.zeros((self.batch_size, self.enc_units))

    - 단어 임베딩 → GRU 순으로 처리

    - return_sequences=True를 통해 모든 time step의 hidden output 반환 (Attention 계산에 필요)
```

<br/>

#### In PyTorch

```python
class EncoderRNN(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(EncoderRNN, self).__init__()
        self.embedding = nn.Embedding(input_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size)

    def forward(self, input_seq, hidden):
        embedded = self.embedding(input_seq).view(seq_len, 1, -1)
        output, hidden = self.gru(embedded, hidden)
        return output, hidden

    def init_hidden(self):
        return torch.zeros(1, 1, self.hidden_size)
```

구조는 TensorFlow와 거의 동일하되, 

PyTorch는 batch dimension이 직접적으로 처리되지 않아 .view()로 차원을 맞춰줌

<br/>

### 3. Decoder with Attention

#### In tensorflow

TensorFlow에서는 Bahdanau Attention 방식의 구조가 포함됩니다.

W1, W2, V로 구성된 Additive Attention (Bahdanau) 사용

Encoder의 모든 output과 Decoder의 이전 hidden state를 조합하여 score 계산

```python
class Decoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, dec_units, batch_size):
        super(Decoder, self).__init__()
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = tf.keras.layers.GRU(dec_units, return_sequences=True, return_state=True)
        self.fc = tf.keras.layers.Dense(vocab_size)
        
        # Attention layers
        # used for attention (기존 이후 추가되는 영역)
        self.W1 = tf.keras.layers.Dense(dec_units)
        self.W2 = tf.keras.layers.Dense(dec_units)
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
        x = tf.concat([tf.expand_dims(context_vector, 1), x], axis=-1) #임베딩과 attention 결합
        output, state = self.gru(x)
        output = tf.reshape(output, (-1, output.shape[2])) # output shape == (batch_size * 1, hidden_size)
        x = self.fc(output) # output shape == (batch_size * 1, vocab)

        return x, state, attention_weights
```

<br/>

#### In pytorch

PyTorch에서는 dot-product 기반의 간단한 attention을 커스텀 구현합니다.

Attention score를 직접 계산

bmm() 함수로 context vector 계산 후 GRU 출력과 연결

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

### 4. 예측 및 평가 (Prediction & Evaluation)

#### In tensorflow

TensorFlow에서는 입력 문장을 토큰화한 후, 

Encoder로부터 전체 시퀀스의 context vector를 얻고 Decoder를 통해 step-by-step 예측을 수행합니다. 

이 과정에서 attention weight도 함께 반환되어 시각화 등에 활용할 수 있습니다.

    - step-by-step 방식으로 예측

    - argmax 방식으로 가장 확률 높은 단어 선택

    - attention weight를 저장하여 시각화 가능

    - <eos> 토큰이 등장하면 디코딩 종료
  
    - pad_sequences, tf.argmax, tf.expand_dims 등의 전처리와 텐서 조작 API 활용 

```python

def evaluate(sentence, encoder, decoder, inp_lang, targ_lang, 
             max_length_inp, max_length_targ):
    attention_plot = np.zeros((max_length_targ, max_length_inp))

    # 입력 전처리
    inputs = [inp_lang.get(word, 0) for word in sentence.split(' ')]
    inputs = pad_sequences([inputs], maxlen=max_length_inp, padding='post')
    inputs = tf.convert_to_tensor(inputs)

    result = ''
    hidden = [tf.zeros((1, decoder.dec_units))]
    enc_out, enc_hidden = encoder(inputs, hidden)

    dec_hidden = enc_hidden
    dec_input = tf.expand_dims([targ_lang['<bos>']], 0)

    for t in range(max_length_targ):
        predictions, dec_hidden, attention_weights = decoder(dec_input, dec_hidden, enc_out)

        # attention 저장
        attention_weights = tf.reshape(attention_weights, (-1,))
        attention_plot[t] = attention_weights.numpy()

        # 예측 결과 선택
        predicted_id = tf.argmax(predictions[0]).numpy()
        result += list(targ_lang.keys())[list(targ_lang.values()).index(predicted_id)] + ' '

        if list(targ_lang.keys())[list(targ_lang.values()).index(predicted_id)] == '<eos>':
            return result.strip(), sentence, attention_plot

        # 다음 입력 설정
        dec_input = tf.expand_dims([predicted_id], 0)

    return result.strip(), sentence, attention_plot
```

<br/>

```python
# 예측 실행 예시
result, input_sentence, attention_plot = evaluate(
    sentence="I feel hungry",
    encoder=encoder,
    decoder=decoder,
    inp_lang=source2idx,
    targ_lang=target2idx,
    max_length_inp=s_max_len,
    max_length_targ=t_max_len
)

print("입력 문장:", input_sentence)
print("예측 결과:", result)
```

<br/>

#### in pytorch

PyTorch는 예측을 위한 translate() 함수를 정의해 문자 단위로 샘플링을 수행합니다. 

확률적 예측을 위해 temperature 매개변수를 통해 

softmax 분포를 조절하고 torch.multinomial()로 샘플링합니다.

    - str2tensor()는 문자열을 문자 ID로 변환

    - torch.multinomial()로 샘플링하여 확률 기반 예측 (예측 결과가 실행마다 다를 수 있음)

    - translate()는 Decoder가 한 글자씩 생성하도록 loop 수행

    - temperature 값을 낮추면 argmax에 가까운 결과, 높이면 다양성 증가

```python
def translate(enc_input='hello', predict_len=100, temperature=0.9):
    # 문자열을 tensor로 변환
    input_var = str2tensor(enc_input)  # e.g., 'hello' -> [tensor IDs]
    encoder_hidden = encoder.init_hidden()

    # Encoder 실행
    encoder_outputs, encoder_hidden = encoder(input_var, encoder_hidden)

    hidden = encoder_hidden
    predicted = ''
    dec_input = str2tensor(SOS_token)  # 시작 토큰

    for cc in range(predict_len):
        output, hidden = decoder(dec_input, hidden)

        # Temperature 기반 샘플링
        output_dist = output.data.view(-1).div(temperature).exp()
        top_i = torch.multinomial(output_dist, 1)[0]

        # EOS 토큰이면 종료
        if top_i.item() == EOS_token:
            break

        predicted_char = chr(top_i.item())
        predicted += predicted_char

        # 다음 입력 설정
        dec_input = str2tensor(predicted_char)

    return enc_input, predicted
```

```python
# 예측 실행 예시
input_seq, output_seq = translate("hello", predict_len=20, temperature=0.8)
print("입력 문장:", input_seq)
print("예측 결과:", output_seq)
```