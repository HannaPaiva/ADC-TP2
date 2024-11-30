from FilterData.filterOutput import *
from bd_connector import criar_conexao, fechar_conexao
import sqlite3
import os

# Função para adicionar um empréstimo
def adicionar_emprestimo(livro_isbn, numero_leitor, id_funcionario, data_emprestimo, data_devolucao=None):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Emprestimos (livro_isbn, numero_leitor, id_funcionario, data_emprestimo, data_devolucao)
            VALUES (?, ?, ?, ?, ?)
        """, (livro_isbn, numero_leitor, id_funcionario, data_emprestimo, data_devolucao))
        conexao.commit()
        print("Empréstimo adicionado com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar empréstimo: {e}")
    fechar_conexao(conexao)


def listar_emprestimos():
    """
    Lista os empréstimos da base de dados utilizando a estrutura genérica criada.
    
    Parâmetros:
    - conexao: Objeto de conexão ao banco de dados.
    
    Retorna:
    - None: Exibe a tabela formatada no terminal.
    """
    conexao = criar_conexao()
    query = "SELECT * FROM emprestimos"  
    dados, headers = executar_query(conexao, query)  # Captura os dados e os headers
    return exibir_tabela(dados, headers)  # Exibe a tabela formatada

# Função para atualizar um empréstimo
def atualizar_emprestimo(id_emprestimo, livro_isbn=None, numero_leitor=None, id_funcionario=None, 
                         data_emprestimo=None, data_devolucao=None):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    campos = []
    valores = []

    if livro_isbn:
        campos.append("livro_isbn = ?")
        valores.append(livro_isbn)
    if numero_leitor:
        campos.append("numero_leitor = ?")
        valores.append(numero_leitor)
    if id_funcionario:
        campos.append("id_funcionario = ?")
        valores.append(id_funcionario)
    if data_emprestimo:
        campos.append("data_emprestimo = ?")
        valores.append(data_emprestimo)
    if data_devolucao:
        campos.append("data_devolucao = ?")
        valores.append(data_devolucao)

    if campos:
        valores.append(id_emprestimo)
        sql = f"UPDATE Emprestimos SET {', '.join(campos)} WHERE id_emprestimo = ?"
        try:
            cursor.execute(sql, valores)
            conexao.commit()
            print("Empréstimo atualizado com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao atualizar empréstimo: {e}")
    else:
        print("Nenhum campo para atualizar.")
    
    fechar_conexao(conexao)


# Função para deletar um empréstimo
def deletar_emprestimo(id_emprestimo):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM Emprestimos WHERE id_emprestimo = ?", (id_emprestimo,))
        conexao.commit()
        print("Empréstimo deletado com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao deletar empréstimo: {e}")
    fechar_conexao(conexao)



def verificarFuncionarioExiste(ID):
    """
    Verifica se um funcionário existe na tabela 'Funcionarios'.

    :param ID: ID do funcionário a ser verificado.
    :type ID: int
    :return: Retorna True se o funcionário existe, False caso contrário.
    :rtype: bool
    """
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM Funcionarios WHERE id_funcionario = ?", (ID,))
        resultado = cursor.fetchone()
        return resultado is not None
    finally:
        fechar_conexao(conn)



def verificarLeitorExiste(ID):
    """
    Verifica se um leitor existe na tabela 'Leitores'.

    :param ID: ID do leitor a ser verificado.
    :type ID: int
    :return: Retorna True se o leitor existe, False caso contrário.
    :rtype: bool
    """
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM Leitores WHERE numero_leitor = ?", (ID,))
        resultado = cursor.fetchone()
        return resultado is not None
    finally:
        fechar_conexao(conn)

