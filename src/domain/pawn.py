import players


def try_to_move(current_point, target_point, board):
    current_x, current_y = current_point
    _, initial_player = board[current_x][current_y]

    def pos_moves_white():
        if current_x + 1 < 8:
            yield current_x + 1, current_y
        if current_x == 1:
            if board[2][current_y] is None:
                yield current_x + 2, current_y

    def pos_takes_white():
        if current_x + 1 < 8 and current_y + 1 < 8:
            yield current_x + 1, current_y + 1
        if current_x + 1 < 8 and current_y - 1 > -1:
            yield current_x + 1, current_y - 1

    def pos_moves_black():
        if current_x - 1 > -1:
            yield current_x - 1, current_y
        if current_x == 6:
            if board[5][current_y] is None:
                yield current_x - 2, current_y

    def pos_takes_black():
        if current_x - 1 > -1 and current_y + 1 < 8:
            yield current_x - 1, current_y + 1
        if current_x - 1 > -1 and current_y - 1 > -1:
            yield current_x - 1, current_y - 1

    def iter_reachable_points():
        if initial_player == players.WHITE_PLAYER:
            for x, y in pos_moves_white():
                if board[x][y] is None:
                    yield x, y
                for move in pos_takes_white():
                    x, y = move
                    if board[x][y] is not None:
                        _, player = board[x][y]
                        if player == players.BLACK_PLAYER:
                            yield x, y
        elif initial_player == players.BLACK_PLAYER:
            for move in pos_moves_black():
                x, y = move
                if board[x][y] is None:
                    yield x, y
            for move in pos_takes_black():
                x, y = move
                if board[x][y] is not None:
                    _, player = board[x][y]
                    if player == players.WHITE_PLAYER:
                        yield x, y

    return target_point in set(iter_reachable_points())
