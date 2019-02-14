__author__ = 'Nikhil Pandey'

"""
file: grid_reader.py
Author: Nikhil Pandey np7803@rit.edu
Description: Maze solver
"""

import os
import io


class BaseReader(object):

    def __init__(self, file_name):
        if os.path.exists(file_name):
            f = open(file_name, 'r')
        else:
            f = io.StringIO(file_name)

        self._row_count, self._column_count = (int(x) for x in
                                               f.readline().split())
        self._input_grid = [list(l.rstrip('\n')) for l in f.readlines()]

        self._cell_count = self._row_count * self._column_count

        self._cells = [[None for _ in range(0, self._column_count)] for __ in
                       range(0, self._row_count)]

        f.close()

    def get_row_count(self):
        return self._row_count

    def get_column_count(self):
        return self._column_count

    def get_cells(self):
        return self._cells

    def get_cell(self, row, col):
        return self._cells[row][col]

    def __str__(self):
        input_grid = self._input_grid
        for row in self._cells:
            for cell in row:
                input_grid[cell.get_row() * 2 + 1][cell.get_column() * 2 + 1] = str(
                    cell.get_value()) if cell.has_value() else '.'
        return '%d %d\n%s' % (self._row_count, self._column_count, '\n'.join([''.join(x) for x in input_grid]))
