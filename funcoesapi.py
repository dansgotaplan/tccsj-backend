#- AMBIENTE EXPERIMENTAL -
#--- FUNÇÕES PARA A API --

#--------- SETUP ---------
import mysql.connector
from flask import Flask, make_response, jsonify, request

app = flask(__name__)
cnx = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="aluno",
    database="tccsjdb"
)

#----- LEITURA (GET) -----
#----- EDIÇÃO (POST) -----

#-------------------------
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)