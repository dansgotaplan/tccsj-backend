#TESTE DA ROTA DE LOCAIS DE INTERESSE INTEGRADO COM TAGS

# Instruções

1. Verifique se tem as seguintes bibliotecas instaladas: flask, mysql-connector-python.
2. Instale o Postman Desktop Agent para teste de APIs REST.
3. Crie uma database no MySQL Workbench com os comandos encontrados em MINIDB.sql, nesta mesma pasta.
4. Alimente o DB com os comandos encontrados em MINIFEED.sql, nesta mesma pasta.
5. Substitua os dados em MINIAPI.py pelos seus dados de acesso ao MySQL.
6. Execute MINIAPI.py, acesse a URL com a rota /admin/locais-de-interesse/1 e cheque o resultado.

# Resultado Esperado (Output da API GET)

[
    {
        'cod': 1,
        'descricao': 'Feira de Caruaru',
        'resumo': 'A Feira de Caruaru, localizada no Parque 18 de Maio, é uma das maiores feiras ao ar livre da América Latina e um importante símbolo cultural do Nordeste.',
        'endereco'; 'Av. Lourival José da Silva - Petrópolis, Caruaru-PE, 55030-200',
        'latitude': -8.289007
        'longitude': -35.972379
        'link_image': 'https://www.sindloja.com.br/webfile/imagesno/1027x535preenchimento100-20170605_593564c79a902.jpg'
        'dias_funcionamento': 'Todos os dias',
        'icone': 'https://cdn-icons-png.flaticon.com/512/2037/2037749.png'
        'horario_inicio': '0:00:00'
        'horario_fim': '23:59:59'
        'tags': [
            'Cultural',
            'Comércio'
        ]
    }
]
