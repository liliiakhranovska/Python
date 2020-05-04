def __compute_all_bishop_possible_moves (initial_space):
    all_possible_bishop_moves=[]
    x=y=0
    (x,y) = __reset_to_initial_coordinates (x,y,initial_space)
    while x<7 and y<7:
        x += 1
        y += 1
        all_possible_bishop_moves.append((x,y))
    (x,y) = __reset_to_initial_coordinates (x,y,initial_space)
    while x>0 and y<7:
        x -= 1
        y += 1
        all_possible_bishop_moves.append((x,y))
    (x,y) = __reset_to_initial_coordinates (x,y,initial_space)
    while x>0 and y>0:
        x -= 1
        y -= 1
        all_possible_bishop_moves.append((x,y))
    (x,y) = __reset_to_initial_coordinates (x,y,initial_space)
    while x<7 and y>0:
        x += 1
        y -= 1
        all_possible_bishop_moves.append((x,y))
    return all_possible_bishop_moves

def __reset_to_initial_coordinates (x,y, initial_space):
    initial_x, initial_y = initial_space
    (x,y)=initial_x, initial_y
    return (x,y)

def __remove_possible_move_bishop (all_possible_bishop_moves, initial_space, start_space):
    initial_x, initial_y = initial_space
    start_x, start_y = start_space
    possible_bishop_moves = all_possible_bishop_moves
    possible_bishop_moves.remove(start_space)
    x=y=0
    if start_x-initial_x>0 and start_y-initial_y>0:
        (x,y) = __reset_to_initial_coordinates (x,y,start_space)
        while x<7 and y<7:
            x += 1
            y += 1
            possible_bishop_moves.remove((x,y))
    if start_x-initial_x<0 and start_y-initial_y>0:
        (x,y) = __reset_to_initial_coordinates (x,y,start_space)
        while x>0 and y<7:
            x -= 1
            y += 1
            possible_bishop_moves.remove((x,y))
    if start_x-initial_x<0 and start_y-initial_y<0:
        (x,y) = __reset_to_initial_coordinates (x,y,start_space)
        while x>0 and y>0:
            x -= 1
            y -= 1
            possible_bishop_moves.remove((x,y))
    if start_x-initial_x>0 and start_y-initial_y<0:
        (x,y) = __reset_to_initial_coordinates (x,y,start_space)
        while x<7 and y>0:
            x -= 1
            y += 1
            possible_bishop_moves.remove((x,y))
    return possible_bishop_moves

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
                __remove_possible_move_bishop (possible_bishop_moves, initial_space, start_space)
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
                    __remove_possible_move_bishop (possible_bishop_moves, initial_space, start_space)     
    return possible_bishop_moves
