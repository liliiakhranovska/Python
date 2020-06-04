
def try_to_move(current_point, target_point, board):
    current_x, current_y = current_point
    _, initial_player = board[current_x][current_y] 
    
    def nnw():
        return current_x - 1, current_y + 2

    def wnw():
        return current_x - 2, current_y + 1

    def wsw():
        return current_x - 2, current_y - 1

    def ssw():
        return current_x - 1, current_y - 2

    def sse():
        return current_x + 1, current_y - 2

    def ese():
        return current_x + 2, current_y - 1

    def ene():
        return current_x + 2, current_y + 1

    def nne():
        return current_x + 1, current_y + 2

    
    def iter_reachable_points():
        for direction in (nnw, wnw, wsw, ssw, sse, ese, ene, nne):
            current_x, current_y = direction()
            if board[current_x][current_y] is not None:
                    _, player = board[current_x][current_y]
                    if player != initial_player:
                        yield current_x, current_y
                    break
            yield current_x, current_y
  
    return target_point in set(iter_reachable_points())   
        






