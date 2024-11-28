from Controller.livros import *

def gerenciar_livros():
    """
    Gere cada operação do tipo CRUD que age como uma interface de menu cliente-sistema.

    Esta função serve para gerir as operações das funções principais que são realizadas na base de dados.

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da inserção no banco de dados.

    :return: None
    """
    while True:
        print("\nGerenciar Livros")
        print("1. Adicionar Livro")
        print("2. Listar Livro")
        print("3. Listar Livro Por ISBN")
        print("4. Atualizar Livro")
        print("5. Deletar Livro")
        print("6. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        # Adicionar Livros
        if opcao == '1':
            try:
                while True:
                    isbn = input("ISBN: ")
                    if isbn.isdigit():
                        break
                    else:
                        print("ISBN deve ser um número, tente novamente.")

                titulo = input("Título do Livro: ")
                autor = input("Autor do Livro: ")
                categoria = input("Categoria do Livro: ")

                while True:
                    ano_publicacao = input("Ano de Publicação do Livro (ex: 2023): ")
                    if ano_publicacao.isdigit() and len(ano_publicacao) == 4:
                        break
                    else:
                        print("Ano de publicação deve conter apenas 4 dígitos numéricos. Tente novamente.")
            
            except sqlite3.Error as e:
                print(f"Erro ao adicionar livro: {e}")
            else:
                adicionar_livro(isbn, titulo, autor, categoria, ano_publicacao)

        # Listar Livros
        elif opcao == '2':
            try:
                livros = listar_livro()
                print("\nLista de Livros:")
                print(livros)
            except sqlite3.Error as e:
                print(f"Erro ao listar livros: {e}")

        # Listar Livro por ISBN
        elif opcao == '3':
            try:
                while True:
                    isbn = input("ISBN do livro a procurar: ")
                    if isbn.isdigit():
                        break
                    else:
                        print("ISBN inválido! O valor deve ser numérico. Tente novamente.")
                
                resultado = listar_livro_por_id(int(isbn))
                if resultado:
                    print(resultado)
                else:
                    print("Nenhum livro encontrado com o ISBN fornecido.")
            
            except sqlite3.Error as e:
                print(f"Erro ao listar o livro especificado: {e}")

        # Atualizar Livros
        elif opcao == '4':
            try:
                while True:
                    isbn = input("ISBN do livro a atualizar: ")
                    if isbn.isdigit() and isbn != None:
                        break
                    else:
                        print("ISBN inválido ou vazio, tente novamente, o valor deve ser numérico.")

                print("Deixe o campo em branco para não atualizar o valor.")
                titulo = input("Novo titulo do livro: ")
                autor = input("Novo autor do livro: ")
                categoria = input("Nova categoria do livro: ")
                while True:
                    ano_publicacao = input("Novo ano de pulicação do livro: ")
                    if isbn.isdigit() and isbn != None:
                        break
                    else:
                        print("ISBN inválido ou vazio, tente novamente, o valor deve ser numérico.")

            except sqlite3.Error as e:
                print(f"Erro ao atualizar livro: {e}")
            else:
                atualizar_livro(isbn, titulo or None, autor or None, categoria or None, ano_publicacao or None)
        
        # Apagar Livros
        elif opcao == '5':
            while True:
                isbn = input("ISBN do livro a deletar: ")
                if isbn.isdigit() and isbn != None:
                    break
                else:
                    print("ISBN inválido ou vazio, tente novamente, o valor deve ser numérico.")    
            deletar_livro(isbn)

        # Sair
        elif opcao == '6':
            break

        else:
            print("Opção inválida! Tente novamente.")
