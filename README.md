# ADC-TP2

**ADC-TP2** é um sistema para gestão de bibliotecas, desenvolvido como parte da disciplina de **Ambientes de Desenvolvimento Colaborativo**.  
O projeto permite gerenciar livros, leitores, funcionários e empréstimos de maneira eficiente e organizada, com uma interface de menu interativa para facilitar o uso.

---

## Estrutura do Projeto

A organização das pastas e ficheiros do projeto é a seguinte:

```plaintext
ADC-TP2/
├── _pycache_/         # Arquivos gerados automaticamente pelo Python
├── Controller/        # Contém os menus para gerir os diferentes módulos
│   ├── menu_emprestimos.py
│   ├── menu_funcionarios.py
│   ├── menu_leitor.py
│   └── menu_livro.py
├── docs/              # Documentação gerada usando o Sphinx
│   ├── conf.py
│   ├── Makefile
│   ├── make.bat
│   ├── *.rst
├── src/               # Código principal do projeto
│   ├── Controller/
│   ├── database/
│   │   ├── base_de_dados  # Pasta para armazenar a base de dados SQLite
│   │   └── base_de_dados.bd
│   ├── FilterData/
│   │   ├── filterInput.py
│   │   └── filterOutput.py
│   ├── Model/
│   │   ├── emprestimos.py
│   │   ├── Funcionarios.py
│   │   ├── leitor.py
│   │   └── livros.py
│   ├── app.py         # Ponto de entrada principal da aplicação
│   └── bd_connector.py # Gestão de conexão com a base de dados SQLite
├── requirements.txt   # Dependências do projeto
└── README.md          # Este ficheiro
```

## Instalação
### Clone o repositório:
```
git clone https://github.com/HannaPaiva/ADC-TP2.git
cd ADC-TP2
```
**Instale as dependências**: Certifique-se de ter o Python 3.8+ instalado. Depois, instale as dependências usando o pip:

```
pip install -r requirements.txt
```

Configuração da Base de Dados: O projeto utiliza um banco de dados SQLite armazenado no ficheiro base_de_dados.bd. Certifique-se de que o ficheiro está presente na pasta database.

## Utilização
Execute o ficheiro principal app.py:

```
python src/app.py
```

Navegue pelo menu interativo para gerir:

Livros

Leitores

Funcionários

Empréstimos


## Funcionalidades
- Gestão de Livros:
  - Adicionar, editar e remover livros
  - Pesquisar livros no catálogo
- Gestão de Leitores:
  - Cadastrar novos leitores
  - Atualizar informações de leitores
- Gestão de Funcionários:
  - Gerir informações de funcionários
- Gestão de Empréstimos:
  - Registar novos empréstimos
  - Controlar devoluções
 
# Autores

Desenvolvido por:
- **Hanna Paiva**
  - a85299@ualg.pt
- **Adriano Muncaciu**
  - a83998@ualg.pt
- **João Cunha**
  - a85284@ualg.pt
- **Paulo Ferreira**
  - a85285@ualg.pt
