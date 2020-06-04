import chessset 
import players

empty_board = [[None] * 8 for i in range(8)]

default_board = [[(chessset.ROOK, players.WHITE_PLAYER), (chessset.KNIGHT, players.WHITE_PLAYER), (chessset.BISHOP, players.WHITE_PLAYER), (chessset.QUEEN, players.WHITE_PLAYER), (chessset.KING, players.WHITE_PLAYER), (chessset.BISHOP, players.WHITE_PLAYER), (chessset.KNIGHT, players.WHITE_PLAYER), (chessset.ROOK, players.WHITE_PLAYER)],
            [(chessset.PAWN, players.WHITE_PLAYER), (chessset.PAWN, players.WHITE_PLAYER), (chessset.PAWN, players.WHITE_PLAYER), (chessset.PAWN, players.WHITE_PLAYER),
             (chessset.PAWN, players.WHITE_PLAYER), (chessset.PAWN, players.WHITE_PLAYER), (chessset.PAWN, players.WHITE_PLAYER), (chessset.PAWN, players.WHITE_PLAYER)],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [(chessset.PAWN, players.BLACK_PLAYER), (chessset.PAWN, players.BLACK_PLAYER), (chessset.PAWN, players.BLACK_PLAYER), (chessset.PAWN, players.BLACK_PLAYER),
             (chessset.PAWN, players.BLACK_PLAYER), (chessset.PAWN, players.BLACK_PLAYER), (chessset.PAWN, players.BLACK_PLAYER), (chessset.PAWN, players.BLACK_PLAYER)],
            [(chessset.ROOK, players.BLACK_PLAYER), (chessset.KNIGHT, players.BLACK_PLAYER), (chessset.BISHOP, players.BLACK_PLAYER), (chessset.QUEEN, players.BLACK_PLAYER), (chessset.KING, players.BLACK_PLAYER), (chessset.BISHOP, players.BLACK_PLAYER), (chessset.KNIGHT, players.BLACK_PLAYER), (chessset.ROOK, players.BLACK_PLAYER)]]






