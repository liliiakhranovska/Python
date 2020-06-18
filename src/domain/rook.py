import directions


def try_to_move(current_point, target_point, board):
    current_x, current_y = current_point

    def iter_reachable_points():
        _, initial_player = board[current_x][current_y]
        for direction in (directions.north(current_x, current_y), directions.south(current_x, current_y), directions.west(current_x, current_y), directions.east(current_x, current_y)):
            for (x, y) in direction:
                if board[x][y] is not None:
                    _, player = board[x][y]
                    if player != initial_player:
                        yield x, y
                    break
                yield x, y

    return target_point in set(iter_reachable_points())



