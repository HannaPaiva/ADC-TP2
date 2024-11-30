from Controller.menu_livro import gerenciar_livros
from Controller.menu_leitor import gerenciar_leitores
from Controller.menu_emprestimos import gerenciar_emprestimos
from Controller.menu_funcionarios import gerenciar_funcionarios
from Controller.menu_funcionarios import gerenciar_funcionarios

# Define um diretório específico para o __pycache__ neste projeto

def menu():
    """
        Exibe o menu principal do sistema da biblioteca e gerencia a navegação entre
        diferentes funcionalidades, como a gestão de livros, leitores, funcionários e
        empréstimos.
        O menu apresenta uma interface interativa no terminal, permitindo ao utilizador
        selecionar diferentes opções para gerenciar os recursos da biblioteca. A função
        permanece em execução até que a opção de saída seja selecionada.
    """

    while True:
        print("\n+-------------------------+")
        print("|    MENU DA BIBLIOTECA  |")
        print("+-------------------------+")
        print("| 1. Gerir Livros        |")
        print("| 2. Gerir Leitores      |")
        print("| 3. Gerir Funcionários  |")
        print("| 4. Gerir Empréstimos   |")
        print("| 5. Sair                |")
        print("+-------------------------+")

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


#Se o local de execução é a partir do main
if __name__ == '__main__':
    menu()
