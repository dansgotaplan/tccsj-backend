# ORDEM DAS ROTAS:
# 1. EVENTOS
# 2. EXIBIÇÕES
# 3. ATRAÇÕES
# 4. LOCAIS DE INTERESSE
# 5. COMIDAS
# 6. HOMENAGEADOS

# IMPORTANTE: Manter a ordem correta para manter a clareza e organização do código.

import mysql.connector
from flask import Flask, make_response, jsonify, request

#- AMBIENTE EXPERIMENTAL -

app = flask(__name__)
cnx = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="aluno",
    database="tccsjdb"
)

#----- LEITURA (GET) -----
@app.route("/")
def homepage():
    return "API está funcionando, você está na homepage"

@app.route("/admin")
def admin_home():
    return "Você está na página homepage de administração"

@app.route("admin/eventos", methods=['GET'])
def listar_eventos():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM evento')
    rows = cursor.fetchall()
    cursor.close()
    eventos = []
    for row in rows:
        eventos.append({
            'cod': row[0],
            'descricao': row[1],
            'endereco': row[2],
            'latitude': row[3],
            'longitude': row[4],
            'resumo': row[5],
            'data_inicio': row[6],
            'data_encerramento': row[7]
        })
    return make_response(jsonify(eventos))

@app.route("/admin/exibicoes", methods=['GET'])
def listar_exibicoes():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM exibicao')
    rows = cursor.fetchall()
    cursor.close()
    exibicoes = []
    for row in rows:
        exibicoes.append({
            'cod': row[0],
            'fk_evento': row[1],
            'data_exibicao': row[2],
            'horario': row[3],
            'sequencia': row[4]
        })
    return make_response(jsonify(exibicoes))

@app.route("/admin/atracoes", methods=['GET'])
def listar_atracoes():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM atracao')
    rows = cursor.fetchall()
    cursor.close()
    atracoes = []
    for row in rows:
        atracoes.append({
            'cod': row[0],
            'fk_exibicao': row[1],
            'nome': row[2],
            'principal': row[3]
        })
    return make_response(jsonify(atracoes))

@app.route("/admin/locais-de-interesse", methods=['GET'])
def listar_locais_interesse():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM locais_de_interesse')
    rows = cursor.fetchall()
    cursor.close()
    locais = []
    for row in rows:
        locais.append({
            'cod': row[0],
            'descricao': row[1],
            'resumo': row[2],
            'endereco': row[3],
            'latitude': row[4],
            'longitude': row[5],
            'link_imagem': row[6],
            'dias_funcionamento': row[7],
            'icone': row[8],
            'horario_inicio': row[9],
            'horario_fim': row[10]
        })
    return make_response(jsonify(locais))

@app.route("admin/comidas", methods=['GET'])
def listar_homenageados():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM comidas')
    rows = cursor.fetchall()
    cursor.close()
    comidas = []
    for row in rows:
        comidas.append({
            'cod': row[0],
            'descricao': row[1],
            'data_comida': row[2],
            'horario': row[3],
            'endereco': row[4],
            'latitude': row[5],
            'longitude': row[6],
            'resumo': row[7],
        })
    return make_response(jsonify(comidas))

@app.route("admin/homenageados", methods=['GET'])
def listar_homenageados():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM homenageados')
    rows = cursor.fetchall()
    cursor.close()
    homenageados = []
    for row in rows:
        homenageados.append({
            'cod': row[0],
            'ano': row[1],
            'obras': row[2],
            'nome': row[3],
            'descricao': row[4]
        })
    return make_response(jsonify(homenageados))

@app.route("/admin/eventos/")

#----- EDIÇÃO (POST) -----

#-------------------------
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)