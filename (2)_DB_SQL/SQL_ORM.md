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
   User.objects.all()
   ```

      ```sql
   -- sql 
   SELECT * FROM users;
      ```

2. user 레코드 생성

   ```python
   # orm
   User.objects.create(first_name='길동',last_name='홍',age=100,country='제주도', phone='010-1234-4567', balance=10000,)
   <User: User object (101)>
   ```

   ```sql
   -- sql 
   INSERT INTO users VALUES (101, '현주', '김', 25, '대전광역시', '010-4951-9122', '200');
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `102` 번 id의 전체 레코드 조회

   ```python
   # orm
   User.objects.get(pk=101)
   <User: User object (101)>
   ```

   ```sql
   -- sql 
   SELECT * FROM users WHERE id = 102;
   ```

4. 해당 user 레코드 수정

   - ORM: `102` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `102` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   ```

      ```sql
   -- sql
   UPDATE users SET first_name='철수' WHERE id=102;
      ```

5. 해당 user 레코드 삭제

   - ORM: `102` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 

   ```python
   # orm
   ```

   ```sql
   -- sql
   DELETE FROM users WHERE id=101;
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
   SELECT  COUNT(*) FROM users;
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   ```

      ```sql
   -- sql
   SELECT first_name FROM users WHERE age = 30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   ```python
   # orm
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users WHERE age >= 30;
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users WHERE age <= 20;
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users WHERE age = 30 AND last_name = '김';
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   # orm
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users WHERE age = 30 OR last_name = '김';
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users WHERE phone LIKE '02-%';
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users WHERE country = '강원도' AND last_name = '황';
      ```



---



### 3. 정렬 및 LIMIT, OFFSET (4)

1. 나이가 많은 사람순으로 10명

   ```python
   # orm
   ```

      ```sql
   -- sql
   SELECT * FROM users ORDER BY age DESC LIMIT 10;
      ```

2. 잔액이 적은 사람순으로 10명

   ```python
   # orm
   ```

      ```sql
   -- sql
   SELECT * FROM users ORDER BY balance ASC LIMIT 10;
      ```

3. ##### ///잔고는 오름차순, 나이는 내림차순으로 10명?///

      ```python
   # orm
   ```

   ```sql
   -- sql
   SELECT * FROM users_user ORDER BY balance, age DESC LIMIT 10;
   ```
   
   두개 열을 기준으로 정할때 첫번째 나온 컬럼부터 정리함
   
   근데 balance는 지정해준게 없으니까 ASC 로 정리하는거임 (ASC가 기본값)
   
   그다음 나온 컬럼을 이제 뒤에 나온 ASC DESC 여부에 따라 정리르 하는거임 알겟냐 ?
   
   그니까 위 코드의 경우는 balance 가 먼저 나왔으니까 balance를 오름차순해서 정렬시킨 다음
   
   age를 여기서는 DESC 나왔으니까 내림차순으로 만든거임
   
   
   
4. ##### ///성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   ```

      ```sql
   -- sql
   SELECT * FROM users_user ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 4;
      ```
   
   둘다 내림차순이니까 둘다 명시를 해줘야됨 + 5번째 한명만 보여주니까 offset  사용하기



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
   SELECT AVG(age) FROM users;
      ```

2. ##### ///김씨의 평균 나이

   ```python
   # orm
   ```

      ```sql
   -- sql
   SELECT AVG(age) FROM users WHERE last_name = '김';
      ```

3. ##### ///강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   ```

   ```sql
   -- sql
   SELECT AVG(balance) FROM users WHERE country = '강원도';
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   ```

      ```sql
   -- sql
   SELECT balance FROM users GROUP BY balance ORDER BY balance DESC LIMIT 1;
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   ```

      ```sql
   -- sql
   SELECT SUM(balance) FROM users;
      ```



#### 4.2 Annotate (1)

1. 지역별 인원 수

   ```PYTHON
   # orm
   ```

   ```SQL
   -- sql
   SELECT country, COUNT(*) FROM users GROUP BY country;
   ```
   
   

## +) 0314 hw

1) countries 테이블을 생성하시오. 

   ```sql
   CREATE TABLE countries(
       room_num TEXT,
       check_in TEXT,
       check_out TEXT,
       grade TEXT,
       price INTEGER
   );
   ```

   

2) 데이터를 입력하시오. 

   ```sql
   INSERT INTO countries VALUES 
   ('B203', '2019-12-31', '2020-01-03', 'suite', 900),
   ('1102', '2020-01-04', '2020-01-08', 'suite', 850),
   ('303', '2020-01-01', '2020-01-03', 'deluxe', 500),
   ('807', '2020-01-04', '2020-01-07', 'superior', 300);
   ```

   

3) 테이블의 이름을 hotels로 변경하시오. 

   ```sql
   ALTER TABLE countries RENAME TO hotels;
   ```

   

4) 객실 가격을 내림차순으로 정렬하여 상위 2개의 room_num과 price를 조회하시오. 

   ```sql
   SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;
   ```

   

5) grade 별로 분류하고 분류된 grade 개수를 내림차순으로 조회하시오. 

   ```sql
   SELECT *, COUNT(*) FROM hotels GROUP BY grade ORDER BY COUNT(*) DESC;
   ```

   

6) 객실의 위치가 지하 혹은 등급이 deluxe인 객실의 모든 정보를 조회하시오. 

   ```sql
   SELECT * FROM hotels WHERE grade='deluxe' OR room_num LIKE 'B%';
   ```

   

7) 지상층 객실이면서 2020년 1월 4일에 체크인 한 객실의 목록을 price 오름차순으로 조회하시오.

   ```sql
   SELECT * FROM hotels WHERE check_in='2020-01-04' ORDER BY price ASC;
   ```

   