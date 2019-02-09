__author__ = 'Nikhil Pandey'

"""
file: __main__.py
Author: Nikhil Pandey np7803@rit.edu
Description: Maze solver
"""

from solvers import *
from readers import *
import sys

while True:
    print('Which solver do you want to use?')
    print('1: Brute Force Solver')
    print('2: Vanilla MRV')
    print('3: MRV and track numbers')
    print('4: MRV and track numbers and forward checking')
    print('5: MRV and track numbers and forward checking and human-like checking')
    i = input('>')

    if i == '1':
        solver = BruteForceSolver()
    elif i == '2':
        solver = MRVSolver()
    elif i == '3':
        solver = MRVSolver()
    elif i == '4':
        solver = MRVSolver()
    elif i == '5':
        solver = MRVSolver()
    else:
        continue

    file_name = input('Enter the file name: ').strip()
    break

grid = BitReader(file_name) # if isinstance(solver, BruteForceSolver) else GridReader(file_name)
grid.prepare()
solved_grid = solver.solve(grid)
print(solved_grid)