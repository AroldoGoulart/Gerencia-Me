# Coding: UTF-8
# Dentro do Constrollers serão salvas as funções back-end
from app import app



# Configurando as rotas
@app.route("/")
def index():
	return ("Ola mundo, socorro")