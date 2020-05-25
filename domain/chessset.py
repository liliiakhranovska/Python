KING = 'KING'

QUEEN = 'QUEEN'

ROOK = 'ROOK'

BISHOP = 'BISHOP'

KNIGHT = 'KNIGHT'

PAWN = 'PAWN'


def is_valid_item(item):
    return item in {KING, QUEEN, ROOK, BISHOP, KNIGHT, PAWN}
