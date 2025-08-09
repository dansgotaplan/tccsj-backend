CREATE DATABASE tccsjtests;

USE tccjtests;

CREATE TABLE locais_de_interesse (
    cod int primary key auto_increment,
    descricao varchar(255) not null,
    resumo text,
    endereco varchar(500),
    latitude decimal (10,8) not null,
    longitude decimal (11,8) not null,
    link_imagem text not null,
    dias_funcionamento varchar(255),
    icone varchar(255),
    horario_inicio time not null,
    horario_fim time not null
);

CREATE TABLE tags (
    cod int primary key auto_incrememt,
    nome varchar(255)
);

CREATE TABLE locaistags (
    fk_local int,
    fk_tag int,
    primary key (fk_local, fk_tag),
    foreign key fk_local references locais_de_interesse(cod),
    foreign key fk_tag references tags(cod)
);