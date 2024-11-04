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
    print("\nGerenciar Funcionários")
    # Adicione funções para CRUD de funcionários aqui

def gerenciar_emprestimos():
    print("\nGerenciar Empréstimos")

   

# Inicia o menu
menu()
