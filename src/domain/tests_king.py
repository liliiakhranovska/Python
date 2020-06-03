import unittest
import default_board
import players
import chessset
import king
import test_utils


class TestKing(unittest.TestCase):

    def test_that_king_cant_move_either_point_if_sourrounded_by_the_same_color(self):
        board = test_utils.empty_board
        board[5][4] = (chessset.KING, players.BLACK_PLAYER)
        board[4][3] = (chessset.BISHOP, players.BLACK_PLAYER)
        board[4][4] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[4][5] = (chessset.ROOK, players.BLACK_PLAYER)
        board[5][3] = (chessset.BISHOP, players.BLACK_PLAYER)
        board[5][5] = (chessset.PAWN, players.BLACK_PLAYER)
        board[6][3] = (chessset.PAWN, players.BLACK_PLAYER)
        board[6][4] = (chessset.PAWN, players.BLACK_PLAYER)
        board[6][5] = (chessset.PAWN, players.BLACK_PLAYER)
        self.assertFalse(king.try_to_move((5, 4), (6, 3), board))

    def test_that_king_can_attack_opponent_piece(self):
        board = test_utils.empty_board
        board[1][4] = (chessset.KING, players.BLACK_PLAYER)
        board[2][3] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(king.try_to_move((1, 4), (2, 3), board))

    def test_that_king_cant_attack_piece_the_same_color(self):
        board = test_utils.empty_board
        board[3][6] = (chessset.KING, players.WHITE_PLAYER)
        board[4][7] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertFalse(king.try_to_move((3, 6), (4, 7), board))

    def test_that_king_cannt_jump_over_square(self):
        board = test_utils.empty_board
        board[6][2] = (chessset.KING, players.WHITE_PLAYER)
        self.assertFalse(king.try_to_move((6, 2), (4, 2), board))

    def test_that_king_cannt_move_to_the_same_piece(self):
        board = test_utils.empty_board
        board[7][0] = (chessset.KING, players.WHITE_PLAYER)
        self.assertFalse(king.try_to_move((7, 0), (7, 0), board))

    def test_that_king_can_move_from_corner(self):
        board = test_utils.empty_board
        board[0][0] = (chessset.KING, players.BLACK_PLAYER)
        self.assertTrue(king.try_to_move((0, 0), (1, 0), board))

    def test_that_king_can_move_right(self):
        board = test_utils.empty_board
        board[4][0] = (chessset.KING, players.BLACK_PLAYER)
        self.assertTrue(king.try_to_move((4, 0), (4, 1), board))

    def test_that_king_can_move_left(self):
        board = test_utils.empty_board
        board[4][3] = (chessset.KING, players.BLACK_PLAYER)
        self.assertTrue(king.try_to_move((4, 3), (4, 2), board))

    def test_that_king_can_move_up(self):
        board = test_utils.empty_board
        board[4][3] = (chessset.KING, players.BLACK_PLAYER)
        self.assertTrue(king.try_to_move((4, 3), (3, 3), board))

    def test_that_king_can_move_down(self):
        board = test_utils.empty_board
        board[4][3] = (chessset.KING, players.BLACK_PLAYER)
        self.assertTrue(king.try_to_move((4, 3), (5, 3), board))

    def test_that_king_can_move_north_east(self):
        board = test_utils.empty_board
        board[4][3] = (chessset.KING, players.BLACK_PLAYER)
        self.assertTrue(king.try_to_move((4, 3), (5, 4), board))

    def test_that_king_can_move_south_east(self):
        board = test_utils.empty_board
        board[4][3] = (chessset.KING, players.BLACK_PLAYER)
        self.assertTrue(king.try_to_move((4, 3), (5, 2), board))

    def test_that_king_can_move_south_west(self):
        board = test_utils.empty_board
        board[4][3] = (chessset.KING, players.BLACK_PLAYER)
        self.assertTrue(king.try_to_move((4, 3), (3, 2), board))

    def test_that_king_can_move_north_west(self):
        board = test_utils.empty_board
        board[4][3] = (chessset.KING, players.BLACK_PLAYER)
        self.assertTrue(king.try_to_move((4, 3), (3, 4), board))


if __name__ == '__main__':
    unittest.main()
