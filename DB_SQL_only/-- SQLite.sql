-- SQLite
ALTER TABLE examples RENAME TO users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    contry TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

SELECT * FROM users;

INSERT INTO users VALUES (101, '현주', '김', 25, '대전광역시', '010-4951-9122', '20');
INSERT INTO users VALUES (102, '경희', '이', 61, '대전광역시', '010-4107-9122', '10000');

SELECT * FROM users WHERE id = 102;

DROP TABLE users;

UPDATE users SET first_name='철수' WHERE id=102;
SELECT * FROM users WHERE id = 102;

DELETE FROM users WHERE id=101;