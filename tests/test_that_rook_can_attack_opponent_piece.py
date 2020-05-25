from src.domain.players import players
from src.domain.chessset import chessset
from src.domain.rook import rook
from src.domain.boards import boards


def test_that_rook_can_attack_opponent_piece():
  board = boards.empty_board()
  board[0][2] = (chessset.ROOK, players.BLACK_PLAYER)
  board[5][2] = (chessset.ROOK, players.WHITE_PLAYER)

  actual_result = rook.try_to_move((0, 2), (5, 2), board)
  return actual_result == True

print (test_that_rook_can_attack_opponent_piece())