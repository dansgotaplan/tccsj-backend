CREATE DATABASE tccsjtests;

USE tccsjtests;

CREATE TABLE eventos (
    cod int primary key auto_increment,
    nome varchar(255) not null,
    endereco varchar(500),
    latitude decimal not null,
    longitude decimal not null,
    resumo text,
    data_inicio date not null,
    data_fim not null
);