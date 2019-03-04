__author__ = 'Nikhil Pandey'

"""
file: instrument.py
Author: Nikhil Pandey np7803@rit.edu
Description: Instrument the process and record the statistics.
"""

from solvers import Solver
from readers import GridReader
from comparators import *
from validators import *
from pruners import *
import time
import numpy

CALL_TO_SOLVE = 0
TOTAL_MOVES = 1
FAILED_VALIDATION = 2
ASSIGNED_MOVES = 3
WRONG_MOVES = -1  # 4

counter = [0, 0, 0, 0, 0]

grids = [
    # 1 star
    'data/pp4391',
    'data/pp4396',
    'data/pp4479',

    # 2 Star
    'data/pp4521',
    'data/pp4392',
    'data/pp4397',
    'data/pp5151',
    'data/pp5512',
    'data/pp4483',
    'data/pp4810',
    'data/pp5509',
    'data/pp4508',
    'data/pp4467',
    'data/pp4402', # Special black boxes
    'data/pp6008',
    'data/pp4606',
    'data/pp4651',

    # 3 Star
    'data/pp4665',
    'data/pp4629',
    'data/pp4466',
    'data/pp5518',
    'data/pp4394',
    # 'data/pp5060',
    # 'data/pp4806',
    # 'data/pp4495',
    # 'data/pp4489',
    # 'data/pp4475',
    # 'data/pp4604',
    # 'data/pp4511',
    # 'data/pp4590',
    # 'data/pp4661',
    # 'data/pp5833',
    # 'data/pp4419',

    # 4 Star
    'data/pp4828',
    'data/pp4493',
    'data/pp4525',
    'data/pp4395',
    'data/pp4471',
    'data/pp5161',
    'data/pp4505',
    'data/pp4658',

    # Given
    'data/re0',
    'data/re1',
    'data/re10a',
    'data/re10b',
    'data/re18',
]

solvers = [
    # Human like solvers
    Solver(
        next_human_like_mrv_cell,
        human_like_next_move,
        naive_validator,
        value_pruner,
        count_log=counter
    ),
    Solver(
        next_human_like_mrv_cell,
        human_like_next_move,
        naive_validator,
        forward_pruner,
        count_log=counter
    ),
    Solver(
        next_human_like_mrv_cell,
        human_like_next_move,
        localized_validator,
        value_pruner,
        count_log=counter
    ),
    Solver(
        next_human_like_mrv_cell,
        human_like_next_move,
        localized_validator,
        forward_pruner,
        count_log=counter
    ),
    # MRV Solvers
    Solver(
        next_mrv_cell,
        default_next_move,
        naive_validator,
        value_pruner,
        count_log=counter
    ),
    Solver(
        next_mrv_cell,
        default_next_move,
        naive_validator,
        forward_pruner,
        count_log=counter
    ),
    Solver(
        next_mrv_cell,
        default_next_move,
        localized_validator,
        value_pruner,
        count_log=counter
    ),
    Solver(
        next_mrv_cell,
        default_next_move,
        localized_validator,
        forward_pruner,
        count_log=counter
    ),
    # Brute Forcers
    Solver(
        next_empty_cell,
        default_next_move,
        naive_validator,
        default_pruner,
        count_log=counter
    ),
    Solver(
        next_empty_cell,
        default_next_move,
        localized_validator,
        default_pruner,
        count_log=counter
    ),
    Solver(
        next_empty_cell,
        default_next_move,
        naive_validator,
        value_pruner,
        count_log=counter
    ),
    Solver(
        next_empty_cell,
        default_next_move,
        localized_validator,
        value_pruner,
        count_log=counter
    ),
    Solver(
        next_empty_cell,
        default_next_move,
        naive_validator,
        forward_pruner,
        count_log=counter
    ),
    Solver(
        next_empty_cell,
        default_next_move,
        localized_validator,
        forward_pruner,
        count_log=counter
    ),
]

if __name__ == '__main__':
    f = open('out/results.csv', 'w')
    for grid_file in grids:
        print(grid_file)
        for solver in solvers:
            print('\t', solver)
            times = []
            count = 10
            for i in range(count):
                for idx in range(len(counter)):
                    counter[idx] = 0
                start = time.time()
                grid = GridReader(grid_file)
                solved_grid = solver.solve(grid)
                end = time.time()
                print('\t\tRun %s: %s' % (i + 1, end - start))
                times.append(end - start)

            average_time = sum(times) / len(times)
            median_time = numpy.median(times)

            h = open(grid_file + '.sol', 'r')
            content = h.readlines()
            h.close()
            is_solution = str(solved_grid).strip() == (
                ''.join(content)).strip()

            # File name, Grid Size, Solver, Clock Time (avg of 10 run in ms), Median
            # Clock time,  Calls to Solve, Total Value Selection,
            # Failed Validation, Total Assignments, Wrong Moves, Solved, Exact
            f.write('%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s\n' % (
                grid_file,
                str(grid.row_count) + 'x' + str(grid.column_count),
                solver,
                average_time * 1000,
                median_time * 1000,
                counter[CALL_TO_SOLVE],
                counter[TOTAL_MOVES],
                counter[FAILED_VALIDATION],
                counter[ASSIGNED_MOVES],
                counter[WRONG_MOVES],
                solved_grid is not None,
                is_solution
            ))
            f.flush()

    f.close()
