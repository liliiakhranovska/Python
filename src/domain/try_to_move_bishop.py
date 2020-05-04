import compute_bishop_possible_moves
import chessset
import players

def __try_to_move_bishop (initial_space, move_space, board):
    possible_moves = compute_bishop_possible_moves.__compute_bishop_possible_moves (board, initial_space)
    count=0
    for possible_move in possible_moves:
        if move_space == possible_move:
            return True
            break
        else:
            count += 1
            if count == len(possible_moves):
                return False
