def __compute_all_bishop_possible_moves (initial_space):
    initial_x, initial_y = initial_space
    poss_moves_first_quater = set((x,y) for x in range(initial_x+1,8) for y in range(initial_y+1,8) if abs(x-initial_x) == abs(y-initial_y))
    poss_moves_second_quater = set((x,y) for x in range(initial_x-1,-1,-1) for y in range(initial_y+1,8)if abs(x-initial_x) == abs(y-initial_y))
    poss_moves_third_quater = set((x,y) for x in range(initial_x-1,-1,-1) for y in range(initial_y-1,-1,-1)if abs(x-initial_x) == abs(y-initial_y))
    poss_moves_fourth_quater = set((x,y) for x in range(initial_x+1,8) for y in range(initial_y-1,-1,-1)if abs(x-initial_x) == abs(y-initial_y))
    return set.union(poss_moves_first_quater, poss_moves_second_quater, poss_moves_third_quater, poss_moves_fourth_quater)

def __remove_possible_move_bishop (all_possible_bishop_moves, initial_space, start_space):
    initial_x, initial_y = initial_space
    start_x, start_y = start_space
    need_to_be_removed_first_quater = set((x,y) for x in range(start_x,8) for y in range(start_y,8) if abs(x-initial_x) == abs(y-initial_y) and start_x - initial_x > 0 and start_y - initial_y > 0)
    need_to_be_removed_second_quater = set((x,y) for x in range(start_x,-1,-1) for y in range(start_y,8) if abs(x-initial_x) == abs(y-initial_y) and start_x - initial_x < 0 and start_y - initial_y > 0)
    need_to_be_removed_third_quater = set((x,y) for x in range(start_x,-1,-1) for y in range(start_y,-1,-1) if abs(x-initial_x) == abs(y-initial_y) and start_x - initial_x < 0 and start_y - initial_y < 0)
    need_to_be_removed_fourth_quater = set((x,y) for x in range(start_x,8) for y in range(start_y,-1,-1) if abs(x-initial_x) == abs(y-initial_y) and start_x - initial_x > 0 and start_y - initial_y < 0)
    need_to_be_removed = set.union (need_to_be_removed_first_quater, need_to_be_removed_second_quater, need_to_be_removed_third_quater, need_to_be_removed_fourth_quater)
    return all_possible_bishop_moves.difference(need_to_be_removed) 


def __compute_bishop_possible_moves (board, initial_space):
    initial_x, initial_y = initial_space
    possible_bishop_moves = __compute_all_bishop_possible_moves (initial_space)
    initial_piece, initial_player = board[initial_x][initial_y]
    for possible_move in possible_bishop_moves:
        possible_move_x, possible_move_y = possible_move
        if board[possible_move_x][possible_move_y] != None:
            _, player = board[possible_move_x][possible_move_y]
            if player == initial_player:
                start_space = (possible_move_x, possible_move_y)
                possible_bishop_moves = __remove_possible_move_bishop (possible_bishop_moves, initial_space, start_space)
            if player != initial_player:
                if possible_move_x - initial_x > 0:
                    step_x = 1
                else:
                    step_x = -1
                if possible_move_y - initial_y > 0:
                    step_y = 1
                else:
                    step_y = -1
                if possible_move_x+step_x>=0 and possible_move_x+step_x<=7 and possible_move_y+step_y>=0 and possible_move_y+step_y<=7:
                    start_space = (possible_move_x+step_x, possible_move_y+step_y)
                    possible_bishop_moves = __remove_possible_move_bishop (possible_bishop_moves, initial_space, start_space)     
    return possible_bishop_moves


def __try_to_move_bishop (initial_space, move_space, board):
    possible_moves = __compute_bishop_possible_moves (board, initial_space)
    for possible_move in possible_moves:
        if move_space == possible_move:
            return True
    return False
