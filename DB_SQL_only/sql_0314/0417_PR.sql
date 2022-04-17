-- SQLite
CREATE TABLE articles(
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

INSERT INTO articles VALUES ('1번제목', '1번내용');

-- ALTER TABLE 
ALTER TABLE articles RENAME TO arti;

ALTER TABLE arti ADD COLUMN stst text NOT NULL DEFAULT 'ST';