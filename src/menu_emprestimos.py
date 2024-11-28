from Controller.emprestimos import adicionar_emprestimo, listar_emprestimos, atualizar_emprestimo, deletar_emprestimo
from FilterData.filterInput import *
from FilterData.filterOutput import *

def gerenciar_emprestimos():
    while True:
        print("\n+------------------------------+")
        print("|    GERENCIAR EMPRÉSTIMOS    |")
        print("+------------------------------+")
        print("| 1. Adicionar Empréstimo     |")
        print("| 2. Listar Empréstimos       |")
        print("| 3. Atualizar Empréstimo     |")
        print("| 4. Deletar Empréstimo       |")
        print("| 5. Voltar ao Menu Principal |")
        print("+------------------------------+")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            livro_isbn = inputString("ISBN do livro: ")
            numero_leitor = inputInt("Número do leitor: ")
            id_funcionario = inputInt("ID do funcionário: ")
            data_emprestimo = inputDate("Data do empréstimo (DD-MM-YYYY): ")
            data_devolucao = inputDate("Data da devolução esperada (DD-MM-YYYY): ")
            adicionar_emprestimo(livro_isbn, numero_leitor, id_funcionario, data_emprestimo, data_devolucao or None)

        elif opcao == '2':
            spaces()
            emprestimos = listar_emprestimos()
           
    #atualizar
        elif opcao == '3':
            id_emprestimo = inputInt("ID do empréstimo a atualizar: ")
            print("Deixe o campo em branco para não atualizar o valor.")
            livro_isbn = input("Novo ISBN do livro: ")
            numero_leitor = input("Novo número do leitor: ")
            id_funcionario = input("Novo ID do funcionário: ")
            data_emprestimo = input("Nova data do empréstimo (YYYY-MM-DD): ")
            data_devolucao = input("Nova data de devolução (YYYY-MM-DD): ")

            atualizar_emprestimo(
                id_emprestimo,
                livro_isbn or None,
                numero_leitor or None,
                id_funcionario or None,
                data_emprestimo or None,
                data_devolucao or None
            )

        elif opcao == '4':
            id_emprestimo = int(input("ID do empréstimo a deletar: "))
            deletar_emprestimo(id_emprestimo)

        elif opcao == '5':
            break

        else:
            print("Opção inválida! Tente novamente.")
