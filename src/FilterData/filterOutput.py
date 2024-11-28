from datetime import datetime
from tabulate import tabulate

def filterDateOutput(date):
    """
    Recebe uma data como string (no formato YYYY-MM-DD) ou como objeto datetime.
    Retorna a data formatada no padrão DD-MM-YYYY.
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
    Executa uma query e retorna os resultados e os headers das colunas.
    
    Parâmetros:
    - conexao: Objeto de conexão ao banco de dados.
    - query: String contendo a query SQL.
    
    Retorna:
    - Tuple (dados, headers): 
        - dados: Resultado da query (lista de tuplas).
        - headers: Lista de nomes das colunas.
    """
    cursor = conexao.cursor()
    cursor.execute(query)
    dados = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]  # Captura os nomes das colunas
    cursor.close()
    return dados, headers

def exibir_tabela(dados, colunas):
    """
    Exibe dados em formato de tabela, com conversão automática de datas.

    Parâmetros:
    - dados: Lista de tuplas (resultado da consulta ao banco de dados).
    - colunas: Lista de nomes das colunas.

    Retorna:
    - None: Apenas exibe a tabela no terminal.
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

def spaces():
    print()
    print()
    print()
    print()
    print()