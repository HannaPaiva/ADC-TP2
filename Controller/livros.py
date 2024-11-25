from bd_connector import criar_conexao, fechar_conexao
import sqlite3

def adicionar_livro(isbn, titulo, autor, categoria, ano_publicacao):
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
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Livros")
    livros = cursor.fetchall()
    fechar_conexao(conexao)
    return livros


def atualizar_livro(isbn, titulo=None, autor=None, categoria=None, ano_publicacao=None):
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
        campos.append("ano publicacao = ?")
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
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM Livros WHERE isbn = ?", (isbn,))
        conexao.commit()
        print("Livro deletado com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao deletar leitor: {e}")
    fechar_conexao(conexao)
