__author__ = 'Nikhil Pandey'

"""
file: __main__.py
Author: Nikhil Pandey np7803@rit.edu
Description: Maze solver
"""

from game_grid import GameGrid
from solvers import *
import sys

if 'brute-force' in sys.argv:
    solver = BruteForceSolver()
elif 'mrv' in sys.argv:
    solver = MRVSolver(recompute_moves=True)
elif 'mrvfwd' in sys.argv:
    solver = MRVSolver(recompute_moves=True, forward_checking=True)
else:
    while True:
        print('Which solver do you want to use?')
        print('1: Brute Force Solver')
        print('2: Vanilla MRV')
        print('3: MRV and track numbers')
        print('4: MRV and track numbers and forward checking')
        i = input()

        if i == '1':
            solver = BruteForceSolver()
        elif i == '2':
            solver = MRVSolver()
        elif i == '3':
            solver = MRVSolver(recompute_moves=True)
        elif i == '4':
            solver = MRVSolver(recompute_moves=True,forward_checking=True)
        else:
            continue

        file_name = input('Enter the file name: ').strip()
        break

try:
    grid = GameGrid(file_name)
    grid.prepare_cells()
except (IndexError, FileNotFoundError):
    print('Usage: python3 __main__.py <grid_file>')
    sys.exit(1)

solved_grid = solver.solve(grid)

print(solved_grid)