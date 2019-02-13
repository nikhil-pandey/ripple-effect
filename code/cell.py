__author__ = 'Nikhil Pandey'

"""
file: cell.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Exmaple Description
"""


class Cell(object):

    def __init__(self, row, col, value):
        self._row = row
        self._col = col
        self._possible_moves = set()
        self._room = None
        self._value = value

    def get_row(self):
        return self._row

    def get_column(self):
        return self._col

    def assign_room(self, room):
        self._room = room

    def add_move(self, val):
        self._possible_moves.add(val)

    def remove_move(self, val):
        self._possible_moves.discard(val)

    def get_move_count(self):
        return len(self._possible_moves)

    def has_moves(self):
        return self.get_move_count() > 0

    def assign_value(self, val):
        self._value = val

    def has_value(self):
        return self._value is not None

    def get_moves(self):
        return self._possible_moves

    def get_room(self):
        return self._room

    def get_value(self):
        return self._value

    def __eq__(self, other):
        return self._row == other._row and self._col == other._col

    def __hash__(self):
        return hash((self._row, self._col))

    def __repr__(self):
        return 'Cell(%d,%d,%s)' % (self._row, self._col, str(self._value) if not None else 'x')

    def __str__(self):
        return "Cell(%d)" % (self._value if self._value else 0)
