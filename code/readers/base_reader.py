__author__ = 'Nikhil Pandey'

"""
file: base_reader.py
Author: Nikhil Pandey np7803@rit.edu
Description: Base Reader
"""

import os
import io


class BaseReader(object):

    def __init__(self, file_name):
        """
        Read and set up.
        :param file_name: Name of the file or String like input
        """
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
        """
        Get the number of rows.
        :return: Returns the number of rows.
        """
        return self._row_count

    def get_column_count(self):
        """
        Get the number of columns.
        :return: Returns the number of columns.
        """
        return self._column_count

    def get_cells(self):
        """
        Get the cells.
        :return: Return the cells.
        """
        return self._cells

    def get_cell(self, row, col):
        """
        Get cell at given row and column.
        :param row: The row.
        :param col: The col.
        :return: The cell at given row and column.
        """
        return self._cells[row][col]

    def __str__(self):
        """
        String representation of the grid.
        :return: Returns the string representation of the grid.
        """
        input_grid = self._input_grid
        for row in self._cells:
            for cell in row:
                input_grid[cell.get_row() * 2 + 1][
                    cell.get_column() * 2 + 1] = str(
                    cell.get_value()) if cell.has_value() else '.'
        return '%d %d\n%s' % (self._row_count, self._column_count,
                              '\n'.join([''.join(x) for x in input_grid]))
