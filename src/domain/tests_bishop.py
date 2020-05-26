import unittest
import boards
import players
import chessset
import bishop


class TestStringMethods(unittest.TestCase):

    def test_that_bishop_can_attack_opponent_piece(self):
        board = boards.empty_board()
        board[1][4] = (chessset.BISHOP, players.BLACK_PLAYER)
        board[3][2] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(bishop.try_to_move((1, 4), (3, 2), board))

    def test_that_bishop_cant_move_either_point_if_sourrounded_by_the_same_color(self):
        board = boards.empty_board()
        board[2][3] = (chessset.BISHOP, players.BLACK_PLAYER)
        board[3][2] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[1][2] = (chessset.ROOK, players.BLACK_PLAYER)
        board[1][4] = (chessset.BISHOP, players.BLACK_PLAYER)
        board[3][4] = (chessset.PAWN, players.BLACK_PLAYER)
        self.assertFalse(bishop.try_to_move((2, 3), (4, 5), board))


if __name__ == '__main__':
    unittest.main()
