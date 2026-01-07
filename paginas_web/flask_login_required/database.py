import sqlite3

DB_NAME = "database.db"

def init_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = init_db()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password INTEGER NOT NULL
            )
    """)
    conn.commit()
    conn.close()