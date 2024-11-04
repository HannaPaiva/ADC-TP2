from bd_connector import criar_conexao, fechar_conexao

def adicionar_leitor(nome, morada, telefone, nif, email):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO Leitores (nome, morada, telefone, nif, email) VALUES (?, ?, ?, ?, ?)", 
                       (nome, morada, telefone, nif, email))
        conexao.commit()
        print("Leitor adicionado com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar leitor: {e}")
    fechar_conexao(conexao)


def listar_leitores():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Leitores")
    leitores = cursor.fetchall()
    fechar_conexao(conexao)
    return leitores

