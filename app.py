


from flask import Flask, render_template, request, redirect, url_for
import sqlite3

from rotas_funcionarios import rotas_funcionario
from rotas_leitores import rotas_leitor
from rotas_emprestimos import rotas_emprestimo
from rotas_livros import rotas_livro

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

app.register_blueprint(rotas_funcionario)
app.register_blueprint(rotas_leitor)
app.register_blueprint(rotas_emprestimo)
app.register_blueprint(rotas_livro)

def get_db_connection():
    conn = sqlite3.connect('base_de_dados.db')
    conn.row_factory = sqlite3.Row  # Para obter resultados como dicionários
    return conn

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# --- Rotas para Leitores ---

# Página para exibir todos os leitores
@app.route('/leitores')
def leitores():
    conn = get_db_connection()
    leitores = conn.execute('SELECT * FROM Leitores').fetchall()
    conn.close()
    return render_template('leitores.html', leitores=leitores)

# Página para adicionar um novo leitor
@app.route('/add_leitor', methods=('GET', 'POST'))
def add_leitor():
    if request.method == 'POST':
        nome = request.form['nome']
        morada = request.form['morada']
        telefone = request.form['telefone']
        nif = request.form['nif']
        email = request.form['email']

        conn = get_db_connection()
        conn.execute('INSERT INTO Leitores (nome, morada, telefone, nif, email) VALUES (?, ?, ?, ?, ?)',
                     (nome, morada, telefone, nif, email))
        conn.commit()
        conn.close()
        return redirect(url_for('leitores'))

    return render_template('add_leitor.html')

# --- Rotas para Livros ---

# Página para exibir todos os livros
@app.route('/livros')
def livros():
    conn = get_db_connection()
    livros = conn.execute('SELECT * FROM Livros').fetchall()
    conn.close()
    return render_template('livros.html', livros=livros)

# Página para adicionar um novo livro
@app.route('/add_livro', methods=('GET', 'POST'))
def add_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        categoria = request.form['categoria']
        isbn = request.form['isbn']
        ano_publicacao = request.form['ano_publicacao']

        conn = get_db_connection()
        conn.execute('INSERT INTO Livros (isbn, titulo, autor, categoria, ano_publicacao) VALUES (?, ?, ?, ?, ?)',
                     (isbn, titulo, autor, categoria, ano_publicacao))
        conn.commit()
        conn.close()
        return redirect(url_for('livros'))

    return render_template('add_livro.html')

# --- Rotas para Funcionários ---

# Página para exibir todos os funcionários
@app.route('/funcionarios')
def funcionarios():
    conn = get_db_connection()
    funcionarios = conn.execute('SELECT * FROM Funcionarios').fetchall()
    conn.close()
    return render_template('funcionarios.html', funcionarios=funcionarios)

# Página para adicionar um novo funcionário
@app.route('/add_funcionario', methods=('GET', 'POST'))
def add_funcionario():
    if request.method == 'POST':
        nome = request.form['nome']
        morada = request.form['morada']
        telefone = request.form['telefone']
        nif = request.form['nif']
        email = request.form['email']

        conn = get_db_connection()
        conn.execute('INSERT INTO Funcionarios (nome, morada, telefone, nif, email) VALUES (?, ?, ?, ?, ?)',
                     (nome, morada, telefone, nif, email))
        conn.commit()
        conn.close()
        return redirect(url_for('funcionarios'))

    return render_template('add_funcionario.html')

# Executando a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
