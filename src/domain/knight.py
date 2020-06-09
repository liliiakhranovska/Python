def try_to_move(current_point, target_point, board):
    current_x, current_y = current_point
    _, initial_player = board[current_x][current_y] 
    
    def pos_moves():
        return [(x, y) for x in range(8) for y in range(8) if (abs(x - current_x) == 1 and abs(y - current_y) == 2) or (abs(x - current_x) == 2 and abs(y - current_y) == 1)]
    
    def iter_reachable_points():
        for (x, y) in pos_moves():
            if board[x][y] is not None:
              _, player = board[x][y]
              if player != initial_player:
                    yield x, y
              break
            yield x, y
  
    return target_point in set(iter_reachable_points())





