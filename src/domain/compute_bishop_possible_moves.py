def compute_bishop_possible_moves (initial_space, chess_board):
    possible_moves=[]
    x,y = initial_space
    initial_piece, initial_player = chess_board[x][y]
    first_quarter_bishop_route_length = min(7-x,7-y)
    second_quarter_bishop_route_length = min(x,7-y)
    third_quarter_bishop_route_length = min(x,y)
    fourth_quarter_bishop_route_length = min(7-x,y)
    i = 1
    while i <= first_quarter_bishop_route_length:
        if chess_board[x+i][y+i] == None:
            possible_moves.append((x+i,y+i))
        if chess_board[x+i][y+i] != None:
            piece, player = chess_board[x+i][y+i]
            if player != initial_player:
                possible_moves.append((x+i,y+i))
                break
            else:
                break
        i += 1
    i = 1
    while i <= second_quarter_bishop_route_length:
        if chess_board[x-i][y+i] == None:
            possible_moves.append((x-i,y+i))
        if chess_board[x-i][y+i] != None:
            piece, player = chess_board[x-i][y+i]
            if player != initial_player:
                possible_moves.append((x-i,y+i))
                break
            else:
                break
        i += 1
    i = 1
    while i <= third_quarter_bishop_route_length:
        if chess_board[x-i][y-i] == None:
            possible_moves.append((x-i,y-i))
        if chess_board[x-i][y-i] != None:
            piece, player = chess_board[x-i][y-i]
            if player != initial_player:
                possible_moves.append((x-i,y-i))
                break
            else:
                break
        i += 1
    i = 1
    while i <= fourth_quarter_bishop_route_length:
        if chess_board[x+i][y-i] == None:
            possible_moves.append((x+i,y-i))
        if chess_board[x+i][y-i] != None:
            piece, player = chess_board[x+i][y-i]
            if player != initial_player:
                possible_moves.append((x+i,y-i))
                break
            else:
                break
        i += 1
    return possible_moves