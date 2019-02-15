__author__ = 'Nikhil Pandey'

"""
file: _room.py
language: python3
author: np7803@rit.edu Nikhil Pandey
description: Exmaple Description
"""
import logging

class Room(object):

    def __init__(self):
        self._cells = set()
        self._possible_options = {}
        self._size = 0

    def add_cell(self, cell):
        # logging.debug('ROOM: Adding Cell: %s to Room: %s' % (cell, self))
        self._cells.add(cell)

    def add_move(self, number, cell):
        # logging.debug('ROOM: Adding Move: %s for Cell: %s to Room: %s' % (number, cell, self))
        if not (number in self._possible_options):
            self._possible_options[number] = set()

        self._possible_options[number].add(cell)

        # logging.debug('ROOM: Added Move: %s for Cell: %s to Room: %s' % (number, cell, self))

    def remove_move(self, number, cell):
        # logging.debug('ROOM: Removing Move: %s for Cell: %s Room: %s' % (number, cell, self))
        if not (number in self._possible_options):
            return

        self._possible_options[number].discard(cell)
        # logging.debug('ROOM: Removed Move: %s for Cell: %s Room: %s' % (number, cell, self))

    def get_size(self):
        return len(self._cells)

    def get_cells(self):
        return self._cells

    def get_options(self):
        return self._possible_options

    def __repr__(self):
        return 'Room(size=%d, options=%s)' % (self._size, self._possible_options)
