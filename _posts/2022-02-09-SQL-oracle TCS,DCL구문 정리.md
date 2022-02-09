---
layout: post
title:  "Oracle sql TCS, DCL 구문 정리"
subtitle:   "Oracle TCS, DCL 구문 정리"
categories: SQL
comments: true
tags: Oracle
---

## oracle DB의 TSC, DCL 구문을 정리하려고 합니다

### 1.TSC 구문

TRANSACTION CONTROL STATEMENT 의 약자이므로

해당 구문은 트랜잭션과 관련된 제어 구문이다.

트랜잭션은 함께 수행되는 작업의 논리적인 단위이다.

이전에 이 트랜잭션을 은행의 송금 방식에 비유해 이야기 하였는데

은행의 송금 방식의 핵심은 

중간에 어떠한 상황으로 인해 송금이 진행이 되지 않았다면

다시 송금 전으로 돌아갈 수 있어야된다는 것과

송금이 완료되면 이를 되돌리기 위해서는 추가적인 작업이 필요하다는 것이다.

<br/>

송금의 단계를 진행하고 이를 완료하는 것을

SQL구문에서는 commit이라고 하며

    COMMIT;

을 수행하게 되면 트랜잭션이 종료되게 된다.

보통은 DML, DDL 구문의 수행 이후에,

정상적인 트랜잭션 내용을 반영하기 위해서 수행을 해준다.

<br/>

그리고 중간에 송금 전 상황으로 돌아갈 수 있게 해주는 것을 롤백이라고 한다.

COMMIT을 하지 않고, 변경 내용을 모두 취소하기 위해서 사용한다.

    ROLLBACK;

을 수행하게 되면 취소 후에 트랜잭션을 종료하게 된다.

<br/>

한 트랜잭션 안에 변경 사항이 많게 되었을 때,

위에처럼 ROLLBACK을 사용하게 되면 모든 변경 사항들이 취소가 되게 된다.

그렇기 때문에 중간 중간 원하는 지점으로 ROLLBACK을 하고 싶은 경우를 위해

SAVEPOINT가 존재한다.

    변경 쿼리1;
    SAVEPOINT point이름1;

    변경 쿼리2;
    SAVEPOINT point이름2;

원하는 변경 사항 이후에 해당 쿼리를 실행시켜 주게 되면

SAVEPOINT가 생성이 되고

    ROLLBACK TO SAVEPOINT point이름1;

을 수행하게 되면 

변경 쿼리2가 수행이 되지 않은 상태로 트랜잭션이 롤백된다.

이 상황에서 

    ROLLBACK TO SAVEPOINT point이름2;

를 하게 되면, 이미 이전 시점으로 롤백이 되었기에

해당 쿼리는 에러가 발생하게 된다.

<br/> 

### 2.DCL 구문

DATA CONTOL LANGUAGE로 데이터 제어, 즉 권한과 관련된게 가장 큰 구문이다.

그렇기에 주로 사용자 관리, 권한 & 롤 부여 등을 수행하는 구문이 있다.

    CREATE USER user_name IDENTIFIED BY user_password;

해당 구문은 사용자를 생성하는 구문으로

계정 접속자가 해당 user_name/password로 DB에 접속할 수 있다.

ALTER를 통해서 비밀번호 변경, 계정 잠금/해제 등이 가능하며

DROP을 통해서 사용자 삭제가 가능하다.

<br/>

이렇게 사용자가 계정을 통해 접속해서 모든걸 할 수 있는건 아니다.

시스템 권한/ 오브젝트 권한을 부여하는 방식으로

사용자의 무분별한 작업을 방지시킬 수 있다.

<br/>

권한은 부여시에는 GRANT, 취소시에는 REVOKE가 사용이 된다.

시스템 권한 중에서 가장 많이 부여할 것이 테이블 생성 권한이다.

    GRANT CREATE TABLE TO user_name;

그리고 일반적인 유저에게 가장 많이 부여하는 것이 오브젝트 권한이다.

    GRANT SELECT, INSERT ON table_name1 TO user_name;

해당 테이블 하나에 접근, 데이터 삽입 권한을 부여하는 개념이다.

<br/>

마지막으로 ROLE은 사용자와 비슷한 개념이지만

권한과 사용자 사이에 중간 연결 통로 같은 개념이다.

권한을 사용자 각각에게 부여해서 관리가 어렵게 되는 것 보다는

특정 권한들을 모아서 ROLE에 부여하고 이를 사용자에게 부여하는 방식으로

효율적인 권한 관리가 가능해진다.

    CREATE ROLE role_name1;

를 통해서 ROLE을 만들고

권한 부여/삭제 방식은 GRANT/REVOKE를 통해서 하면 된다.

또한 ROLE은 사용자에도 가능하고, ROLE에도 부여가 가능하다.

    GRANT role_name2 TO role_name1;

    GRANT role_name1 TO user_name1;

다만 이러한 적용은 다시 접속을 수행하여야지 적용이 된다.