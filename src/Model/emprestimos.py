"""
Módulo de Gerenciamento de Empréstimos
==============================================
Autor: [Hanna Paiva]
Data: [01/12/2024]
"""
from FilterData.filterOutput import *
from bd_connector import criar_conexao, fechar_conexao
import sqlite3

# Função para adicionar um empréstimo
def adicionar_emprestimo(livro_isbn, numero_leitor, id_funcionario, data_emprestimo, data_devolucao=None):
    """
    Adiciona um novo empréstimo ao banco de dados.

    :param livro_isbn: ISBN do livro a ser emprestado.
    :type livro_isbn: str
    :param numero_leitor: Número identificador do leitor.
    :type numero_leitor: int
    :param id_funcionario: ID do funcionário responsável pelo empréstimo.
    :type id_funcionario: int
    :param data_emprestimo: Data do empréstimo no formato YYYY-MM-DD.
    :type data_emprestimo: str
    :param data_devolucao: Data prevista para a devolução no formato YYYY-MM-DD, padrão é None.
    :type data_devolucao: str, optional
    :raises sqlite3.Error: Se ocorrer um erro ao inserir os dados no banco de dados.
    :return: None
    """
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
    Lista todos os empréstimos cadastrados no banco de dados.

    Esta função utiliza a função `executar_query` para capturar os dados da tabela
    de empréstimos e exibe os resultados em formato de tabela.

    :raises sqlite3.Error: Se ocorrer um erro ao consultar os dados.
    :return: None. Os dados são exibidos no terminal.
    :rtype: None
    """
    conexao = criar_conexao()
    query = """
        SELECT 
            Emprestimos.id_emprestimo,
            Emprestimos.livro_isbn,
            Livros.titulo AS titulo_livro,
            Livros.autor AS autor_livro,
            Emprestimos.numero_leitor,
            Leitores.nome AS nome_leitor,
            Emprestimos.id_funcionario,
            Funcionarios.nome AS nome_funcionario,
            Emprestimos.data_emprestimo,
            Emprestimos.data_devolucao
        FROM Emprestimos
        LEFT JOIN Livros ON Emprestimos.livro_isbn = Livros.isbn
        LEFT JOIN Leitores ON Emprestimos.numero_leitor = Leitores.numero_leitor
        LEFT JOIN Funcionarios ON Emprestimos.id_funcionario = Funcionarios.id_funcionario
    """ 
    dados, headers = executar_query(conexao, query)  # Captura os dados e os headers
    return exibir_tabela(dados, headers)  # Exibe a tabela formatada


def atualizar_emprestimo(id_emprestimo, livro_isbn=None, numero_leitor=None, id_funcionario=None, 
                         data_emprestimo=None, data_devolucao=None):
    """
    Atualiza os dados de um empréstimo existente no banco de dados.

    :param id_emprestimo: ID do empréstimo a ser atualizado.
    :type id_emprestimo: int
    :param livro_isbn: Novo ISBN do livro, se necessário.
    :type livro_isbn: str, optional
    :param numero_leitor: Novo número identificador do leitor, se necessário.
    :type numero_leitor: int, optional
    :param id_funcionario: Novo ID do funcionário, se necessário.
    :type id_funcionario: int, optional
    :param data_emprestimo: Nova data do empréstimo no formato YYYY-MM-DD, se necessário.
    :type data_emprestimo: str, optional
    :param data_devolucao: Nova data de devolução no formato YYYY-MM-DD, se necessário.
    :type data_devolucao: str, optional
    :raises sqlite3.Error: Se ocorrer um erro ao atualizar os dados.
    :return: None
    """
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
    """
    Deleta um empréstimo existente no banco de dados.

    :param id_emprestimo: ID do empréstimo a ser deletado.
    :type id_emprestimo: int
    :raises sqlite3.Error: Se ocorrer um erro ao deletar os dados.
    :return: None
    """
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


def verificarLivroExiste(ISBN):
    """
    Verifica se um livro existe na tabela 'Livros'.

    :param ISBN: ISBN do livro a ser verificado.
    :type ISBN: str
    :return: Retorna True se o livro existe, False caso contrário.
    :rtype: bool
    """
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM Livros WHERE isbn = ?", (ISBN,))
        resultado = cursor.fetchone()
        return resultado is not None
    finally:
        fechar_conexao(conn)

def verificarTabelasVazias():
    """
    Verifica se alguma das tabelas ('Funcionarios', 'Leitores', 'Livros') está vazia.

    :return: Retorna uma tupla (achou, tabela). Se alguma tabela estiver vazia,
             'achou' será True e 'tabela' será o nome da tabela vazia. 
             Caso todas as tabelas tenham registros, retorna (False, None).
    :rtype: tuple
    """
    conn = criar_conexao()
    try:
        cursor = conn.cursor()

        tabelas = {
            "Funcionarios": "SELECT COUNT(*) FROM Funcionarios",
            "Leitores": "SELECT COUNT(*) FROM Leitores",
            "Livros": "SELECT COUNT(*) FROM Livros"
        }

        for tabela, query in tabelas.items():
            cursor.execute(query)
            count = cursor.fetchone()[0]
            if count == 0:
                return True, tabela

        return False, None
    finally:
        fechar_conexao(conn)