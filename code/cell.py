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
        """
        Init cell.
        :param row: The row.
        :param col: The col.
        :param value: The value or None
        """
        self._row = row
        self._col = col
        self._possible_moves = set()
        self._room = None
        self._value = value
        self._tries = 0
        self._next_move = None

    def get_row(self):
        """
        Returns the row.
        :return: The row.
        """
        return self._row

    def get_column(self):
        """
        Returns the column.
        :return: The column.
        """
        return self._col

    def assign_room(self, room):
        """
        Assigns a room
        :param room: The room to assign.
        :return: None
        """
        # logging.debug('CELL: Adding Room: %s to Cell: %s' % (room, self))
        self._room = room

    def add_move(self, val):
        """
        Adds a possible move.
        :param val: The move to add.
        :return: None
        """
        # logging.debug('CELL: Adding Move: %d to Cell: %s' % (val, self))
        self._possible_moves.add(val)
        # logging.debug('CELL: Added Move: %d to Cell: %s' % (val, self))

    def remove_move(self, val):
        """
        Removes the possible move.
        :param val: The move to remove.
        :return: None
        """
        # logging.debug('CELL: Removing Move: %d from Cell: %s' % (val, self))
        self._possible_moves.discard(val)
        # logging.debug('CELL: Removed Move: %d from Cell: %s' % (val, self))

    def get_move_count(self):
        """
        Returns the total possible moves count.
        :return: The count of possible moves.
        """
        return len(self._possible_moves)

    def has_moves(self):
        """
        Returns if the cell has possible moves.
        :return: True if moves are possible else False
        """
        return self.get_move_count() > 0

    def assign_value(self, val):
        """
        Assigns a value to the cell.
        :param val: The value.
        :return: None
        """
        # logging.debug('CELL: Assigning value: %s to Cell: %s' % (val, self))
        # logging.debug('CELL: Previous number of assignments: %d' % (
        # self._tries))
        self._tries += 1
        self._value = val

    def has_value(self):
        """
        Checks if a value has been assigned.
        :return: None
        """
        return self._value is not None

    def get_moves(self):
        """
        Returns the possible moves.
        :return: Set of possible moves.
        """
        return self._possible_moves

    def get_room(self):
        """
        Returns the Room the cell belongs to.
        :return: The room.
        """
        return self._room

    def get_value(self):
        """
        Returns the value of the cell.
        :return: The value.
        """
        return self._value

    def get_tries(self):
        """
        Returns the umber of times a value has been assigned to the cell.
        :return: The number of times a value has been assigned to the cell.
        """
        return self._tries

    def assign_next_move(self, number):
        """
        Assigns a prioritized next move.
        :param number: The next move.
        :return: None
        """
        # logging.debug('CELL: Assigning next move: %d to Cell: %s' % (
        # number, self))
        self._next_move = number

    def remove_next_move(self):
        """
        Removes the prioritized next move.
        :return: None
        """
        # logging.debug('CELL: Removing next move: %s from Cell: %s' % (
        # self._next_move, self))
        self._next_move = None

    def get_next_move(self):
        """
        Returns the prioritized next move
        :return: The prioritized next move.
        """
        return self._next_move

    def __eq__(self, other):
        """
        Returns if it is equal to another cell.
        :param other: Another cell.
        :return: True if both are the same cell else False
        """
        return self._row == other._row and self._col == other._col

    def __hash__(self):
        """
        Returns the hash of the cell.
        :return: The hash.
        """
        return hash((self._row, self._col))

    def __repr__(self):
        """
        Returns the representation of the cell.
        :return: The representation of the cell.
        """
        return 'Cell(row=%d,col=%d,n=%s,value=%s,moves=%s)' % (
            self._row, self._col, self._next_move, self._value,
            self._possible_moves)
