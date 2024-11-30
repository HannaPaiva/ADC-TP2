# menu_leitores.py

from Model.leitor import adicionar_leitor, listar_leitores, atualizar_leitor, deletar_leitor

def gerenciar_leitores():
    while True:
        print("\n+------------------------------+")
        print("|      GERENCIAR LEITORES      |")
        print("+------------------------------+")
        print("| 1. Adicionar Leitor          |")
        print("| 2. Listar Leitores           |")
        print("| 3. Atualizar Leitor          |")
        print("| 4. Deletar Leitor            |")
        print("| 5. Voltar ao Menu Principal  |")
        print("+------------------------------+")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do leitor: ")
            morada = input("Morada do leitor: ")
            telefone = input("Telefone do leitor: ")
            nif = input("NIF do leitor: ")
            email = input("Email do leitor: ")
            adicionar_leitor(nome, morada, telefone, nif, email)

        elif opcao == '2':
            leitores = listar_leitores()
            print("\nLista de Leitores:")
            for leitor in leitores:
                print(leitor)

        elif opcao == '3':
            numero_leitor = int(input("Número do leitor a atualizar: "))
            print("Deixe o campo em branco para não atualizar o valor.")
            nome = input("Novo nome do leitor: ")
            morada = input("Nova morada do leitor: ")
            telefone = input("Novo telefone do leitor: ")
            nif = input("Novo NIF do leitor: ")
            email = input("Novo email do leitor: ")
            atualizar_leitor(numero_leitor, nome or None, morada or None, telefone or None, nif or None, email or None)

        elif opcao == '4':
            numero_leitor = int(input("Número do leitor a deletar: "))
            deletar_leitor(numero_leitor)

        elif opcao == '5':
            break

        else:
            print("Opção inválida! Tente novamente.")
