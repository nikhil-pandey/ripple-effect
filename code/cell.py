__author__ = 'Nikhil Pandey'

"""
file: cell.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Exmaple Description
"""
import logging

class Cell(object):

    def __init__(self, row, col, value):
        self._row = row
        self._col = col
        self._possible_moves = set()
        self._room = None
        self._value = value
        self._tries = 0
        self._next_move = None

    def get_row(self):
        return self._row

    def get_column(self):
        return self._col

    def assign_room(self, room):
        # logging.debug('CELL: Adding Room: %s to Cell: %s' % (room, self))
        self._room = room

    def add_move(self, val):
        # logging.debug('CELL: Adding Move: %d to Cell: %s' % (val, self))
        self._possible_moves.add(val)
        # logging.debug('CELL: Added Move: %d to Cell: %s' % (val, self))

    def remove_move(self, val):
        # logging.debug('CELL: Removing Move: %d from Cell: %s' % (val, self))
        self._possible_moves.discard(val)
        # logging.debug('CELL: Removed Move: %d from Cell: %s' % (val, self))

    def get_move_count(self):
        return len(self._possible_moves)

    def has_moves(self):
        return self.get_move_count() > 0

    def assign_value(self, val):
        # logging.debug('CELL: Assigning value: %s to Cell: %s' % (val, self))
        # logging.debug('CELL: Previous number of assignments: %d' % (self._tries))
        self._tries += 1
        self._value = val

    def has_value(self):
        return self._value is not None

    def get_moves(self):
        return self._possible_moves

    def get_room(self):
        return self._room

    def get_value(self):
        return self._value

    def get_tries(self):
        return self._tries

    def assign_next_move(self, number):
        # logging.debug('CELL: Assigning next move: %d to Cell: %s' % (number, self))
        self._next_move = number

    def remove_next_move(self):
        # logging.debug('CELL: Removing next move: %s from Cell: %s' % (self._next_move, self))
        self._next_move = None

    def get_next_move(self):
        return self._next_move

    def __eq__(self, other):
        return self._row == other._row and self._col == other._col

    def __hash__(self):
        return hash((self._row, self._col))

    def __repr__(self):
        return 'Cell(row=%d,col=%d,n=%s,value=%s,moves=%s)' % (self._row, self._col, self._next_move, self._value, self._possible_moves )
