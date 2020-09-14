from flask import Flask, abort, jsonify, Response
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
    if gateway.get_state_by_id(id) is not None:
        return jsonify(gateway.get_state_by_id(id))
    else:
        abort(404)

@app.route("/games", methods=['POST'])
def create_game():
    if gateway.new_game():
        return Response('Game %s is created' % (gateway.new_game()), status=201, mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)