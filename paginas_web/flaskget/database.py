import sqlite3

DB_NAME = "database.db"

def init_db():
    return sqlite3.connect(DB_NAME)

def crear_tabla():
    conn = init_db()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS personas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL
            )
    """)
    conn.commit()
    conn.close()