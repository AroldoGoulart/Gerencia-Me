# Conexão com o banco de dados

import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='ifmt3210',
                             db='Teste',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def createAlunos(Nome, Email, Telefone, Data_de_Nascimento, Genero):
    try:    
        #verificar qual state do
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `Alunos` (Nome, Email, Telefone, Data_de_Nascimento, Genero) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (Nome, Email, Telefone, Data_de_Nascimento, Genero))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        connection.close()




    