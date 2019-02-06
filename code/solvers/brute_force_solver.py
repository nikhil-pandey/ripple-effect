__author__ = 'Nikhil Pandey'

"""
file: brute_force_solver.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Brute Force Solver Class
"""

from copy import deepcopy

from solver import Solver

class BruteForceSolver(Solver):

    def __init__(self):
        pass

    def solve(self, grid):

        if not grid.is_valid():
            return None
        
        if grid.is_complete():
            return grid

        cell = grid.get_next_empty_cell()

        for val in cell.get_possible_moves():
            cell.value = val
            solution = self.solve(grid)

            if solution:
                return solution

        cell.value = None
        
        return None
