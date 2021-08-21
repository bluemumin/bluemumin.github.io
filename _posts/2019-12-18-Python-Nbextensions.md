---
layout: post
title:  "jupyter notebook Nbextensions 코드 숨기기 등 유용한 기능 설정"
subtitle:   "jupyter notebook Nbextensions 코드 숨기기 등 유용한 기능 설정"
categories: Python
tags: Tip
comments: true
---

#### 글을 작성하기 앞서 해당 글을 작성하기 이전에
#### Nbextensions의 기능을 알게 된 [사이트](https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231) 입니다.

<br/>

python을 사용 하는 사람들 중 일부는 jupyter notebook을 활용하여 분석을 할 것 입니다.

저 또한 jupyter notebook에서 간단한 분석 및 머신러닝 코드를 작성하고 실행시키고 있습니다.

이번 글에서는 이러한 jupyter notebook을 더 유용하게 사용할 수 있는 Nbextensions를 소개하려고 합니다.

<br/>

일단 Nbextensions는 무엇인가?라고 하면 간단히 말해서 부가 프로그램일 것이다.

마크다운으로 만들어진 목차를 한 눈에 보기 혹은 해당 목차로의 이동,

작성된 코드를 가리고 결과물만 보거나

혹은 코드를 보기 편하게 정리를 해주거나, dataframe 출력물을 즉석에서 정렬하는 것이 가능하다.

<br/>

이외에도, 현재 Nbextensions에서는 다양한 부가 기능이 존재하지만

이 글에서는, Nbextensions의 설치 방법 및 필자가 사용하는 기능들에 대해서 소개하려고 한다.

<br/>

1.일단 먼저 설치하는 방법은 간단하다. jupyter notebook을 키고 terminal에 들어가

pip install jupyter_contrib_nbextensions 를 입력한다.

<img data-action="zoom" src='{{ "/assets/img/nbextensions/1.PNG" | relative_url }}' alt='absolute'>

<br/>

2.위에서 입력한 코드를 실행하고 설치가 완료 되면

jupyter contrib nbextension install 을 입력한다.

<img data-action="zoom" src='{{ "/assets/img/nbextensions/2.PNG" | relative_url }}' alt='absolute'>

<br/>

3.1,2 실행 후 다시 jupyter notebook을 키면 Nbextensions가 추가가 된다.

<img data-action="zoom" src='{{ "/assets/img/nbextensions/3.PNG" | relative_url }}' alt='absolute'>

<br/>

4.이제 해당 Nbextensions를 클릭하면, 다음과 같은 창으로 이동하며, 

사용하고자 하는 기능들의 요약본을 확인 가능합니다.

하지만, 중간 중간 이미지가 사라져있거나,

설명한 부실한 경우가 있을 경우 구글 검색을 추천드립니다.

<img data-action="zoom" src='{{ "/assets/img/nbextensions/4.PNG" | relative_url }}' alt='absolute'>

Nbextensions의 가장 좋은 점이라면, 이렇게 클릭 방식으로 추가적인 설치 없이 바로 사용/비 사용이 가능하다는 것입니다.

이 다음 부터는, 제가 사용하는 Nbextensions의 기능과 자주 사용되는 기능들을 소개해드리려고 합니다.

<br/>

- Hide input all : 코드 숨기기

  화면에 보이는 눈 모양 아이콘을 클릭하시면, 코드는 감추어지고
  
  코드에서 나온 결과물(변수명, 그래프 등)만 보이게 됩니다.
  
<img data-action="zoom" src='{{ "/assets/img/nbextensions/hide.gif" | relative_url }}' alt='absolute'>

[사진 출처](https://towardsdatascience.com/the-most-in-demand-tech-skills-for-data-scientists-d716d10c191d)

<br/>

- Table of Conents (2) : 목차 한 눈에 보기 및 해당 목차로 이동

   단축 아이콘 중 nbextensions에 의해 추가 된 리스트 모양을 클릭하시면
   
   사이드에 현재 마크다운 형식으로 작성을 한 목차들의 리스트가 나오게 됩니다.
   
   이동하고자 하는 목차를 선택하게 되면, 해당 목차로 이동을 하게 됩니다.

<img data-action="zoom" src='{{ "/assets/img/nbextensions/목차.PNG" | relative_url }}' alt='absolute'>

<br/>

   추가적으로, 목차에 자동으로 번호를 부여하고 싶다면, 
   
   빨간 상자에 있는 것을 체크하시면 됩니다.

<img data-action="zoom" src='{{ "/assets/img/nbextensions/설정.PNG" | relative_url }}' alt='absolute'>

<br/>

- ExecuteTime : 코드 실행시간 보기

  코드가 실행이 되는 셀의 밑에 자동으로 측정시간이 기록됩니다.
  
  제가 이전에 포스팅 한 telegram 메세지 받는 코드와 같이 실행하면
  
  원활한 업무가 가능할 것입니다.

<img data-action="zoom" src='{{ "/assets/img/nbextensions/time.PNG" | relative_url }}' alt='absolute'>

<br/>

- table_beautifier : dataframe 정렬하기 및 보이기 개선

일반 dataframe은 변수명 왼쪽에 화살표가 없지만, nbextensions를 활용하면,

변수 옆에 오름차순, 내림차순이 가능한 화살표가 나타나게 되고, 나온 dataframe 내에서는

추가적인 sort_values 코드 없이 바로 차순 정렬이 가능합니다. 

(실제 datafrmae 저장은 아님)

<img data-action="zoom" src='{{ "/assets/img/nbextensions/sort.PNG" | relative_url }}' alt='absolute'>

<br/>

- Code Font Size : 코드 창만 폰트 사이즈 조절

기존에 ctrl 과 +, - 창으로 창 크기를 조절하셨다면, 해당 기능을 추가하시게 된다면

코드 cell의 폰트 크기만 조절이 가능하게 할 수 있습니다.

<img data-action="zoom" src='{{ "/assets/img/nbextensions/크기.png" | relative_url }}' alt='absolute'>

<br/>

(markdown 크기는 조절 안됨, 애초에 #갯수로 조절하기 때문으로 보임)

<br/>

다음 2개의 기능은 Nbextensions를 소개할 때 자주 사용이 되지만, 

저는 사용하지 않는 기능들입니다.

<br/>

- Autopep8 : 자동 코드 정리 기능

코드를 pep8 형식으로 바꾸어주는 기능으로, 단순한 빈칸 정렬이 아닌 형식에 맞춰 정리를 해주는 것으로 보입니다.

(예전에는 잘 됬는데 지금은 local error로 되고 있어 사용하지 않습니다.)


<img data-action="zoom" src='{{ "/assets/img/nbextensions/888.gif" | relative_url }}' alt='absolute'>

[사진 출처](https://towardsdatascience.com/the-most-in-demand-tech-skills-for-data-scientists-d716d10c191d)

<br/>

- Variable inspector : 변수 type, size, shape 등 확인 가능

데이터를 많이 불러오고, jupyter notebook에 할당된 dataframe, list 등 이 많을 경우에 유용한 기능일 것입니다.

팝업 형태로 나오는 것으로 기억이 되며, 확실히 좋은 부가 기능이지만,

아직까지는 이 정도까지는 필요하지 않을 것으로 보여 사용하지 않고 있습니다.

<img data-action="zoom" src='{{ "/assets/img/nbextensions/variable.png" | relative_url }}' alt='absolute'>

[사진 출처](https://towardsdatascience.com/the-most-in-demand-tech-skills-for-data-scientists-d716d10c191d)

<br/>

###### 다만 주의하셔야 할 점은, 해당 Nbextensions은 부가 프로그램이기 때문에,
###### Nbextensinos를 설치하지 않은 사용자에게는 해당 프로그램 기능이 보이지 않습니다.
###### (ex - ExecuteTime, Table of Conents 미적용)
###### 하지만, 사용을 하는 당사자는 매우 편리한 부가 프로그램이며,
###### 해당 기능을 모르는 분들에게 이러한 기능들을 추천드렸을 때, 매우 긍정적인 반응을 보이셨습니다.
