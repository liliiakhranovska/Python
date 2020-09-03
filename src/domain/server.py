import fake_data
from flask import jsonify
from flask import Flask
app = Flask(__name__)

@app.route("/games/<int:id>", methods=['GET'])
def show_user_profile(id):
    if id ==32:
        return jsonify(fake_data.board, fake_data.moves_counter, fake_data.next_player)
    else:
        return 'Wrong gameID' 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)

    