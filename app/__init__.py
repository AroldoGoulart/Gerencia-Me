# Instanciar arquivos paginas, declarando-os
from flask import Flask

# Intanciando app
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Instanciando conexão com banco# Instanciando as rotas

#100% FEITO
from app.controllers.tables import alunos
from app.controllers.tables import escolas
from app.controllers.tables import turmas
from app.controllers.tables import aluno_x_turma
from app.controllers import routes

alunos.createJson()