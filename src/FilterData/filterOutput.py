"""
Módulo de Gerenciamento de outputs
=============================================
Autor: [Hanna Paiva]
Data: [01/12/2024]
"""
from datetime import datetime
from tabulate import tabulate

def filterDateOutput(date):
    """
    Converte uma data para o formato DD-MM-YYYY.

    Esta função recebe uma data no formato de string (YYYY-MM-DD) ou como objeto `datetime`
    e a converte para o formato DD-MM-YYYY. Caso a entrada seja inválida, uma exceção é levantada.

    :param date: Data no formato de string (YYYY-MM-DD) ou objeto `datetime`.
    :type date: str ou datetime
    :raises ValueError: Caso a entrada não seja uma string válida no formato YYYY-MM-DD ou um objeto `datetime`.
    :return: Data formatada no formato DD-MM-YYYY.
    :rtype: str
    """
    try:
        # Se for string no formato YYYY-MM-DD, tenta converter para datetime
        if isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d")
        elif not isinstance(date, datetime):
            raise ValueError("A entrada deve ser uma string no formato YYYY-MM-DD ou um objeto datetime.")
        
        # Retorna a data no formato DD-MM-YYYY
        return date.strftime("%d-%m-%Y")
    except ValueError as e:
        raise ValueError(f"Erro ao processar a data: {e}")


def executar_query(conexao, query):
    """
    Executa uma consulta SQL no banco de dados e retorna os resultados e os nomes das colunas.

    Esta função executa a query fornecida no banco de dados conectado via o objeto de conexão,
    e retorna os dados da consulta e os headers das colunas.

    :param conexao: Objeto de conexão ao banco de dados.
    :type conexao: sqlite3.Connection
    :param query: Consulta SQL a ser executada.
    :type query: str
    :return: Uma tupla contendo:
             - dados: Lista de tuplas com os resultados da consulta.
             - headers: Lista com os nomes das colunas do resultado.
    :rtype: tuple (list of tuple, list of str)
    """
    cursor = conexao.cursor()
    cursor.execute(query)
    dados = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]  # Captura os nomes das colunas
    cursor.close()
    return dados, headers


def exibir_tabela(dados, colunas):
    """
    Exibe dados formatados em uma tabela com cabeçalhos.

    Esta função recebe dados em formato de lista de tuplas e os nomes das colunas.
    As datas no formato YYYY-MM-DD são automaticamente convertidas para o formato DD-MM-YYYY.
    A tabela é exibida no terminal no formato de grade.

    :param dados: Lista de tuplas contendo os resultados da consulta ao banco de dados.
    :type dados: list of tuple
    :param colunas: Lista com os nomes das colunas do resultado.
    :type colunas: list of str
    :return: Nenhum valor é retornado. A tabela é exibida no terminal.
    :rtype: None
    """
    if not dados:
        print("Nenhum dado encontrado.")
        return

    # Converte datas no formato YYYY-MM-DD para DD-MM-YYYY
    dados_formatados = []
    for linha in dados:
        nova_linha = [
            filterDateOutput(item) if isinstance(item, str) and "-" in item and len(item) == 10 else item
            for item in linha
        ]
        dados_formatados.append(nova_linha)

    # Exibe a tabela formatada
    tabela = tabulate(dados_formatados, headers=colunas, tablefmt="grid")
    print(tabela)
