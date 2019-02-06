__author__ = 'Nikhil Pandey'

"""
file: maze23.py
Author: Nikhil Pandey np7803@rit.edu
Description: Maze solver
"""

import sys
import itertools
from cell import Cell
from room import Room
from queue import PriorityQueue


class GameGrid(object):

    def __init__(self):
        """
        Read a maze from file.

        Returns:
                2-D list containing the maze values.
        """
        try:
            file = sys.argv[1]
            with open(file, 'r') as f:
                self.row_count, self.column_count = (int(x) for x in f.readline().split())
                self.input_grid = [list(l.rstrip('\n')) for idx, l in
                             enumerate(f.readlines())]

            self.main_queue = set(itertools.product(range(0, self.row_count),
                                                    range(0, self.column_count)))

            self.cells = [[None for _ in range(0, self.column_count)] for __ in
                          range(0, self.row_count)]
            self.rooms = []

        except (IndexError, FileNotFoundError):
            print('Usage: python3 __main__.py <grid_file>')
            sys.exit(1)

    def prepare_cells(self):
        while self.main_queue:
            room = Room()
            self.rooms.append(room)
            cell = self.get_or_create_cell(*self.main_queue.pop())
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
                        self.main_queue.discard((row, col))
                        room_queue.append((row, col))
        
        for room in self.rooms:
            count = len(room.cells) + 1
            for cell in room.cells:
                cell.possible_moves = set(range(1, count))

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
                                        self.input_grid[row * 2 + 1][col * 2 + 1])

        return self.cells[row][col]


    def get_next_empty_cell(self):
        for row in self.cells:
            for cell in row:
                if not cell.has_value():
                    return cell

    def get_next_mrv_cell(self):
        lowest_count = 0
        lowest_cell = None
        for row in self.cells:
            for cell in row:
                if not cell.has_value() and (lowest_cell is None or len(cell.possible_moves) < lowest_count):
                    lowest_count = len(cell.possible_moves)
                    lowest_cell = cell

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
        for cidx in range(max(0, cell.col - cell.value), min(self.column_count, cell.col + cell.value + 1)):
            if cidx != cell.col and cell.value == self.cells[cell.row][cidx].value:
                return False

        for ridx in range(max(0, cell.row - cell.value), min(self.row_count, cell.row + cell.value + 1)):
            if ridx != cell.row and cell.value == self.cells[ridx][cell.col].value:
                return False

        return True

    def is_solved(self):
        return self.is_valid(complete=True)

    def __str__(self):
        input_grid = self.input_grid
        for row in self.cells:
            for cell in row:
                input_grid[cell.row * 2 + 1][cell.col * 2 + 1] = str(cell.value) if cell.value else ' '
        return '\n'.join([''.join(x) for x in input_grid])
