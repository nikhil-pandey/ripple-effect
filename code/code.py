__author__ = 'Nikhil Pandey'

"""
file: maze23.py
Author: Nikhil Pandey np7803@rit.edu
Description: Maze solver
"""

from grid_reader import GridReader


def main():
    """
    The main method.

    Returns:
            None
    """
    g = GridReader()
    g.prepare_cells()
    for row in g.cells:
        for c in row:
            print(c, end=' -> ')
            room = c.room
            for cx in room.cells:
                print(cx, end=' ')
            print()
        print()


# Execute from command line
if __name__ == '__main__':
    main()
