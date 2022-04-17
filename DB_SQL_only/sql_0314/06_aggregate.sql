SELECT COUNT(age) FROM users;

SELECT rowid, * FROM users;

SELECT AVG(age) FROM users WHERE age>=30;
SELECT MAX(age) FROM users WHERE age>=30;
SELECT MIN(age) FROM users WHERE age>=30;
SELECT SUM(age) FROM users WHERE age>=30;