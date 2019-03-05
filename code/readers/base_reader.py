import os
import io


class BaseReader(object):

    def __init__(self, file_name):
        """
        Read and set up.
        :param file_name: Name of the file or String like input
        """
        if os.path.exists(file_name):
            f = open(file_name, 'r')
        else:
            f = io.StringIO(file_name)

        self.row_count, self.column_count = (int(x) for x in
                                             f.readline().split())

        self.input_grid = [[' ' for __ in range(self.column_count * 2 + 1)] for _ in range(self.row_count * 2 + 1)]

        for row, line in enumerate(f):
            if row > self.row_count * 2:
                break
            for idx, char in enumerate(line):
                if char == '\n' or idx > self.column_count * 2:
                    break
                self.input_grid[row][idx] = char

        self.cell_count = self.row_count * self.column_count

        self.cells = [[None for _ in range(0, self.column_count)] for __ in
                      range(0, self.row_count)]

        f.close()

    def __str__(self):
        """
        String representation of the grid.
        :return: Returns the string representation of the grid.
        """
        input_grid = self.input_grid
        for row in self.cells:
            for cell in row:
                input_grid[cell.row * 2 + 1][
                    cell.col * 2 + 1] = str(
                    cell.value) if cell.value is not None else '.'
        return '%d %d\n%s' % (self.row_count, self.column_count,
                              '\n'.join([''.join(x) for x in input_grid]))
