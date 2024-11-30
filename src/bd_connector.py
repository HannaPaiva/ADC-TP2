import os
import sqlite3

def criar_conexao():
    """
    Cria e retorna uma conexão com o banco de dados SQLite.

    :return: Objeto de conexão SQLite.
    :rtype: sqlite3.Connection
    :raises sqlite3.Error: Se ocorrer um erro ao conectar ao banco de dados.
    """
    try:
        # Caminho absoluto para o banco de dados
        db_path = os.path.join(os.path.dirname(__file__), "database/base_de_dados")
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise

def fechar_conexao(conn):
    """
    Fecha uma conexão com o banco de dados SQLite.

    :param conn: Objeto de conexão SQLite a ser fechado.
    :type conn: sqlite3.Connection
    """
    if conn:
        conn.close()
