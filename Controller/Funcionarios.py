import sqlite3
from bd_connector import criar_conexao, fechar_conexao


# Função para listar todos os funcionários
def listar_funcionarios():
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM funcionarios')
    funcionarios = cursor.fetchall()
    fechar_conexao(conn)
    return funcionarios

# Função para adicionar um novo funcionário
def adicionar_funcionario(nome, morada, telefone, nif, email):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO funcionarios (nome, morada, telefone, nif, email)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, morada, telefone, nif, email))
    conn.commit()
    fechar_conexao(conn)

# Função para atualizar um funcionário
def atualizar_funcionario(id_funcionario, nome=None, morada=None, telefone=None, nif=None, email=None):
    conn = criar_conexao()
    cursor = conn.cursor()
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
        valores.append(id_funcionario)
        sql = f"UPDATE funcionarios SET {', '.join(campos)} WHERE id_funcionario = ?"
        cursor.execute(sql, valores)
        conn.commit()
    else:
        print("Nenhum campo para atualizar.")
    
    fechar_conexao(conn)

# Função para deletar um funcionário
def deletar_funcionario(id_funcionario):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM funcionarios WHERE id_funcionario = ?', (id_funcionario,))
    conn.commit()
    fechar_conexao(conn)

# Função para filtrar funcionários
def filtrar_funcionarios(nome=None, morada=None, telefone=None, nif=None, email=None):
    conn = criar_conexao()
    cursor = conn.cursor()
    filtros = []
    valores = []

    if nome:
        filtros.append("nome LIKE ?")
        valores.append(f"%{nome}%")
    if morada:
        filtros.append("morada LIKE ?")
        valores.append(f"%{morada}%")
    if telefone:
        filtros.append("telefone LIKE ?")
        valores.append(f"%{telefone}%")
    if nif:
        filtros.append("nif LIKE ?")
        valores.append(f"%{nif}%")
    if email:
        filtros.append("email LIKE ?")
        valores.append(f"%{email}%")

    sql = "SELECT * FROM funcionarios"
    if filtros:
        sql += " WHERE " + " AND ".join(filtros)

    cursor.execute(sql, valores)
    funcionarios = cursor.fetchall()
    fechar_conexao(conn)
    return funcionarios
