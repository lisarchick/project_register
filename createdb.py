import sqlite3
conn = sqlite3.connect("users.db")

cursor = conn.cursor()
def create_users():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            login TEXT NOT NULL,
            password TEXT NOT NULL
                    )
    """
                )
    
def add_users_into_database(login,password):
    cursor.execute("""
    INSERT INTO users(login,password) VALUES(?,?)
""", (login,password))
    conn.commit()
    
def find_users_in_database(login,password):
    cursor.execute("""
    SELECT id FROM users WHERE login = ? AND password = ?
""", (login,password))
    users_id = cursor.fetchone()
    conn.close()
    return users_id is not None