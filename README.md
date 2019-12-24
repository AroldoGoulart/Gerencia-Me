# Gerencia-Me
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

## Objetivo
Desenvolver um sistema de controle de alunos de uma escola.

## Status de conclusão;
 - [x] Banco de Dados.
 - [x] Conexão BD / Codigo.
 - [x] CRUD para todas as tabelas.
 - [x] Back-end.
 - [ ] Front-end

## Tecnologias
- Python 3.
- MySQL.
- Flask.
- React.

## Requesitos
- PIP, gerenciador de pacotes python. 
- Servidor MYSQL.

Ps: Em textes foi utilizado o mysql workbench.


## Recomendações
- Utilizar um ambiente virtual para a executação sem interferência de outros pacotes instalados na máquina.

Ps: Em textes foi utilizado o virtualenv.

## Instalação

Utilize o git para clonar o repositório em sua máquina local.

```
git clone https://github.com/SnowLew/Gerencia-Me
```

Navegue até a pasta do repositório e instale as dependências.

```
pip3 install flask flask-cors pymysql requests
```

Utilize o codigo MySql contido na raiz do diretório em seu servidor local.

Verifique se os dados de conexão do arquivo App/db.json correspondem aos da sua máquina, caso não, modifique para os corretos.

## Execução

Inicie seu serviço MYSQL 

Execute o arquivo principal para inciar.

```
python3 run.py
```

----
## Funcionamento e Metodos

### Run.py
> Inicia a aplicação de fora da página de recursos "app"

### App/____Init____.py
> Todos os modulos serão evocados, com suas respectivas funções.
> Camada usada tambem para execução de funções das tabelas do importadas.

### App/Controllers
> Nesta pasta estão contidos os métodos de gerenciamento e CRUD de cada tabela do banco de dados.

### App/Controllers/routes.js
> Como cada chamada HTTP deve responder

### Controllers/Tables/Alunos.py
Funções:
> - createAluno(Nome, Email, Telefone, Data_de_Nascimento, Genero)
> - - Cria um novo aluno no Banco de Dados.

> - deleteAluno(Id)
> - - Deleta um aluno do Banco de Dados

> - updateAluno(Id, Nome, Email, Telefone, Data_de_Nascimento, Genero)
> - - Atualiza os dados de um aluno no Banco de Dados.

> - searchAluno("Dado a ser Buscado", "metodos")
> - - Os métodos possíveis são:
> - - Nome, Email
> - - Cria um JSON contendo os dados da pesquisa realizada.

> - createJson()
> - - Cria um JSON contendo todos os alunos cadastrados no banco de dados, utilizado para banco de dados offline.

### Controllers/Tables/Escolas.py
Funções:
> - getAPICloud()
> - - Coleta os dados da API para integração fornecida e os converte e cadastra no banco MYSQL.

> - createEscola(Nome_Escola, Regiao, Cidade, Estado, Data_Escola, Situação)
> - - Cadastra nova escola no Banco de Dados.

> - deleteEscola(Id)
> - - Deleta escola do Banco de Dados.

> - searchEscola("Conteudo a ser buscado", "Metodo")
> - - Os métodos possíveis são:
> - - Nome_Escola, Endereço, Data_Escola, Situação ou Id.
> - - Cria um JSON contendo os dados da pesquisa realizada.

> - updateEscola(Id, Nome_Escola, Regiao, Cidade, Estado, Data_Escola, Situação)
> - - Atualiza o conteúdo da escola.

### Controllers/Tables/Turmas.py
> - createTurma(Ano, Nivel_de_Ensino, Serie, Turno, Id_Escola)
> - - Cria uma nova turma no banco de dados.

> - deleteTurma(Id)
> - - Deleta os dados de uma turma do banco de dados.

> - updateTurma(
> - - Atualiza os dados da turma.

> - searchTurma("Dado a ser Buscado", "metodo")
> - - Os métodos possíveis são:
> - - Ano, Nivel_de_Ensino, Serie, Turno, Id_Escola
> - - Cria um JSON contendo os dados da pesquisa realizada.

### Controllers/Tables/aluno_x_turma.py
> - createAlunoTurma(Id_Aluno, Id_Turma)
> - - Cria uma nova relação aluno/turma no banco de dados.

> - deleteAlunoTurma(Id_Aluno)
> - - Deleta os dados de uma relação aluno/turma do banco de dados.

> - searchTurma("Dado a ser Buscado", "metodo")
> - - Os métodos possíveis são:
> - - Id_Turma, Id_Aluno
> - - Cria um JSON contendo os dados da pesquisa realizada.



## Ideia
* [Estuda.com](http://estuda.com/)
