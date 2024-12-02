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

    Esta função consulta todos os registros na tabela `funcionarios` e exibe os resultados
    formatados em uma tabela.

    :raises sqlite3.Error: Se ocorrer um erro durante a consulta ao banco de dados.

    :return: None
    """
    conexao = criar_conexao()
    query = "SELECT * FROM funcionarios"  
    dados, headers = executar_query(conexao, query)  # Captura os dados e os headers
    return exibir_tabela(dados, headers)  # Exibe uma tabela com funcionários

def adicionar_funcionario(nome, morada, telefone, nif, email):
    """
    Adiciona um novo funcionário à base de dados.

    Esta função insere um novo registro na tabela `funcionarios` do banco de dados
    com as informações fornecidas pelos parâmetros.

    :param nome: Nome completo do funcionário.
    :type nome: str
    :param morada: Endereço de residência do funcionário.
    :type morada: str
    :param telefone: Número de telefone do funcionário.
    :type telefone: str
    :param nif: Número de identificação fiscal (NIF) do funcionário.
    :type nif: str
    :param email: Endereço de e-mail do funcionário.
    :type email: str

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da inserção no banco de dados.

    :return: None
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
    Atualiza as informações de um funcionário existente no banco de dados.

    Esta função atualiza os dados de um funcionário específico identificado pelo
    `id_funcionario`. Os parâmetros opcionais permitem a atualização de
    nome, morada, telefone, nif e email do funcionário.

    :param id_funcionario: ID do funcionário a ser atualizado.
    :type id_funcionario: int
    :param nome: Novo nome do funcionário (opcional).
    :type nome: str, optional
    :param morada: Novo endereço do funcionário (opcional).
    :type morada: str, optional
    :param telefone: Novo número de telefone do funcionário (opcional).
    :type telefone: str, optional
    :param nif: Novo número de identificação fiscal do funcionário (opcional).
    :type nif: str, optional
    :param email: Novo endereço de e-mail do funcionário (opcional).
    :type email: str, optional

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da atualização no banco de dados.

    :return: None
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

    Esta função exclui o registro de um funcionário específico identificado pelo
    `id_funcionario`.

    :param id_funcionario: ID do funcionário a ser removido.
    :type id_funcionario: int

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da exclusão no banco de dados.

    :return: None
    """
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM funcionarios WHERE id_funcionario = ?', (id_funcionario,))
    conn.commit()
    fechar_conexao(conn)

def filtrar_funcionarios(nome=None, morada=None, telefone=None, nif=None, email=None):
    """
    Filtra os funcionários com base em critérios fornecidos.

    Esta função busca registros na tabela `funcionarios` que atendam aos critérios especificados.
    Campos que não forem fornecidos serão ignorados no filtro.

    :param nome: Nome a ser filtrado (opcional).
    :type nome: str, optional
    :param morada: Endereço a ser filtrado (opcional).
    :type morada: str, optional
    :param telefone: Telefone a ser filtrado (opcional).
    :type telefone: str, optional
    :param nif: NIF a ser filtrado (opcional).
    :type nif: str, optional
    :param email: E-mail a ser filtrado (opcional).
    :type email: str, optional

    :raises sqlite3.Error: Se ocorrer um erro durante a consulta ao banco de dados.

    :return: Lista de tuplas com os funcionários filtrados.
    :rtype: list of tuple
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
