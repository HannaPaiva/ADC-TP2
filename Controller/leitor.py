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


def atualizar_leitor(numero_leitor, nome=None, morada=None, telefone=None, nif=None, email=None):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    campos = []
    valores = []

    if nome:
        campos.append("nome = ?")
        valores.append(nome)
    if morada:
        campos.append("morada = ?")
        valores.append(morada)
    if telefone:
        campos.append("telefone = ?")
        valores.append(telefone)
    if nif:
        campos.append("nif = ?")
        valores.append(nif)
    if email:
        campos.append("email = ?")
        valores.append(email)

    if campos:
        valores.append(numero_leitor)
        sql = f"UPDATE Leitores SET {', '.join(campos)} WHERE numero_leitor = ?"
        try:
            cursor.execute(sql, valores)
            conexao.commit()
            print("Leitor atualizado com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao atualizar leitor: {e}")
    else:
        print("Nenhum campo para atualizar.")
    
    fechar_conexao(conexao)

