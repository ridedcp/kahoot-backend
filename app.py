from flask import Flask, request, jsonify

import os

app = Flask(__name__)

# Estructura de datos en memoria (simple para empezar)
games = {}

@app.route('/create_game', methods=['POST'])
def create_game():
    game_id = request.json.get('game_id')
    games[game_id] = {'participants': []}
    return jsonify({"message": "Game created", "game_id": game_id})

@app.route('/join_page/<game_id>', methods=['GET'])
def join_page(game_id):
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Unirse a la Partida</title>
    </head>
    <body>
        <h2>Introduce tu nombre para unirte a la partida</h2>
        <form action="/join_game/{}" method="POST">
            <input type="text" name="name" placeholder="Tu nombre" required>
            <button type="submit">Unirse</button>
        </form>
    </body>
    </html>
    '''.format(game_id)

@app.route('/get_participants/<game_id>', methods=['GET'])
def get_participants(game_id):
    if game_id not in games:
        return jsonify({"error": "Game not found"}), 404

    return jsonify({"participants": games[game_id]['participants']})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render asigna el puerto automáticamente
    app.run(host='0.0.0.0', port=port)

@app.route('/test_post', methods=['POST'])
def test_post():
    return jsonify({"message": "POST request successful"})
