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

    def add_cell(self, cell):
        self.cells.add(cell)
