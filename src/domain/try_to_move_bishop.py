def try_to_move_bishop(initial_space, move_space, chess_board):
    possible_moves=[]
    x,y = initial_space
    print (chess_board[x][y])
    initial_piece, initial_color = chess_board[x][y]
    first_quarter_bishop_route_length = min(7-x,7-y)
    second_quarter_bishop_route_length = min(x,7-y)
    third_quarter_bishop_route_length = min(x,y)
    fourth_quarter_bishop_route_length = min(7-x,y)
    i = 1
    while i <= first_quarter_bishop_route_length:
        if chess_board[x+i][y+i] == None:
            possible_moves.append((x+i,y+i))
        if chess_board[x+i][y+i] != None:
            move_piece, move_color = chess_board[x+i][y+i]
            if move_color != initial_color:
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
            move_piece, move_color = chess_board[x-i][y+i]
            if move_color != initial_color:
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
            move_piece, move_color = chess_board[x-i][y-i]
            if move_color != initial_color:
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
            move_piece, move_color = chess_board[x+i][y-i]
            if move_color != initial_color:
                possible_moves.append((x+i,y-i))
                break
            else:
                break
        i += 1
    count=0
    for possible_move in possible_moves:
        if move_space == possible_move:
            print ('True')
            break
        else:
            count += 1
            if count == len(possible_moves):
                print ('False')
