__author__ = 'Nikhil Pandey'

"""
file: cell.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Cell
"""


class Cell(object):

    def __init__(self, row, col, value):
        """
        Init cell.
        :param row: The row.
        :param col: The col.
        :param value: The value or None
        """
        self.row = row
        self.col = col
        self.possible_moves = set()
        self.region = None
        self.value = value
        self.tries = 0
        self.next_move = None

    def __eq__(self, other):
        """
        Returns if it is equal to another cell.
        :param other: Another cell.
        :return: True if both are the same cell else False
        """
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        """
        Returns the hash of the cell.
        :return: The hash.
        """
        return hash((self.row, self.col))

    def __repr__(self):
        """
        Returns the representation of the cell.
        :return: The representation of the cell.
        """
        return 'Cell(row=%d,col=%d,n=%s,value=%s,moves=%s)' % (
            self.row, self.col, self.next_move, self.value,
            self.possible_moves)
