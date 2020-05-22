import sys
sys.path.append('/Users/lilia/Documents/PythonGame/Python_Game/src/domain') 

import boards
import players
import chessset
import bishop


def test_that_bishop_can_attack_opponent_piece():
  board = boards.empty_board()
  board[1][4] = (chessset.BISHOP, players.BLACK_PLAYER)
  board[3][2] = (chessset.BISHOP, players.WHITE_PLAYER)

  actual_result = bishop.try_to_move((1, 4), (3, 2), board)
  return actual_result == True

print (test_that_bishop_can_attack_opponent_piece())