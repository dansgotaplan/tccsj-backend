CREATE DATABASE tccsj;

USE DATABASE tccsj;

CREATE TABLE evento(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    dia DATE NOT NULL,
    horario TIME NOT NULL,
    endereco VARCHAR(500) NOT NULL,
    latitude DECIMAL NOT NULL,
    longitude DECIMAL NOT NULL
);

CREATE TABLE polo(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    inicio DATE NOT NULL,
    fim DATE NOT NULL,
    endereco VARCHAR(500) NOT NULL,
    latitude DECIMAL NOT NULL,
    longitude DECIMAL NOT NULL,
);

CREATE TABLE exibicao(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    sequencia TINYINT UNSIGNED AUTO_INCREMENT,
    fkpolo INT NOT NULL,
    dia DATE NOT NULL,
    horario TIME,
    FOREIGN KEY (fkpolo) REFERENCES polo(cod)
);

CREATE TABLE atracao(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    sequencia TINYINT UNSIGNED AUTO_INCREMENT,
    fkexibicao INT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    principal BOOLEAN NOT NULL,
    FOREIGN KEY (fkexibicao) REFERENCES exibicao(cod)
);

CREATE TABLE locais(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    dias VARCHAR(255),
    inicio TIME NOT NULL,
    fim TIME NOT NULL,
    endereco VARCHAR(500) NOT NULL,
    latitude DECIMAL (10,8) NOT NULL,
    longitude DECIMAL (11,8) NOT NULL,
    urlimage TEXT NOT NULL,
    urlicone VARCHAR(255) NOT NULL
);

CREATE TABLE tag(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE locaistags(
    fklocal INT,
    fktag INT,
    PRIMARY KEY (fklocal, fktag),
    FOREIGN KEY (fklocal) REFERENCES locais(cod),
    FOREIGN KEY (fktag) REFERENCES tag(cod)
);

CREATE TABLE pessoatags(
    fkpessoa INT,
    fktag INT,
    PRIMARY KEY (fkpessoa, fktag)
    FOREIGN KEY (fkpessoa) REFERENCES pessoa(cod)
    FOREIGN KEY (fktag) REFERENCES tag(cod)
);

CREATE TABLE pessoa(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    obras VARCHAR(500) NOT NULL,
    nascido DATE NOT NULL,
    morte DATE,
    ishomenageado BOOLEAN NOT NULL,
    anohomenagem DATE NOT NULL
);

CREATE TABLE usuario(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    isadmin BOOLEAN NOT NULL
);