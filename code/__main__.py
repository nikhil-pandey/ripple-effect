__author__ = 'Nikhil Pandey'

"""
file: __main__.py
Author: Nikhil Pandey np7803@rit.edu
Description: Maze solver
"""

from game_grid import GameGrid
from solvers.brute_force_solver import BruteForceSolver
from solvers.mrv_solver import MRVSolver

grid = GameGrid()
grid.prepare_cells()

solver = MRVSolver()
solved_grid = solver.solve(grid)

print(solved_grid)