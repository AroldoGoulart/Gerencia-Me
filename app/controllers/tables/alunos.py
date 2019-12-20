# -*- coding: utf-8 -*-
# Arquivos responsavel pelo CRUD da tabela Alunos 

from datetime import datetime
import pymysql.cursors, sys, json

# Classes Privadas
# Converter coluna Data_de_Nascimento para formato reconhecido em JSON
def __dt_conversor__(dt):
    return dt.isoformat()

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


# Criar um novo Aluno
def createAluno(Nome, Email, Telefone, Data_de_Nascimento, Genero):
    try:
        connection = __connect__()
        
        # Fazendo requesição QUERY no Banco de dados
        with connection.cursor() as cursor:
            sql = "INSERT INTO `Alunos` (Nome, Email, Telefone, Data_de_Nascimento, Genero) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (Nome, Email, Telefone, Data_de_Nascimento, Genero))

        # Executar atualização no Banco de Dados
        connection.commit()

        # Atualizar arquivo JSON
        createJson()
    except:
        print("Erro em createAluno")
    finally:
        connection.close()

# Deletar Aluno por ID
def deleteAluno(Id):
    # Verificar se o valor digitado é Inteiro
    if(isinstance(Id, int)): 
        try:  
            connection = __connect__()

             # Fazendo requesição QUERY no Banco de dados
            with connection.cursor() as cursor:
                sql = "DELETE FROM `Alunos` WHERE  Id = (%s)"
                cursor.execute(sql, Id)

            # Executar atualização no Banco de Dados
            connection.commit()

            # Atualizar arquivo JSON
            createJson()

        except:
            print("falha ao conectar com o banco")
        finally:
            connection.close()
    else:
        print("Valor passado não é inteiro")

# Procurar Aluno por Nome ou Email
def searchAluno(IdOrEmail, metodo):
    try:
        connection = __connect__()

        # Colocando filtros para o sql
        IdOrEmail = "%"+IdOrEmail+"%"

        # Verificando qual foi o metodo solicitado
        if(metodo == "Email"):
            sql = "SELECT * FROM Alunos WHERE Email LIKE %s"
        else:
            sql = "SELECT * FROM Alunos WHERE Nome LIKE (%s)"

        # Fazendo requesição QUERY no Banco de dados
        with connection.cursor() as cursor:
            cursor.execute(sql, IdOrEmail)

        # Guardar dados da pesquisa em um json
        records = cursor.fetchall()
        with open('./frontend/src/data/pesquisa.json', 'w') as fp:
            json.dump(records, fp, default=__dt_conversor__)

        # Fechando abertura QUERY
        cursor.close()
    except:
        print("Erro em searchAluno")
    finally:
        connection.close()
   
# Atualizar dados de aluno
def updateAluno(Id, Nome, Email, Telefone, Data_de_Nascimento, Genero):
    try:
        connection = __connect__()
        with connection.cursor() as cursor:
                sql = "UPDATE `Alunos` SET Nome = (%s), Email = (%s), Telefone = (%s), Data_de_Nascimento = (%s), Genero = (%s) WHERE  Id = (%s)"
                cursor.execute(sql, (Nome, Email, Telefone, Data_de_Nascimento, Genero, Id))
      
        # Executar atualização no Banco de Dados
        connection.commit()

        # Atualizar arquivo JSON
        createJson()    
    except:
        print('Erro na conexão com o banco em updateAluno')
    finally:
        connection.close()

# Cria um arquivo no formato Json de todos os alunos cadastrados
def createJson():
    try:
        connection = __connect__()
        with connection.cursor() as cursor:
            sql = 'SELECT * from Alunos'
            cursor.execute(sql)

        # Criando (se não existente) e escrevendo dados em alunos.json
        records = cursor.fetchall()

        with open('./frontend/src/data/alunos.json', 'w') as fp:
            json.dump(records, fp, default=__dt_conversor__)
    finally:
        connection.close()    
    
