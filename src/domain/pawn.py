import players
import default_board
import chessset

current_point = (5,5)
board = [[None] * 8 for i in range(8)]
board [5][5] = (chessset.PAWN, players.BLACK_PLAYER)
board [4][6] = (chessset.PAWN, players.BLACK_PLAYER)
target_point = (5,6)


def try_to_move(current_point, target_point, board):
    current_x, current_y = current_point
    _, initial_player = board[current_x][current_y]

    def within_board (x,y):
        if x < 8 and x > -1 and y < 8 and y > -1:
            return 1
        else:
            return 0
    
    def direction (initial_player):
        if initial_player == players.WHITE_PLAYER:
            return 1
        else:
            return -1

    def moves():
        if board[current_x + direction (initial_player)][current_y] == None :
            yield current_x + direction (initial_player), current_y
        if initial_player == players.WHITE_PLAYER and current_x == 1 and board[2][current_y] is None and board[3][current_y] is None:
            yield current_x + 2, current_y
        elif initial_player == players.BLACK_PLAYER and current_x == 6 and board[5][current_y] is None and board[4][current_y] is None:
            yield current_x - 2, current_y
    
    def takes():
        if board[current_x + direction (initial_player)][current_y + direction (initial_player)] != None:
            _, player = board[current_x + direction (initial_player)][current_y + direction (initial_player)]
            if initial_player != player:
                yield current_x + direction (initial_player), current_y + direction (initial_player)
        if board[current_x + direction (initial_player)][current_y - direction (initial_player)] != None:
            _, player = board[current_x + direction (initial_player)][current_y - direction (initial_player)]
            if initial_player != player:
                yield current_x + direction (initial_player), current_y - direction (initial_player)
    
    return takes()
    
print (list(try_to_move(current_point, target_point, board)))


'''def iter_reachable_points():
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

    return target_point in set(iter_reachable_points())'''


