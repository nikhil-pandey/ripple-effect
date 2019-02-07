__author__ = 'Nikhil Pandey'

"""
file: brute_force_solver.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Brute Force Solver Class
"""

from .base_solver import BaseSolver

class BruteForceSolver(BaseSolver):

    def __init__(self):
        print("Using brute force")
        pass

    def solve(self, grid):


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
