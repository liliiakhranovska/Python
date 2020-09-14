import sys
import os
sys.path.append(os.path.join(sys.path[0], '../domain'))
import default_board
import players


class BoardGame:
    def __init__(self, 
                board = list(map(lambda row: list(map(lambda cell: {'piece': cell[0], ' colour': cell[1]} if cell != None else cell, row)), default_board.default_board())), 
                moves_counter = 0, 
                next_player = players.WHITE_PLAYER):
        self.board = board
        self.moves_counter = moves_counter
        self.next_player = next_player

__db = {32: BoardGame()}

def get_state_by_id(id):
    if id in __db:
        return __db[id].board, __db[id].moves_counter, __db[id].next_player
    else:
        return None

def new_game():
    __db[max(__db.keys())+1] = BoardGame()
    return max(__db.keys())