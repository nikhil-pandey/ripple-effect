__author__ = 'Nikhil Pandey'

"""
file: __main__.py
Author: Nikhil Pandey np7803@rit.edu
Description: Ripple effect solver.
"""

from solvers import *
from readers import *
from cell_selectors import *
from move_selectors import *
from validators import *
from pruners import *
from plotter import Plotter
import time


def ask(options):
    print(options['prompt'])
    for idx, option in options['options'].items():
        print('%s: %s' % (idx, option.__name__))

    answer = int(input('> '))
    if answer:
        return options['options'][answer]

    return ask(options)


inputs = [
    {
        'prompt': 'Which solver do you want to use?',
        'options': {
            1: next_empty_cell,
            2: next_mrv_cell,
            3: next_forward_pruning_mrv_cell,
            4: next_human_like_mrv_cell,
        }
    },
    {
        'prompt': 'Which pruner do you want to use?',
        'options': {
            1: default_pruner,
            2: forward_pruner,
        }
    },
]

counter = [0, 0, 0, 0, 0]
log = []

which_solver = ask(inputs[0])
pruner = default_pruner if which_solver in [next_empty_cell, next_mrv_cell] else forward_pruner
file_name = input('Enter the file name: ').strip()

solver = Solver(
    which_solver,
    default_next_move,
    localized_validator,
    pruner,
    log,
    counter
)

grid = GridReader(file_name)
grid_copy = GridReader(str(grid))

start_time = time.time()
solved_grid = solver.solve(grid)
elapsed_time = time.time() - start_time

print(solved_grid)
print('Solved in %s seconds' % (elapsed_time))
print('Called Solve Method: %s times' % (counter[0]))
print('Total Moves Evaluated: %s' % (counter[1]))
print('Moves whose Validation Failed: %s' % (counter[2]))
print('Assigned Moves: %s times' % (counter[3]))
print('Wrong Moves Assigned: %s times' % (counter[4]))

if input('Do you want to show the solution using matplotlib? [y/n] ') == 'y':
    p = Plotter(solved_grid)
    p.show_solution()

if input('Do you want to generate a video using matplotlib? [y/n] ') == 'y':
    file_name = None
    if input('\tDo you want to save the video to a file? [y/n] ') == 'y':
        file_name = input('\t\tOutput file name: ')
    p = Plotter(grid_copy, log, out_file=file_name)
    p.animate()
