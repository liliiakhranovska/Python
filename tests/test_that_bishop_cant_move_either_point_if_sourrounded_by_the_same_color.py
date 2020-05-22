import sys
sys.path.append('/Users/lilia/Documents/PythonGame/Python_Game/src/domain') 

import boards
import players
import chessset
import bishop

def test_that_bishop_cant_move_either_point_if_sourrounded_by_the_same_color():
  board = boards.empty_board()
  board[2][3] = (chessset.BISHOP, players.BLACK_PLAYER)
  board[3][2] = (chessset.QUEEN, players.BLACK_PLAYER)
  board[1][2] = (chessset.ROOK, players.BLACK_PLAYER)
  board[1][4] = (chessset.BISHOP, players.BLACK_PLAYER)
  board[3][4] = (chessset.PAWN, players.BLACK_PLAYER)

  actual_result = bishop.try_to_move((2, 3), (4, 5), board)
  return actual_result == False

print (test_that_bishop_cant_move_either_point_if_sourrounded_by_the_same_color())
