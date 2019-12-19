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
from app.controllers.tables import turmas
from app.controllers.tables import aluno_x_turma

# Metodos de Aluno
# deleteAluno() - parametro (Id do aluno)
# createAluno() - parametro (Nome, Email, Telefone, Data_de_Nascimento, Genero)
# searchAluno() - parametro (informação a ser buscada, metodo)  os metodos são Email, Nome
# updateAluno() - parametro (Id do aluno a ser alterado, Nome, Email, Telefone, Data_de_Nascimento, Genero )
# createJson() - sem parametro

# Metodos de Escolas
# getAPICloud() - sem parametro
# createEscola() - parametro (nomeEscola, Região, Cidade ,Estado, anoEscola, situaçaoEscola) 
# deleteEscola() - parametro (Id da Escola)
# searchEscola() - parametro (conteudo a ser buscado, Nome_Escola ou Endereço Data_Escola Situação)
# updateEscola() - parametro (Id da escola a ser alterado, Nome_Escola, Regiao, Cidade ,Estado, Data_Escola, Situação )

# Metodos de Turmas
# createTurma() - parametro (Ano, Nivel_de_Ensino, Serie ,Turno, Id_Escola)
# deleteTurma() - parametro (Id da turma)
# searchTurma() - parametro ((conteudo a ser buscado, Id, Ano, Nivel_de_Ensino, Serie, Turno,  Id_Escola)
# updateTurma() - parametro (Id, Ano, Nivel_de_Ensino, Serie, Turno, Id_Escola)

# Metodos de Alunos_X_Turma
# createAlunoTurma() - parametro (Id_Aluno, Id_Turma)
# searchAlunoTurma() - parametro (item a ser buscado, Id_Aluno ou Id_Turma)
# updateAlunoTurma() - parametro (Id_Aluno, novo id_aluno, novo id_turma)
# deleteAlunoTurma() - parametro (Id_Aluno)

