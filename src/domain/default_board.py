import players
import chessset

EMPTY_BOARD = [[None] * 8] * 8

def default_board():
    return [[(chessset.ROOK, players.WHITE_PLAYER), (chessset.KNIGHT, players.WHITE_PLAYER), (chessset.BISHOP, players.WHITE_PLAYER), (chessset.QUEEN, players.WHITE_PLAYER), (chessset.KING, players.WHITE_PLAYER), (chessset.BISHOP, players.WHITE_PLAYER), (chessset.KNIGHT, players.WHITE_PLAYER), (chessset.ROOK, players.WHITE_PLAYER)],
            [(chessset.PAWN, players.WHITE_PLAYER), (chessset.PAWN, players.WHITE_PLAYER), (chessset.PAWN, players.WHITE_PLAYER), (chessset.PAWN, players.WHITE_PLAYER),
             (chessset.PAWN, players.WHITE_PLAYER), (chessset.PAWN, players.WHITE_PLAYER), (chessset.PAWN, players.WHITE_PLAYER), (chessset.PAWN, players.WHITE_PLAYER)],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [(chessset.PAWN, players.BlACK_PLAYER), (chessset.PAWN, players.BlACK_PLAYER), (chessset.PAWN, players.BlACK_PLAYER), (chessset.PAWN, players.BlACK_PLAYER),
             (chessset.PAWN, players.BlACK_PLAYER), (chessset.PAWN, players.BlACK_PLAYER), (chessset.PAWN, players.BlACK_PLAYER), (chessset.PAWN, players.BlACK_PLAYER)],
            [(chessset.ROOK, players.BlACK_PLAYER), (chessset.KNIGHT, players.BlACK_PLAYER), (chessset.BISHOP, players.BlACK_PLAYER), (chessset.QUEEN, players.BlACK_PLAYER), (chessset.KING, players.BlACK_PLAYER), (chessset.BISHOP, players.BlACK_PLAYER), (chessset.KNIGHT, players.BlACK_PLAYER), (chessset.ROOK, players.BlACK_PLAYER)]]
