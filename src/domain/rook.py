
def try_to_move(current_point, target_point, board):
  current_x, current_y = current_point


  def north():
    return [(current_x, y) for y in range(current_y + 1, 8)]

  def south():
    return [(current_x, y) for y in range(0, current_y)]
  
  def west():
    return [(x, current_y) for x in range(0, current_x)]

  def east():
    return [(x, current_y) for x in range(current_x + 1, 8)]
  
  def iter_reachable_points():
      _, initial_player = board[current_x][current_y] 
      for direction in (north, south, west, east):
        for (x, y) in direction():
            if board[x][y] is not None:
              _, player = board[x][y]
              if player != initial_player:
                    yield x, y
              break
            yield x, y
  
  return target_point in set(iter_reachable_points())


