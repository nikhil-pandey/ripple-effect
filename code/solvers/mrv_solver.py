__author__ = 'Nikhil Pandey'

"""
file: mrv_solver.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Brute Force Solver Class
"""

from .base_solver import BaseSolver
from helpers import *


class MRVSolver(BaseSolver):

    def __init__(self):
        print("Using MRV")

    @count
    def solve(self, grid):
        print("Call count: ", self.solve.calls)
        cell = grid.get_next_mrv_cell()

        if cell is None:
            if grid.is_solved():
                return grid

            return None

        for move in cell.get_possible_moves():
            try:
                cell.assign_value(move)
            except ValueError:
                continue

            cell.room.remove_possible_move(cell.value, cell)
            removed, should_continue = grid.recompute_moves(cell)

            if should_continue:
                solution = self.solve(grid)
                if solution:
                    return solution

            cell.room.add_possible_move(move, cell)
            grid.patch_removed_values(removed)

        cell.assign_value(None)
        return None
