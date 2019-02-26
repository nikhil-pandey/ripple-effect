__author__ = 'Nikhil Pandey'

"""
file: instrument.py
Author: Nikhil Pandey np7803@rit.edu
Description: 
"""

from solvers import Solver
from readers import GridReader
from comparators import *
from validators import *
from pruners import *
import time
import numpy

counter = [0, 0, 0, 0]

grids = [
    'data/re0',
    'data/re1',
    'data/re10a',
    'data/re10b',
    'data/pp4395',
    'data/pp4471',
    'data/pp4493',
    'data/pp4505',
    'data/pp4525',
    'data/pp4658',
    'data/pp4828',
    'data/pp5161',
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
                grid = GridReader(grid_file)
                start = time.time()
                solved_grid = solver.solve(grid)
                end = time.time()
                print('\t\tRun %s: %s' % (i + 1, end - start))
                times.append(end - start)

                del grid, start, end

            average_time = sum(times) / len(times)
            median_time = numpy.median(times)

            h = open(grid_file + '.sol', 'r')
            content = h.readlines()
            h.close()
            is_solution = str(solved_grid).strip() == (
                ''.join(content)).strip()

            # File name, Solver, Clock Time (avg of 10 run in ms), Median
            # Clock time,  Calls to Solve, Validation Checks,
            # Total Assignments, Wrong Assignments, Solved
            f.write('%s|%s|%s|%s|%s|%s|%s|%s|%s\n' % (
                grid_file, solver, average_time * 1000, median_time * 1000, counter[1], counter[3],
                counter[2], counter[0], is_solution))
            f.flush()
            del solved_grid

    f.close()
