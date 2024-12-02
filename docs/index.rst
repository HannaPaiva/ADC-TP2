Biblioteca Documentation
=========================

Bem-vindo à documentação do sistema de Biblioteca! Aqui você encontrará informações detalhadas sobre todos os módulos e funcionalidades do projeto.

Conteúdo
--------

.. toctree::
   :maxdepth: 2
   :caption: Índice:
   
   Introdução <introduction>
   Módulos Principais <modules>
   Componentes Auxiliares <components>

Introdução
----------

Este projeto implementa um sistema completo para gerenciamento de uma biblioteca, incluindo empréstimos de livros, cadastro de leitores, gestão de funcionários e manutenção de registros no banco de dados. A documentação é organizada por módulos para facilitar a navegação e consulta.

### Funcionalidades Principais:
- **Gerenciamento de Livros:** Cadastro, atualização e exclusão de registros de livros.
- **Controle de Leitores:** Registro de novos leitores e manutenção de dados.
- **Administração de Funcionários:** Gestão de usuários que operam o sistema.
- **Sistema de Empréstimos:** Registro e controle de empréstimos e devoluções de livros.

Módulos Principais
-------------------

Os módulos principais do projeto estão detalhados nas seções abaixo.

.. toctree::
   :maxdepth: 1
   :caption: Módulos:

   app <app>
   bd_connector <bd_connector>

Menu de interação
-------------------

Os módulos de menu do projeto estão detalhados nas seções abaixo.

.. toctree::
   :maxdepth: 1
   :caption: Menus:

   menu_emprestimos <menu_emprestimos>
   menu_funcionarios <menu_funcionarios>
   menu_leitor <menu_leitor>
   menu_livro <menu_livro>

Componentes Auxiliares
----------------------

Além dos módulos principais, o sistema inclui componentes auxiliares para a implementação de funcionalidades específicas.

.. toctree::
   :maxdepth: 1
   :caption: Componentes:

   Emprestimos <emprestimos>
   Leitores <leitor>
   Livros <livros>
   Funcionários <Funcionarios>

Referências
-----------

- **Documentação Sphinx:** [Sphinx Docs](https://www.sphinx-doc.org/en/master/)
- **Python Oficial:** [Python Docs](https://docs.python.org/3/)
- **SQLite:** [SQLite Docs](https://sqlite.org/docs.html)
