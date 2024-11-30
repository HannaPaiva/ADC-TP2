from Model.Funcionarios import adicionar_funcionario, listar_funcionarios, atualizar_funcionario, deletar_funcionario, filtrar_funcionarios

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
            nome = input("Nome do funcionário: ")
            morada = input("Morada do funcionário: ")
            telefone = input("Telefone do funcionário: ")
            nif = input("NIF do funcionário: ")
            email = input("Email do funcionário: ")
            adicionar_funcionario(nome, morada, telefone, nif, email)
            print("Funcionário adicionado com sucesso!")

        elif opcao == '2':
           listar_funcionarios()

        elif opcao == '3':
            id_funcionario = int(input("ID do funcionário a atualizar: "))
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
            deletar_funcionario(id_funcionario)
            print("Funcionário deletado com sucesso!")

        elif opcao == '5':  # Nova opção para filtrar
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

            print("\nFuncionários Filtrados:")
            if funcionarios:
                for funcionario in funcionarios:
                    print(f"ID: {funcionario[0]}, Nome: {funcionario[1]}, Morada: {funcionario[2]}, Telefone: {funcionario[3]}, NIF: {funcionario[4]}, Email: {funcionario[5]}")
            else:
                print("Nenhum funcionário encontrado com os critérios fornecidos.")

        elif opcao == '6':
            break

        else:
            print("Opção inválida! Tente novamente.")