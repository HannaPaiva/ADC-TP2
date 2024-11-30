from Model.emprestimos import *
from FilterData.filterInput import *
from FilterData.filterOutput import *

def gerenciar_emprestimos():
    """
        Gerencia as operações relacionadas com empréstimos na biblioteca.

        Este menu permite adicionar, listar, atualizar e eliminar empréstimos,
        além de possibilitar o regresso ao menu principal. Utiliza funcionalidades
        de validação de entrada e saída para garantir a integridade dos dados.
        
    """
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
            # Verificar se as tabelas têm registros
            achou_vazia, tabela_vazia = verificarTabelasVazias()
            if achou_vazia:
                print(f"A tabela '{tabela_vazia}' está vazia. Adicione registros antes de continuar.")
                continue

            livro_isbn = inputString("ISBN do livro: ")
            if not verificarLivroExiste(livro_isbn):
                print(f"O livro com ISBN {livro_isbn} não existe. verifique os dados e tente novamente mais tarde.")
                continue

            numero_leitor = inputInt("Número do leitor: ")
            if not verificarLeitorExiste(numero_leitor):
                print(f"O leitor com número {numero_leitor} não existe. verifique os dados e tente novamente mais tarde.")
                continue

            id_funcionario = inputInt("ID do funcionário: ")
            if not verificarFuncionarioExiste(id_funcionario):
                print(f"O funcionário com ID {id_funcionario} não existe. verifique os dados e tente novamente mais tarde.")
                continue
            
            data_emprestimo = inputDate("Data do empréstimo (DD-MM-YYYY): ")
            data_devolucao = inputDate("Data da devolução esperada (DD-MM-YYYY): ")

            adicionar_emprestimo(livro_isbn, numero_leitor, id_funcionario, data_emprestimo, data_devolucao or None)

        elif opcao == '2':
    
            listar_emprestimos()
           
        #atualizar
        elif opcao == '3':
            id_emprestimo = inputInt("ID do empréstimo a atualizar: ")
            print("Deixe o campo em branco para não atualizar o valor.")
            livro_isbn = input("Novo ISBN do livro: ")
            numero_leitor = input("Novo número do leitor: ")
            id_funcionario = input("Novo ID do funcionário: ")
            data_emprestimo = None
            data_devolucao = input("Nova data de devolução (YYYY-MM-DD): ")

            # Verificar se os valores fornecidos são válidos
            if livro_isbn and not verificarLivroExiste(livro_isbn):
                print(f"O livro com ISBN {livro_isbn} não existe. Atualização cancelada.")
                continue
            if numero_leitor and not verificarLeitorExiste(numero_leitor):
                print(f"O leitor com número {numero_leitor} não existe. Atualização cancelada.")
                continue
            if id_funcionario and not verificarFuncionarioExiste(id_funcionario):
                print(f"O funcionário com ID {id_funcionario} não existe. Atualização cancelada.")
                continue

            atualizar_emprestimo(
                id_emprestimo,
                livro_isbn or None,
                numero_leitor or None,
                id_funcionario or None,
                data_emprestimo or None,
                data_devolucao or None
            )

        elif opcao == '4':
            id_emprestimo = inputInt("ID do empréstimo a deletar: ")

            conexao = criar_conexao()
            cursor = conexao.cursor()
            cursor.execute("SELECT 1 FROM Emprestimos WHERE id_emprestimo = ?", (id_emprestimo,))
            emprestimo_existe = cursor.fetchone()
            fechar_conexao(conexao)

            if not emprestimo_existe:
                print(f"O empréstimo com ID {id_emprestimo} não existe. Operação cancelada.")
                continue

            # Deletar empréstimo
            deletar_emprestimo(id_emprestimo)

        elif opcao == '5':
            break

        else:
            print("Opção inválida! Tente novamente.")
