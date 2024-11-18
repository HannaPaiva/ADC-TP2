from bd_connector import criar_conexao, fechar_conexao
import sqlite3

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


# Função para listar todos os empréstimos
def listar_emprestimos():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Emprestimos")
    emprestimos = cursor.fetchall()
    fechar_conexao(conexao)
    return emprestimos