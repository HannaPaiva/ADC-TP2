import sqlite3

# Função para conectar ao banco de dados
def conectar():
    conn = sqlite3.connect('base_de_dados.db')
    return conn

# Função para criar a tabela de funcionários, se não existir
def criar_tabela_funcionarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cargo TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para listar todos os funcionários
def listar_funcionarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM funcionarios')
    funcionarios = cursor.fetchall()
    conn.close()
    return funcionarios

# Função para adicionar um novo funcionário
def adicionar_funcionario(nome, cargo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO funcionarios (nome, cargo) VALUES (?, ?)', (nome, cargo))
    conn.commit()
    conn.close()

# Função para atualizar um funcionário
def atualizar_funcionario(id, nome, cargo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE funcionarios SET nome = ?, cargo = ? WHERE id = ?', (nome, cargo, id))
    conn.commit()
    conn.close()

# Função para deletar um funcionário
def deletar_funcionario(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM funcionarios WHERE id = ?', (id,))
    conn.commit()
    conn.close()
