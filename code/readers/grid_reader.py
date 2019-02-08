__author__ = 'Nikhil Pandey'

"""
file: grid_reader.py
Author: Nikhil Pandey np7803@rit.edu
Description: Maze solver
"""

import itertools
from cell import Cell
from room import Room
from .base_reader import BaseReader


class GridReader(BaseReader):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.rooms = []

    def prepare(self):
        main_queue = set(itertools.product(range(0, self.row_count),
                                           range(0, self.column_count)))
        while main_queue:
            room = Room()
            self.rooms.append(room)
            cell = self.get_or_create_cell(*main_queue.pop())
            cell.assign_room(room)
            room.add_cell(cell)

            visited = set()
            visited.add((cell.row, cell.col))
            room_queue = [(cell.row, cell.col)]

            while room_queue:

                state = room_queue.pop(0)
                successors = self.get_successors(state)

                for row, col in successors:
                    if (row, col) not in visited:
                        visited.add((row, col))
                        new_cell = self.get_or_create_cell(row, col)
                        new_cell.assign_room(room)
                        room.add_cell(new_cell)
                        main_queue.discard((row, col))
                        room_queue.append((row, col))

        self.rooms.sort(key=lambda x: x.size, reverse=True)

        for room in self.rooms:
            count = len(room.cells) + 1
            for number in range(1, count):
                room.possible_options[number] = set()
                for cell in room.cells:
                    room.possible_options[number].add(cell)
                    cell.possible_moves.add(number)

    def get_successors(self, position):
        """
        Generates successors of a state.

        Args:
                position: The current position.

        Returns:
                Generates next states
        """

        actual_grid_pos = position[0] * 2 + 1, position[1] * 2 + 1

        # Possible moves
        sfs = [
            lambda x, y: ((x + 1, y), ((x + 2) // 2, y // 2)),
            lambda x, y: ((x - 1, y), ((x - 2) // 2, y // 2)),
            lambda x, y: ((x, y + 1), (x // 2, (y + 2) // 2)),
            lambda x, y: ((x, y - 1), (x // 2, (y - 2) // 2)),
        ]

        for s in sfs:
            separator, actual_succ_posn = s(*actual_grid_pos)

            if actual_succ_posn[0] < 0 or actual_succ_posn[0] - 1 >= \
                    self.row_count \
                    or actual_succ_posn[1] < 0 or actual_succ_posn[
                1] - 1 >= self.column_count:
                continue

            if self.input_grid[separator[0]][separator[1]] == '|' or \
                    self.input_grid[separator[0]][separator[1]] == '-':
                continue

            yield actual_succ_posn

    def get_or_create_cell(self, row, col):
        if not self.cells[row][col]:
            self.cells[row][col] = Cell(self, row, col,
                                        self.input_grid[row * 2 + 1][
                                            col * 2 + 1])

        return self.cells[row][col]

    def get_next_empty_cell(self):
        for row in self.cells:
            for cell in row:
                if not cell.has_value():
                    return cell

    def get_next_mrv_with_humane_check(self):
        lowest_count = 0
        lowest_cell = None
        for room in self.rooms:
            for cell in room.cells:
                if (not cell.has_value()) and \
                        (lowest_cell is None or
                         len(cell.possible_moves) < lowest_count):
                    lowest_count = len(cell.possible_moves)
                    lowest_cell = cell
        print(repr(lowest_cell), lowest_count)
        return lowest_cell

    def get_next_mrv_cell(self):
        if self.humane_check:
            return self.get_next_mrv_with_humane_check()

        lowest_count = 0
        lowest_cell = None
        for row in self.cells:
            for cell in row:
                if (not cell.has_value()) and \
                        (lowest_cell is None or
                         len(cell.possible_moves) < lowest_count):
                    lowest_count = len(cell.possible_moves)
                    lowest_cell = cell
        print(repr(lowest_cell), lowest_count)
        a = input()
        return lowest_cell

    def is_valid(self, complete=False):
        for room in self.rooms:
            if not room.is_valid(complete):
                return False

        row_seen = [{} for _ in range(self.row_count)]
        col_seen = [{} for _ in range(self.column_count)]
        for ridx, row in enumerate(self.cells):
            for cidx, cell in enumerate(row):
                if not cell.has_value():
                    if complete:
                        return False
                    continue

                if cell.value in row_seen[ridx]:
                    if cidx - row_seen[ridx][cell.value] <= cell.value:
                        return False
                row_seen[ridx][cell.value] = cidx

                if cell.value in col_seen[cidx]:
                    if ridx - col_seen[cidx][cell.value] <= cell.value:
                        return False

                col_seen[cidx][cell.value] = ridx

        return True

    def validate_rows_cols(self, cell):
        for cidx in range(max(0, cell.col - cell.value),
                          min(self.column_count, cell.col + cell.value + 1)):
            if cidx != cell.col and \
                    cell.value == self.cells[cell.row][cidx].value:
                return False

        for ridx in range(max(0, cell.row - cell.value),
                          min(self.row_count, cell.row + cell.value + 1)):
            if ridx != cell.row and \
                    cell.value == self.cells[ridx][cell.col].value:
                return False

        return True

    def is_solved(self):
        return self.is_valid(complete=True)

    def recompute_moves(self, cell):

        if not self.check_moves:
            return [], True

        removed = []
        for room_cell in cell.room.cells:
            if cell == room_cell or room_cell.has_value():
                continue

            if cell.value in room_cell.possible_moves:
                room_cell.remove_possible_move(cell.value)
                room_cell.room.remove_possible_move(cell.value, room_cell)
                removed.append((room_cell, cell.value))
                if not room_cell.has_possible_moves():
                    return removed, False

        for cidx in range(max(0, cell.col - cell.value),
                          min(self.column_count, cell.col + cell.value + 1)):
            this_cell = self.cells[cell.row][cidx]

            if cell == this_cell or this_cell.has_value():
                continue

            if cell.value in this_cell.possible_moves:
                this_cell.remove_possible_move(cell.value)
                this_cell.room.remove_possible_move(cell.value, this_cell)
                removed.append((this_cell, cell.value))
                if not this_cell.has_possible_moves():
                    return removed, False

        for ridx in range(max(0, cell.row - cell.value),
                          min(self.row_count, cell.row + cell.value + 1)):
            this_cell = self.cells[ridx][cell.col]

            if cell == this_cell or this_cell.has_value():
                continue

            if cell.value in this_cell.possible_moves:
                this_cell.remove_possible_move(cell.value)
                this_cell.room.remove_possible_move(cell.value, this_cell)
                removed.append((this_cell, cell.value))
                if not this_cell.has_possible_moves():
                    return removed, False

        return removed, True

    def patch_removed_values(self, items):
        for cell, val in items:
            cell.room.add_possible_move(val, cell)
            cell.add_possible_move(val)

    def __str__(self):
        input_grid = self.input_grid
        for row in self.cells:
            for cell in row:
                input_grid[cell.row * 2 + 1][cell.col * 2 + 1] = str(
                    cell.value) if cell.value else 'x'
        return '\n'.join([''.join(x) for x in input_grid])
