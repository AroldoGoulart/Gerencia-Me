# Gerencia as rotas do aplicativo
from app import app
from flask import request
from flask_cors import CORS

from app.controllers.tables import alunos
from app.controllers.tables import escolas
from app.controllers.tables import turmas
from app.controllers.tables import aluno_x_turma
from app.controllers import routes
import json
from flask import jsonify
import sys

CORS(app)


@app.route('/json/alunos', methods = ['GET'])
def json():	
	alunos.createJson()
	return 'a'

@app.route("/delete/<int:Id>")
def index(Id):
	alunos.deleteAluno(Id)
	return id



