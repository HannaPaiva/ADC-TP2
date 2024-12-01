"""
Módulo de Gerenciamento de Funcionários (Menu)
==============================================

Este módulo fornece um menu interativo para gerenciar funcionários,
permitindo operações de CRUD (Criar, Ler, Atualizar, Deletar) e filtragem.

Funcionalidades principais:
---------------------------
1. Adicionar novo funcionário.
2. Listar todos os funcionários.
3. Atualizar informações de um funcionário existente.
4. Remover um funcionário.
5. Filtrar funcionários com base em critérios específicos.
6. Sair para o menu principal.

Dependências:
-------------
- Funções CRUD e de filtragem do módulo `Model.Funcionarios`.
- Entrada de dados validada pelo módulo `FilterData.filterInput`.
- Validação de funcionários do módulo `Model.emprestimos`.
- Formatação de saída com `FilterData.filterOutput`.

Autor: [Seu Nome]
Data: [Data]
"""

from Model.Funcionarios import adicionar_funcionario, listar_funcionarios, atualizar_funcionario, deletar_funcionario, filtrar_funcionarios
from FilterData.filterInput import inputString, inputInt
from Model.emprestimos import verificarFuncionarioExiste
from FilterData.filterOutput import exibir_tabela

def gerenciar_funcionarios():
    """
    Interface de gerenciamento de funcionários.

    Este método exibe um menu interativo para que o usuário realize operações sobre os dados de funcionários.
    As opções incluem adicionar, listar, atualizar, deletar e filtrar funcionários.

    O programa solicita entradas do usuário, valida as informações e utiliza funções de outros módulos para
    manipular os dados armazenados na base de dados.

    Fluxo de execução:
    ------------------
    1. O usuário escolhe uma opção do menu.
    2. O programa chama a função correspondente.
    3. O menu é exibido novamente até que o usuário escolha sair.

    Exceções tratadas:
    ------------------
    - Verificação de existência de funcionários para operações de atualização e deleção.
    - Campos deixados em branco são ignorados nas atualizações e filtragens.

    Retorno:
    --------
    Nenhum. O resultado das operações é exibido diretamente no terminal.
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
            # Adicionar novo funcionário
            nome = inputString("Nome do funcionário: ")
            morada = inputString("Morada do funcionário: ")
            telefone = inputInt("Telefone do funcionário: ")
            nif = inputInt("NIF do funcionário: ")
            email = inputString("Email do funcionário: ")
            adicionar_funcionario(nome, morada, telefone, nif, email)
            print("Funcionário adicionado com sucesso!")

        elif opcao == '2':
            # Listar todos os funcionários
            listar_funcionarios()

        elif opcao == '3':
            # Atualizar informações de um funcionário
            id_funcionario = inputInt("ID do funcionário a atualizar: ")
            if not verificarFuncionarioExiste(id_funcionario):
                print(f"O funcionário com ID {id_funcionario} não existe. Verifique os dados e tente novamente.")
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
            # Deletar um funcionário
            id_funcionario = inputInt("ID do funcionário a deletar: ")
            if not verificarFuncionarioExiste(id_funcionario):
                print(f"O funcionário com ID {id_funcionario} não existe. Verifique os dados e tente novamente.")
                continue
            deletar_funcionario(id_funcionario)
            print("Funcionário deletado com sucesso!")

        elif opcao == '5':
            # Filtrar funcionários por critérios
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
                exibir_tabela(funcionarios, headers)  # Formata a saída com cabeçalhos
            else:
                print("Nenhum funcionário encontrado com os critérios fornecidos.")

        elif opcao == '6':
            # Voltar ao menu principal
            break

        else:
            print("Opção inválida! Tente novamente.")
