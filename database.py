import sqlite3

def criar_banco():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        concluida BOOLEAN DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()