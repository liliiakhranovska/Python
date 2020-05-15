import math

WHOLE_BOARD = frozenset([(x, y) for x in range(8) for y in range(8)])

board = [[None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, (PAWN, BlACK_PLAYER), None, None, None, None, None, None],
    [None, None, None, None, None, None, (PAWN, WHITE_PLAYER), None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, (BISHOP, BlACK_PLAYER), None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, (BISHOP, WHITE_PLAYER), None, None, None, None, None]]

def __iter_diagonals(point):
  x, y = point
  while (x+1, y+1) in WHOLE_BOARD:
    x += 1
    y += 1
    yield x, y
  x, y = point
  while (x-1, y-1) in WHOLE_BOARD:
    x -= 1
    y -= 1
    yield x, y
  x, y = point
  while (x+1, y-1) in WHOLE_BOARD:
    x += 1
    y -= 1
    yield x, y
  x, y = point
  while (x-1, y+1) in WHOLE_BOARD:
    x -= 1
    y += 1
    yield x, y

def __remove_moves(point, board):
    x, y = point
    _, initial_player = board[x][y]
    for iter_diag in list(__iter_diagonals(point)):
        x_id, y_id = iter_diag
        if board[x_id][y_id] != None:
          _, player = board[x_id][y_id]
          if player == initial_player:
            yield x_id, y_id
          while (x_id + int(math.copysign(1,x_id-x)), y_id + int(math.copysign(1,y_id-y))) in WHOLE_BOARD:
            x_id = x_id + int(math.copysign(1,x_id-x))
            y_id = y_id + int(math.copysign(1,y_id-y))
            yield x_id, y_id  

def __bishop_moves (board, point):
  all_moves = __iter_diagonals(point)
  remove_moves = __remove_moves(point, board)
  return set(list(all_moves))-set(list(remove_moves))

def __try_to_move_bishop (point, move_point, board):
    possible_moves = __bishop_moves(board, point)
    for possible_move in possible_moves:
        if move_point == possible_move:
            return True
    return False