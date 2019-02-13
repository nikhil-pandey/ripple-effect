__author__ = 'Nikhil Pandey'

"""
file: grid_reader.py
Author: Nikhil Pandey np7803@rit.edu
Description: Maze solver
"""

from cell import Cell
from room import Room
from .base_reader import BaseReader
from collections import deque


class GridReader(BaseReader):

    def __init__(self, file_name):
        super().__init__(file_name)
        self._rooms = []

    def prepare(self):

        main_visited = set()
        for i in range(0, self._cell_count):
            row = i // self._row_count
            col = i - row * self._column_count

            if (row, col) in main_visited:
                continue

            room = Room()
            self._rooms.append(room)
            cell = self.get_or_create_cell(room, row, col)

            visited = set()
            main_visited.add((row, col))
            visited.add((row, col))

            room_queue = deque()
            room_queue.append((cell.get_row(), cell.get_column()))

            while room_queue:

                state = room_queue.popleft()
                successors = self.get_successors(state)

                for row, col in successors:
                    if (row, col) not in visited:
                        self.get_or_create_cell(room, row, col)
                        main_visited.add((row, col))
                        visited.add((row, col))
                        room_queue.append((row, col))

        self._rooms.sort(key=lambda x: x.get_size(), reverse=True)

        for room in self._rooms:
            for number in range(1, room.get_size() + 1):
                for cell in room.get_cells():
                    if cell.has_value():
                        # And prune values
                        continue
                    room.add_move(number, cell)
                    cell.add_move(number)

    def get_successors(self, position):
        actual_grid_pos = position[0] * 2 + 1, position[1] * 2 + 1

        sfs = [
            lambda x, y: ((x + 1, y), ((x + 2) // 2, y // 2)),
            lambda x, y: ((x - 1, y), ((x - 2) // 2, y // 2)),
            lambda x, y: ((x, y + 1), (x // 2, (y + 2) // 2)),
            lambda x, y: ((x, y - 1), (x // 2, (y - 2) // 2)),
        ]

        for s in sfs:
            separator, actual_succ_posn = s(*actual_grid_pos)

            if actual_succ_posn[0] < 0 or actual_succ_posn[0] - 1 >= \
                    self._row_count \
                    or actual_succ_posn[1] < 0 or actual_succ_posn[
                1] - 1 >= self._column_count:
                continue

            if self._input_grid[separator[0]][separator[1]] == '|' or \
                    self._input_grid[separator[0]][separator[1]] == '-':
                continue

            yield actual_succ_posn

    def get_or_create_cell(self, room, row, col):
        if not self._cells[row][col]:
            value = self._input_grid[row * 2 + 1][col * 2 + 1]
            value = int(value) if value != '.' else None
            self._cells[row][col] = Cell(row, col, value)
            self._cells[row][col].assign_room(room)
            room.add_cell(self._cells[row][col])

        return self._cells[row][col]

    def is_solved(self):
        return self.is_valid(complete=True)

    def get_rooms(self):
        return self._rooms

    def get_row_count(self):
        return self._row_count

    def get_column_count(self):
        return self._column_count

    def get_cells(self):
        return self._cells

    def get_cell(self, row, col):
        return self._cells[row][col]

    def __str__(self):
        input_grid = self._input_grid
        for row in self._cells:
            for cell in row:
                input_grid[cell.get_row() * 2 + 1][cell.get_column() * 2 + 1] = str(
                    cell.get_value()) if cell.has_value() else 'x'
        return '\n'.join([''.join(x) for x in input_grid])
