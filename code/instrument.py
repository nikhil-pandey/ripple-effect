__author__ = 'Nikhil Pandey'

"""
file: instrument.py
Author: Nikhil Pandey np7803@rit.edu
Description: Instrument the process and record the statistics.
"""

from solvers import Solver
from readers import GridReader
from cell_selectors import *
from move_selectors import *
from validators import *
from pruners import *
import time
import numpy

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
    'data/pp6008',
    'data/pp4606',
    'data/pp4651',

    # 3 Star
    'data/pp4665',
    'data/pp4629',
    'data/pp4466',
    'data/pp5518',
    'data/pp4394',
    'data/pp5060',
    'data/pp4806',
    'data/pp4489',
    'data/pp4604',
    'data/pp4511',
    'data/pp4590',
    'data/pp5833',

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

solvers = {
    # Human like solvers
    'Human': Solver(
        next_human_like_mrv_cell,
        human_like_next_move,
        localized_validator,
        forward_pruner,
        count_log=counter
    ),
    # Optimized MRV Solvers
    'OMRV': Solver(
        next_optimized_mrv_cell,
        default_next_move,
        localized_validator,
        forward_pruner,
        count_log=counter
    ),
    # MRV Solvers
    'MRVFWD': Solver(
        next_mrv_cell,
        default_next_move,
        localized_validator,
        forward_pruner,
        count_log=counter
    ),
    'MRV': Solver(
        next_mrv_cell,
        default_next_move,
        localized_validator,
        default_pruner,
        count_log=counter
    ),
    # Brute Forcers
    'BF': Solver(
        next_empty_cell,
        default_next_move,
        localized_validator,
        default_pruner,
        count_log=counter
    ),
}

if __name__ == '__main__':
    f = open('out/results.csv', 'w')
    f.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (
        'File',
        'Grid Size',
        'Number of Cells',
        'Number of Regions',
        'Region with Size 1',
        'Region with Size 2',
        'Region with Size 3',
        'Region with Size 4',
        'Region with Size 5',
        'Region with Size 6',
        'Region with Size 7',
        'Region with Size 8',
        'Region with Size 9',
        'Solver',
        'Mean Clock Time (ms)',
        'Median Clock Time (ms)',
        'Calls to Solve Method',
        'Total Moves Checked',
        'Failed Validation Checks',
        'Total Moves Assigned',
        'Total Wrong Moves',
        'Solved',
        'Matches Given Solution',
    ))
    for grid_file in grids:
        print(grid_file)
        for solver_name, solver in solvers.items():
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
                print('\t\tRun %s: %s seconds' % (i + 1, end - start))
                times.append(end - start)

            average_time = sum(times) / len(times)
            median_time = numpy.median(times)

            h = open(grid_file + '.sol', 'r')
            content = h.readlines()
            h.close()
            is_solution = str(solved_grid).strip().replace(' ', '') == (
                ''.join(content)).strip().replace(' ', '')

            f.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (
                grid_file,
                str(grid.row_count) + 'x' + str(grid.column_count),
                grid.cell_count,
                len(grid.rooms),
                sum(1 for room in grid.rooms if len(room.cells) == 1),
                sum(1 for room in grid.rooms if len(room.cells) == 2),
                sum(1 for room in grid.rooms if len(room.cells) == 3),
                sum(1 for room in grid.rooms if len(room.cells) == 4),
                sum(1 for room in grid.rooms if len(room.cells) == 5),
                sum(1 for room in grid.rooms if len(room.cells) == 6),
                sum(1 for room in grid.rooms if len(room.cells) == 7),
                sum(1 for room in grid.rooms if len(room.cells) == 8),
                sum(1 for room in grid.rooms if len(room.cells) == 9),
                solver_name,
                average_time * 1000,
                median_time * 1000,
                counter[0],
                counter[1],
                counter[2],
                counter[3],
                counter[4],
                solved_grid is not None,
                is_solution
            ))
            f.flush()

    f.close()
