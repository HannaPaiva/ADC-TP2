from datetime import datetime

def inputString(texto):
    """
    Solicita uma string ao usuário. Não permite strings vazias.
    """
    while True:
        user_input = input(texto)
        if user_input.strip():  # Verifica se a string não está vazia ou só com espaços
            return user_input
        print("Entrada inválida! O valor não pode ser vazio.")

def inputInt(texto):
    """
    Solicita um número inteiro ao usuário. Verifica e só aceita entrada válida.
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
    Solicita uma data ao usuário no formato DD-MM-YYYY. 
    Verifica e só aceita a entrada correta.
    """
    while True:
        try:
            user_input = input(texto)
            parsed_date = datetime.strptime(user_input, "%d-%m-%Y")
            return parsed_date  # Retorna a data como objeto datetime
        except ValueError:
            print("Formato inválido! Por favor, insira a data no formato DD-MM-YYYY.")


if __name__ == "__main__":
    # Entrada de data
    data = inputDate("Digite uma data no formato DD-MM-YYYY: ")
    print(f"Data válida: {data.strftime('%d-%m-%Y')}")



def inputStringUpdate(texto):
    """
    Solicita uma string ao usuário. Não permite strings vazias.
    """
    while True:
        user_input = input(texto)
        if user_input.strip():  # Verifica se a string não está vazia ou só com espaços
            return user_input
        print("Entrada inválida! O valor não pode ser vazio.")

def inputIntUpdate(texto):
    """
    Solicita um número inteiro ao usuário. Verifica e só aceita entrada válida.
    """
    while True:
        try:
            user_input = input(texto)
            parsed_int = int(user_input)  # Tenta converter para inteiro
            return parsed_int
        except ValueError:
            print("Formato inválido! Por favor, insira um número inteiro válido.")

def inputDateUpdate(texto):
    """
    Solicita uma data ao usuário no formato DD-MM-YYYY. 
    Verifica e só aceita a entrada correta.
    """
    while True:
        try:
            user_input = input(texto)
            parsed_date = datetime.strptime(user_input, "%d-%m-%Y")
            return parsed_date  # Retorna a data como objeto datetime
        except ValueError:
            print("Formato inválido! Por favor, insira a data no formato DD-MM-YYYY.")


if __name__ == "__main__":
    # Entrada de data
    data = inputDate("Digite uma data no formato DD-MM-YYYY: ")
    print(f"Data válida: {data.strftime('%d-%m-%Y')}")


