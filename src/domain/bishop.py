import math

WHOLE_BOARD = frozenset([(x, y) for x in range(8) for y in range(8)])


def __iter_possible_moves(point, board):
    x, y = point
    _, initial_player = board[x][y]
    directions = [(step_for_x, step_for_y) for step_for_x in (-1,1) for step_for_y in (-1,1)]
    for direction in directions:
        x, y = point
        while (x+direction[0], y+direction[1]) in WHOLE_BOARD:
            if board[x+direction[0]][y+direction[1]] == None:
                yield x+direction[0], y+direction[1]
            if board[x+direction[0]][y+direction[1]] != None:
                _, player = board[x+direction[0]][y+direction[1]]
                if player != initial_player:
                    yield x+direction[0], y+direction[1]
                break
            x += direction[0]
            y += direction[1]


def try_to_move_bishop(point, move_point, board):
    return move_point in __iter_possible_moves(point, board)