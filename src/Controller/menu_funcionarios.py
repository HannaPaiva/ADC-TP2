from Model.Funcionarios import adicionar_funcionario, listar_funcionarios, atualizar_funcionario, deletar_funcionario, filtrar_funcionarios
from FilterData.filterInput import *
from Model.emprestimos import verificarFuncionarioExiste
from tabulate import tabulate


def gerenciar_funcionarios():
    """
    Interface de gerenciamento de funcionários

    Este método fornece um menu interativo para executar operações de CRUD (Criar, Ler, Atualizar, Deletar)
    e filtrar funcionários, utilizando funções de um módulo controlador.

    Funcionalidades disponíveis:
        1. Adicionar funcionário
        2. Listar funcionários
        3. Atualizar informações de um funcionário
        4. Deletar um funcionário
        5. Filtrar funcionários por critérios
        6. Voltar ao menu principal

    O programa solicita entradas do usuário e chama funções adequadas para manipular os dados.

    """
    while True:
        print("\n+------------------------------+")
        print("|      GERENCIAR FUNCIONARIOS     |")
        print("+------------------------------+")
        print("| 1. Adicionar funcionário        |")
        print("| 2. Listar funcionários          |")
        print("| 3. Atualizar funcionário        |")
        print("| 4. Deletar funcionário          |")
        print("| 5. Filtrar Funcionários         |")
        print("| 6. Voltar ao Menu Principal     |")
        print("+------------------------------+")
        

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = inputString("Nome do funcionário: ")
            morada = inputString("Morada do funcionário: ")
            telefone = inputInt("Telefone do funcionário: ")
            nif = inputInt("NIF do funcionário: ")
            email = inputString("Email do funcionário: ")
            adicionar_funcionario(nome, morada, telefone, nif, email)
            print("Funcionário adicionado com sucesso!")

        elif opcao == '2':
           listar_funcionarios()

        elif opcao == '3':
            id_funcionario = int(inputInt("ID do funcionário a atualizar: "))
            if not verificarFuncionarioExiste(id_funcionario):
                print(f"O funcionário com ID {id_funcionario} não existe. verifique os dados e tente novamente mais tarde.")
                continue
            print("Deixe o campo em branco para não atualizar o valor.")
            nome = input("Novo nome do funcionário: ")
            morada = input("Nova morada do funcionário: ")
            telefone = input("Novo telefone do funcionário: ")
            nif = input("Novo NIF do funcionário: ")
            email = input("Novo email do funcionário: ")
            atualizar_funcionario(id_funcionario, nome or None, morada or None, telefone or None, nif or None, email or None)
            print("Funcionário atualizado com sucesso!")

        elif opcao == '4':
            id_funcionario = int(input("ID do funcionário a deletar: "))
            if not verificarFuncionarioExiste(id_funcionario):
                print(f"O funcionário com ID {id_funcionario} não existe. verifique os dados e tente novamente mais tarde.")
                continue
            deletar_funcionario(id_funcionario)
            print("Funcionário deletado com sucesso!")

        elif opcao == '5':  
            print("\nFiltrar Funcionários")
            print("Deixe o campo em branco para ignorar o critério.")
            nome = input("Filtrar por Nome: ")
            morada = input("Filtrar por Morada: ")
            telefone = input("Filtrar por Telefone: ")
            nif = input("Filtrar por NIF: ")
            email = input("Filtrar por Email: ")

            funcionarios = filtrar_funcionarios(
                nome=nome or None,
                morada=morada or None,
                telefone=telefone or None,
                nif=nif or None,
                email=email or None
            )

            if funcionarios:
                headers = ["ID", "Nome", "Morada", "Telefone", "NIF", "Email"]
                print("\nFuncionários Filtrados:")
                print(tabulate(funcionarios, headers=headers, tablefmt="grid"))  # Formata os dados com tabulate
            else:
                print("Nenhum funcionário encontrado com os critérios fornecidos.")

        elif opcao == '6':
            break

        else:
            print("Opção inválida! Tente novamente.")
