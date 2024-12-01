"""
Módulo de Gerenciamento de Funcionários
=======================================

Este módulo fornece funções para gerenciar registros de funcionários em uma base de dados SQLite.

Funções disponíveis:
--------------------
- listar_funcionarios(): Lista todos os funcionários.
- adicionar_funcionario(): Adiciona um novo funcionário à base de dados.
- atualizar_funcionario(): Atualiza os dados de um funcionário existente.
- deletar_funcionario(): Remove um funcionário da base de dados.
- filtrar_funcionarios(): Filtra funcionários com base em critérios fornecidos.

Dependências:
-------------
Este módulo depende das funções de conexão com o banco de dados, `criar_conexao` e `fechar_conexao`,
disponíveis no módulo `bd_connector`. Também utiliza a formatação de saída de dados do módulo `FilterData.filterOutput`.
"""

import sqlite3
from bd_connector import criar_conexao, fechar_conexao
from FilterData.filterOutput import *

def listar_funcionarios():
    """
    Lista todos os funcionários da base de dados.

    A função executa uma consulta SQL para obter todos os registros da tabela de funcionários
    e exibe os resultados formatados em uma tabela.

    Dependências:
        - `criar_conexao()`: Para estabelecer a conexão com a base de dados.
        - `executar_query()`: Para executar a consulta SQL.
        - `exibir_tabela()`: Para formatar e exibir os resultados.

    Retorna:
        None: Os dados são exibidos no terminal.
    """
    conexao = criar_conexao()
    query = "SELECT * FROM funcionarios"  
    dados, headers = executar_query(conexao, query)  # Captura os dados e os headers
    return exibir_tabela(dados, headers)  # Exibe uma tabela com funcionários

def adicionar_funcionario(nome, morada, telefone, nif, email):
    """
    Adiciona um novo funcionário à base de dados.

    Esta função insere um novo registro na tabela de funcionários com as informações fornecidas.

    Parâmetros:
        - nome (str): O nome do funcionário.
        - morada (str): A morada do funcionário.
        - telefone (str): O telefone do funcionário.
        - nif (str): O NIF do funcionário.
        - email (str): O email do funcionário.

    Dependências:
        - `criar_conexao()`: Para estabelecer a conexão com a base de dados.
        - `fechar_conexao()`: Para encerrar a conexão com a base de dados.
    """
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO funcionarios (nome, morada, telefone, nif, email)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, morada, telefone, nif, email))
    conn.commit()
    fechar_conexao(conn)

def atualizar_funcionario(id_funcionario, nome=None, morada=None, telefone=None, nif=None, email=None):
    """
    Atualiza as informações de um funcionário na base de dados.

    Permite atualizar qualquer um dos campos de um funcionário com base no ID fornecido.
    Se um campo não for fornecido, ele será ignorado na atualização.

    Parâmetros:
        - id_funcionario (int): O ID do funcionário a ser atualizado.
        - nome (str, opcional): O novo nome do funcionário. (pode ser `None` para não alterar)
        - morada (str, opcional): A nova morada do funcionário. (pode ser `None` para não alterar)
        - telefone (str, opcional): O novo telefone do funcionário. (pode ser `None` para não alterar)
        - nif (str, opcional): O novo NIF do funcionário. (pode ser `None` para não alterar)
        - email (str, opcional): O novo email do funcionário. (pode ser `None` para não alterar)

    Exceções:
        - Nenhuma. Caso não haja campos para atualizar, a função apenas imprime um aviso.

    Dependências:
        - `criar_conexao()`: Para estabelecer a conexão com a base de dados.
        - `fechar_conexao()`: Para encerrar a conexão com a base de dados.
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

def deletar_funcionario(id_funcionario):
    """
    Remove um funcionário da base de dados.

    Exclui um funcionário da tabela de funcionários com base no ID fornecido.

    Parâmetros:
        - id_funcionario (int): O ID do funcionário a ser removido.

    Dependências:
        - `criar_conexao()`: Para estabelecer a conexão com a base de dados.
        - `fechar_conexao()`: Para encerrar a conexão com a base de dados.
    """
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM funcionarios WHERE id_funcionario = ?', (id_funcionario,))
    conn.commit()
    fechar_conexao(conn)

def filtrar_funcionarios(nome=None, morada=None, telefone=None, nif=None, email=None):
    """
    Filtra os funcionários com base em critérios fornecidos.

    Busca registros na tabela de funcionários que atendam aos critérios especificados.
    Campos que não forem fornecidos serão ignorados no filtro.

    Parâmetros:
        - nome (str, opcional): Nome a ser filtrado. (pode ser `None` para não filtrar por nome)
        - morada (str, opcional): Morada a ser filtrada. (pode ser `None` para não filtrar por morada)
        - telefone (str, opcional): Telefone a ser filtrado. (pode ser `None` para não filtrar por telefone)
        - nif (str, opcional): NIF a ser filtrado. (pode ser `None` para não filtrar por nif)
        - email (str, opcional): Email a ser filtrado. (pode ser `None` para não filtrar por email)

    Retorna:
        list: Uma lista de tuplas com os funcionários filtrados. Cada tupla contém os campos
              (ID, nome, morada, telefone, nif, email).

    Dependências:
        - `criar_conexao()`: Para estabelecer a conexão com a base de dados.
        - `fechar_conexao()`: Para encerrar a conexão com a base de dados.
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
