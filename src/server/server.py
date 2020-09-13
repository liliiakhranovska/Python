from flask import abort
from flask import Flask
from flask import jsonify
from flask import Response
import gateway
import default_board
import players
import sys
import os
import json
sys.path.append(os.path.join(sys.path[0], '../domain'))
app = Flask(__name__)


@app.route("/games/<int:id>", methods=['GET'])
def show_game_status(id):
    if id in gateway.db:
        return jsonify(gateway.db[id])
    else:
        abort(404)

@app.route("/games", methods=['POST'])
def create_game():
    gateway.db[max(gateway.db.keys())+1] = {'board': list(map(lambda row: list(map(lambda cell: {'piece': cell[0], ' colour': cell[1]} if cell != None else cell, row)), default_board.default_board())), 'moves_counter': 0, 'next_player' : players.WHITE_PLAYER}
    return Response('New game is created', status=201, mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)
