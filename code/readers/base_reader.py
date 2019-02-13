__author__ = 'Nikhil Pandey'

"""
file: grid_reader.py
Author: Nikhil Pandey np7803@rit.edu
Description: Maze solver
"""

import itertools
from cell import Cell
from room import Room


class BaseReader(object):

    def __init__(self, file_name):
        with open(file_name, 'r') as f:
            self._row_count, self._column_count = (int(x) for x in
                                                   f.readline().split())
            self._input_grid = [list(l.rstrip('\n')) for l in f.readlines()]

        self._cell_count = self._row_count * self._column_count

        self._cells = [[None for _ in range(0, self._column_count)] for __ in
                       range(0, self._row_count)]

        self._humane_check = True
        self._check_moves = True
        self._forward_checking = True

    def prepare(self):
        pass
