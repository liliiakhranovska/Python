import chessset
import players
import rook
import unittest

from  test_utils import empty_board


class TestRook(unittest.TestCase):

    def test_that_rook_can_attack_opponent_piece(self):
        board = empty_board
        board[0][0] = (chessset.ROOK, players.BLACK_PLAYER)
        board[0][6] = (chessset.ROOK, players.WHITE_PLAYER)
        self.assertTrue(rook.try_to_move((0, 0), (0, 6), board))

    def test_that_rook_cant_move_either_point_if_surrounded_by_the_same_color(self):
        board = empty_board
        board[0][0] = (chessset.ROOK, players.BLACK_PLAYER)
        board[3][2] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[4][0] = (chessset.KING, players.BLACK_PLAYER)
        board[6][4] = (chessset.BISHOP, players.BLACK_PLAYER)
        board[6][1] = (chessset.PAWN, players.BLACK_PLAYER)
        self.assertFalse(rook.try_to_move((0, 0), (2, 5), board))


if __name__ == '__main__':
    unittest.main()

    