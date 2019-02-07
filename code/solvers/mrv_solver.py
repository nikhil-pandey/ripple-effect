__author__ = 'Nikhil Pandey'

"""
file: mrv_solver.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Brute Force Solver Class
"""

from solver import Solver

class MRVSolver(Solver):

    def __init__(self, recompute_moves=False, forward_checking=False):
        print("Using MRV")
        self.recompute_moves = recompute_moves
        self.forward_checking = forward_checking

        if self.forward_checking:
            self.recompute_moves = True

    def solve(self, grid):

        cell = grid.get_next_mrv_cell()

        if cell is None:
            if grid.is_solved():
                return grid
            
            return None

        for val in cell.get_possible_moves():

            try:
                cell.assign_value(val)
            
                if self.recompute_moves:
                    removed = grid.recompute_moves(cell)

                if self.forward_checking and not grid.check_forward():
                    continue
            
            except ValueError:
                continue
            
            solution = self.solve(grid)

            if solution:
                return solution

            if self.recompute_moves:
                grid.patch_removed_values(removed)

        cell.assign_value(None)
        
        return None
