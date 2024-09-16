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

class Board:
    """Generates boards"""
    def __init__(self, pieces: list, size: tuple = (8, 8)):

        self.tiles = np.full(size, ".")
        for piece in pieces:
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


if __name__ == "__main__":
    example_pieces = [King((0, 4))]
    board = Board(example_pieces)
    board.print_board()
