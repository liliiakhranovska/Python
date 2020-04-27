from compute_bishop_possible_moves import *

def try_to_move_bishop (initial_space, move_space, chess_board):
    possible_moves = compute_bishop_possible_moves (initial_space, chess_board)
    count=0
    for possible_move in possible_moves:
        if move_space == possible_move:
            return True
            break
        else:
            count += 1
            if count == len(possible_moves):
                return False

