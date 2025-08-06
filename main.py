from flask import Flask, make_response, jsonify, request
import mysql.connector

app = Flask(__name__)
cnx = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="aluno", #!!! colocar senha dps de acordo com o MySQL Workbench
    database="tccsjdb"
)

@app.route("/admin") #homepage do adm
def homepage ():
    return "API está funcionando, você está na homepage"

@app.route("/admin/r-eventos", methods=['GET'])
def lertudo():
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
    #return make_response(jsonify (eventos))
    return make_response(eventos)

#@app.route("/admin/create")

#@app.route("/admin/update")

#@app.route("/admin/delete")

if __name__ == "__main__": #deixar no FINAL. roda o app
    app.run(host='0.0.0.0', port=5000, debug=True)