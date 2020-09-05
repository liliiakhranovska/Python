import fake_data
import sys
import os
sys.path.append(os.path.join(sys.path[0], '../domain'))
from flask import jsonify
from flask import Flask
app = Flask(__name__)

@app.route("/games/<int:id>", methods=['GET'])
def show_user_profile(id):
    if id ==32:
        return jsonify(fake_data.board, fake_data.moves_counter, fake_data.next_player)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)

    