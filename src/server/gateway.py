import sys
import os
sys.path.append(os.path.join(sys.path[0], '../domain'))
import default_board
import players

board = default_board.default_board()
moves_counter = 157
next_player = players.WHITE_PLAYER

db = {32:{'board': list(map(lambda row: list(map(lambda cell: {'piece': cell[0], ' colour': cell[1]} if cell != None else cell, row)), board)), 'moves_counter': moves_counter, 'next_player' : next_player}}
