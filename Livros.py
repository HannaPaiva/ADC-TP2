import sqlite3
# from app import conexao
def conexao():
    conn = sqlite3.connect('base_de_dados')
    return conn

# Função que lista todos os livros na tabela Livros
def listar_livros():
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Livros')
    livros = cursor.fetchall()
    conn.close()
    return livros

# Função que lista o livro desejado através do ISBN
def listar_livros_id():
    isbn = input("Insira o ISBN do livro que deseja procurar: ")
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Livros WHERE isbn = ?;',(isbn,))
    livros = cursor.fetchall()
    conn.commit()
    conn.close()
    return livros

# Função que adiciona um novo livro à base de dados
def adicionar_livro():
    isbn = input("ISBN: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    categoria = input("Categoria: ")
    ano_publicacao = input("Ano de publicação: ")
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Livros (isbn, titulo, autor, categoria, ano_publicacao) VALUES(?, ?, ?, ?, ?)',(isbn,titulo,autor,categoria,ano_publicacao,))
    livros = cursor.fetchall()
    conn.commit()
    conn.close()
    return livros

# Função que atualiza os dados de um livro com base no ISBN fornecido
def atualizar_livro():
    isbn = input("ISBN: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    categoria = input("Categoria: ")
    ano_publicacao = input("Ano de publicação: ")
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('UPDATE Livros SET titulo='', autor='', categoria='', ano_publicacao=0 WHERE isbn=?', (titulo,autor,categoria,ano_publicacao,isbn,))
    livros = cursor.fetchall()
    conn.commit()
    conn.close()
    return livros

# Função que apaga um livro da base de dados através do ISBN
def apagar_livro():
    isbn = input("ISBN: ")
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Livros WHERE isbn=?', (isbn,))
    livros = cursor.fetchall()
    conn.commit()
    conn.close()
    return livros

listar_livros()