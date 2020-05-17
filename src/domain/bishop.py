import math

WHOLE_BOARD = frozenset([(x, y) for x in range(8) for y in range(8)])

def __iter_while_vacant(point, board):
    x, y = point
    _, initial_player = board[x][y]
    while (x+1, y+1) in WHOLE_BOARD:
        if board[x+1][y+1] == None:
            yield x+1, y+1
        if board[x+1][y+1] != None:
            _, player = board[x+1][y+1]
            if initial_player != player:
                yield x+1, y+1
            break
        x += 1
        y += 1
    x, y = point
    while (x-1, y+1) in WHOLE_BOARD:
        if board[x-1][y+1] == None:
            yield x-1, y+1
        if board[x-1][y+1] != None:
            _, player = board[x-1][y+1]
            if initial_player != player:
                yield x-1, y+1
            break
        x -= 1
        y += 1
    x, y = point
    while (x-1, y-1) in WHOLE_BOARD:
        if board[x-1][y-1] == None:
            yield x-1, y-1
        if board[x-1][y-1] != None:
            _, player = board[x-1][y-1]
            if initial_player != player:
                yield x-1, y-1
            break
        x -= 1
        y -= 1
    x, y = point
    while (x+1, y-1) in WHOLE_BOARD:
        if board[x+1][y-1] == None:
            yield x+1, y-1
        if board[x+1][y-1] != None:
            _, player = board[x+1][y-1]
            if initial_player != player:
                yield x+1, y-1
            break
        x += 1
        y -= 1


def try_to_move_bishop(point, move_point, board):
    return move_point in __iter_while_vacant(point, board)
