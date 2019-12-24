drop database if exists gerencia;
create database if not exists gerencia
default character set utf8mb4
default collate utf8mb4_general_ci; 
use gerencia;


create table Alunos(
	Id int NOT NULL AUTO_INCREMENT,
	Nome varchar(255) NOT NULL,
	Telefone varchar(30),
	Email varchar(100) NOT NULL,
	Data_de_Nascimento date,
	Genero enum("Masculino","Feminino"),
	primary key (Id)
);


create table Escolas(
	Id int NOT NULL AUTO_INCREMENT,
	Nome_Escola varchar(100) NOT NULL,
    	Endereço varchar(255),
    	Data_Escola year(4),
    	Situação enum("Em atividade","Paralisada","Extinta","Extinta no ano anterior") NOT NULL,
	primary key (Id)
);

create table Turmas(
	Id int NOT NULL AUTO_INCREMENT,
	Ano year,
	Nivel_de_Ensino enum('Fundamental', 'Medio'), 
	Serie int(1) NOT NULL,
	Turno varchar(20),
	Id_Escola int,
	primary key (Id),
	foreign key(Id_Escola) references Escolas(Id)
);

create table Alunos_X_Turma(
	Id_Aluno int,
	Id_Turma int,
	foreign key(Id_Aluno) references Alunos(Id) on delete cascade,
	foreign key(Id_Turma) references Turmas(Id) on delete cascade,
	primary key(Id_Aluno, Id_Turma)
);
