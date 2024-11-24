from Controller.Funcionarios import listar_funcionarios, adicionar_funcionario, atualizar_funcionario, deletar_funcionario 

from menu_livro import gerenciar_livros
from menu_leitor import gerenciar_leitores
from menu_emprestimos import gerenciar_emprestimos
from menu_funcionarios import gerenciar_funcionarios
from menu_funcionarios import gerenciar_funcionarios


def menu():
    while True:
        print("\n   Menu da Biblioteca  ")
        print("1. Gerir Livros")
        print("2. Gerir Leitores")
        print("3. Gerir Funcionários")
        print("4. Gerir Empréstimos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            gerenciar_livros()
        elif opcao == '2':
            gerenciar_leitores()
        elif opcao == '3':
            gerenciar_funcionarios()
        elif opcao == '4':
            gerenciar_emprestimos()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Inicia o menu
menu()
