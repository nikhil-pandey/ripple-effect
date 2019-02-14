__author__ = 'Nikhil Pandey'

"""
file: solver.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Solver Class
"""

from helpers import *
from pruners.forward_pruner import patch_removed_values


class Solver(object):

    def __init__(self, cell_selector, move_selector, validator, pruner):
        self._cell_selector = cell_selector
        self._move_selector = move_selector
        self._validator = validator
        self._pruner = pruner

    def solve(self, grid):
        cell = self._cell_selector(grid.get_cells())

        if cell is None:
            return grid

        for move in self._move_selector(cell):
            if not self._validator(grid, cell, move):
                continue

            cell.assign_value(move)
            cell.get_room().remove_move(cell.get_value(), cell)

            pruned, should_continue = self._pruner(grid, cell)

            if should_continue:
                solution = self.solve(grid)
                if solution:
                    return solution

            patch_removed_values(pruned)

        cell.assign_value(None)

        return None
