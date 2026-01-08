import sqlite3

DB_NAME = "users.db"

def init_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = init_db()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL  
            )
    """)
    conn.commit()
    conn.close()