from flask import Flask, request, jsonify, make_response
import mysql.connector

app = Flask(__name__)

cnx = mysql.connector.connect(
 host='127.0.0.1',
 user='root',
 password='aluno',
 database='tccsj'
)

@app.route('/', methods=['GET'])
def homepage():
 return "API está funcionando, você está na homepage"

@app.route('/evento', methods=['GET', 'POST'])
def evento():
 if request.method == 'GET':
  results = []
  cursor = cnx.cursor()
  cursor.execute("SELECT * FROM evento")
  rows = cursor.fetchall()
  for row in rows:
   results.append({
    'cod' : row[0],
    'id' : row[1],
    'nome' : row[2],
    'descricao' : row[3],
    'dia': row [4],
    'horario' : row[5],
    'endereco' : row[6],
    'latitude' : row[7],
    'longitude' : row[8]
   })
  return make_response(jsonify(results))
 elif request.method == 'POST':
  return 'OK'
 
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000, debug=True)