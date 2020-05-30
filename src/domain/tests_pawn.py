import unittest
import default_board
import players
import chessset
import pawn
import test_utils


class TestPawn(unittest.TestCase):

    def test_that_pawn_can_attack_opponent_piece(self):
        board = test_utils.empty_board
        board[3][3] = (chessset.PAWN, players.WHITE_PLAYER)
        board[4][2] = (chessset.BISHOP, players.BLACK_PLAYER)
        self.assertTrue(pawn.try_to_move((3, 3), (4, 2), board))

    def test_that_pawn_cant_attack_piece_the_same_color(self):
        board = test_utils.empty_board
        board[5][6] = (chessset.PAWN, players.WHITE_PLAYER)
        board[6][5] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertFalse(pawn.try_to_move((5, 6), (6, 5), board))

    def test_that_pawn_cant_move_either_point_if_the_next_piece_is_occupied_with_the_same_color(self):
        board = test_utils.empty_board
        board[5][6] = (chessset.PAWN, players.WHITE_PLAYER)
        board[6][6] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertFalse(pawn.try_to_move((5, 6), (6, 6), board))

    def test_that_pawn_cant_move_either_point_if_the_next_piece_is_occupied_with_the_other_color(self):
        board = test_utils.empty_board
        board[5][6] = (chessset.PAWN, players.WHITE_PLAYER)
        board[6][6] = (chessset.BISHOP, players.BLACK_PLAYER)
        self.assertFalse(pawn.try_to_move((5, 6), (6, 6), board))

    def test_that_white_pawn_can_jump_one_piece_if_the_first_move(self):
        board = test_utils.empty_board
        board[1][4] = (chessset.PAWN, players.WHITE_PLAYER)
        self.assertTrue(pawn.try_to_move((1, 4), (3, 4), board))

    def test_that_black_pawn_can_jump_one_piece_if_the_first_move(self):
        board = test_utils.empty_board
        board[6][4] = (chessset.PAWN, players.BLACK_PLAYER)
        self.assertTrue(pawn.try_to_move((6, 4), (4, 4), board))

    def test_that_white_pawn_cannt_jump_over__piece_if_the_first_move(self):
        board = test_utils.empty_board
        board[1][4] = (chessset.PAWN, players.WHITE_PLAYER)
        board[2][4] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertFalse(pawn.try_to_move((1, 4), (3, 4), board))

    def test_that_black_pawn_cannt_jump_over__piece_if_the_first_move(self):
        board = test_utils.empty_board
        board[6][3] = (chessset.PAWN, players.BLACK_PLAYER)
        board[5][3] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertFalse(pawn.try_to_move((6, 3), (4, 3), board))

    def test_that_pawn_cannt_move_to_the_same_piece(self):
        board = test_utils.empty_board
        board[7][0] = (chessset.PAWN, players.WHITE_PLAYER)
        self.assertFalse(pawn.try_to_move((7, 0), (7, 0), board))

    def test_that_white_pawn_can_move(self):
        board = test_utils.empty_board
        board[2][6] = (chessset.PAWN, players.WHITE_PLAYER)
        self.assertTrue(pawn.try_to_move((2, 6), (3, 6), board))

    def test_that_black_pawn_can_move(self):
        board = test_utils.empty_board
        board[2][6] = (chessset.PAWN, players.BLACK_PLAYER)
        self.assertTrue(pawn.try_to_move((2, 6), (1, 6), board))


if __name__ == '__main__':
    unittest.main()
