import unittest
import default_board
import players
import chessset
import queen
import test_utils


class TestBishop(unittest.TestCase):

    def test_that_queen_can_attack_opponent_piece(self):
        board = test_utils.empty_board
        board[1][4] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[3][2] = (chessset.QUEEN, players.WHITE_PLAYER)
        self.assertTrue(queen.try_to_move((1, 4), (3, 2), board))

    def test_that_queen_cant_attack_piece_the_same_color(self):
        board = test_utils.empty_board
        board[1][4] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[3][2] = (chessset.BISHOP, players.BLACK_PLAYER)
        self.assertFalse(queen.try_to_move((1, 4), (3, 2), board))

    def test_that_queen_cant_move_either_point_if_sourrounded_by_the_same_color(self):
        board = test_utils.empty_board
        board[2][3] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[3][2] = (chessset.BISHOP, players.BLACK_PLAYER)
        board[1][2] = (chessset.ROOK, players.BLACK_PLAYER)
        board[1][4] = (chessset.BISHOP, players.BLACK_PLAYER)
        board[3][4] = (chessset.PAWN, players.BLACK_PLAYER)
        self.assertFalse(queen.try_to_move((2, 3), (4, 5), board))

    def test_that_queen_cant_jump_over_piece(self):
        board = test_utils.empty_board
        board[5][2] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[3][4] = (chessset.ROOK, players.BLACK_PLAYER)
        self.assertFalse(queen.try_to_move((5, 2), (1, 6), board))

    def test_that_queen_can_cross_whole_board_diagonal(self):
        board = test_utils.empty_board
        board[7][0] = (chessset.QUEEN, players.BLACK_PLAYER)
        self.assertTrue(queen.try_to_move((7, 0), (0, 7), board))

    def test_that_queen_can_cross_whole_board_straight(self):
        board = test_utils.empty_board
        board[5][7] = (chessset.QUEEN, players.BLACK_PLAYER)
        self.assertTrue(queen.try_to_move((5, 7), (5, 0), board))

    def test_that_queen_can_move_north_east(self):
        board = test_utils.empty_board
        board[5][4] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[3][6] = (chessset.QUEEN, players.WHITE_PLAYER)
        board[2][1] = (chessset.ROOK, players.BLACK_PLAYER)
        board[7][2] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(queen.try_to_move((5, 4), (7, 6), board))

    def test_that_queen_can_move_south_east(self):
        board = test_utils.empty_board
        board[5][4] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[3][6] = (chessset.ROOK, players.WHITE_PLAYER)
        board[2][1] = (chessset.KNIGHT, players.BLACK_PLAYER)
        board[7][2] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(queen.try_to_move((5, 4), (6, 3), board))

    def test_that_queen_can_move_south_west(self):
        board = test_utils.empty_board
        board[5][4] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[3][6] = (chessset.BISHOP, players.WHITE_PLAYER)
        board[2][1] = (chessset.ROOK, players.BLACK_PLAYER)
        board[7][2] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(queen.try_to_move((5, 4), (3, 2), board))

    def test_that_queen_can_move_north_west(self):
        board = test_utils.empty_board
        board[5][4] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[3][6] = (chessset.BISHOP, players.WHITE_PLAYER)
        board[2][1] = (chessset.ROOK, players.BLACK_PLAYER)
        board[7][2] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(queen.try_to_move((5, 4), (4, 5), board))

    def test_that_queen_can_move_north(self):
        board = test_utils.empty_board
        board[5][4] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[5][7] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(queen.try_to_move((5, 4), (5, 6), board))

    def test_that_queen_can_move_east(self):
        board = test_utils.empty_board
        board[5][4] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[5][7] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(queen.try_to_move((5, 4), (7, 4), board))

    def test_that_queen_can_move_south(self):
        board = test_utils.empty_board
        board[5][4] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[5][0] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(queen.try_to_move((5, 4), (5, 1), board))

    def test_that_queen_can_move_west(self):
        board = test_utils.empty_board
        board[5][4] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[5][0] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(queen.try_to_move((5, 4), (2, 4), board))

    def test_that_queen_can_move_north(self):
        board = test_utils.empty_board
        board[5][4] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[5][0] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(queen.try_to_move((5, 4), (5, 7), board))


if __name__ == '__main__':
    unittest.main()
