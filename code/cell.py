__author__ = 'Nikhil Pandey'

"""
file: file.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Exmaple Description
"""


class Cell(object):

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.room = None
        self.value = None

        if value != '.':
            self.value = int(value)

    def assign_room(self, room):
        self.room = room


    def has_value(self):
        return self.value is not None


    def get_possible_moves(self):
        return self.room.get_possible_moves()


    def __str__(self):
        return "Cell(%d)" % (self.value if self.value else 0)
