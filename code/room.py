__author__ = 'Nikhil Pandey'

"""
file: room.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Room
"""


class Room(object):

    def __init__(self):
        self.cells = set()
        self.possible_options = {}

    def __repr__(self):
        return 'Room(size=%d, options=%s)' % (
        len(self.cells), self.possible_options)
