from tkinter import *
from chess_GUI import chessBoard
from piece import piece


root = Tk()

pawn_white = PhotoImage(file="pieces/pawn_white.gif")
pawn_black = PhotoImage(file="pieces/pawn_black.gif")
knight_white = PhotoImage(file="pieces/knight_white.gif")
knight_black = PhotoImage(file="pieces/knight_black.gif")
bishop_white = PhotoImage(file="pieces/bishop_white.gif")
bishop_black = PhotoImage(file="pieces/bishop_black.gif")
rook_white = PhotoImage(file="pieces/rook_white.gif")
rook_black = PhotoImage(file="pieces/rook_black.gif")
queen_white = PhotoImage(file="pieces/queen_white.gif")
queen_black = PhotoImage(file="pieces/queen_black.gif")
king_white = PhotoImage(file="pieces/king_white.gif")
king_black = PhotoImage(file="pieces/king_black.gif")

# pawn = 1, knight = 2, bishop = 3, rook = 4, queen = 5, king = 6
initial_position = [piece(rook_white, 0, 0), piece(knight_white, 1, 0), piece(bishop_white, 2, 0), piece(queen_white, 3, 0), piece(king_white, 4, 0),
                    piece(bishop_white, 5, 0), piece(knight_white, 6, 0), piece(rook_white, 7, 0),
                    piece(pawn_white, 0, 1), piece(pawn_white, 1, 1), piece(pawn_white, 2, 1), piece(pawn_white, 3, 1), piece(pawn_white, 4, 1),
                    piece(pawn_white, 5, 1), piece(pawn_white, 6, 1), piece(pawn_white, 7, 1),
                    piece(pawn_black, 0, 6), piece(pawn_black, 1, 6), piece(pawn_black, 2, 6), piece(pawn_black, 3, 6), piece(pawn_black, 4, 6),
                    piece(pawn_black, 5, 6), piece(pawn_black, 6, 6), piece(pawn_black, 7, 6),
                    piece(rook_black, 0, 7), piece(knight_black, 1, 7), piece(bishop_black, 2, 7), piece(queen_black, 3, 7), piece(king_black, 4, 7),
                    piece(bishop_black, 5, 7), piece(knight_black, 6, 7), piece(rook_black, 7, 7)]

board = chessBoard(root, "Chess GUI", initial_position)

root.mainloop()
