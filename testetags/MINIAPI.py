import mysql.connector
from flask import Flask, jsonify, make_response

app = Flask(__name__)
cnx = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'tccsjtests'
)

@app.route('/admin/locais-de-interesse/<int cod_local>', methods=['GET'])
def listar_locais_cod(cod_local):
    cursor = cnx.cursor()
    cursor.execute('SELECT fk_tags FROM locaistags WHERE fl_locais = ', (cod_local,))
    chaves = cursor.fetchall()
    tags = []
    for chave in chaves:
        cursor.execute('SELECT nome FROM tags WHERE cod = ', (chave,))
        nomes = cursor.fetchall()
        for nome in nomes:
            tags.append(nome)
    cursor.execute('SELECT * FROM locais_de_interesse WHERE cod = ', (cod_local,))
    locais = []
    rows = cursor.fetchall()
    cursor.close()
    for row in rows:
        locais.append({
            'cod': row[0],
            'descricao': row[1],
            'resumo': row[2],
            'endereco': row[3],
            'latitude': row[4],
            'longitude': row[5]
            'link_imagem': row[6],
            'dias_funcionamento': row[7],
            'icone': row[8],
            'horario_inicio': row[9],
            'horario_fim': row[10],
            'tags': tags
        })
    return make_response(jsonify(locais))