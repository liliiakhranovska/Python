import os
import sys
sys.path.append(os.path.join(sys.path[0], '../domain'))
import default_board
import players


class GameState:
    def __init__(self, 
                board,
                moves_counter=0, 
                next_player=players.WHITE_PLAYER):
        if board == None:
            board = default_board.default_board()
        self.board = board
        self.moves_counter = moves_counter
        self.next_player = next_player

__db = {32: GameState(None)}

def get_state_by_id(id):
    return __db.get(id)

def post_new_game():
    __db[max(__db.keys())+1] = GameState(None)
    return max(__db.keys())