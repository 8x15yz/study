[TOC]

# SQL with django ORM

## 기본 준비 사항

* django app

  * 가상환경 세팅

  * 패키지 설치

  * migrate

    ```bash
    $ python manage.py migrate
    ```
  
* 제공 받은 `users.csv` 파일은 db.sqlite3와 같은 곳에 위치하도록 이동

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ sqlite3 db.sqlite3
    ```

  * 테이블 확인

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    ```
    
  * csv 파일 data 로드 및 확인

    ```sqlite
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    
    sqlite > SELECT COUNT(*) FROM users_user;
    100
    ```



---



## 문제

> ORM은 django extensions의 shell_plus에서,
>
> SQL은 수업에서 진행한 [SQLite 확장프로그램](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) 사용 방식으로 진행

### 1. 기본 CRUD 로직 (5)

1. 모든 user 레코드 조회

   ```python
   # orm
   ```

      ```sql
   -- sql 
      ```

2. user 레코드 생성

   ```python
   # orm
   ```

   ```sql
   -- sql 
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `102` 번 id의 전체 레코드 조회

   ```python
   # orm
   ```

   ```sql
   -- sql 
   ```

4. 해당 user 레코드 수정

   - ORM: `102` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `102` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

5. 해당 user 레코드 삭제

   - ORM: `102` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 

   ```python
   # orm
   ```

   ```sql
   -- sql
   ```



---



### 2. 조건에 따른 쿼리문 (8)

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
   ```

   ```sql
   -- sql
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   ```

   ```sql
   -- sql
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   # orm
   ```

   ```sql
   -- sql
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```



---



### 3. 정렬 및 LIMIT, OFFSET (4)

1. 나이가 많은 사람순으로 10명

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

2. 잔액이 적은 사람순으로 10명

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

3. ##### ///잔고는 오름차순, 나이는 내림차순으로 10명?///

      ```python
   # orm
   ```

   ```sql
   -- sql
   ```
   
   
   
4. ##### ///성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```



---



### 4. 표현식

#### 4.1 Aggregate (5) 2, 3

> - https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#aggregation
>- '종합', '집합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용
>- `Django_aggregation.md` 문서 참고

1. 전체 평균 나이

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

2. ##### ///김씨의 평균 나이

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

3. ##### ///강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   ```

   ```sql
   -- sql
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```



#### 4.2 Annotate (1)

1. 지역별 인원 수

   ```PYTHON
   # orm
   ```

   ```SQL
   -- sql
   ```

   

## +) 0314 hw

1) countries 테이블을 생성하시오. 

   room_num TEXT,

     check_in TEXT,

     check_out TEXT,

     grade TEXT,

     price INTEGER

   ```sql
   
   ```

   

2) 데이터를 입력하시오. 

   ('B203', '2019-12-31', '2020-01-03', 'suite', 900),

   ('1102', '2020-01-04', '2020-01-08', 'suite', 850),

   ('303', '2020-01-01', '2020-01-03', 'deluxe', 500),

   ('807', '2020-01-04', '2020-01-07', 'superior', 300)

   ```sql
   
   ```

   

3) 테이블의 이름을 hotels로 변경하시오. 

   ```sql
   ```

   

4) 객실 가격을 내림차순으로 정렬하여 상위 2개의 room_num과 price를 조회하시오. 

   ```sql
   
   ```

   

5) grade 별로 분류하고 분류된 grade 개수를 내림차순으로 조회하시오. 

   ```sql
   
   ```

   

6) 객실의 위치가 지하 혹은 등급이 deluxe인 객실의 모든 정보를 조회하시오. 

   ```sql
   ```

   

7) 지상층 객실이면서 2020년 1월 4일에 체크인 한 객실의 목록을 price 오름차순으로 조회하시오.

   ```sql
   ```

   