import default_board
import chessset
import players
import knight
import test_utils
import unittest


class TestRook(unittest.TestCase):
    
    def test_knight_name_figure(self):
        self.assertEqual(chessset.KNIGHT, 'KNIGHT')
        self.assertNotEqual(chessset.KNIGHT, 'knightt')

    def test_if_knight_has_correct_initially_coordinates_at_the_beginning_of_the_game(self):
        self.assertTrue(test_utils.default_board[0][1], ('KNIGHT', 'WHITE_PLAYER'))
        self.assertTrue(test_utils.default_board[0][6], ('KNIGHT', 'WHITE_PLAYER'))
        self.assertTrue(test_utils.default_board[7][1], ('KNIGHT', 'BLACK_PLAYER'))
        self.assertTrue(test_utils.default_board[7][6], ('KNIGHT', 'BLACK_PLAYER'))     


    def test_that_knight_can_move_north_north_west(self):
        board = test_utils.empty_board
        board[2][2] = (chessset.KNIGHT, players.BLACK_PLAYER)
        board[2][3] = (chessset.PAWN, players.WHITE_PLAYER)
        self.assertTrue(knight.try_to_move((2, 2), (1, 4), board))
    

    def test_that_knight_can_move_west_north_west(self):
        board = test_utils.empty_board
        board[2][2] = (chessset.KNIGHT, players.BLACK_PLAYER)
        board[1][1] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(knight.try_to_move((2, 2), (0, 3), board))


    def test_that_knight_can_move_west_south_west(self):
        board = test_utils.empty_board
        board[2][2] = (chessset.KNIGHT, players.BLACK_PLAYER)
        board[1][3] = (chessset.KING, players.WHITE_PLAYER)
        self.assertTrue(knight.try_to_move((2, 2), (0, 1), board))


    def test_that_knight_can_move_south_south_west(self):
        board = test_utils.empty_board
        board[2][2] = (chessset.KNIGHT, players.BLACK_PLAYER)
        board[1][2] = (chessset.QUEEN, players.WHITE_PLAYER)
        self.assertTrue(knight.try_to_move((2, 2), (1, 0), board))

    def test_that_knight_can_move_south_south_east(self):
        board = test_utils.empty_board
        board[2][2] = (chessset.KNIGHT, players.BLACK_PLAYER)
        board[3][1] = (chessset.QUEEN, players.WHITE_PLAYER)
        self.assertTrue(knight.try_to_move((2, 2), (3, 0), board))
    

    def test_that_knight_can_move_east_south_east(self):
        board = test_utils.empty_board
        board[2][2] = (chessset.KNIGHT, players.BLACK_PLAYER)
        board[3][2] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(knight.try_to_move((2, 2), (4, 1), board))


    def test_that_knight_can_move_east_north_east(self):
        board = test_utils.empty_board
        board[5][5] = (chessset.KNIGHT, players.BLACK_PLAYER)
        board[7][5] = (chessset.KING, players.WHITE_PLAYER)
        self.assertTrue(knight.try_to_move((5, 5), (7, 6), board))


    def test_that_knight_can_move_north_north_east(self):
        board = test_utils.empty_board
        board[5][5] = (chessset.KNIGHT, players.BLACK_PLAYER)
        board[6][6] = (chessset.QUEEN, players.WHITE_PLAYER)
        self.assertTrue(knight.try_to_move((5, 5), (6, 7), board))



    def test_that_knight_cant_attack_piece_the_same_color(self):
        board = test_utils.empty_board
        board[2][2] = (chessset.KNIGHT, players.BLACK_PLAYER)
        board[0][1] = (chessset.KING, players.BLACK_PLAYER)
        self.assertFalse(knight.try_to_move((2, 2), (0, 1), board))                        
  

    def test_that_knight_can_attack_opponent_piece(self):
        board = test_utils.empty_board
        board[2][2] = (chessset.KNIGHT, players.BLACK_PLAYER)
        board[4][1] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(knight.try_to_move((2, 2), (4, 1), board))


    def test_that_knight_can_move_either_point_if_surrounded_by_the_same_color(self):
        board = test_utils.empty_board
        board[2][2] = (chessset.KNIGHT, players.BLACK_PLAYER)
        board[1][3] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[1][2] = (chessset.KING, players.BLACK_PLAYER)
        board[1][1] = (chessset.BISHOP, players.BLACK_PLAYER)
        board[2][1] = (chessset.PAWN, players.BLACK_PLAYER)
        board[3][1] = (chessset.BISHOP, players.BLACK_PLAYER)
        board[3][2] = (chessset.ROOK, players.BLACK_PLAYER)
        board[3][3] = (chessset.PAWN, players.BLACK_PLAYER)
        board[2][3] = (chessset.PAWN, players.BLACK_PLAYER)
        board[1][3] = (chessset.PAWN, players.BLACK_PLAYER)
        self.assertTrue(knight.try_to_move((2, 2), (4, 1), board))


if __name__ == '__main__':
    unittest.main()

    