import sqlite3 as sql


class MyDB:
    def __init__(self):
        self.con = sql.connect("app.sqlite3")
        self.cur = self.con.cursor()

    def create_tables(self):
        with self.con:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
                            full_name TEXT,
                            username TEXT,
                            email TEXT,
                            password TEXT,
                            date TEXT
                            )""")

    def insert_method(self, **kwargs):
        with self.con:
            self.cur.execute("""
            INSERT INTO 
            users (full_name, username, password, email, date) 
            VALUES (?, ?, ?, ?, ?)
            """, (
                kwargs['full_name'], kwargs['username'],
                kwargs['password'], kwargs['email'],
                kwargs['date']
            ))

    def select_method(self, username, password):
        with self.con:
            user = self.cur.execute("""
                    SELECT * FROM users WHERE username = ? AND password = ?
                    """, (username, password))

            return user.fetchone()


