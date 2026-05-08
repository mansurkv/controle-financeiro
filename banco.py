import sqlite3

def conectar():
    return sqlite3.connect('financeiro.db')

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL,
                tipo TEXT NOT NULL,
                data TEXT NOT NULL
                )
    """)

    conexao.commit()
    conexao.close()
    print('Tabela Criada!')
