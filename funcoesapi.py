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

#----- Primeira Camada -----

@app.route("/")
def homepage():
    return "API está funcionando, você está na homepage"

@app.route("/admin")
def admin_home():
    return "Você está na página homepage de administração"

@app.route("/admin/comidas", methods=['GET'])
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

@app.route("/admin/homenageados", methods=['GET'])
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

@app.route("/admin/usuarios", methods=['GET'])
def listar_usuarios():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM usuario')
    rows = cursor.fetchall()
    cursor.close()
    usuarios = []
    for row in rows:
        usuarios.append({
            'cod': row[0],
            'email': row[1],
            'senha': row[2],
            'nivel_de_acesso': row[3]
        })
    return make_response(jsonify(usuarios))

@app.route("/admin/eventos/new")
def vazio():
    return 'vazio, por enquanto'
#-------------------------
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)