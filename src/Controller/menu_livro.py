from Model.livros import *

def gerenciar_livros():
    while True:

        print("\n+------------------------------+")
        print("|      GERENCIAR LIVROS       |")
        print("+------------------------------+")
        print("| 1. Adicionar Livro          |")
        print("| 2. Listar Livro             |")
        print("| 3. Atualizar Livro          |")
        print("| 4. Deletar Livro            |")
        print("| 5. Voltar ao Menu Principal |")
        print("+------------------------------+")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            isbn = input("ISBN: ")
            titulo = input("Titulo do Livro: ")
            autor = input("Autor do Livro: ")
            categoria = input("Categoria do Livro: ")
            ano_publicacao = input("Ano de Publicação do Livro: ")
            adicionar_livro(isbn, titulo, autor, categoria, ano_publicacao)

        elif opcao == '2':
            livros = listar_livro()
            print("\nLista de Livros:")
            for livro in livros:
                print(livros)

        elif opcao == '3':
            isbn = int(input("ISBN do livro a atualizar: "))
            print("Deixe o campo em branco para não atualizar o valor.")
            titulo = input("Novo titulo do livro: ")
            autor = input("Novo autor do livro: ")
            categoria = input("Nova categoria do livro: ")
            ano_publicacao = input("Novo ano de pulicação do livro: ")
            atualizar_livro(isbn, titulo or None, autor or None, categoria or None, ano_publicacao or None)

        elif opcao == '4':
            isbn = int(input("ISBN do livro a deletar: "))
            deletar_livro(isbn)

        elif opcao == '5':
            break

        else:
            print("Opção inválida! Tente novamente.")
