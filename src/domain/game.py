import castling
import players
import chessset
import bishop
import queen
import pawn
import rook
import king
import state


def game(current_point, target_point, board):
    current_x, current_y = current_point
    target_x, target_y = target_point
    initial_piece, initial_player = board[current_x][current_y]
    if move_is_valid(current_point, target_point, board, state.white_king_has_moved, state.black_king_has_moved, state.white_sw_rook_has_moved, state.white_nw_rook_has_moved, state.black_se_rook_has_moved, state.black_sw_rook_has_moved) is True:
        if initial_piece == chessset.KING and (king.try_to_move(current_point, target_point, board) is False):
            __move_castling(current_point, target_point, board)
        board[target_x][target_y] = board[current_x][current_y]
        board[current_x][current_y] = None
        state.white_king_has_moved = True
    if initial_piece == chessset.KING and initial_player == players.WHITE_PLAYER:
        state.white_king_has_moved = True
    if initial_piece == chessset.KING and initial_player == players.BLACK_PLAYER:
        state.black_king_has_moved = True
    if initial_piece == chessset.ROOK and initial_player == players.WHITE_PLAYER and current_point == (0, 0):
        state.white_sw_rook_has_moved = True
    if initial_piece == chessset.ROOK and initial_player == players.WHITE_PLAYER and current_point == (0, 7):
        state.white_nw_rook_has_moved = True
    if initial_piece == chessset.ROOK and initial_player == players.BLACK_PLAYER and current_point == (7, 0):
        state.white_se_rook_has_moved = True
    if initial_piece == chessset.ROOK and initial_player == players.BLACK_PLAYER and current_point == (7, 7):
        state.white_ne_rook_has_moved = True
    return board


def move_is_valid(current_point, target_point, board, white_king_has_moved, black_king_has_moved, white_sw_rook_has_moved, white_nw_rook_has_moved, black_se_rook_has_moved, black_sw_rook_has_moved):
    current_x, current_y = current_point
    target_x, target_y = target_point
    initial_piece, initial_player = board[current_x][current_y]
    if initial_piece == chessset.KING:
        castling_type = castling.c_type(current_point, target_point, board)
        if castling.check(current_point, target_point, board, state.white_king_has_moved, state.black_king_has_moved, state.white_sw_rook_has_moved, state.white_nw_rook_has_moved, state.black_se_rook_has_moved, state.black_sw_rook_has_moved) or king.try_to_move(current_point, target_point, board):
            return True
    if initial_piece == chessset.QUEEN and queen.try_to_move(current_point, target_point, board) is True:
        return True
    if initial_piece == chessset.BISHOP and bishop.try_to_move(current_point, target_point, board) is True:
        return True
    if initial_piece == chessset.KNIGHT and knight.try_to_move(current_point, target_point, board) is True:
        return True
    if initial_piece == chessset.ROOK and rook.try_to_move(current_point, target_point, board) is True:
        return True
    if initial_piece == chessset.PAWN and pawn.try_to_move(current_point, target_point, board) is True:
        return True


def __move_castling(current_point, target_point, board):
    if castling.c_type(current_point, target_point, board) == 'south_west':
        board[0][2] = board[0][0]
        board[0][0] = None
    if castling.c_type(current_point, target_point, board) == 'north_west':
        board[0][5] = (chessset.ROOK, players.WHITE_PLAYER)
        board[0][7] = None
    if castling.c_type(current_point, target_point, board) == 'north_east':
        board[7][5] = (chessset.ROOK, players.BLACK_PLAYER)
        board[7][7] = None
    if castling.c_type(current_point, target_point, board) == 'south_east':
        board[7][2] = (chessset.ROOK, players.BLACK_PLAYER)
        board[7][0] = None
    return board