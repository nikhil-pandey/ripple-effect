__author__ = 'Nikhil Pandey'

"""
file: mrv_solver.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Brute Force Solver Class
"""

from solver import Solver


class MRVSolver(Solver):

    def __init__(self):
        pass

    def solve(self, grid):
        
        cell = grid.get_next_mrv_cell()

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
