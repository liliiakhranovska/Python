def try_to_move(current_point, target_point, board):
    current_x, current_y = current_point

    def north_east():
        return [(x, y) for x in range(current_x + 1, 8) for y in range(current_y + 1, 8) if x-current_x == y-current_y]

    def south_east():
        return [(x, y) for x in range(current_x + 1, 8) for y in range(current_y-1, -1, -1) if x-current_x == current_y-y]

    def south_west():
        return [(x, y) for x in range(current_x-1, -1, -1) for y in range(current_y-1, -1, -1) if x-current_x == y-current_y]

    def north_west():
        return [(x, y) for x in range(current_x-1, -1, -1) for y in range(current_y + 1, 8)if x-current_x == current_y-y]

    def iter_reachable_points():
        _, initial_player = board[current_x][current_y]
        for (x, y) in north_east():
            if board[x][y] is not None:
                _, player = board[x][y]
                if player != initial_player:
                    yield x, y
                break
            yield x, y
        for (x, y) in south_east():
            if board[x][y] is not None:
                _, player = board[x][y]
                if player != initial_player:
                    yield x, y
                break
            yield x, y
        for (x, y) in south_west():
            if board[x][y] is not None:
                _, player = board[x][y]
                if player != initial_player:
                    yield x, y
                break
            yield x, y
        for (x, y) in north_west():
            if board[x][y] is not None:
                _, player = board[x][y]
                if player != initial_player:
                    yield x, y
                break
            yield x, y

    return target_point in set(iter_reachable_points())
