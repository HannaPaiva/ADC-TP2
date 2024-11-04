from Controller.Funcionarios import criar_tabela_funcionarios, listar_funcionarios, adicionar_funcionario, atualizar_funcionario, deletar_funcionario 


from menu_leitor import gerenciar_leitores
from Emprestimos import *
import sqlite3

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
            conexao()
        elif opcao == '2':
            gerenciar_leitores()  # Chama o menu de leitores
        elif opcao == '3':
            gerenciar_funcionarios()
        elif opcao == '4':
            gerenciar_emprestimos()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def gerenciar_livros():
    print("\nGerenciar Livros")
    # Adicione funções para CRUD de livros aqui

def gerenciar_funcionarios():
    criar_tabela_funcionarios()  # Certifique-se de que a tabela existe
    while True:
        print("\nGerenciar Funcionários")
        print("1. Listar Funcionários")
        print("2. Adicionar Funcionário")
        print("3. Atualizar Funcionário")
        print("4. Deletar Funcionário")
        print("5. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            funcionarios = listar_funcionarios()
            for func in funcionarios:
                print(f"ID: {func[0]}, Nome: {func[1]}, Cargo: {func[2]}")
        elif opcao == '2':
            nome = input("Digite o nome do funcionário: ")
            cargo = input("Digite o cargo do funcionário: ")
            adicionar_funcionario(nome, cargo)
            print("Funcionário adicionado com sucesso!")
        elif opcao == '3':
            id = int(input("Digite o ID do funcionário que deseja atualizar: "))
            nome = input("Digite o novo nome do funcionário: ")
            cargo = input("Digite o novo cargo do funcionário: ")
            atualizar_funcionario(id, nome, cargo)
            print("Funcionário atualizado com sucesso!")
        elif opcao == '4':
            id = int(input("Digite o ID do funcionário que deseja deletar: "))
            deletar_funcionario(id)
            print("Funcionário deletado com sucesso!")
        elif opcao == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")

def gerenciar_emprestimos():
    print("\nGerenciar Empréstimos")

   

# Inicia o menu
menu()
