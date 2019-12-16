#Cadastro alunos
- API 
	- listagem 
	- Busca
	- Cadastro
	- Edição
	- Exclusão de aluno

- Campos: ID, nome, telefone, 
e-mail, data nascimento, genero

- Campos Obrigatorios: nome, e-email

DICA: Um aluno pode estar ligado a muitas turmas
1  - n

#Cadastro de Turmas
- API
	- Listagem
	- Busca
	- Cadastro
	- Edição
	- Exclusão das turmas

- Campos: Ano, Nivel de Ensino(fundamental, medio),
serie, turno

DICA: Uma turma deve estar ligada a uma escola

#Cadastro de Escolas
- API
	- Busca
	- Cadastro
	- Edição
	- Exclusão de Escola

Campos: ID, Nome da Escola, endereço

Campos Obrigatorios: ID, Data, Situação

DIca: Uma escola tem varias turmas
Exibir total de alunos

API para integraçao

Os dados da escola serão buscados via api:
http://educacao.dadosabertosbr.com/api/docs/%2Fapi%2Fescolas%2Fbuscaavancada

http://educacao.dadosabertosbr.com/api/escolas/buscaavancada?estado=MT

Extra: Localização no mapa
	- Exibir colegio no mapa dinamico ou fixo


