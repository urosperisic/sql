____________________ sqlite cmd ____________________

sqlite3 data.db

.exit

.headers on
.mode column

____________________ sqlite cmd ____________________

CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT);

INSERT INTO users (name, email) VALUES ('Uros', 'u@gmail.com');

SELECT * FROM users;