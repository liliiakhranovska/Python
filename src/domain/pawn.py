import players
import directions


def try_to_move(current_point, target_point, board):
    current_x, current_y = current_point

    def iter_reachable_points():
        _, initial_player = board[current_x][current_y]
        if initial_player is players.WHITE_PLAYER:
            for direction in [directions.east(current_x, current_y)]:
                for (x, y) in direction:
                    if board[x][y] is None:
                        if current_x == 1 and board[x+1][y] is None:
                            yield x+1, y
                        yield x, y
                        break
                    else:
                        break
            for direction in [directions.south_east(current_x, current_y), directions.north_east(current_x, current_y)]:
                for (x, y) in direction:
                    if board[x][y] is not None:
                        _, player = board[x][y]
                        if player != initial_player:
                            yield x, y
                            break
                    else:
                        break

        if initial_player is players.BLACK_PLAYER:
            for direction in [directions.west(current_x, current_y)]:
                for (x, y) in direction:
                    if board[x][y] is None:
                        if current_x == 6 and board[x-1][y] is None:
                            yield x-1, y
                        yield x, y
                        break
                    else:
                        break
            for direction in [directions.south_west(current_x, current_y), directions.north_west(current_x, current_y)]:
                for (x, y) in direction:
                    if board[x][y] is not None:
                        _, player = board[x][y]
                        if player != initial_player:
                            yield x, y
                            break
                    else:
                        break
    return target_point in set(iter_reachable_points())
