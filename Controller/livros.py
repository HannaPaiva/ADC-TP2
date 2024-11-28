from bd_connector import criar_conexao, fechar_conexao
from tabulate import tabulate
import sqlite3

def adicionar_livro(isbn, titulo, autor, categoria, ano_publicacao):
    '''Função que tem como objetivo preparar e executar a query para inserir um livro novo na base de dados, com os valores de input introduzidos que originam de menu_livro.py, opção 1
    Inclui tratamento de erro'''
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
    '''Função que tem como objetivo preparar e executar a query para listar todos os livros na base de dados, esta função é chamada através de menu_livro.py, opção 2
    Inclui tratamento de erros e formatação de output com a biblioteca tabulate [pip install tabulate]'''
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
    '''Função que tem como objetivo preparar e executar a query para listar um dado livro na base de dados através do seu ISBN, esta função é chamada através de menu_livro.py, opção 2
    Inclui tratamento de erros e formatação de output com a biblioteca tabulate [pip install tabulate]'''
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT * FROM Livros WHERE ISBN = ?", (isbn))
        livros = cursor.fetchall()
        fechar_conexao(conexao)
        headers = ["ISBN", "Título", "Autor", "Categoria", "Ano de Publicação"]
        table = tabulate(livros, headers, tablefmt="grid")
    except sqlite3.Error as e:
        print(f"Erro ao listar o livro especificado: {e}")
    return table
        

def atualizar_livro(isbn, titulo=None, autor=None, categoria=None, ano_publicacao=None):
    '''Função que tem como objetivo preparar e executar a query para atualizar um livro com base no ISBN na base de dados, com os valores de input introduzidos que originam de menu_livros.py, opção 3
    Inclui tratamento de erros'''
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
    
def deletar_livro(isbn):
    '''Função que tem como objetivo preparar e executar a query para apagar um livro com base no ISBN na base de dados, com o valor de input introduzidos que originam de menu_livros.py, opção 4
    Inclui tratamento de erros'''
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM Livros WHERE isbn = ?", (isbn,))
        conexao.commit()
        print("Livro deletado com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao deletar leitor: {e}")
    fechar_conexao(conexao)
