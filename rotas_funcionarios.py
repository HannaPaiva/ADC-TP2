# ok

from rotas_funcionarios import *
from flask import Flask, render_template, request, redirect, url_for, Blueprint

from funcoes import *

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

rotas_funcionario = Blueprint("rotas_funcionario", __name__)


@rotas_funcionario.route('/funcionarios')
def listar_funcionarios():
    dados = free_select('''SELECT id_funcionario, nome, morada, telefone, nif, email
FROM Funcionarios;
 
        ''')
    
  
    action = "pesquisar-funcionario"
    if dados is not None:
        return render_template('funcionarios.html', dados=dados, action=action, departamentos = departamentos)
    else:
        return render_template('funcionarios.html')



# @rotas_funcionario.route('/criar-funcionario', methods=['GET', 'POST'])
# def criar_funcionario():

#     dados = {
#         "primeiroNome": request.form["primeiroNome"],
#         "nomeDoMeio": request.form["nomeDoMeio"],
#         "ultimoNome": request.form["ultimoNome"],
#         "contribuinte": request.form["contribuinte"],
#         "CC": request.form["CC"],
#         "email": request.form["email"],
#         "telefone": request.form["telefone"],
#         "dataNascimento": request.form["dataNascimento"],
#         "status": request.form["status"],
#         "genero": request.form["genero"],
#         "iddepartamento": request.form["iddepartamento"],
#     }

#     conn.insert_data("funcionario", dados)
#     return redirect(url_for('rotas_funcionario.listar_funcionarios'))


# @rotas_funcionario.route('/editar-funcionario', methods=['GET', 'POST'])
# def editar_funcionario():
#     idfuncionario = {"idfuncionario": request.form["idfuncionario"]}
#     dados = {
#         "primeiroNome": request.form["primeiroNome"],
#         "nomeDoMeio": request.form["nomeDoMeio"],
#         "ultimoNome": request.form["ultimoNome"],
#         "contribuinte": request.form["contribuinte"],
#         "CC": request.form["CC"],
#         "email": request.form["email"],
#         "telefone": request.form["telefone"],
#         "dataNascimento": request.form["dataNascimento"],
#         "status": request.form["status"],
#         "genero": request.form["genero"],
#         "iddepartamento": request.form["iddepartamento"],
       
#     }
#     print(dados)

#     conn.update_data("funcionario", dados, idfuncionario)
#     return redirect(url_for('rotas_funcionario.listar_funcionarios'))


# @rotas_funcionario.route('/apagar-funcionario', methods=['GET', 'POST'])
# def apagar_funcionario():
#     idfuncionario = {"idfuncionario": request.form["idfuncionario"]}
#     conn.delete_data("funcionario", idfuncionario)
#     return redirect(url_for('rotas_funcionario.listar_funcionarios'))


# @rotas_funcionario.route('/pesquisar-funcionario', methods=['GET', 'POST'])
# def pesquisar_funcionario():
#     param = request.form["param"]

#     dados = conn.select_data(table="funcionario", search=param)

#     if dados:
#         return render_template('pesquisa.html', dados=dados)
#     else:
#         return render_template('pesquisa.html', dados=[{"response": "Não encontrado"}])



# app.register_blueprint(rotas_funcionario)
# if __name__ == '__main__':
#     app.run(debug=True)
