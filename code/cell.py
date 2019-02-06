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

        if value != '.':
            self.value = int(value)

    def assign_room(self, room):
        self.room = room

    def __repr__(self):
        return "Cell(%d, %d, %d)" % (self.row, self.col, self.value)
