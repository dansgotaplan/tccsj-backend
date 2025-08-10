# IMPORTANTE: Manter a ordem correta para manter a clareza e organização do código.

import mysql.connector
from flask import Flask, make_response, jsonify, request

#- AMBIENTE EXPERIMENTAL -

app = Flask(__name__)
cnx = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="aluno",
    database="tccsjdb"
)

def sevazio(results):
    if len(results) == 0:
        return 'Nenhum resultado encontrado.'

@app.route("/")
def homepage():
    return "API está funcionando, você está na homepage"

@app.route("/admin")
def admin_home():
    return "Você está na página homepage de administração"

@app.route("/admin/eventos", methods=['GET', 'POST'])
def listar_eventos():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM evento')
    rows = cursor.fetchall()
    cursor.close()
    results = []
    for row in rows:
        results.append({
            'cod': row[0],
            'descricao': row[1],
            'endereco': row[2],
            'latitude': row[3],
            'longitude': row[4],
            'resumo': row[5],
            'data_inicio': row[6],
            'data_fim': row[7]
        })
    sevazio(results)
    return make_response(jsonify(results))

@app.route("/admin/eventos/<int:i>", methods=['GET'])
def listar_eventos_cod(i):
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM evento WHERE cod = %s', (i,))
    results = []
    for row in rows:
        results.append({
            'cod': row[0],
            'descricao': row[1],
            'endereco': row[2],
            'latitude': row[3],
            'longitude': row[4],
            'resumo': row[5],
            'data_inicio': row[6],
            'data_fim': row[7]
        })
    sevazio(results)
    return make_response(jsonify(results))

@app.route("/admin/exibicoes", methods=['GET', 'POST'])
def listar_exibicoes():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM exibicao')
    results = []
    for row in rows:
        results.append({
            'cod': row[0],
            'fk_evento': row[1],
            'data_exibicao': row[2],
            'horario': row[3],
            'sequencia': row[4]
        })
    sevazio(results)
    return make_response(jsonify(results))

@app.route("/admin/exibicoes/<int:i>", methods=['GET'])
def listar_exibicoes_cod(i):
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM exibicao WHERE cod = %s', (i,))
    rows = cursor.fetchall()
    cursor.close()
    results = []
    for row in rows:
        results.append({
            'cod': row[0],
            'fk_evento': row[1],
            'data_exibicao': row[2],
            'horario': row[3],
            'sequencia': row[4]
        })
    sevazio(results)
    return make_response(jsonify(results))

@app.route("/admin/atracoes", methods=['GET', 'POST'])
def listar_atracoes():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM atracao')
    rows = cursor.fetchall()
    cursor.close()
    results = []
    for row in rows:
        results.append({
            'cod': row[0],
            'fk_exibicao': row[1],
            'nome': row[2],
            'principal': row[3]
        })
    sevazio(results)
    return make_response(jsonify(results))

@app.route("/admin/atracoes/<int:i>", methods=['GET'])
def listar_atracoes_cod(i):
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM atracao WHERE cod = %s', (i,))
    rows = cursor.fetchall()
    cursor.close
    results = []
    for row in rows:
        results.append({
            'cod': row[0],
            'fk_exibicao': row[1],
            'nome': row[2],
            'principal': row[3]
        })
    sevazio(results)
    return make_response(jsonify(results))

@app.route("/admin/locais-de-interesse", methods=['GET', 'POST'])
def listar_locais():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM locais_de_interesse')
    rows = cursor.fetchall()
    cursor.close()
    results = []
    for row in rows:
        results.append({
            'cod': row[0],
            'descricao': row[1],
            'resumo': row[2],
            'endereco': row[3],
            'latitude': row[4],
            'longitude': row[5],
            'link_image': row[6],
            'dias_funcionamento': row[7],
            'icone': row[8],
            'horario_inicio': row[9],
            'horario_fim': row[10]
        })
    sevazio(results)
    return make_response(jsonify(results))

@app.route("/admin/locais-de-interesse/<int:i>", methods=['GET'])
def listar_locais_cod(i):
    cursor = cnx.cursor()
    cursor.execute('SELECT fk_tag FROM locaistags WHERE fk_local = %s', (i,))
    chaves = cursor.fetchall()
    tags = []
    for chave in chaves:
        cursor.execute('SELECT nome FROM tags WHERE cod = %s', (chave[0]))
        nomes = cursor.fetchall()
        for nome in nomes:
            tags.append(nome[0])
    cursor.execute('SELECT * FROM locais_de_interesse WHERE cod = %s', (i,))
    results = []
    rows = cursor.fetchall()
    cursor.close()
    for row in rows:
        results.append({
            'cod': row[0],
            'descricao': row[1],
            'resumo': row[2],
            'endereco': row[3],
            'latitude': row[4],
            'longitude': row[5],
            'link_image': row[6],
            'dias_funcionamento': row[7],
            'icone': row[8],
            'horario_inicio': row[9],
            'horario_fim': row[10],
            'tags': tags
        })
    sevazio(results)
    return make_response(jsonify(results))

@app.route("/admin/tags", methods=['GET', 'POST'])
def listar_tags():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM tags')
    rows = cursor.fetchall()
    cursor.close()
    results = []
    for row in rows:
        results.append({
            'cod': row[0],
            'nome': row[1],
            'descricao': row[2]
        })
    sevazio(results)
    return make_response(jsonify(results))

@app.route("/admin/comidas", methods=['GET', 'POST'])
def listar_comidas():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM comidas')
    rows = cursor.fetchall()
    cursor.close()
    results = []
    for row in rows:
        results.append({
            'cod': row[0],
            'descricao': row[1],
            'data_comida': row[2],
            'horario': row[3],
            'endereco': row[4],
            'latitude': row[5],
            'longitude': row[6],
            'resumo': row[7],
        })
    sevazio(results)
    return make_response(jsonify(results))

@app.route("/admin/homenageados", methods=['GET', 'POST'])
def listar_homenageados():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM homenageados')
    rows = cursor.fetchall()
    cursor.close()
    results = []
    for row in rows:
        results.append({
            'cod': row[0],
            'ano': row[1],
            'obras': row[2],
            'nome': row[3],
            'descricao': row[4]
        })
    sevazio(results)
    return make_response(jsonify(results))

@app.route("/admin/usuarios", methods=['GET', 'POST'])
def listar_usuarios():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM usuario')
    rows = cursor.fetchall()
    cursor.close()
    results = []
    for row in rows:
        results.append({
            'cod': row[0],
            'email': row[1],
            'senha': row[2],
            'nivel_de_acesso': row[3]
        })
    sevazio(results)
    return make_response(jsonify(results))

#-------------------------
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)