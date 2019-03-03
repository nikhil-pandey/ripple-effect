from pruners import patch_removed_values

# [Wrong Assignments, Calls to Solve, Total Assignments, Validation Checks]
CALL_TO_SOLVE = 0
TOTAL_MOVES = 1
FAILED_VALIDATION = 2
ASSIGNED_MOVES = 3
WRONG_MOVES = -1  # 4


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
        self.cell_selector = cell_selector
        self.move_selector = move_selector
        self.validator = validator
        self.pruner = pruner
        self.steps_log = steps_log
        self.count_log = count_log

    def solve(self, grid):
        self.__log(CALL_TO_SOLVE, 0, 0, 0)

        cell = self.cell_selector(grid.rooms, grid.cells)

        if cell is None:
            return grid

        for move in self.move_selector(cell):
            self.__log(TOTAL_MOVES, cell.row, cell.col, move)

            if not self.validator(grid, cell, move):
                self.__log(FAILED_VALIDATION, cell.row, cell.col, move)
                continue

            self.__log(ASSIGNED_MOVES, cell.row, cell.col, move)
            cell.value = move
            cell.tries += 1
            cell.next_move = None

            cell.room.possible_options[move].discard(cell)

            pruned, should_continue = self.pruner(grid, cell)

            if should_continue:
                solution = self.solve(grid)
                if solution:
                    return solution

            self.__log(WRONG_MOVES, cell.row, cell.col, move)

            # Restore the state
            cell.room.possible_options[move].add(cell)
            patch_removed_values(pruned)

        cell.value = None

        return None

    def __log(self, action, row, col, value):
        if self.steps_log is not None:
            self.steps_log.append((action, row, col, value))

        if self.count_log is not None:
            self.count_log[action] += 1

    def __repr__(self):
        return 'Solver(%s, %s, %s, %s)' % (
            self.cell_selector.__name__, self.move_selector.__name__,
            self.validator.__name__, self.pruner.__name__)
