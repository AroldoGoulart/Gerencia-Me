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
def createTurma(Ano, Nivel_de_Ensino, Serie ,Turno, Id_Escola):
    try:
        connection = __connect__()

        with connection.cursor() as cursor:
            # Fazendo requesição QUERY no Banco de dados
            sql = "INSERT INTO `Turmas` (Ano, Nivel_de_Ensino, Serie, Turno, Id_Escola) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (Ano, Nivel_de_Ensino, Serie ,Turno, Id_Escola))
        connection.commit()
    except:
        print("Erro ao executar banco de dados em createTurma")
    finally:
        connection.close()


# Deletar Turma
def deleteTurma(Id):
    # Verificar se o valor digitado é Inteiro
    if(isinstance(Id, int)): 
        try:  
            connection = __connect__()

            # Fazendo requesição QUERY no Banco de dados
            with connection.cursor() as cursor:
                sql = "DELETE FROM `Turmas` WHERE  Id = (%s)"
                cursor.execute(sql, Id)

            # Executar atualização no Banco de Dados
            connection.commit()
        except:
            print("Falha ao conectar com o banco e, deleteTurma")
        finally:
            connection.close()
    else:
        print("Valor passado não é inteiro")


# Procurar Turma por Nome_Escola ou Endereço Data_Escola Situação  ou id
def searchTurma(date, metodo):
    try:
        connection = __connect__()

        # Colocando filtros para o sql
        if(isinstance(date,int)):
            sql = "SELECT * FROM Turmas WHERE Id = (%s)"
        else:
            date = "%"+date+"%"

            # Verificando qual foi o metodo solicitado
            if (metodo == "Ano"):
                sql = "SELECT * FROM Turmas WHERE Ano LIKE (%s)"

            elif (metodo == "Nivel_de_Ensino"):
                sql = "SELECT * FROM Turmas WHERE Nivel_de_Ensino LIKE (%s)"

            elif (metodo == "Serie"):
                sql = "SELECT * FROM Turmas WHERE Serie LIKE (%s)"
            
            elif (metodo == "Turno"):
                sql = "SELECT * FROM Turmas WHERE Turno LIKE (%s)"
            else:
                sql = "SELECT * FROM Turmas WHERE Id_Escola LIKE (%s)"

        # Fazendo requesição QUERY no Banco de dados
        with connection.cursor() as cursor:
            cursor.execute(sql, (date))
            # Guardar dados da pesquisa em um json
            records = cursor.fetchall()
            with open('./frontend/src/data/pesquisa.json', 'w') as fp:
                json.dump(records, fp)
    finally:
        connection.close()



def updateTurma(Id, Ano, Nivel_de_Ensino, Serie, Turno, Id_Escola):
    try:
        connection = __connect__()

        with connection.cursor() as cursor:
                sql = "UPDATE `Turmas` SET Ano = (%s), Nivel_de_Ensino = (%s), Serie = (%s), Turno = (%s), Id_Escola =(%s) WHERE  Id = (%s)"
                cursor.execute(sql, (Ano, Nivel_de_Ensino, Serie, Turno, Id_Escola, Id))
          
        # Executar atualização no Banco de Dados
        connection.commit()
    finally:
        connection.close()