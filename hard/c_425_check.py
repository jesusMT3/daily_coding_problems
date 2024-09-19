"""
You are presented with an 8 by 8 matrix representing the 
positions of pieces on a chess board. 
The only pieces on the board are the black king and various white pieces.
Given this matrix, determine whether the king is in check.

For example, given the following matrix:

...K....
........
.B......
......P.
.......R
..N.....
........
.....Q..

You should return True, since the bishop is attacking the king diagonally.
"""
from copy import copy
import numpy as np

class Piece:
    """Base class for a chess piece"""
    def __init__(self, position = tuple):
        self._position = position
        self._value = "F"

    def available_moves(self):
        """Returns the available moves for the piece"""
        raise NotImplementedError

    def get_position(self):
        """Returns the position of the piece"""
        return self._position

    def get_value(self):
        """Returns the value of the piece"""
        return self._value

    def __repr__(self):
        return f"{self.get_value()} {self.get_position()}"

class King(Piece):
    """Class for generating king pieces"""
    def __init__(self, position: tuple):
        super().__init__(position)
        self._value = "K"

    def available_moves(self):
        return None

class Pawn(Piece):
    """Class for generating pawn pieces"""
    def __init__(self, position: tuple):
        super().__init__(position)
        self._value = "P"

    def available_moves(self):
        row, column = self.get_position()
        moves = []
        moves.append((row - 1, column - 1))
        moves.append((row - 1, column + 1))
        for move in copy(moves):
            if move[0] not in range(8) or move[1] not in range(8):
                moves.remove(move)

        return moves

class Rook(Piece):
    """Class for generating rook pieces"""
    def __init__(self, position: tuple):
        super().__init__(position)
        self._value = "R"

    def available_moves(self):
        row, column = self.get_position()
        moves = []
        for i in range(8):
            moves.append((row, i))
            moves.append((i, column))

        for move in copy(moves):
            if move == self.get_position():
                moves.remove(move)

        return moves

class Bishop(Piece):
    """Class for generating bishop pieces"""
    def __init__(self, position: tuple):
        super().__init__(position)
        self._value = "B"

    def available_moves(self):
        row, column = self.get_position()
        moves = []
        for i in range(8):
            distance = abs(i - row)
            moves.append((i, column + distance))
            moves.append((i, column - distance))

        for move in copy(moves):
            if move[0] not in range(8) or move[1] not in range(8):
                moves.remove(move)
            if move == self.get_position():
                moves.remove(move)

        return moves

class Queen(Piece):
    """Class for generating queen pieces"""
    def __init__(self, position: tuple):
        super().__init__(position)
        self._value = "Q"

    def available_moves(self):
        row, column = self.get_position()
        moves = []
        for i in range(8):
            distance = abs(i - row)
            moves.append((i, column + distance))
            moves.append((i, column - distance))
            moves.append((row, i))
            moves.append((i, column))

        for move in copy(moves):
            if move[0] not in range(8) or move[1] not in range(8):
                moves.remove(move)
            if move == self.get_position():
                moves.remove(move)

        return moves

class Knight(Piece):
    """Class for generating knight pieces"""
    def __init__(self, position: tuple):
        super().__init__(position)
        self._value = "N"

    def available_moves(self):
        row, column = self.get_position()
        moves = []
        moves.append((row - 2, column + 1))
        moves.append((row - 2, column - 1))
        moves.append((row + 2, column + 1))
        moves.append((row + 2, column - 1))
        moves.append((row - 1, column + 2))
        moves.append((row - 1, column - 2))
        moves.append((row + 1, column + 2))
        moves.append((row + 1, column - 2))

        for move in copy(moves):
            if move[0] not in range(8) or move[1] not in range(8):
                moves.remove(move)

        print(moves)
        return moves

class Board:
    """Generates boards"""
    def __init__(self, pieces: list, size: tuple = (8, 8)):
        self._pieces = pieces
        self.tiles = np.full(size, ".")
        for piece in pieces:
            if piece.get_value() == "K":
                self.king = piece
            row, column = piece.get_position()
            self.tiles[row, column] = piece.get_value()
        if "K" not in self.tiles:
            raise ValueError(f"Pieces must contain a king. {pieces}")

    def print_board(self):
        """Prints the board"""
        for row in self.tiles:
            print(row)

    def is_check(self):
        """returns True if the king is in check"""
        all_movements = []
        king_position = self.king.get_position()

        for piece in self._pieces:
            piece_movements = piece.available_moves()

            if piece.get_value() != "K":
                for movement in piece_movements:
                    all_movements.append(movement)

        if king_position in all_movements:
            return True

        return False


if __name__ == "__main__":
    example_pieces = [King((0, 3)),
                      Pawn((3, 6)),
                      Rook((4, 7)),
                      Bishop((2, 1)),
                      Queen((7, 5)),
                      Knight((5, 2))]
    board = Board(example_pieces)
    board.print_board()
    print(board.is_check())
