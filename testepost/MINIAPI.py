from flask import Flask, make_response, jsonify, request
import mysql.connector

cnx = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="tccsjtests"
)

app = Flask(__name__)

def sevazio(result):
    if len(results) == 0:
        results = []
        results['status'] = 'GET FAIL - NO RESULTS'
        return make_resonse(jsonify(results))

@app.route('/admin/eventos', methods=['GET', 'POST'])
def listar_eventos():
    cursor = cnx.cursor()
    results = []
    if request.method == 'POST':
        missing = {}
        package = []
        data = request.get_json()
        if data['nome']: package['nome'] = data['endereco']
        else: missing.append('nome')
        if data['endereco']: package['endereco'] = data['endereco']
        if data['latitude']: package['latitude'] = data['latitude']
        else: missing.append('latitude')
        if data['longitude']: package['longitude'] = data['longitude']
        else: missing.append('longitude')
        if data['resumo']: package['resumo'] = data['resumo']
        if data['data_inicio']: package['data_inicio'] = data['data_inicio']
        else: missing.append('data_inicio')
        if data['data_fim']: package['data_fim'] = data['data_fim']
        if len(missing) != 0:
            results['status'] = 'POST SUCCESSFUL'
            for key in package:
                cursor.execute(f'INSERT INTO evento({key}) VALUES ({package[key]})')
                cursor.commit()
            cursor.close()
            return make_response(jsonify(results))
        else:
            results['status'] = 'POST FAIL - MISSING ITEMS'
            results['missing_items'] = missing
            cursor.close()
            return make_response(jsonify(results))
    else:
        cursor.execute('SELECT * FROM evento')
        rows = cursor.fetchall()
        results['status'] = 'GET SUCCESSFUL'
        for row in rows:
            results.append({
                'cod': row[0],
                'nome': row[1],
                'endereco': row[2],
                'latitude': row[3],
                'longitude': row[4],
                'resumo': row[5],
                'data_inicio': row[6],
                'data_fim': row[7]
            })
        sevazio(results)
        return make_response(jsonify(results))
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)