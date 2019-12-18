# Instanciar arquivos paginas, declarando-os
from flask import Flask
# Intanciando app
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Instanciando conexão com banco# Instanciando as rotas


from app.controllers import default
#100% FEITO
from app.controllers.tables import alunos
from app.controllers.tables import escolas

# Metodos de Aluno
# deleteAluno() - parametro (ID)
# createAluno() - parametro (Nome, Email, Telefone, Data_de_Nascimento, Genero)
# searchAluno() - parametro (informação a ser buscada, metodo)  os metodos são Email, Nome
# updateAluno() - parametro (Id do usario a ser alterado, Nome, Email, Telefone, Data_de_Nascimento, Genero )

# Metodos de Escolas
# getAPICloud() - sem parametro
# createEscola() - parametro (nomeEscola, Região, Cidade ,Estado, anoEscola, situaçaoEscola) 
# deleteEscola() - parametro (Id da Escola)
# searchEscola() - parametro ( conteudo a ser buscado, Nome_Escola)  Nome_Escola ou Endereço Data_Escola Situação
# 										  

escolas.searchEscola('Em atividade')
