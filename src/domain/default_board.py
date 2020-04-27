from players import *
from chessset import *

def default_board():
    return [[(ROOK, WHITE_PLAYER), (KNIGHT, WHITE_PLAYER), (BISHOP, WHITE_PLAYER), (QUEEN, WHITE_PLAYER), (KING, WHITE_PLAYER), (BISHOP, WHITE_PLAYER), (KNIGHT, WHITE_PLAYER), (ROOK, WHITE_PLAYER)],
    [(PAWN, WHITE_PLAYER), (PAWN, WHITE_PLAYER), (PAWN, WHITE_PLAYER), (PAWN, WHITE_PLAYER), (PAWN, WHITE_PLAYER), (PAWN, WHITE_PLAYER), (PAWN, WHITE_PLAYER), (PAWN, WHITE_PLAYER)],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [(PAWN, BlACK_PLAYER), (PAWN, BlACK_PLAYER), (PAWN, BlACK_PLAYER), (PAWN, BlACK_PLAYER), (PAWN, BlACK_PLAYER), (PAWN, BlACK_PLAYER), (PAWN, BlACK_PLAYER), (PAWN, BlACK_PLAYER)],
    [(ROOK, BlACK_PLAYER), (KNIGHT, BlACK_PLAYER), (BISHOP, BlACK_PLAYER), (QUEEN, BlACK_PLAYER), (KING, BlACK_PLAYER), (BISHOP, BlACK_PLAYER), (KNIGHT, BlACK_PLAYER), (ROOK, BlACK_PLAYER)]]