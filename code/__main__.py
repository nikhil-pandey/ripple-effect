__author__ = 'Nikhil Pandey'

"""
file: __main__.py
Author: Nikhil Pandey np7803@rit.edu
Description: Maze solver
"""

from game_grid import GameGrid
from solvers.brute_force_solver import BruteForceSolver

grid = GameGrid()
grid.prepare_cells()

solver = BruteForceSolver()
solved_grid = solver.solve(grid)

print(solved_grid)