from bd_connector import criar_conexao, fechar_conexao
import sqlite3

def adicionar_leitor(nome, morada, telefone, nif, email):
    """
    Adiciona um novo leitor ao banco de dados.

    Esta função insere um novo registro na tabela `Leitores` do banco de dados
    com as informações fornecidas pelos parâmetros.

    :param nome: Nome completo do leitor.
    :type nome: str
    :param morada: Endereço de residência do leitor.
    :type morada: str
    :param telefone: Número de telefone do leitor.
    :type telefone: str
    :param nif: Número de identificação fiscal (NIF) do leitor.
    :type nif: str
    :param email: Endereço de e-mail do leitor.
    :type email: str

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da inserção no banco de dados.

    :return: None
    """
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
    """
    Retorna uma lista de todos os leitores no banco de dados.

    Esta função consulta todos os registros na tabela `Leitores` e retorna
    uma lista com as informações dos leitores.

    :raises sqlite3.Error: Se ocorrer um erro durante a consulta ao banco de dados.

    :return: Lista de tuplas, onde cada tupla representa um leitor.
    :rtype: list of tuple
    """
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Leitores")
    leitores = cursor.fetchall()
    fechar_conexao(conexao)
    return leitores


def atualizar_leitor(numero_leitor, nome=None, morada=None, telefone=None, nif=None, email=None):
    """
    Atualiza as informações de um leitor existente no banco de dados.

    Esta função atualiza os dados de um leitor específico identificado pelo
    `numero_leitor`. Os parâmetros opcionais permitem a atualização de
    nome, morada, telefone, nif e email do leitor.

    :param numero_leitor: Número de identificação do leitor a ser atualizado.
    :type numero_leitor: int
    :param nome: Novo nome do leitor (opcional).
    :type nome: str, optional
    :param morada: Novo endereço do leitor (opcional).
    :type morada: str, optional
    :param telefone: Novo número de telefone do leitor (opcional).
    :type telefone: str, optional
    :param nif: Novo número de identificação fiscal do leitor (opcional).
    :type nif: str, optional
    :param email: Novo endereço de e-mail do leitor (opcional).
    :type email: str, optional

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da atualização no banco de dados.

    :return: None
    """
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
    
def deletar_leitor(numero_leitor):
    """
    Deleta um leitor do banco de dados.

    Esta função remove o registro do leitor identificado pelo `numero_leitor`
    da tabela `Leitores`.

    :param numero_leitor: Número de identificação do leitor a ser deletado.
    :type numero_leitor: int

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da exclusão no banco de dados.

    :return: None
    """
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM Leitores WHERE numero_leitor = ?", (numero_leitor,))
        conexao.commit()
        print("Leitor deletado com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao deletar leitor: {e}")
    fechar_conexao(conexao)
