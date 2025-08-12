USE tccsj;

-- Tabela de Eventos como Comidas Gigantes, Queermesse, etc.
DROP TABLE IF EXISTS evento;
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

-- Tabela de Polos como Pátio do Forró, Azulão, SJ na Roça, etc.
DROP TABLE IF EXISTS polo;
CREATE TABLE polo(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    inicio DATE NOT NULL,
    fim DATE NOT NULL,
    endereco VARCHAR(500) NOT NULL,
    latitude DECIMAL(8,5) NOT NULL,
    longitude DECIMAL(8,5) NOT NULL
);

-- Tabela de exibições em determinado polo
DROP TABLE IF EXISTS exibicao;
CREATE TABLE exibicao(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    sequencia TINYINT UNSIGNED,
    fkpolo INT NOT NULL,
    dia DATE NOT NULL,
    horario TIME NOT NULL,
    FOREIGN KEY (fkpolo) REFERENCES polo(cod)
);

-- Tabela de Atrações em determinada exibição de um polo
DROP TABLE IF EXISTS atracao;
CREATE TABLE atracao(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    sequencia TINYINT UNSIGNED,
    fkexibicao INT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    principal BOOLEAN NOT NULL,
    FOREIGN KEY (fkexibicao) REFERENCES exibicao(cod)
);

-- Tabela de Locais de Interesse
DROP TABLE IF EXISTS locais;
CREATE TABLE locais(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    dias VARCHAR(255),
    inicio TIME NOT NULL,
    fim TIME NOT NULL,
    endereco VARCHAR(500) NOT NULL,
    latitude DECIMAL(8,5) NOT NULL,
    longitude DECIMAL(8,5) NOT NULL,
    urlimage TEXT NOT NULL,
    urlicone VARCHAR(255) NOT NULL
);

-- Personalidades marcantes ou homenageados
DROP TABLE IF EXISTS pessoa;
CREATE TABLE pessoa(
    cod INT PRIMARY KEY AUTI_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    obras VARCHAR(500) NOT NULL,
    nascido DATE NOT NULL,
    morte DATE,
    ishomenageado BOOLEAN NOT NULL,
    anohomenagem DATE
);

-- Tabela de tags (Cultural, Comercio, etc)
DROP TABLE IF EXISTS tag;
CREATE TABLE tag(
    cod VARCHAR(255) PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL
);

-- Relacionamento n para n de Tags e Locais
DROP TABLE IF EXISTS locaistags;
CREATE TABLE locaistags(
    fklocal INT,
    fktag INT,
    PRIMARY KEY (fklocal, fktag),
    FOREIGN KEY (fklocal) REFERENCES locais(cod),
    FOREIGN KEY (fktag) REFERENCES tag(cod)
);

-- Relacionamento n para n de Pessoas e Tags
DROP TABLE IF EXISTS pessoatags;
CREATE TABLE pessoatags(
    fkpessoa INT,
    fktag INT,
    PRIMARY KEY (fkpessoa, fktag),
    FOREIGN KEY (fkpessoa) REFERENCES pessoa(cod),
    FOREIGN KEY (fktag) REFERENCES tag(cod)
);

DROP TABLE IF EXISTS usuario;
CREATE TABLE usuario(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    isadmin BOOLEAN NOT NULL
);