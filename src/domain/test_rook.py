import default_board
import chessset
import players
import rook
import test_utils
import unittest


class TestRook(unittest.TestCase):
    
    def test_rook_name_figure(self):
        self.assertEqual(chessset.ROOK, 'ROOK')
        self.assertNotEqual(chessset.ROOK, 'roook')

    def test_if_rook_has_correct_initially_coordinates_at_the_beginning_of_the_game(self):
        self.assertTrue(test_utils.default_board[0][0], ('ROOK', 'WHITE_PLAYER'))
        self.assertTrue(test_utils.default_board[0][7], ('ROOK', 'WHITE_PLAYER'))
        self.assertTrue(test_utils.default_board[7][0], ('ROOK', 'BLACK_PLAYER'))
        self.assertTrue(test_utils.default_board[7][7], ('ROOK', 'BLACK_PLAYER'))     


    def test_that_rook_can_move_south(self):
        board = test_utils.empty_board
        board[3][4] = (chessset.ROOK, players.BLACK_PLAYER)
        board[3][6] = (chessset.QUEEN, players.WHITE_PLAYER)
        self.assertTrue(rook.try_to_move((3, 4), (3, 0), board))
    

    def test_that_rook_can_move_north(self):
        board = test_utils.empty_board
        board[3][4] = (chessset.ROOK, players.BLACK_PLAYER)
        board[2][2] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(rook.try_to_move((3, 4), (3, 6), board))


    def test_that_rook_can_move_east(self):
        board = test_utils.empty_board
        board[3][4] = (chessset.ROOK, players.BLACK_PLAYER)
        board[4][6] = (chessset.KING, players.BLACK_PLAYER)
        self.assertTrue(rook.try_to_move((3, 4), (6, 4), board))


    def test_that_rook_can_move_west(self):
        board = test_utils.empty_board
        board[3][4] = (chessset.ROOK, players.BLACK_PLAYER)
        board[3][6] = (chessset.QUEEN, players.WHITE_PLAYER)
        self.assertTrue(rook.try_to_move((3, 4), (0, 4), board))


    def test_that_rook_cant_jump_over_piece(self):
        board = test_utils.empty_board
        board[3][1] = (chessset.ROOK, players.BLACK_PLAYER)
        board[3][4] = (chessset.QUEEN, players.BLACK_PLAYER)
        self.assertFalse(rook.try_to_move((3, 1), (3, 5), board))    


    def test_that_rook_cant_attack_piece_the_same_color(self):
        board = test_utils.empty_board
        board[1][4] = (chessset.ROOK, players.BLACK_PLAYER)
        board[3][2] = (chessset.KING, players.BLACK_PLAYER)
        self.assertFalse(rook.try_to_move((1, 4), (3, 2), board))                        
  

    def test_that_rook_can_attack_opponent_piece(self):
        board = test_utils.empty_board
        board[0][0] = (chessset.ROOK, players.BLACK_PLAYER)
        board[0][6] = (chessset.BISHOP, players.WHITE_PLAYER)
        self.assertTrue(rook.try_to_move((0, 0), (0, 6), board))


    def test_that_rook_cant_move_either_point_if_surrounded_by_the_same_color(self):
        board = test_utils.empty_board
        board[4][3] = (chessset.ROOK, players.BLACK_PLAYER)
        board[4][2] = (chessset.QUEEN, players.BLACK_PLAYER)
        board[5][3] = (chessset.KING, players.BLACK_PLAYER)
        board[4][4] = (chessset.BISHOP, players.BLACK_PLAYER)
        board[3][3] = (chessset.PAWN, players.BLACK_PLAYER)
        self.assertFalse(rook.try_to_move((4, 3), (4, 5), board))


if __name__ == '__main__':
    unittest.main()

    