USE tccsjtests;

INSERT INTO locais_de_interesse(
    descricao,
    resumo,
    endereco,
    latitude,
    longitude,
    link_imagem,
    dias_funcionamento,
    icone,
    horario_inicio,
    horario_fim
) VALUES (
    'Feira de Caruaru',
    'A Feira de Caruaru, localizada no Parque 18 de Maio, é uma das maiores feiras ao ar livre da América Latina e um importante símbolo cultural do Nordeste.',
    'Av. Lourival José da Silva - Petrópolis, Caruaru-PE, 55030-200',
    -8.289007,
    -35.972379,
    'https://www.sindloja.com.br/webfiles/imagesno/1027x535preenchimento100-20170605_593564c79a902.jpg',
    'Todos os dias',
    'https://www.cdn-icons-png.flaticon.com/512/2037/2037749.png',
    '0:00:00',
    '23:59:59',
);

INSERT INTO tags(
    nome
) VALUES (
    'Cultural'
);

INSERT INTO tags(
    nome
) VALUES (
    'Comércio'
);

INSERT INTO locaistags(
    fk_local,
    fk_tag
) VALUES (
    1,
    1
);

INSERT INTO locaistags(
    fk_local,
    fk_tag
) VALUES (
    1,
    2
);