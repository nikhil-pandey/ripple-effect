import sys
import itertools

from cell import Cell
from room import Room


class GridReader(object):

    def __init__(self):
        """
        Read a maze from file.

        Returns:
                2-D list containing the maze values.
        """
        try:
            file = sys.argv[1]
            with open(file, 'r') as f:
                self.rows, self.cols = (int(x) for x in f.readline().split())
                self.grid = [list(l.rstrip('\n')) for idx, l in
                             enumerate(f.readlines())]

            self.main_queue = set(itertools.product(range(0, self.rows),
                                                    range(0, self.cols)))

            self.cells = [[None for _ in range(0, self.cols)] for __ in
                          range(0, self.rows)]

        except (IndexError, FileNotFoundError):
            print('Usage: python3 rumbe.py <grid_file>')
            sys.exit(1)

    def prepare_cells(self):
        while self.main_queue:
            room = Room()
            cell = self.get_or_create_cell(*self.main_queue.pop())
            cell.assign_room(room)
            room.add_cell(cell)

            visited = set()
            visited.add((cell.row, cell.col))
            room_queue = [(cell.row, cell.col)]

            while room_queue:

                state = room_queue.pop(0)
                successors = self.get_successors(state)

                for row, col in successors:
                    if (row, col) not in visited:
                        visited.add((row, col))
                        new_cell = self.get_or_create_cell(row, col)
                        new_cell.assign_room(room)
                        room.add_cell(new_cell)
                        self.main_queue.discard((row, col))
                        room_queue.append((row, col))

    def get_successors(self, position):
        """
        Generates successors of a state.

        Args:
                position: The current position.

        Returns:
                Generates next states
        """

        actual_grid_pos = position[0] * 2 + 1, position[1] * 2 + 1

        # Possible moves
        sfs = [
            lambda x, y: ((x + 1, y), ((x + 2) // 2, y // 2)),
            lambda x, y: ((x - 1, y), ((x - 2) // 2, y // 2)),
            lambda x, y: ((x, y + 1), (x // 2, (y + 2) // 2)),
            lambda x, y: ((x, y - 1), (x // 2, (y - 2) // 2)),
        ]

        for s in sfs:
            separator, actual_succ_posn = s(*actual_grid_pos)

            if actual_succ_posn[0] < 0 or actual_succ_posn[0] - 1 >= \
                    self.rows \
                    or actual_succ_posn[1] < 0 or actual_succ_posn[
                1] - 1 >= self.cols:
                continue

            if self.grid[separator[0]][separator[1]] == '|' or \
                    self.grid[separator[0]][separator[1]] == '-':
                continue

            yield actual_succ_posn

    def get_or_create_cell(self, row, col):
        if not self.cells[row][col]:
            self.cells[row][col] = Cell(row, col,
                                        self.grid[row * 2 + 1][col * 2 + 1])

        return self.cells[row][col]
