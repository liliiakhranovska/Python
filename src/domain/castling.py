import players


def c_type(current_point, target_point, board):
    current_x, current_y = current_point
    _, initial_player = board[current_x][current_y]
    if initial_player == players.WHITE_PLAYER:
        if current_point == (0, 4) and target_point == (0, 1):
            return 'south_west'
        elif current_point == (0, 4) and target_point == (0, 6):
            return 'north_west'
    else:
        if current_point == (7, 4) and target_point == (7, 1):
            return 'south_east'
        elif current_point == (7, 4) and target_point == (7, 6):
            return 'north_east'


def check(current_point, target_point, board, white_king_has_moved, black_king_has_moved, white_sw_rook_has_moved, white_nw_rook_has_moved, black_se_rook_has_moved, black_ne_rook_has_moved):
    if c_type(current_point, target_point, board) == 'south_west':
        if white_king_has_moved is False and white_sw_rook_has_moved is False and board[0][1] is None and board[0][2] is None and board[0][3] is None:
            return True
    if c_type(current_point, target_point, board) == 'north_west':
        if white_king_has_moved is False and white_nw_rook_has_moved is False and board[0][5] is None and board[0][6] is None:
            return True
    if c_type(current_point, target_point, board) == 'south_east':
        if black_king_has_moved is False and black_se_rook_has_moved is False and board[7][1] is None and board[7][2] is None and board[7][3] is None:
            return True
    if c_type(current_point, target_point, board) == 'north_east':
        if black_king_has_moved is False and black_ne_rook_has_moved is False and board[7][5] is None and board[7][6] is None:
            return True
