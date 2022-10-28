from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

nomes = [
    {
        'id': 1,
        'nome': 'Gabriel',
        'sobrenome': 'Carvalho'
    },
    {
        'id': 2,
        'nome': 'Rafael',
        'sobrenome': 'Antônio'
    },
    {
        'id': 3,
        'nome': 'Rosenice',
        'sobrenome': 'Silva'
    }
]

@app.route('/')

def obter_nomes():
    return jsonify(nomes)

app.run(port=5000, host='localhost', debug=True)