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
  cursor.close()
  for row in rows:
   results.append({
    'cod' : row[0],
    'id' : row[1],
    'nome' : row[2],
    'descricao' : row[3],
    'dia': str(row [4]),
    'horario' : str(row[5]),
    'endereco' : row[6],
    'latitude' : row[7],
    'longitude' : row[8]
   })
  return make_response(jsonify(results))
 elif request.method == 'POST':
  return 'OK'

@app.route('/polo', methods=['GET', 'POST'])
def polo():
 if request.method == 'GET':
  results = []
  cursor = cnx.cursor()
  cursor.execute('SELECT * FROM polo')
  rows = cursor.fetchall()
  for row in rows:
   results.append({
    'cod' : row[0],
    'id' : row[1],
    'nome' : row[2],
    'descricao' : row[3],
    'inicio' : str(row[4]),
    'fim' : str(row[5]),
    'endereco' : row[6],
    'latitude' : float(row[7]),
    'longitude' : float(row[8]),
    'ismultilocal' : row[9]
   })
   return make_response(jsonify(results))
 elif request.method == 'POST':
  return 'OK'
 
@app.route('/exibicao', methods=['GET', 'POST'])
def exibicao():
 if request.method == 'GET':
  results = []
  cursor = cnx.cursor()
  cursor.execute('SELECT * FROM exibicao')
  rows = cursor.fetchall()
  cursor.close()
  for row in rows:
   results.append({
    'cod' : row[0],
    'ordem' : row[1],
    'fkpolo' : row[2],
    'dia' : str(row[3]),
    'horario' : str(row[4]),
    'endereco' : row[5],
    'latitude' : float(row[6]),
    'longitude' : float(row[7])
   })
  return make_response(jsonify(results))
 elif request.method == 'POST':
  return 'OK'
 
@app.route('/atracao', methods=['GET', 'POST'])
def atracao():
 if request.method == 'GET':
  results  = []
  cursor = cnx.cursor()
  cursor.execute('SELECT * FROM atracao')
  rows = cursor.fetchall()
  for row in rows:
   results.append({
    'cod' : row[0],
    'ordem' : row[1],
    'fkexibicao' : row[2],
    'nome' : row[3],
    'descricao' : row[4],
    'principal' : row[5]
   })
  return make_response(jsonify(results))
 elif request.method == 'POST':
  return 'OK'

@app.route('/locais', methods=['GET', 'POST'])
def locais():
 if request.method == 'GET':
  results  = []
  cursor = cnx.cursor()
  cursor.execute('SELECT * FROM locais')
  rows = cursor.fetchall()
  for row in rows:
   results.append({
    'cod' : row[0],
    'id' : row[1],
    'nome' : row[2],
    'descricao' : row[3],
    'dias' : row[4],
    'inicio' : str(row[5]),
    'fim' : str(row[6]),
    'endereco' : row[7],
    'latitude' : float(row[8]),
    'longitude' : float(row[9]),
    'urlimage' : row[10],
    'urlicone' : row[11]
   })
  return make_response(jsonify(results))
 elif request.method == 'POST':
  return 'OK'
 
@app.route('/pessoa', methods=['GET', 'POST'])
def pessoa():
 if request.method == 'GET':
  results  = []
  cursor = cnx.cursor()
  cursor.execute('SELECT * FROM pessoa')
  rows = cursor.fetchall()
  for row in rows:
   results.append({
    'cod' : row[0],
    'id' : row[1],
    'nome' : row[2],
    'descricao' : row[3],
    'obras' : row[4],
    'nascido' : row[5],
    'morte' : row[6],
    'ishomenageado' : row[7],
    'anohomenagem' : row[8]
   })
  return make_response(jsonify(results))
 elif request.method == 'POST':
  return 'OK'
 
@app.route('/tag', methods=['GET', 'POST'])
def tag():
 if request.method == 'GET':
  results  = []
  cursor = cnx.cursor()
  cursor.execute('SELECT * FROM tag')
  rows = cursor.fetchall()
  for row in rows:
   results.append({
    'cod' : row[0],
    'id' : row[1],
    'nome' : row[2] 
   })
  return make_response(jsonify(results))
 elif request.method == 'POST':
  return 'OK'
 
@app.route('/usuario', methods=['GET', 'POST'])
def usuario():
 if request.method == 'GET':
  results  = []
  cursor = cnx.cursor()
  cursor.execute('SELECT * FROM usuario')
  rows = cursor.fetchall()
  for row in rows:
   results.append({
    'cod' : row[0],
    'email' : row[1],
    'senha' : row[2],
    'isadmin' : row[3]
   })
  return make_response(jsonify(results))
 elif request.method == 'POST':
  return 'OK'

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000, debug=True)