def __reset_to_initial_coordinates (x,y, initial_space):
    initial_x, initial_y = initial_space
    (x,y)=initial_x, initial_y
    return (x,y)


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

initial_space = (5,4)
print(__compute_all_bishop_possible_moves (initial_space))