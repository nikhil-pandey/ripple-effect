__author__ = 'Nikhil Pandey'

"""
file: file.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Exmaple Description
"""


class Cell(object):

    def __init__(self, grid, row, col, value):
        self.grid = grid
        self.row = row
        self.col = col
        self.possible_moves = set()
        self.room = None
        self.value = None

        if value != '.':
            self.value = int(value)

    def assign_room(self, room):
        self.room = room

    def add_possible_move(self, val):
        self.possible_moves.add(val)

    def assign_value(self, val):
        if val is None:
            self.value = None
            return

        old_val = self.value
        self.value = val

        if self.grid.validate_rows_cols(self) and self.room.is_valid():
            return

        self.value = old_val
        raise ValueError()

    def has_value(self):
        return self.value is not None

    def get_possible_moves(self):
        return self.possible_moves

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def __str__(self):
        # return "Cell(%d, [%s])" % (self.value if self.value else 0, ',
        # '.join([str(x) for x in self.possible_moves]))
        return "Cell(%d)" % (self.value if self.value else 0)
