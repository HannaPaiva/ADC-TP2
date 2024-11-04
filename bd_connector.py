import sqlite3

def criar_conexao():
    try:
        conexao = sqlite3.connect('base_de_dados')
        return conexao
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def fechar_conexao(conexao):
    if conexao:
        conexao.close()
