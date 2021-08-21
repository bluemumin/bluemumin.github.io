---
layout: post
title:  "python jupyter notebook 활용한 텔레그램 코드 완료 알림 받기!"
subtitle:   "python jupyter notebook 활용한 텔레그램 코드 완료 알림 받기!"
categories: Python
tags: Tip
comments: true
---

#### 글을 작성하기 앞서 해당 텔레그램을 활용한 알림을 받는 방법을 찾은 [출처](https://steemit.com/kr/@sifnax/python-5-telegram-api) 입니다.
<br/>

행의 갯수가 많아 간단한 코드가 오래 실행되는 경우,
<br/>
혹은 복잡한 코드 설정으로 인해 오래 코드가 실행되는 경우에서
<br/>
이 방법은 확실히 효율이 좋은 방법입니다.
<br/>
가장 기본 전제가 되는 것은 텔레그램을 설치하시는 것입니다.
<br/>
텔레그램 설치 방법은 생략하고 시작합니다.


1.일단 텔레그램을 설치하고 가장 처음에 실행이 되는 창입니다.
<br/>
<img data-action="zoom" src='{{ "/assets/img/telegram/t1.PNG" | relative_url }}' alt='absolute'>

<br/>

2.이후 검색창에 BotFather를 검색합니다.
<br/>
<img data-action="zoom" src='{{ "/assets/img/telegram/t2.PNG" | relative_url }}' alt='absolute'>

<br/>

3.검색하여 나오는 BotFather클릭하시면 다음과 같이 나옵니다.
<br/>
<img data-action="zoom" src='{{ "/assets/img/telegram/t3.PNG" | relative_url }}' alt='absolute'>

<br/>

4.start 버튼을 다음과 같은 명령어들이 나오며,
<br/>
  저희는 코드 완료 알림을 받기 위한 봇을 만들기 위해 /newbot을 입력해줍니다.
<br/>
<img data-action="zoom" src='{{ "/assets/img/telegram/t4.PNG" | relative_url }}' alt='absolute'>

<br/>

5./newbot을 입력 이후 bot의 이름을 정해야되는데, 그냥 이름을 보내는 경우,
<br/>
   반드시 bot으로 끝나야 된다고 메세지가 옵니다.
<br/>
<img data-action="zoom" src='{{ "/assets/img/telegram/t5.PNG" | relative_url }}' alt='absolute'>

<br/>

6.정상적으로 bot의 이름을 입력한 경우, 해당 bot의 api token이 나옵니다.
<br/>
  해당 가려진 부분을 복사하셔서 사용하시면 됩니다.
<br/>
<img data-action="zoom" src='{{ "/assets/img/telegram/t6.PNG" | relative_url }}' alt='absolute'>

<br/>

7.이제 만든 bot의 이름을 겁색하여, 코드완료를 위한 알림이 오기 위한 사전 작업을 시작합니다.
<br/>
<img data-action="zoom" src='{{ "/assets/img/telegram/t7.PNG" | relative_url }}' alt='absolute'>

<br/>

8.start 버튼을 누르고, 간단한 채팅으로 아무 메세지를 입력해주세요
<br/>
<img data-action="zoom" src='{{ "/assets/img/telegram/t8.PNG" | relative_url }}' alt='absolute'>

<br/>

# 코드 복사 가능 구간입니다.

9.주피터 노트북으로 들어와서 telegram을 import 해주시고, 
<br/>
(없으신 경우 !pip install python-telegram-bot or !pip install python-telegram-bot --upgrade 활용)
<br/>
  복사를 하신 api키를 할당하시고, 이를 이용하여서 bot을 불러옵니다.
  <br/>
  기존 대화가 없기 때문에 update를 실행해도 빈 창이 뜨실겁니다. 
  <br/>
  (오류가 발생하시면 해당 코드만 다시 실행해주세요)
<br/>

<img data-action="zoom" src='{{ "/assets/img/telegram/t9.PNG" | relative_url }}' alt='absolute'>

<br/>

```python
## !pip install python-telegram-bot
#or 
# !pip install python-telegram-bot --upgrade
import telegram
API_KEY = 'your_api_key'
bot = telegram.Bot(token = API_KEY)   #bot을 선언합니다.
```


```python
updates = bot.getUpdates()
updates
```




    [<telegram.update.Update at 0x22637c7ab38>]




```python
# for i in updates:
#     print(i)
```

<br/>

10.이후 만드신 bot에 들어와서 아무 채팅이나 입력하신다면 다음과 update가 됬다는 리스트가 출력이 되며
<br/>
   이 할당된 updates를 print하시면, 해당 업데이트 내역이 나오게 됩니다.
<br/>
   여기서 주목을 하셔야 할 것은 'chat' : 바로 뒤에 나오는 'id'의 값입니다.
<br/>
   해당 id는 봇을 바꿔도 동일하며 해당 아이디를 알아야지 주피터 노트북을 이용하여서 
<br/>
   텔레그램으로 메세지를 보낼 수 있습니다.

<br/>

<img data-action="zoom" src='{{ "/assets/img/telegram/t11.PNG" | relative_url }}' alt='absolute'>

<br/>

11.밑의 코드를 활용하여서 print해서 나오신 chat id를 입력해주세요 (해당 id는 봇이 바뀌어도 변하지 않습니다.)

```python
chat_id = "your_chat_id"
```

<br/><br/>

이후 텔레그램을 통해서 메세지를 받는 방법은 간단합니다. try 문을 활용하는 것입니다.
<br/>
실행을 원하시는 코드를 try문에 삽입하시고 오류가 발생했을 때의 문장과 성공했을 때의 입력 값을 다르게 주면 됩니다.

<br/>


12.먼저 코드가 정상적으로 실행이 되었을 때의 경우입니다.

<br/>

```python
try:
    a=1
except:
    bot.sendMessage(chat_id = chat_id, text="코드 실행이 실패하였습니다.")
else:
    bot.sendMessage(chat_id = chat_id, text="코드 실행이 성공적으로 진행되었습니다.")
```

코드에 error가 발생하지 않았기 때문에, else에  있는 text가 그대로 텔레그램 메세지로 도착한 것을 볼 수 있습니다.

<img data-action="zoom" src='{{ "/assets/img/telegram/t13.PNG" | relative_url }}' alt='absolute'>

<br/>

13.다음은 코드 실행 중 error가 발생한 경우입니다.

<br/>

```python
try:
    a=1/0
except:
    bot.sendMessage(chat_id = chat_id, text="코드 실행이 실패하였습니다.")
else:
    bot.sendMessage(chat_id = chat_id, text="코드 실행이 성공적으로 진행되었습니다.")
```

코드에 error가 발생하였기 때문에, except에  있는 text가 그대로 텔레그램 메세지로 도착한 것을 볼 수 있습니다.

<br/>

<img data-action="zoom" src='{{ "/assets/img/telegram/t15.PNG" | relative_url }}' alt='absolute'>

<br/>

###### 다만 주의하셔야 할 점은, 기존에 try문에서 발생하는 error가 나타나지 않기 때문에,
###### 오류 확인용으로는 거의 성공에 임박한 반복문, 언제 끝날지 모르는 모형 학습시간 확인용으로
###### 사용하시는게 적절해보입니다.

###### 저 같은 경우, 대용량의 데이터를 처리할 때 해당 기능을 활용하여서 다른 업무를 수행하곤 합니다.
