# Arquivo responsavel pelo requesição API Integrada e CRUD da tabela Escola

import requests

from datetime import datetime
import pymysql.cursors, sys, json



# Conectar ao Banco de dados, alimentando-se do arquivo db.json
def __connect__():
    with open('db.json') as f:    
        data = json.load(f)

    connection = pymysql.connect(host='localhost',
                             user=data['User'],
                             password=data['Password'],
                             db=data['DB_Name'],
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection

# Alimenta o Banco de dados local com as Escolas
def getAPICloud():
    try:
        connection = __connect__()
        # Requesição da API 
        r = requests.get('http://educacao.dadosabertosbr.com/api/escolas/buscaavancada?nome=master&estado=MT')
        rJson = r.json()

        # Filtro de dados da API + Upload para Banco de Dados
        a = 0
        while (a < rJson[0]):
            nomeEscola = rJson[1][a]['nome']
            regiaoEscola = rJson[1][a]['regiao'] + " - " + rJson[1][a]['cidade'] + " - " + rJson[1][a]['estado']
            anoEscola = rJson[1][a]['anoCenso']
            situaçaoEscola= rJson[1][a]['situacaoFuncionamentoTxt']

            
            with connection.cursor() as cursor:
                # Fazendo requesição QUERY no Banco de dados
                sql = "INSERT INTO `Escolas` (Nome_Escola, Endereço, Data_Escola, Situação) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (nomeEscola, regiaoEscola, anoEscola, situaçaoEscola))
            connection.commit()
            a = a +1
    except:
        print("Erro ao executar banco de dados em getAPICloud")
    finally:
        connection.close()

# Inserir Escola 
def createEscola(nomeEscola, Regiao, Cidade ,Estado, anoEscola, situaçaoEscola):
    try:
        connection = __connect__()

        regiaoEscola = Regiao + " - " + Cidade + " - " + Estado
        with connection.cursor() as cursor:
            # Fazendo requesição QUERY no Banco de dados
            sql = "INSERT INTO `Escolas` (Nome_Escola, Endereço, Data_Escola, Situação) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nomeEscola, regiaoEscola, anoEscola, situaçaoEscola))
        connection.commit()
    except:
        print("Erro ao executar banco de dados em getAPICloud")
    finally:
        connection.close()

# Deletar Escla
def deleteEscola(Id):
    # Verificar se o valor digitado é Inteiro
    if(isinstance(Id, int)): 
        try:  
            connection = __connect__()

            # Fazendo requesição QUERY no Banco de dados
            with connection.cursor() as cursor:
                sql = "DELETE FROM `Escolas` WHERE  Id = (%s)"
                cursor.execute(sql, Id)

            # Executar atualização no Banco de Dados
            connection.commit()
        except:
            print("Falha ao conectar com o banco e, deleteAluno")
        finally:
            connection.close()
    else:
        print("Valor passado não é inteiro")

# Procurar Escola por Nome_Escola ou Endereço Data_Escola Situação
def searchEscola(IdOrEmail, metodo):
        connection = __connect__()

        # Colocando filtros para o sql
        IdOrEmail = "%"+IdOrEmail+"%"

        # Verificando qual foi o metodo solicitado
        sql = "SELECT * FROM Escolas WHERE Situação LIKE (%s)"
        # Fazendo requesição QUERY no Banco de dados
        with connection.cursor() as cursor:
            cursor.execute(sql, (IdOrEmail))
            # Guardar dados da pesquisa em um json
            records = cursor.fetchall()
            with open('pesquisa.json', 'w') as fp:
                json.dump(records, fp)

        # Fechando abertura QUERY
        cursor.close()
