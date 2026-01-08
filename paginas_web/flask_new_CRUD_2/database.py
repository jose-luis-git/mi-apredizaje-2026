import sqlite3

DB_NAME = "database.db"

def init_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = init_db()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS people(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            note INTEGER NOT NULL
            )
    """)
    conn.commit()
    conn.close()