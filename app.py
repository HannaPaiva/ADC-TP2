from Emprestimos import *

import sqlite3

def conexao():
    try:
        conexao = sqlite3.connect('base_de_dados')
        print("Conexão realizada com sucesso!")
        return conexao
    except sqlite3.Error as erro:
        print("Erro ao conectar ao banco de dados:", erro)
        return None


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

def gerenciar_livros():
    print("\nGerenciar Livros")
    # Adicione funções para CRUD de livros aqui
    # Exemplo:
    # criar_livro()
    # ler_livros()
    # atualizar_livro()
    # deletar_livro()

def gerenciar_leitores():
    print("\nGerenciar Leitores")
    # Adicione funções para CRUD de leitores aqui

def gerenciar_funcionarios():
    print("\nGerenciar Funcionários")
    # Adicione funções para CRUD de funcionários aqui

def gerenciar_emprestimos():
    print("\nGerenciar Empréstimos")

   

# Inicia o menu
menu()
