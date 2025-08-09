USE tccsjdb;

CREATE TABLE evento( #Polo (EX: Pátio do Forró)
    cod int primary key auto_increment,
    descricao varchar(255) not null,
    endereco varchar(500),
    latitude decimal not null,
    longitude decimal not null,
    resumo text,
    data_inicio date not null,
    data_fim date not null
);

CREATE TABLE exibicao( #Dia de Show (EX: um dia específico de um evento)
    cod int primary key auto_increment,
    fk_evento int,
    data_exibicao date not null,
    horario time,
    sequencia tinyint unsigned,
    foreign key (fk_evento) references evento(cod)
);

CREATE TABLE atracao( #Artista ou Banda
    cod int primary key auto_increment,
    fk_exibicao int,
    nome varchar(500) not null,
    principal boolean,
    foreign key (fk_exibicao) references exibicao(cod)
);

CREATE TABLE locais_de_interesse(
    cod int primary key auto_increment,
    descricao varchar(255) not null,
    resumo text,
    endereco varchar(500),
    latitude decimal(10,8) not null,
    longitude decimal(11,8) not null,
    link_imagem text not null,
    dias_funcionamento varchar(255),
    icone varchar(255),
    horario_inicio time not null,
    horario_fim time not null
);

CREATE TABLE locaistags(
    fk_local int,
    fk_tag int,
    primary key (fk_local, fk_tag),
    foreign key (fk_local) references locais_de_interesse(cod),
    foreign key (fk_tag) references tags(cod)
)

CREATE TABLE tags(
    cod int primary key auto_increment,
    nome varchar(255) not null,
    descricao varchar(255) not null,
);

CREATE TABLE comidas(
    cod int primary key auto_increment,
    descricao varchar(255) not null,
    data_comida date not null,
    horario time,
    endereco varchar(500),
    latitude decimal not null,
    longitude decimal not null,
    resumo text
);

CREATE TABLE homenageados(
    cod int primary key auto_increment,
    ano year not null,
    obras varchar(500) not null,
    nome varchar(255) not null,
    descricao varchar(255) not null
);

CREATE TABLE usuario(
    cod int primary key auto_increment,
    email varchar(255) unique not null,
    senha varchar(255) not null,
    nivel_de_acesso varchar(10) not null
)

INSERT INTO usuario(email, senha, nivel_de_acesso) VALUES ("kauayssa@gmail.com", "amotaroba", "admin")