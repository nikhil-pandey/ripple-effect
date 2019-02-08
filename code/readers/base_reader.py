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
            self.row_count, self.column_count = (int(x) for x in
                                                 f.readline().split())
            self.input_grid = [list(l.rstrip('\n')) for l in f.readlines()]

        self.cells = [[None for _ in range(0, self.column_count)] for __ in
                      range(0, self.row_count)]

        self.humane_check = True
        self.check_moves = True
        self.forward_checking = True

    def prepare(self):
        pass
