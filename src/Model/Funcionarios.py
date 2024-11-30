import sqlite3
from bd_connector import criar_conexao, fechar_conexao
from FilterData.filterOutput import *


def listar_funcionarios():
    conexao = criar_conexao()
    query = "SELECT * FROM funcionarios"  
    dados, headers = executar_query(conexao, query)  # Captura os dados e os headers
    return exibir_tabela(dados, headers)  # Exibe a tabela formatada

# Função para adicionar um novo funcionário

def adicionar_funcionario(nome, morada, telefone, nif, email):
    """
    Adiciona um novo funcionário à base de dados.

    Esta função insere um novo registro na tabela de funcionários com as informações fornecidas.

    Parâmetros:
        nome (str): O nome do funcionário.
        morada (str): A morada do funcionário.
        telefone (str): O telefone do funcionário.
        nif (str): O NIF do funcionário.
        email (str): O email do funcionário.
    """
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
    """
    Atualiza as informações de um funcionário na base de dados.

    Esta função permite atualizar qualquer um dos campos de um funcionário, conforme especificado pelos parâmetros.
    Se um campo não for fornecido, ele será ignorado na atualização.

    Parâmetros:
        id_funcionario (int): O ID do funcionário a ser atualizado.
        nome (str, opcional): O novo nome do funcionário. (pode ser `None` para não alterar)
        morada (str, opcional): A nova morada do funcionário. (pode ser `None` para não alterar)
        telefone (str, opcional): O novo telefone do funcionário. (pode ser `None` para não alterar)
        nif (str, opcional): O novo NIF do funcionário. (pode ser `None` para não alterar)
        email (str, opcional): O novo email do funcionário. (pode ser `None` para não alterar)
    
    Exceções:
        Nenhuma. Se não houver campos para atualizar, a função apenas imprime uma mensagem de aviso.
    """
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
    """
    Deleta um funcionário da base de dados.

    Esta função remove um funcionário da tabela de funcionários com base no seu ID.

    Parâmetros:
        id_funcionario (int): O ID do funcionário a ser deletado.
    """
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM funcionarios WHERE id_funcionario = ?', (id_funcionario,))
    conn.commit()
    fechar_conexao(conn)

# Função para filtrar funcionários
def filtrar_funcionarios(nome=None, morada=None, telefone=None, nif=None, email=None):
    """
    Filtra os funcionários da base de dados com base em critérios fornecidos.

    A função permite buscar funcionários que atendem aos critérios especificados. Os campos que não forem fornecidos
    serão ignorados no filtro.

    Parâmetros:
        nome (str, opcional): Nome a ser filtrado. (pode ser `None` para não filtrar por nome)
        morada (str, opcional): Morada a ser filtrada. (pode ser `None` para não filtrar por morada)
        telefone (str, opcional): Telefone a ser filtrado. (pode ser `None` para não filtrar por telefone)
        nif (str, opcional): NIF a ser filtrado. (pode ser `None` para não filtrar por nif)
        email (str, opcional): Email a ser filtrado. (pode ser `None` para não filtrar por email)
    
    Retorna:
        list: Uma lista de tuplas com os funcionários filtrados. Cada tupla contém as informações de um funcionário (ID, nome, morada, telefone, nif, email).
    """
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
