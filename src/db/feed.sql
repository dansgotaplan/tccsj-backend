INSERT INTO usuario(email, senha, nivel_de_acesso) VALUES ('kauayssa@gmail.com', 'amotaroba', 'admin');
INSERT INTO usuario(email, senha, nivel_de_acesso) VALUES ('joaoguilhermedelimaarruda@gmail.com', 'amosaopaulo', 'admin');
INSERT INTO usuario(email, senha, nivel_de_acesso) VALUES ('viniciusdanielsalves@gmail.com', 'vascodagrana', 'admin');

INSERT INTO evento(descricao, endereco, latitude, longitude, resumo, data_inicio, data_fim) VALUES ('Patio do Forro', 'Av. Rui Limeira Rosal, s/n, Caruaru-PE', -8.2835, -35.9732, 'Principal polo do Sao Joao de Caruaru, com grandes apresentacoes musicais', '2025-06-01', '2025-07-01';)
INSERT INTO evento(descricao, endereco, latitude, longitude, resumo, data_inicio, data_fim) VALUES ('Polo Azulao', 'Rua Armando da Fonte, Caruaru-PE', -8.2841, -35.9740, 'Espaco cultural com shows alternativos e independentes', '2025-06-05', '2025-06-30');

INSERT INTO exibicao(fk_evento, data_exibicao, horario, sequencia) VALUES (1, '2025-06-01', '20:00:00', 1);
INSERT INTO exibicao(fk_evento, data_exibicao, horario, sequencia) VALUES (1, '2025-06-02', '20:00:00', 2);
INSERT INTO exibicao(fk_evento, data_exibicao, horario, sequencia) VALUES (2, '2025-06-05', '19:00:00', 1);

INSERT INTO atracao(fk_exibicao, nome, principal) VALUES (1, 'Elba Ramalho', TRUE);
INSERT INTO atracao(fk_exibicao, nome, principal) VALUES (1, 'Forro do Bom', FALSE);
INSERT INTO atracao(fk_exibicao, nome, principal) VALUES (2, 'Wesley Safadao', TRUE);
INSERT INTO atracao(fk_exibicao, nome, principal) VALUES (3, 'Cordel do Fogo Encantado', TRUE);

INSERT INTO locais_de_interesse(nome, resumo, endereco, latitude, longitude, link_imagem, dias_funcionamento, icone, horario_inicio, horario_fim) VALUES ('Museu do Forro', 'Museu dedicado a historia do forro em Caruaru', 'Rua Sao Joao, 123', -8.2825, -35.9721, 'https://exemplo.com/museu.jpg', 'Seg-Dom', 'museu.png', '09:00:00', '20:00:00');
INSERT INTO locais_de_interesse(nome, resumo, endereco, latitude, longitude, link_imagem, dias_funcionamento, icone, horario_inicio, horario_fim) VALUES ('Parque das Esculturas', 'Parque com esculturas de artistas locais', 'Av. Central, 456', -8.2840, -35.9705, 'https://exemplo.com/parque.jpg', 'Todos os dias', 'parque.png', '08:00:00', '20:00:00');
INSERT INTO locais_de_interesse(nome, resumo, endereco, latitude, longitude, link_imagem, dias_funcionamento, icone, horario_inicio, horario_fim) VALUES ('Feira de Artesanato', 'Feira tradicional com artesanato local', 'Praca Principal', -8.2832, -35.9710, 'https://exemplo.com/feira.jpg', 'Qua-Dom', 'feira.png', '07:00:00', '17:00:00');

INSERT INTO tags(nome) VALUES ('Cultural');
INSERT INTO tags(nome) VALUES ('Historico');
INSERT INTO tags(nome) VALUES ('Arte');
INSERT INTO tags(nome) VALUES ('Gastronomia');
INSERT INTO tags(nome) VALUES ('Turismo');
INSERT INTO tags(nome) VALUES ('Comercial');

INSERT INTO locaistags(fk_local, fk_tag) VALUES (1,1);
INSERT INTO locaistags(fk_local, fk_tag) VALUES (1,2);
INSERT INTO locaistags(fk_local, fk_tag) VALUES (2,1);
INSERT INTO locaistags(fk_local, fk_tag) VALUES (2,3);
INSERT INTO locaistags(fk_local, fk_tag) VALUES (3,4);
INSERT INTO locaistags(fk_local, fk_tag) VALUES (3,6);

INSERT INTO comidas(descricao, data_comida, horario, latitude, longitude, resumo) VALUES ('Canji')