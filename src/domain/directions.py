def north(current_x, current_y):
    return [(current_x, y) for y in range(current_y + 1, 8)]


def south(current_x, current_y):
    return [(current_x, y) for y in range(current_y-1, -1, -1)]


def west(current_x, current_y):
    return [(x, current_y) for x in range(current_x-1, -1, -1)]


def east(current_x, current_y):
    return [(x, current_y) for x in range(current_x + 1, 8)]


def north_east(current_x, current_y):
    return [(x, y) for x in range(current_x + 1, 8) for y in range(current_y + 1, 8) if x - current_x == y - current_y]


def south_east(current_x, current_y):
    return [(x, y) for x in range(current_x + 1, 8) for y in range(current_y - 1, -1, -1) if x - current_x == current_y - y]


def south_west(current_x, current_y):
    return [(x, y) for x in range(current_x - 1, -1, -1) for y in range(current_y - 1, -1, -1) if x - current_x == y - current_y]


def north_west(current_x, current_y):
    return [(x, y) for x in range(current_x - 1, -1, -1) for y in range(current_y + 1, 8)if x - current_x == current_y - y]
