__author__ = 'Nikhil Pandey'

"""
file: bit_reader.py
Author: Nikhil Pandey np7803@rit.edu
Description: Maze solver
"""

from .base_reader import BaseReader
from bitstring import *
from collections import deque


class BitReader(BaseReader):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.rooms = []
        self.cells_count = self.column_count * self.row_count
        self.assigned = BitArray(self.cells_count)
        self.assigned_numbers = {}
        self.assigned_numbers_transpose = {}
        self.possible_numbers = {}

    def prepare(self):
        main_queue = set(range(0, self.cells_count))
        while main_queue:
            cell = main_queue.pop()
            self.set_value_for_pos(cell)
            room = set()
            room.add(cell)
            visited = set()
            visited.add(cell)

            room_queue = deque()
            room_queue.append(cell)

            while len(room_queue) > 0:
                state = room_queue.pop()
                successors = self.get_successors(state)

                for pos in successors:
                    if pos not in visited:
                        visited.add(pos)
                        self.set_value_for_pos(pos)
                        room.add(pos)
                        main_queue.discard(pos)
                        room_queue.append(pos)
            self.rooms.append(room)
            self.populate_moves_for_room(room)

    def get_successors(self, position):
        position = self.get_coord_from_pos(position)
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

            yield self.get_pos_from_coord(actual_succ_posn)

    def get_pos_from_coord(self, args):
        return args[0] * self.column_count + args[1]

    def get_trans_pos_from_coord(self, args):
        return args[1] * self.row_count + args[0]

    def get_coord_from_pos(self, pos):
        return pos // self.column_count, \
               pos - ((pos // self.column_count) * self.column_count)

    def get_coord_from_trans_pos(self, pos):
        return pos - ((pos // self.row_count) * self.row_count), \
               pos // self.row_count

    def set_value_for_pos(self, pos, val=-1):
        row, col = self.get_coord_from_pos(pos)

        if val == -1:
            val = self.input_grid[row * 2 + 1][col * 2 + 1]
            if val == '.':
                return
            val = int(val)

        current_val = self.cells[row][col]

        transpose_pos = self.get_trans_pos_from_coord((row, col))
        if current_val != None:
            if current_val not in self.assigned_numbers:
                self.assigned_numbers[current_val] = BitArray(self.cells_count)
                self.assigned_numbers_transpose[current_val] = BitArray(
                    self.cells_count)
            self.assigned_numbers[current_val][pos] = 0
            self.assigned_numbers_transpose[current_val][transpose_pos] = 0

        if val not in self.assigned_numbers:
            self.assigned_numbers[val] = BitArray(self.cells_count)
            self.assigned_numbers_transpose[val] = BitArray(
                self.cells_count)

        self.cells[row][col] = val
        self.assigned[pos] = 1 if val else 0

        if val is not None:
            self.assigned_numbers[val][pos] = 1
            self.assigned_numbers_transpose[val][transpose_pos] = 1
            self.remove_possibility_around(pos)

    def remove_possibility_around(self, pos):
        pass

    def populate_moves_for_room(self, room):
        for number in range(1, len(room) + 1):
            if number not in self.possible_numbers:
                self.possible_numbers[number] = BitArray(self.cells_count)

            for pos in room:
                self.possible_numbers[number][pos] = 1

    def get_next_empty_pos(self):
        location = self.assigned.find('0b0')
        if location:
            return location[0]

    def is_solved(self):
        return self.assigned.all(True)

    def get_possible_moves_for_pos(self, pos):
        for number, arr in self.possible_numbers.items():
            if arr[pos] == 1:
                yield number

    def is_move_valid(self, pos, value):
        row, col = self.get_coord_from_pos(pos)

        if value not in self.assigned_numbers:
            return True

        min_index = max(row * self.column_count, pos - value)
        max_index = min(self.column_count*(row + 1), pos + value + 1)
        if (self.assigned_numbers[value][min_index:max_index]).any(True):
            return False

        transpose_pos = self.get_trans_pos_from_coord((row, col))
        min_index = max(col * self.row_count, transpose_pos - value)
        max_index = min(self.row_count*(col + 1), transpose_pos + value + 1)
        if (self.assigned_numbers_transpose[value][min_index:max_index]).any(True):
            return False

        for room_positions in self.rooms:
            if pos in room_positions:
                for other_pos in room_positions:
                    if other_pos == pos:
                        continue

                    if self.assigned[other_pos] == 0:
                        continue

                    if self.assigned_numbers[value][other_pos] == 1:
                        return False
                break

        return True

    def __str__(self):
        input_grid = self.input_grid
        for rc, row in enumerate(self.cells):
            for cc, cell in enumerate(row):
                input_grid[rc * 2 + 1][cc * 2 + 1] = str(
                    cell) if cell else 'x'
        return '\n'.join([''.join(x) for x in input_grid])
