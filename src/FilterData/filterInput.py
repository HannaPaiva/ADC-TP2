from datetime import datetime

def inputString(texto):
    """
    Solicita uma string ao usuário, garantindo que a entrada não seja vazia.

    Esta função solicita ao usuário que insira um texto e só aceita uma entrada
    válida, ou seja, que não seja uma string vazia ou composta apenas por espaços.

    :param texto: Mensagem de prompt exibida ao usuário.
    :type texto: str
    :return: String inserida pelo usuário.
    :rtype: str
    """
    while True:
        user_input = input(texto)
        if user_input.strip():  # Verifica se a string não está vazia ou só com espaços
            return user_input
        print("Entrada inválida! O valor não pode ser vazio.")


def inputInt(texto):
    """
    Solicita um número inteiro ao usuário, garantindo que a entrada seja válida.

    Esta função solicita ao usuário que insira um número inteiro. Se a entrada não
    for um número válido, o usuário será solicitado a tentar novamente.

    :param texto: Mensagem de prompt exibida ao usuário.
    :type texto: str
    :return: Número inteiro inserido pelo usuário.
    :rtype: int
    :raises ValueError: Se a entrada não puder ser convertida para um número inteiro.
    """
    while True:
        try:
            user_input = input(texto)
            parsed_int = int(user_input)  # Tenta converter para inteiro
            return parsed_int
        except ValueError:
            print("Formato inválido! Por favor, insira um número inteiro válido.")


def inputDate(texto):
    """
    Solicita uma data ao usuário no formato DD-MM-YYYY, garantindo que a entrada seja válida.

    Esta função solicita ao usuário que insira uma data no formato DD-MM-YYYY.
    Se a entrada não for válida, o usuário será solicitado a tentar novamente.
    A data é retornada como um objeto `datetime`.

    :param texto: Mensagem de prompt exibida ao usuário.
    :type texto: str
    :return: Data inserida pelo usuário como objeto `datetime`.
    :rtype: datetime
    :raises ValueError: Se a entrada não estiver no formato DD-MM-YYYY.
    """
    while True:
        try:
            user_input = input(texto)
            parsed_date = datetime.strptime(user_input, "%d-%m-%Y")
            return parsed_date  # Retorna a data como objeto datetime
        except ValueError:
            print("Formato inválido! Por favor, insira a data no formato DD-MM-YYYY.")


# Exemplo de uso
if __name__ == "__main__":
    """
    Exemplo de uso das funções inputString, inputInt e inputDate.

    Solicita ao usuário uma string, um número inteiro e uma data no formato DD-MM-YYYY.
    Exibe os valores válidos inseridos pelo usuário.
    """
    # Entrada de string
    texto = inputString("Digite uma string: ")
    print(f"String válida: {texto}")

    # Entrada de número inteiro
    numero = inputInt("Digite um número inteiro: ")
    print(f"Número inteiro válido: {numero}")

    # Entrada de data
    data = inputDate("Digite uma data no formato DD-MM-YYYY: ")
    print(f"Data válida: {data.strftime('%d-%m-%Y')}")
