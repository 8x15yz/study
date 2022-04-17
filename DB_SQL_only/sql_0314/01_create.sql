-- create
CREATE TABLE classmates (
  name TEXT,
  age TEXT,
  adress TEXT
);

INSERT INTO classmates (rowid, name, age, adress) VALUES (5, '홍길동', 30, '서울');

-- pk포함해서 테이블 보고싶을때 쓰는 쿼리
SELECT rowid, * FROM classmates;

DROP TABLE classmates;

CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INT NOT NULL,
  adress TEXT NOT NULL
);

INSERT INTO classmates VALUES 
('홍길동', 30, '서울'),
('김철수', 28, '대전'),
('이싸피', 24, '광주'),
('김싸피', 31, '구미'),
('김현주', 45, '부울경');


-- 여기서부터는 read

INSERT INTO classmates VALUES ('홍길동', 30, '서울'), ('홍길동', 30, '대전'),('김싸피', 30, '광주'),('이삼성', 29, '구미'),('홍길동', 28, '부산');

SELECT rowid, name FROM classmates;

SELECT rowid, name FROM classmates LIMIT 1;

SELECT rowid, name FROM classmates LIMIT 2 OFFSET 2;

SELECT rowid, name FROM classmates WHERE adress = '서울';

SELECT DISTINCT adress FROM classmates;

