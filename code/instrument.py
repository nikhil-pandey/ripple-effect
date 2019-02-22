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

log = []

grids = [
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
        log
    ),
    Solver(
        next_human_like_mrv_cell,
        human_like_next_move,
        naive_validator,
        forward_pruner,
        log
    ),
    Solver(
        next_human_like_mrv_cell,
        human_like_next_move,
        localized_validator,
        value_pruner,
        log
    ),
    Solver(
        next_human_like_mrv_cell,
        human_like_next_move,
        localized_validator,
        forward_pruner,
        log
    ),
    # MRV Solvers
    Solver(
        next_mrv_cell,
        default_next_move,
        naive_validator,
        value_pruner,
        log
    ),
    Solver(
        next_mrv_cell,
        default_next_move,
        naive_validator,
        forward_pruner,
        log
    ),
    Solver(
        next_mrv_cell,
        default_next_move,
        localized_validator,
        value_pruner,
        log
    ),
    Solver(
        next_mrv_cell,
        default_next_move,
        localized_validator,
        forward_pruner,
        log
    ),
    # Brute Forcers
    Solver(
        next_empty_cell,
        default_next_move,
        naive_validator,
        default_pruner,
        log
    ),
    Solver(
        next_empty_cell,
        default_next_move,
        naive_validator,
        value_pruner,
        log
    ),
    Solver(
        next_empty_cell,
        default_next_move,
        naive_validator,
        forward_pruner,
        log
    ),
    Solver(
        next_empty_cell,
        default_next_move,
        localized_validator,
        forward_pruner,
        log
    ),
    Solver(
        next_empty_cell,
        default_next_move,
        localized_validator,
        value_pruner,
        log
    ),
    Solver(
        next_empty_cell,
        default_next_move,
        localized_validator,
        default_pruner,
        log
    ),
]

if __name__ == '__main__':
    f = open('out/results.csv', 'w')
    for grid_file in grids:
        print(grid_file)
        for solver in solvers:
            print('\t', solver)
            times = []
            count = 1 if 'mrv' not in str(solver) and 're18' in grid_file else 10
            for i in range(count):
                grid = GridReader(grid_file)
                start = time.time()
                solved_grid = solver.solve(grid)
                end = time.time()
                times.append(end-start)

                if i == count-1:
                    # -1, 0, 1, 2
                    # Removal, Solve call, Assignment, Validation
                    counter = [0, 0, 0, 0]
                    for item in log:
                        counter[item[0] + 1] += 1

                del grid, start, end, log[:]

            average_time = sum(times)/len(times)

            h = open(grid_file + '.sol', 'r')
            content = h.readlines()
            h.close()
            is_solution = str(solved_grid).strip() ==  (''.join(content)).strip()

            # File name, Solver, Clock Time (avg of 10 run in ms), Calls to Solve, Validation Checks, Total Assignments, Wrong Assignments, Solved
            f.write('%s|%s|%s|%s|%s|%s|%s|%s\n' % (grid_file, solver, average_time * 1000, counter[1], counter[3], counter[2], counter[0], is_solution))
            f.flush()
            del solved_grid, counter

    f.close()