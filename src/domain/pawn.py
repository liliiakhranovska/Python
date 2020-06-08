import players


def try_to_move(current_point, target_point, board):
    current_x, current_y = current_point
    _, initial_player = board[current_x][current_y]

    def direction(initial_player):
        if initial_player == players.WHITE_PLAYER:
            return 1
        else:
            return -1

    def moves():
        if current_x + direction(initial_player) < 8 and current_x + direction(initial_player) > -1:
            yield current_x + direction(initial_player), current_y
        if initial_player == players.WHITE_PLAYER and current_x == 1 and board[current_x + 1][current_y] == None:
            yield current_x + 2, current_y
        elif initial_player == players.BLACK_PLAYER and current_x == 6 and board[current_x - 1][current_y] == None:
            yield current_x - 2, current_y

    def takes():
        if current_x + direction(initial_player) > -1 and current_x + direction(initial_player) < 8 and current_y + direction(initial_player) > -1 and current_y + direction(initial_player) < 8:
            yield current_x + direction(initial_player), current_y + direction(initial_player)
        if current_x + direction(initial_player) > -1 and current_x + direction(initial_player) < 8 and current_y - direction(initial_player) > -1 and current_y - direction(initial_player) < 8:
            yield current_x + direction(initial_player), current_y - direction(initial_player)

    def iter_reachable_points():
        for x, y in moves():
            if board[x][y] is None:
                yield x, y
        for x, y in takes():
            if board[x][y] is not None:
                _, player = board[x][y]
                if player != initial_player:
                    yield x, y

    return target_point in set(iter_reachable_points())
