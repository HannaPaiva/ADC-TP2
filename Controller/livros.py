from bd_connector import criar_conexao, fechar_conexao
from tabulate import tabulate
import sqlite3

def adicionar_livro(isbn, titulo, autor, categoria, ano_publicacao):
    """
    Adiciona um novo livro ao banco de dados.

    Esta função insere um novo registro na tabela `Livros` do banco de dados
    com as informações fornecidas pelos parâmetros.

    :param isbn: ISBN (International Standard Book Number) do livro.
    :type isbn: int
    :param titulo: Título do livro.
    :type titulo: str
    :param autor: Autor do livro.
    :type autor: str
    :param categoria: Categoria do livro.
    :type categoria: str
    :param ano_publicacao: Ano de publicação do livro.
    :type ano_publicacao: int

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da inserção no banco de dados.

    :return: None
    """
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO Livros (isbn, titulo, autor, categoria, ano_publicacao) VALUES (?,?,?,?,?)",(isbn,titulo,autor,categoria,ano_publicacao))
        conexao.commit()
        print("Livro adicionado com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar livro: {e}")
    fechar_conexao(conexao)

def listar_livro():
    """
    Lista um novo livro ao banco de dados.

    Esta função lista todos os registos na tabela `Livros` do banco de dados e 
    etorna cada registo em formato de tabela.

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da listagem no banco de dados.

    :return: table
    :type: str
    """
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT * FROM Livros")
        livros = cursor.fetchall()
        fechar_conexao(conexao)
        headers = ["ISBN", "Título", "Autor", "Categoria", "Ano de Publicação"]
        table = tabulate(livros, headers, tablefmt="grid")
    except sqlite3.Error as e:
        print(f"Erro ao listar livros: {e}")
    return table

def listar_livro_por_id(isbn):
    """
    Lista um livro em específico do banco de dados.

    Esta função pesquisa um registro na tabela `Livros` do banco de dados
    com a informação fornecida pelo parâmetro ISBN, que é o identificador do livro.

    Retorna o registro encontrado em formato de tabela.

    :param isbn: ISBN (International Standard Book Number) do livro.
    :type isbn: int
    :raises sqlite3.Error: Se ocorrer um erro durante a execução da pesquisa no banco de dados.

    :return: str (Tabela formatada) ou None se nenhum livro for encontrado.
    """
    conexao = criar_conexao()
    cursor = conexao.cursor()
    table = None
    try:
        cursor.execute("SELECT * FROM Livros WHERE ISBN = ?", (isbn,))
        livros = cursor.fetchall()

        if livros:
            headers = ["ISBN", "Título", "Autor", "Categoria", "Ano de Publicação"]
            table = tabulate(livros, headers, tablefmt="grid")
    except sqlite3.Error as e:
        print(f"Erro ao listar o livro especificado: {e}")
    finally:
        fechar_conexao(conexao)

    return table
        

def atualizar_livro(isbn, titulo=None, autor=None, categoria=None, ano_publicacao=None):
    """
    Atualiza um livro no banco de dados.

    Esta função atualiza um registro na tabela `Livros` do banco de dados
    com as informações fornecidas pelos parâmetros.

    :param isbn: ISBN (International Standard Book Number) do livro.
    :type isbn: int
    :param titulo: Título do livro.
    :type titulo: str
    :param autor: Autor do livro.
    :type autor: str
    :param categoria: Categoria do livro.
    :type categoria: str
    :param ano_publicacao: Ano de publicação do livro.
    :type ano_publicacao: int

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da atualização no banco de dados.

    :return: None
    """
    conexao = criar_conexao()
    cursor = conexao.cursor()
    campos = []
    valores = []

    if isbn:
        campos.append("isbn = ?")
        valores.append(isbn)
    if titulo:
        campos.append("titulo = ?")
        valores.append(titulo)
    if autor:
        campos.append("autor = ?")
        valores.append(autor)
    if categoria:
        campos.append("categoria = ?")
        valores.append(categoria)
    if ano_publicacao:
        campos.append("ano_publicacao = ?")
        valores.append(ano_publicacao)

    if campos:
        valores.append(isbn)
        sql = f"UPDATE Livros SET {', '.join(campos)} WHERE isbn = ?"
        try:
            cursor.execute(sql, valores)
            conexao.commit()
            print("Livro atualizado com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao atualizar leitor: {e}")
    else:
        print("Nenhum campo para atualizar.")
    
    fechar_conexao(conexao)
    

def deletar_livro(isbnInp):
    """
    Apaga um livro do banco de dados.

    Esta função apaga um registro na tabela `Livros` do banco de dados
    com a informação fornecida pelo parâmetro ISBN, que é o identificador do livro.

    :param isbnInp: ISBN (International Standard Book Number) do livro a ser deletado.
    :type isbnInp: int

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da remoção no banco de dados.

    :return: None
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM Livros WHERE isbn = ?", (isbnInp,))
        livro = cursor.fetchone()

        if livro:
            cursor.execute("DELETE FROM Livros WHERE isbn = ?", (isbnInp,))
            conexao.commit()
            print("Livro deletado com sucesso.")
        else:
            print("ISBN não encontrado no banco de dados.")

    except sqlite3.Error as e:
        print(f"Erro ao deletar livro: {e}")

    finally:
        fechar_conexao(conexao)