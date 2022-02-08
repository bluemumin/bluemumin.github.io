---
layout: post
tags: []
categories: []
#date: 2019-06-25 13:14:15
#excerpt: ''
#image: 'BASEURL/assets/blog/img/.png'
#description:
#permalink:
title: 'title'
---


### TSC, DCL 구문

### 1.TSC 구문

TRANSACTION CONTROL STATEMENT 의 약자이므로

해당 구문은 트랜잭션과 관련된 제어 구문이다.

트랜잭션은 함께 수행되는 작업의 논리적인 단위이다.

그렇기에, 작업의 종료, 작업의 롤백으로 되어있다.

COMMIT을 수행하게 되면 트랜잭션이 종료되게 되고

ROLLBACK을 실행하면 트랜잭션 중에 실행된 항목의 이전으로 돌아가고 종료를 한다.

SAVEPOINT는 롤백 저장저을 생성하고 해당 시점으로 돌아가게 할 수 있다.

한 번 SAVEPOINT로 롤백을 하면, 그 이후 시점에 생성된 포인트들은 사라지게 된다

락킹 매커니즘???

<br/> 

### 2.DCL 구문

DATA CONTOL LANGUAGE로 데이터 제어, 즉 권한과 관련된게 가장 큰 구문이다.

그렇기에 주로 사용자 관리, 권한 & 롤 부여 등을 수행하는 구문이 있다.

USER 관련 구문

권한은 부여시에는 GRANT, 취소시에는 REVOKE가 사용이 된다.

롤은 권한과 사용자 사이에 있는 중간 연결통로 개념으로

권한을 사용자 각각에게 부여해서 관리가 어렵게 되는 것 보다는

특정 권한들을 모아서 ROLE에 부여하고 이를 사용자에게 부여하는 방식으로

효율적인 권한 관리가 가능해진다.

