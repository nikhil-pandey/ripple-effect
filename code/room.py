__author__ = 'Nikhil Pandey'

"""
file: _room.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Exmaple Description
"""


class Room(object):

    def __init__(self):
        self._cells = set()
        self._possible_options = {}
        self._size = 0

    def add_cell(self, cell):
        self._cells.add(cell)

    def add_move(self, number, cell):
        if number not in self._possible_options:
            self._possible_options[number] = set()

        self._possible_options[number].add(cell)

    def remove_move(self, number, cell):
        if number not in self._possible_options:
            return
        self._possible_options[number].discard(cell)

    def is_valid(self, complete=False):

        val_seen = {}

        for cell in self._cells:
            if cell.value in val_seen:
                return False

            if cell.value is None:
                if complete:
                    return False
                continue

            if cell.value < 0 or cell.value > len(self._cells):
                return False

            val_seen[cell.value] = 1

        return True

    def get_size(self):
        return len(self._cells)

    def get_cells(self):
        return self._cells
