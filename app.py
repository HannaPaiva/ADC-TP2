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
    print("1- Mostrar todos os Livros")
    print("2- Procurar Livro por ISBN")
    print("3- Inserir Livro")
    print("4- Atualizar Livro")
    print("5- Apagar Livro")
    opcao = input("Opção: ")
    if opcao == '1':
        listar_livros()
    elif opcao == '2':
        listar_livros_id()
    elif opcao == '3':
        adicionar_livros()
    elif opcao == '4':
        atualizar_livros()
    elif opcao == '5':
        apagar_livros()

def gerenciar_funcionarios():
    print("\nGerenciar Funcionários")
    # Adicione funções para CRUD de funcionários aqui

def gerenciar_emprestimos():
    print("\nGerenciar Empréstimos")

   

# Inicia o menu
menu()
