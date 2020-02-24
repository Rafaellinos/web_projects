from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}}) # to flask acceptep any origin

BOOKS = [
    {
        'id': 1,
        'title': 'Caixa de Pássaros',
        'score': 6,
        'readed': True,
    },
    {
        'id': 2,
        'title': 'LOVECRAFT Contos vol1',
        'score': 8,
        'readed': False,
    },
    {
        'id': 3,
        'title': 'A Noite dos Mortos Vivos',
        'score': 9,
        'readed': True,
    },
    {
        'id': 4,
        'title': 'Apocalipse Z O princípio do fim',
        'score': 10,
        'readed': True,
    }
]

@app.route('/books', methods=['GET','POST'])
def ping_pong():
    if request.method == 'POST':
        return jsonify("POST")
    else:
        return jsonify(BOOKS)


if __name__ == '__main__':
    app.run(debug=True)