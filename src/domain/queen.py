import bishop
import rook


def try_to_move(current_point, target_point, board):
    return bishop.try_to_move(current_point, target_point, board) or rook.try_to_move(current_point, target_point, board)
