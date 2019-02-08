__author__ = 'Nikhil Pandey'

"""
file: brute_force_solver.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Brute Force Solver Class
"""

from .base_solver import BaseSolver
from helpers import *
from readers import *


class BruteForceSolver(BaseSolver):

    def __init__(self):
        print("Using brute force")

    @count
    def solve(self, grid):

        if isinstance(grid, BitReader):
            return self.bit_wise_solve(grid)

        return self.grid_solve(grid)

    def bit_wise_solve(self, grid):

        cell = grid.get_next_empty_pos()

        if cell is None:
            if grid.is_solved():
                return grid

            return None

        for val in grid.get_possible_moves_for_pos(cell):

            if not grid.is_move_valid(cell, val):
                continue

            grid.set_value_for_pos(cell, val)

            solution = self.bit_wise_solve(grid)

            if solution:
                return solution

        grid.set_value_for_pos(cell, None)
        return None

    def grid_solve(self, grid):
        cell = grid.get_next_empty_cell()

        if cell is None:
            if grid.is_solved():
                return grid

            return None

        for val in cell.get_possible_moves():

            try:
                cell.assign_value(val)
            except ValueError:
                continue

            solution = self.solve(grid)

            if solution:
                return solution

        cell.assign_value(None)
        return None
