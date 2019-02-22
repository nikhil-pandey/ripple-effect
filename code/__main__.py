__author__ = 'Nikhil Pandey'

"""
file: __main__.py
Author: Nikhil Pandey np7803@rit.edu
Description: Ripple effect solver.
"""

from solvers import *
from readers import *
from comparators import *
from validators import *
from pruners import *
import time


# import logging
# logging.basicConfig(level=# logging.DEBUG)


def ask(options):
    print(options['prompt'])
    for idx, option in options['options'].items():
        print('%s: %s' % (idx, option.__name__))

    answer = int(input('>'))
    if answer:
        return options['options'][answer]

    return ask(options)


inputs = [
    {
        'prompt': 'How do you want to select the next cell?',
        'options': {
            1: next_empty_cell,
            2: next_mrv_cell,
            3: next_human_like_mrv_cell,
        }
    },
    {
        'prompt': 'How do you want to select the next value?',
        'options': {
            1: default_next_move,
            2: human_like_next_move,
        }
    },
    {
        'prompt': 'Which validator do you want to use?',
        'options': {
            1: naive_validator,
            2: localized_validator,
        }
    },
    {
        'prompt': 'Which pruner do you want to use?',
        'options': {
            1: default_pruner,
            2: value_pruner,
            3: forward_pruner,
        }
    },
]

log = []

solver = Solver(
    ask(inputs[0]),
    ask(inputs[1]),
    ask(inputs[2]),
    ask(inputs[3]),
    log
)

grid = GridReader(input('Enter the file name: ').strip())

start_time = time.time()
solved_grid = solver.solve(grid)
elapsed_time = time.time() - start_time
print(solved_grid)
print('Solved in %s seconds' % (elapsed_time))
# from plotter import Plotter
# p = Plotter(solved_grid, log)
# p.show_solution()
