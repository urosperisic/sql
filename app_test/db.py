import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)"
        )
        self.conn.commit()

    def add_user(self, name):
        self.cur.execute("INSERT INTO users (name) VALUES (?)", (name,))
        self.conn.commit()

    def get_all_users(self):
        self.cur.execute("SELECT * FROM users")
        return self.cur.fetchall()

    def close(self):
        self.conn.close()