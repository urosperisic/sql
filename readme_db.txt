____________________ sqlite cmd ____________________

sqlite3 data.db

.exit

.headers on
.mode column

.table

____________________ sqlite cmd ____________________

CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT);

INSERT INTO users (name, email) VALUES ('Uros', 'u@gmail.com');

SELECT * FROM users;

SELECT * FROM users WHERE email = 'm@gmail.com'

SELECT * FROM users WHERE id < 3 AND email != 'u@gmail.com';

DROP TABLE IF EXISTS users;