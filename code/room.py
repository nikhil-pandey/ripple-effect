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
        self.possible_moves = []

    def add_cell(self, cell):
        if not self.possible_moves:
            self.possible_moves.append(1)
        else:
            self.possible_moves.append(self.possible_moves[-1]+1)
        
        self.cells.add(cell)


    def get_possible_moves(self):
        return self.possible_moves


    def is_valid(self, complete=False):

        val_seen = {}
        
        for cell in self.cells:
            if cell.value in val_seen:
                return False

            if cell.value is None:
                if complete:
                    return False
                continue

            if cell.value < 0 or cell.value > len(self.possible_moves):
                return False

            val_seen[cell.value] = 1

        return True
