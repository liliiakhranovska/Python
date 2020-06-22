import unittest
import default_board
import players
import chessset
import castling
import test_utils


class TestCastling(unittest.TestCase):

    def test_that_south_west_type_is_identified_correctly(self):
        board = test_utils.empty_board
        board[0][4] = (chessset.KING, players.WHITE_PLAYER)
        board[0][0] = (chessset.ROOK, players.WHITE_PLAYER)
        self.assertEqual(castling.c_type((0, 4), (0, 1), board), 'south_west')

    def test_that_north_west_type_is_identified_correctly(self):
        board = test_utils.empty_board
        board[0][4] = (chessset.KING, players.WHITE_PLAYER)
        board[0][7] = (chessset.ROOK, players.WHITE_PLAYER)
        self.assertEqual(castling.c_type((0, 4), (0, 6), board), 'north_west')

    def test_that_south_east_type_is_identified_correctly(self):
        board = test_utils.empty_board
        board[7][4] = (chessset.KING, players.BLACK_PLAYER)
        board[7][0] = (chessset.ROOK, players.BLACK_PLAYER)
        self.assertEqual(castling.c_type((7, 4), (7, 1), board), 'south_east')

    def test_that_north_east_type_is_identified_correctly(self):
        board = test_utils.empty_board
        board[7][4] = (chessset.KING, players.BLACK_PLAYER)
        board[7][7] = (chessset.ROOK, players.BLACK_PLAYER)
        self.assertEqual(castling.c_type((7, 4), (7, 6), board), 'north_east')

    def test_that_castling_can_not_be_done_if_it_is_not_the_first_move_for_king(self):
        board = test_utils.empty_board
        board[0][4] = (chessset.KING, players.WHITE_PLAYER)
        board[0][7] = (chessset.ROOK, players.WHITE_PLAYER)
        self.assertFalse(castling.check ((0,4), (0,1), board, True, False, False, False, False, False))

    def test_that_castling_can_not_be_done_if_it_is_not_the_first_move_for_rook(self):
        board = test_utils.empty_board
        board[0][4] = (chessset.KING, players.WHITE_PLAYER)
        board[0][7] = (chessset.ROOK, players.WHITE_PLAYER)
        self.assertFalse(castling.check ((0,4), (0,6), board, False, False, False, True, False, False))

    def test_that_castling_can_not_be_done_if_there_is_a_piece_between_king_and_rook(self):
        board = test_utils.empty_board
        board[7][4] = (chessset.KING, players.BLACK_PLAYER)
        board[7][2] = (chessset.BISHOP, players.BLACK_PLAYER)
        board[7][0] = (chessset.ROOK, players.BLACK_PLAYER)
        self.assertFalse(castling.check ((7,4), (7,1), board, False, False, False, False, False, False))


if __name__ == '__main__':
    unittest.main()
