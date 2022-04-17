-- SQLite

UPDATE classmates SET name='홍길동', adress='제주도' WHERE rowid=5;

--INSERT INTO classmates (rowid, name, age, adress) VALUES (5, '홍길동', 30, '서울');
SELECT rowid, * FROM classmates;