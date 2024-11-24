from Controller.Funcionarios import adicionar_funcionario, listar_funcionarios, atualizar_funcionario, deletar_funcionario, filtrar_funcionarios

def gerenciar_funcionarios():
    while True:
        print("\nGerenciar Funcionários")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Atualizar Funcionário")
        print("4. Deletar Funcionário")
        print("5. Filtrar Funcionários")  # Nova opção
        print("6. Voltar ao Menu Principal")

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
            funcionarios = listar_funcionarios()
            print("\nLista de Funcionários:")
            for funcionario in funcionarios:
                print(f"ID: {funcionario[0]}, Nome: {funcionario[1]}, Morada: {funcionario[2]}, Telefone: {funcionario[3]}, NIF: {funcionario[4]}, Email: {funcionario[5]}")

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
