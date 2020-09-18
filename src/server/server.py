import os
import sys
import json
from flask import Flask, abort, jsonify, Response
import gateway
import default_board
import players

sys.path.append(os.path.join(sys.path[0], '../domain'))
app = Flask(__name__)

def convert_GameState_instance_to_json(instance):
    board = instance.board
    moves_counter = instance.moves_counter
    next_player = instance.next_player
    json_board = list(map(lambda row: list(map(lambda cell: {'piece': cell[0], 'colour': cell[1]} if cell != None else cell, row)), board))
    return {'board': json_board, 'moves_counter': moves_counter, 'next_player': next_player}

@app.route("/games/<int:id>", methods=['GET'])
def show_game_status(id):
    if gateway.get_state_by_id(id) is not None:
        return convert_GameState_instance_to_json(gateway.get_state_by_id(id))
    else:
        abort(404)

@app.route("/games", methods=['POST'])
def create_new_game():
    id = gateway.post_new_game()
    return Response("{'Game_id': %s}" % (id), status=201, mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)
