import fake_data
import sys
import os
sys.path.append(os.path.join(sys.path[0], '../domain'))
from flask import jsonify
from flask import Flask
from flask import abort
app = Flask(__name__)

@app.route("/games/<int:id>", methods=['GET'])
def show_user_profile(id):
    if id ==32:
        return jsonify(board = fake_data.board, moves_counter = fake_data.moves_counter, next_player = fake_data.next_player)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)

    