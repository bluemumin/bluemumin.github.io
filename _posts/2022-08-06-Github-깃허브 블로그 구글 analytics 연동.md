---
layout: post
title:  "깃허브 블로그를 구글 애널리틱스에 연동하기"
subtitle:   "깃허브 블로그를 구글 애널리틱스에 연동하기"
categories: Github
tags: blog
comments: true
toc : true
toc_sticky : true
---

## 깃허브 블로그를 구글 애널리틱스에 연동하는 방법들을 소개하려고 합니다.

<br/>

[구글 애널리틱스](https://analytics.google.com/analytics/web/?hl=ko&pli=1) 는

등록한 사이트의 사용자 수, 실시간 보고서 등 여러가지를 제공해주는 곳입니다.

현재 구글 애널리틱스는 GA4라고 불리우는 버전입니다.

만약 다른 블로그들에서 깃허브 연동시 "UA"로 시작되는 것을 찾으라고 하거나

해당 번호로 등록을 하라는 경우는 이전 버전의 경우이기에, GA4에서는 찾으실수가 없습니다.

<br/>

생성 절차의 경우, 블로그 url을 이용해서 등록만 하면 되기 때문에 생략하도록 하겠습니다.

<img data-action="zoom" src='{{ "/assets/img/blog_update/측정ID.PNG" | relative_url }}' alt='absolute'> 

생성이 된 이후에 보이는 이 측정 ID를 깃허브 블로그에 연동을 시키면 간단합니다.

보이시지 않는다면 관리자 > 데이터 스트림으로 이동하셔서 보시면 됩니다.

<br/>

_config.yml 파일로 이동하시게 되면

<img data-action="zoom" src='{{ "/assets/img/blog_update/measurement_id.jpg" | relative_url }}' alt='absolute'> 

해당 항목이 있는 경우도 있고, 직접 입력해야되는 경우가 있을 것입니다.

tracking_id의 경우 GA4 이전 버전에서 사용 한 것으로 알고 있고

measurement_id가 GA4에서 사용 되는 것으로 알고 있습니다.

어쨌든 둘 중 하나는 사용을 한다는 것이기에 입력 해주시고 commit으로 업데이트 하시면 됩니다.

<br/>

이렇게 되면 블로그에 업데이트가 완료 된 이후에, 정상적으로 된 경우라면

데이터를 받고 있다는 내용이 나오게 됩니다.

이러면 마무리가 되었습니다.

<br/>

하지만, 블로그가 GA4에 맞춰져서 개발이 되지 않은 경우라면 적용이 되지 않을 것입니다.

제 블로그가 그랬습니다.

그러할 경우에는 google-gtag를 통해서 블로그에 태그를 설치하셔야 합니다.

먼저 관리자 > 데이터 스트림으로 이동 해서 상세 창으로 들어가신 다음

제일 하단에 태그 안내 보기를 클릭하시면 됩니다.

<img data-action="zoom" src='{{ "/assets/img/blog_update/태그_안내.jpg" | relative_url }}' alt='absolute'> 

<br/>

그 다음에 나오는 코드를 복사하여서 head에 넣으라고 합니다.

저의 경우는 _includes 폴더 안에있는 head.html 을 열어서 제일 첫 부분에 붙여넣기 하였습니다.

<img data-action="zoom" src='{{ "/assets/img/blog_update/설치_안내.jpg" | relative_url }}' alt='absolute'> 

이렇게 하면 GA4로 개발이 되지 않은 블로그에서도 구글 태그를 통해

구글 애널리틱스를 연동할 수 있게 됩니다.