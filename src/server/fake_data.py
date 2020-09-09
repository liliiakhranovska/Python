import sys
import os
sys.path.append(os.path.join(sys.path[0], '../domain'))
import default_board
import players

board = default_board.default_board()
moves_counter = 157
next_player = players.WHITE_PLAYER