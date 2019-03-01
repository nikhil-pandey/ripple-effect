__author__ = 'Nikhil Pandey'

"""
file: solver.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Solver Class
"""

from pruners import patch_removed_values
import logging


class Solver(object):

    def __init__(self, cell_selector, move_selector, validator, pruner,
                 steps_log=None, count_log=None):
        """
        Set up dependency injected parts of the search algorithm.
        :param cell_selector: The cell selector.
        :param move_selector: The move selector.
        :param validator: The validator.
        :param pruner: The pruner.
        :param steps_log: Log for visualization.
        :param count_log: Count different actions. For instrumentation.
        """
        self._cell_selector = cell_selector
        self._move_selector = move_selector
        self._validator = validator
        self._pruner = pruner
        self._steps_log = steps_log
        self._count_log = count_log

    def solve(self, grid):
        # logging.debug('SOLVER: Current grid\n%s' % (grid))

        if self._steps_log is not None:
            self._steps_log.append((0, 0, 0, 0))

        if self._count_log is not None:
            self._count_log[0] += 1

        cell = self._cell_selector(grid.get_rooms(), grid.get_cells())

        if cell is None:
            return grid

        for move in self._move_selector(cell):
            # logging.debug('SOLVER: Testing move %d for %s' % (move, cell))
            if self._steps_log is not None:
                self._steps_log.append(
                    (2, cell.get_row(), cell.get_column(), move))
            if self._count_log is not None:
                self._count_log[2] += 1

            if not self._validator(grid, cell, move):
                # logging.debug('SOLVER: Validation failed for move %d for
                # %s' % (move, cell))
                continue

            if self._steps_log is not None:
                self._steps_log.append(
                    (1, cell.get_row(), cell.get_column(), move))

            if self._count_log is not None:
                self._count_log[1] += 1

            cell.assign_value(move)
            cell.remove_next_move()
            # logging.debug('SOLVER: Removing %s from %s' % (cell,
            # cell.get_room()))
            cell.get_room().remove_move(cell.get_value(), cell)
            # logging.debug('SOLVER: Removed %s from %s' % (cell,
            # cell.get_room()))

            pruned, should_continue = self._pruner(grid, cell)

            if should_continue:
                solution = self.solve(grid)
                if solution:
                    return solution

            if self._steps_log is not None:
                self._steps_log.append(
                    (-1, cell.get_row(), cell.get_column(), move))

            if self._count_log is not None:
                self._count_log[-1] += 1

            # Restore the state
            cell.get_room().add_move(cell.get_value(), cell)
            patch_removed_values(pruned)

        cell.assign_value(None)

        return None

    def __repr__(self):
        return 'Solver(%s, %s, %s, %s)' % (
            self._cell_selector.__name__, self._move_selector.__name__,
            self._validator.__name__, self._pruner.__name__)
