def try_to_move(current_point, target_point, board):
    current_x, current_y = current_point
    _, initial_player = board[current_x][current_y]

    def move():
        return [(x, y) for x in range(current_x-1, current_x + 2) for y in range(current_y-1, current_y + 2) if (x, y) != (current_x, current_y) and x > -1 and y > -1 and x < 8 and y < 8]

    def iter_reachable_points():
        for movement in move():
            x, y = movement
            if board[x][y] is not None:
                _, player = board[x][y]
                if player != initial_player:
                    yield x, y
            else:
                yield x, y

    return target_point in set(iter_reachable_points())
