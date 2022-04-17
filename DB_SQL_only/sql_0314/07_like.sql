-- LIKE

SELECT rowid, * FROM users;

SELECT * FROM users WHERE phone LIKE '%5114%';


-- ORDER BY

SELECT first_name, last_name, balance FROM users ORDER BY balance DESC LIMIT 10;

-- GROUP BY

SELECT AVG(balance) FROM users GROUP BY last_name;

SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;