__author__ = 'Nikhil Pandey'

"""
file: room.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Exmaple Description
"""


class Room(object):

    def __init__(self):
        self.cells = set()
        self.possible_options = {}
        self.size = 0

    def add_cell(self, cell):
        self.size += 1
        self.cells.add(cell)

    def add_possible_move(self, number, cell):
        self.possible_options[number].add(cell)

    def remove_possible_move(self, number, cell):
        self.possible_options[number].discard(cell)

    def is_valid(self, complete=False):

        val_seen = {}

        for cell in self.cells:
            if cell.value in val_seen:
                return False

            if cell.value is None:
                if complete:
                    return False
                continue

            if cell.value < 0 or cell.value > len(self.cells):
                return False

            val_seen[cell.value] = 1

        return True
