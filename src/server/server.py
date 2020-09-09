import fake_data
import sys
import os
import json
sys.path.append(os.path.join(sys.path[0], '../domain'))
from flask import jsonify
from flask import Flask
from flask import abort
app = Flask(__name__)

@app.route("/games/<int:id>", methods=['GET'])
def show_user_profile(id):
    if id ==32:
        return jsonify(board = list(map(lambda row: list(map(lambda cell: {'piece': cell[0], ' color': cell[1]} if cell != None else cell, row)), fake_data.board)), moves_counter = fake_data.moves_counter, next_player = fake_data.next_player)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)