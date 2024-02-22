---
layout: post
title:  "Tensorflow & Pytorch 비교 RNN" 
subtitle:   "Tensorflow & Pytorch 비교 RNN"
categories: Python
tags: DL
comments: true
---

## RNN 모델의 Encoder / Decoder 코드를 Tensorflow와 Pytorch에서 비교한 게시물 입니다.

<br/>

tensorflow와 pytorch를 동시에 사용하기 위해서, 

Main Base : [Tensorflow 실습 코드 출처](https://github.com/hunkim/DeepLearningZeroToAll/tree/master/tf2)

비교용 Base : [Pytorch 실습 코드 출처](https://github.com/hunkim/PyTorchZeroToAll/tree/master)

or pytorch 2.2.0+cpu version에서 오류 수정 한 버전으로 비교.

전체 파일 내용은 [추후 추가 링크]() 확인 가능.

해당 블로그에는 비교 내용 작성.

<br/>

### 1. Encoder

in tensorflow

```python

def gru(units):
    return tf.keras.layers.GRU(units, return_sequences=True,
                              return_state=True, recurrent_initializer = 'glorot_uniform')

class Encoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, enc_units, batch_size):
        super(Encoder, self).__init__()
        self.batch_size = batch_size
        self.enc_units = enc_units
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = gru(self.enc_units)
        
    def call(self, x, hidden):
        x = self.embedding(x)
        output, state = self.gru(x, initial_state = hidden)
        
        return output, state
    
    def initialize_hidden_state(self):
        return tf.zeros((self.batch_size, self.enc_units))

```

<br/>

in pytorch

```python

class EncoderRNN(nn.Module):

    def __init__(self, input_size, hidden_size, n_layers=1):
        self.hidden_size = hidden_size
        self.n_layers = n_layers

        super(EncoderRNN, self).__init__()

        self.embedding = nn.Embedding(input_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size, n_layers)

    def forward(self, word_inputs, hidden):
        # Note: we run this all at once (over the whole input sequence)
        seq_len = len(word_inputs)
        # input shape: S x B (=1) x I (input size)
        embedded = self.embedding(word_inputs).view(seq_len, 1, -1)
        output, hidden = self.gru(embedded, hidden)
        return output, hidden

    def init_hidden(self):
        # (num_layers * num_directions, batch, hidden_size)
        return cuda_variable(torch.zeros(self.n_layers, 1, self.hidden_size))
        '''
        num_layers x batch_size x hidden_size인 모든 요소가 0인 텐서를 생성
        순환 신경망의 초기 hidden state 나타내는데 사용
        일반적으로 모든 값을 0으로 초기화 후, 시작하는 것이 일반적인 초기화 방법.
        모델의 학습이 시작되면서 역전파에 의해 이 값이 조정될 것.
        '''
```

<br/>

### 2. Decoder

in tensorflow

```python

def gru(units):
    return tf.keras.layers.GRU(units, return_sequences=True,
                              return_state=True, recurrent_initializer = 'glorot_uniform')

class Decoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, dec_units, batch_size):
        super(Decoder, self).__init__()
        self.batch_size = batch_size
        self.dec_units = dec_units
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = gru(self.dec_units)
        self.fc = tf.keras.layers.Dense(vocab_size)
        
    def call(self, x, hidden, enc_output):
        x = self.embedding(x)
        output, state = self.gru(x, initial_state = hidden)
        
        output = tf.reshape(output, (-1, output.shape[2])) # output shape == (batch_size * 1, hidden_size)
        
        x = self.fc(output) # output shape == (batch_size * 1, vocab)
        
        return x, state
    
    def initialize_hidden_state(self):
        return tf.zeros((self.batch_size, self.dec_units))

```

<br/>

in pytorch

```python


class DecoderRNN(nn.Module):

    def __init__(self, hidden_size, output_size, n_layers=1):
        super(DecoderRNN, self).__init__()

        self.embedding = nn.Embedding(output_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size, n_layers)
        self.out = nn.Linear(hidden_size, output_size)

    def forward(self, input, hidden):
        # input shape: S(=1) x B (=1) x I (input size)
        # Note: we run this one step at a time. (Sequence size = 1)
        output = self.embedding(input).view(1, 1, -1)
        output, hidden = self.gru(output, hidden)
        output = self.out(output[0])
        # No need softmax, since we are using CrossEntropyLoss
        return output, hidden

    def init_hidden(self):
        # (num_layers * num_directions, batch, hidden_size)
        return cuda_variable(torch.zeros(self.n_layers, 1, self.hidden_size))

```

<br/>

### 3. 학습 방법

in tensorflow

```python

for epoch in range(epochs):
    
    hidden = encoder.initialize_hidden_state()
    total_loss = 0
    
    for ii, (s_len, s_input, t_len, t_input, t_output): in enumerate(data):
            loss = 0
            with tf.GradientTape() as tape:
                enc_output, enc_hidden = encoder(s_input, hidden)
                dec_hidden = enc_hidden
                dec_input = tf.expand_dims([target2idx['<bos>']] * batch_size, 1)
                
                for tt in range(1, t_input.shape[1]):
                    
                    predictions, dec_hidden = decoder(dec_input, dec_hidden, enc_output)
                    loss += loss_function(t_input[:, tt], predictions)
                    dec_input = tf.expand_dims(t_input[:, tt], 1) #using teacher forcing ->>> 확인 필요
                    
            batch_loss = (loss / int(t_input.shape[1]))
            total_loss += batch_loss
            variables = endocer.variables * decoder.variables
            gradient = tape.gradient(loss, variables)
            optimizer.apply_gradients(zip(gradient, variables))
            
        if epoch % 10 == 0 :
            print('epoch {} loss {:.4f} batch loss {:.4f}'.format(epoch,
                                                                 total_loss / n_batch,
                                                                 batch_loss.numpy()))
            checkpoint,save(file_prefix = checkpoint_prefix)
```

<br/>

in pytorch

```python

def train(src, target):
    src_var = str2tensor(src)
    target_var = str2tensor(target, eos = True)
    
    encoder_hidden = encoder.init_hidden()
    encoder_outputs, encoder_hidden = encoder(src_var, encoder_hidden)
    
    hidden = encoder_hidden
    loss = 0
    
    for cc in range(len(target_var)):
        token = target_var[cc - 1] if cc else str2tensor(SOS_token)
        output, hidden = decoder(token, hidden)
        
        
        predicted_char_index = torch.argmax(output)
        target_char_index = torch.tensor(target_var[cc])
        loss += criterion(output.view(1, -1), target_char_index.view(1))
        
        decoder_in = target_char_index
        
    encoder.zero_grad()
    decoder.zero_grad()
    loss.backward()
    optimizer.step()
    
    return loss.item() / len(target_var)  # loss.item()을 사용하여 손실 값을 가져옴

for epoch in range(1, N_EPOCH + 1):
    for ii, (srcs, targets) in enumerate(train_loader):
        train_loss = train(srcs[0], targets[0])

```
<br/>

### 4. 예측 및 평가

in tensorflow

```python

def prediction(sentence, encoder, decoder, inp_lang, targ_lang, 
               max_length_inp, max_length_targ):
    inputs = [inp_lang[ii] for ii in sentence.split(' ')]
    inputs = pad_sequences([inputs, maxlen=max_length_inp, padding='post'])
    inputs = tf.convert_to_tensor(inputs)
    
    result = ''
    
    hidden = [tf.zeros((1, units))]
    enc_out, enc_hidden = encoder([inputs, hidden])
    
    for tt in range(max_length_targ):
        predictions, dec_hidden = decoder(dec_input, dec_hidden, enc_out)
        predicted_id = tf.argmax(predictions[0].numpy())
        result += idx2target[predicted_id] + ' '
        
        if idx2target.get(predicted_id) == '<eos>':
            return result, sentence
        
        dec_input = tf.expand_dims([predicted_id], 0)
    
    return result, sentence

sentence = 'I feel hungry'

result, output_sentence = prediction(sentence, encoder, decoder,
                                    source2idx, target2idx,
                                    s_max_len, t_max_len)

print(sentence)
print(result)
```

<br/>

in pytorch

```python
def test():
    encoder_test = sm.EncoderRNN(10, 10, 2)
    decoder_test = sm.AttnDecoderRNN(10,10,2)
    
    if torch.cuda.is_available():
        encoder_test.cuda()
        decoder_test.cuda()
        
    encoder_hidden = encoder_test.init_hidden()
    word_input = cuda.variable(torch.LongTensor([1,2,3]))
    encoder_outputs, encoder_hidden = encoder_test(word_input, encoder_hidden)
    print(encoder_outputs,size())
    
    word_target = cuda_variable(torch.LongTensor([1,2,3]))
    decoder_attns = torch.zeros(1,3,3)
    decoder_hidden = encoder_hidden
    
    for cc in ragne(len(word_target)):
        decoder_output, decoder_hidden, decoder_attn = decoder_test(word_target[cc],
                                                                   decoder_hidden,
                                                                   encoder_outputs)
        
        print(decoder_output.size(), decoder_hidden.size(), decoder_attn.size())
        decoder_attns[0, cc] = decoder_attn.squeeze(0).cpu().data

```





in tensorflow

```python


def evaluate(sentence, encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ):
    attention_plot = np.zeros((max_length_targ, max_length_inp))
    
    inputs = [inp_lang[i] for i in sentence.split(' ')]
    inputs = pad_sequences([inputs], maxlen=max_length_inp, padding='post')
    inputs = tf.convert_to_tensor(inputs)
    
    result = ''
    
    hidden = [tf.zeros((1,units))]
    enc_out, enc_hidden = encoder(inputs, hidden)
    dec_hidden = enc_hidden
    dec_input = tf.expand_dims([targ_lang['<bos>']], 0)
    
    for tt in range(max_length_targ):
        predictions, dec_hidden, attention_weights = decoder(dec_input, dec_hidden, enc_out)
        
        attention_weights = tf.reshape(attention_weights, (-1, ))
        attention_plot[tt] = attention_weights.numpy()
        
        predicted_id = tf.argmax(predictions[0]).numpy()
        result += idx2target[predicted_id] + ' '
        
        if idx2target.get(predicted_id) == '<eos>':
            return result, sentence, attention_plot
        
        dec_input = tf.expand_dims([predicted_id], 0)
    
    return result, sentence, attention_plot

```

<br/>

in pytorch

```python

def translate(enc_input = 'example.sentence.', predict_len = 100, temperature = 0.9):
    input_var = str2tensor(enc_input)
    encoder_hidden = encoder.init_hidden()
    encoder_outputs, encoder_hidden = encoder(input_var, encoder_hidden)
    
    hidden = encoder_hidden
    
    predicted = ''
    dec_input = str2tensor(SOS_token)
    for cc in range(predict_len):
        output, hidden = decoder(dec_input, hidden)
        
        output_dist = output.data.view(-1).div(temperature).exp()
        top_i = torch.multinomial(output_dist, 1)[0]
        
        if top_i == EOS_token:
            break
            
        predicted_char = chr(top_i.item())
        predicted += predicted_char
        
        dec_input = str2tensor(predicted_char)
        
    return enc_input, predicted

```