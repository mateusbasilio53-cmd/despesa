import sqlite3

def criar_tabela(): 
    conexao = sqlite3.connect('financas.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS despesas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            categoria TEXT NOT NULL,
            valor REAL NOT NULL,
            data TEXT NOT NULL
        )
        ''')

    conexao.commit()
    conexao.close()
