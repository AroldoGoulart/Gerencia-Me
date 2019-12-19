# Arquivo responsavel pelo requesição API Integrada e CRUD da tabela Escola

import requests

from datetime import datetime
import pymysql.cursors, sys, json

# Conectar ao Banco de dados, alimentando-se do arquivo db.json
def __connect__():
    with open('./app/db.json') as f:    
        data = json.load(f)

    connection = pymysql.connect(host='localhost',
                             user=data['User'],
                             password=data['Password'],
                             db=data['DB_Name'],
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection

# Inserir Turma 
def createAlunoTurma(Id_Aluno, Id_Turma):
    try:
        connection = __connect__()

        with connection.cursor() as cursor:
            # Fazendo requesição QUERY no Banco de dados
            sql = "INSERT INTO `Alunos_X_Turma` (Id_Aluno, Id_Turma) VALUES (%s, %s)"
            cursor.execute(sql, (Id_Aluno, Id_Turma))
        connection.commit()
    except:
        print("Erro ao executar banco de dados em createAlunoTurma")
    finally:
        connection.close()


# Deletar AlunoTurma
def deleteAlunoTurma(Id):
    # Verificar se o valor digitado é Inteiro
    if(isinstance(Id, int)): 
        try:  
            connection = __connect__()

            # Fazendo requesição QUERY no Banco de dados
            with connection.cursor() as cursor:
                sql = "DELETE FROM `Alunos_X_Turma` WHERE  Id = (%s)"
                cursor.execute(sql, Id)

            # Executar atualização no Banco de Dados
            connection.commit()
        except:
            print("Falha ao conectar com o banco e, deleteAlunoTurma")
        finally:
            connection.close()
    else:
        print("Valor passado não é inteiro")


# Procurar Aluno_x_turma
def searchAlunoTurma(date, metodo):
    try:
        connection = __connect__()

        # Colocando filtros para o sql
        if(isinstance(date,int)):
            if(metodo == "Id_Aluno"):
                sql = "SELECT * FROM Alunos_X_Turma WHERE Id_Aluno = (%s)"
            else:
                sql = "SELECT * FROM Alunos_X_Turma WHERE Id_Turma = (%s)"

        # Fazendo requesição QUERY no Banco de dados
        with connection.cursor() as cursor:
            cursor.execute(sql, (date))
            # Guardar dados da pesquisa em um json
            records = cursor.fetchall()
            with open('./frontend/src/data/pesquisa.json', 'w') as fp:
                json.dump(records, fp)
    except:
        print("Erro em searchAlunoTurma")
    finally:
        connection.close()



def updateAlunoTurma(Id_Aluno, Id_Novo_Aluno, Id_Turma):
    try:
        connection = __connect__()

        with connection.cursor() as cursor:
                sql = "UPDATE `Alunos_X_Turma` SET Id_Aluno = (%s), Id_Turma = (%s) WHERE  Id_Aluno = (%s)"
                cursor.execute(sql, (Id_Novo_Aluno, Id_Turma, Id_Aluno))
          
        # Executar atualização no Banco de Dados
        connection.commit()
    finally:
        connection.close()