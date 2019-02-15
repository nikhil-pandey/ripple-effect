__author__ = 'Nikhil Pandey'

"""
file: __main__.py
Author: Nikhil Pandey np7803@rit.edu
Description: 
"""

from solvers import *
from readers import *
from comparators import *
from validators import *
from pruners import *
import logging

# logging.basicConfig(level=# logging.DEBUG)


log = []
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
            log
        )
    elif i == '2':
        solver = Solver(
            next_mrv_cell,
            default_next_move,
            localized_validator,
            forward_pruner,
            log
        )
    elif i == '3':
        solver = Solver(
            next_mrv_cell,
            default_next_move,
            localized_validator,
            forward_pruner,
            log
        )
    elif i == '4':
        solver = Solver(
            next_mrv_cell,
            default_next_move,
            localized_validator,
            forward_pruner,
            log
        )
    elif i == '5':
        solver = Solver(
            next_human_like_mrv_cell,
            human_like_next_move,
            localized_validator,
            forward_pruner,
            log
        )
    else:
        continue

    file_name = input('Enter the file name: ').strip()
    break

grid = GridReader(file_name)
initial_grid = GridReader(str(grid))
solved_grid = solver.solve(grid)
# with open('steps.log', 'w') as f:
#     f.writelines([str(x) + '\n' for x in log])

print(solved_grid)

# from plotter import Plotter
# p = Plotter(initial_grid, 1, log)
# # p.show_grid()
# p.animate()