# Instanciar arquivos paginas, declarando-os
from flask import Flask

# Intanciando app
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Instanciando conexão com banco
from app.controllers import connection
# Instanciando as rotas
from app.controllers import default

connection.createAlunos('Sthefany Monteiro', 'emy@gmail.com', '6591335', '2001-07-31', 'Feminino')