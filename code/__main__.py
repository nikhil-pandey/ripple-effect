__author__ = 'Nikhil Pandey'

"""
file: __main__.py
Author: Nikhil Pandey np7803@rit.edu
Description: Maze solver
"""

from solvers import *
from readers import *
from comparators import *
from validators import *
from pruners import *

while True:
    print('Which solver do you want to use?')
    print('1: Brute Force Solver')
    print('2: Vanilla MRV')
    print('3: MRV and track numbers')
    print('4: MRV and track numbers and forward checking')
    print(
        '5: MRV and track numbers and forward checking and human-like '
        'checking')
    i = input('>')

    if i == '1':
        solver = Solver(
            next_empty_cell,
            default_next_move,
            naive_validator,
            forward_pruner,
        )
    elif i == '2':
        solver = Solver(
            next_mrv_cell,
            default_next_move,
            localized_validator,
            forward_pruner,
        )
    elif i == '3':
        solver = Solver(
            next_mrv_cell,
            default_next_move,
            localized_validator,
            forward_pruner,
        )
    elif i == '4':
        solver = Solver(
            next_mrv_cell,
            default_next_move,
            localized_validator,
            forward_pruner,
        )
    elif i == '5':
        solver = Solver(
            next_mrv_cell,
            default_next_move,
            localized_validator,
            default_pruner,
        )
    else:
        continue

    file_name = input('Enter the file name: ').strip()
    break

grid = GridReader(file_name)
solved_grid = solver.solve(grid)
print('Called ', Solver.solve.calls)
# from visualizer import Visualizer
# vis = Visualizer(solved_grid, 1, None, Solver.solve.grids)
# vis.show_grid()
# vis.animate_grid_solution()